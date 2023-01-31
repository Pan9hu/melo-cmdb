<template>
  <div class="about-view">
    <h1>This is an about page</h1>
  </div>
</template>

<script setup>
import {onMounted} from 'vue';
onMounted(()=>{
  document.title = "关于CMDB"
})
</script>
<style scoped>

</style>
