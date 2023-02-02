<template>
  <div class="about-me-view">
    <n-page-header>
      <template #header>
        <n-breadcrumb>
          <n-breadcrumb-item>关于我</n-breadcrumb-item>
        </n-breadcrumb>
      </template>
    </n-page-header>
    <n-card>
      <div class="cards">
        <div class="card">
          <div class="card-title">姓名</div>
          <div class="card-content">小林 / Z2000426</div>
        </div>
        <div class="card">
          <div class="card-title">使用 Melo CMDB 天数</div>
          <div class="card-content">122</div>
        </div>
        <div class="card">
        <div class="card-title">组织架构</div>
        <div class="card-content">互动娱乐事业部/基础架构/可靠性组</div>
      </div>
      </div>
    </n-card>
    <div style="width: 100%; padding-top: 20px;font-size: 8pt; color: gray;">
      <span>更多内容, 敬请期待...</span>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.about-me-view {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.cards {
  width: 100%;
  display: flex;
}

.card {
  min-width: 420px;
  min-height: 85px;
  padding-top: 10px;
  padding-left: 15px;
  padding-right: 15px;
  padding-bottom: 10px;
  display: flex;
  flex-direction: column;
}

.card-title {
  font-size: 12pt;
  color: gray;
  height: 50%;
  display: flex;
  align-items: end;
  padding-bottom: 5px;
}

.card-content {
  padding-top: 5px;
  font-size: 18pt;
  height: 50%;
}

</style>
