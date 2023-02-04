<script setup>
import {onMounted, ref} from "vue";
import {darkTheme} from "naive-ui";

let systemDarkModeMedia = window.matchMedia('(prefers-color-scheme: dark)');

let useDarkTheme = ref(systemDarkModeMedia.matches);

onMounted(() => {
  let systemThemeCallback = (e) => {
    let preferDarkMode = e.matches;
    useDarkTheme.value = !!preferDarkMode;
  };

  if (typeof systemDarkModeMedia.addEventListener === 'function') {
    systemDarkModeMedia.addEventListener('change', systemThemeCallback);
  } else if (typeof systemDarkModeMedia.addListener === 'function') {
    systemDarkModeMedia.addListener(systemThemeCallback);
  }
})

</script>


<template>
  <div class="app-view">
    <n-config-provider style="width: 100%;" :theme="useDarkTheme ? darkTheme : null">
      <n-message-provider>
        <n-dialog-provider>
          <router-view style="width: 100%; height: 100%; flex: 1"/>
        </n-dialog-provider>
      </n-message-provider>
    </n-config-provider>
  </div>
</template>


<style scoped>
.app-view {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>
