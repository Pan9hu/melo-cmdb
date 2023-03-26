import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


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
        target: "http://127.0.0.1:5000",
        ws: true,
        rewrite: (path)=> path.replace(/^\/api/,''),
      }
    }
  }
})
