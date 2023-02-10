import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    cors: true,
    proxy: {
      "^/api": {
        changeOrigin: true,
        target: "http://localhost:5000",
        ws: true,
        rewrite: (path)=> path.replace(/^\/api/,''),
      }
    }
  }
})
