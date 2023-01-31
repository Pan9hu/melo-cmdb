<template>
  <div class="home-view">
    <div class="welcome-text">欢迎使用 Melo CMDB</div>
    <div class="version-text">v1.0.0</div>
    <div class="left-img">
      <img src="../../assets/image/undraw_ideas_re_7twj.svg" alt="" style="width: 100%;height: 100%;">
    </div>
    <div class="right-img">
      <img src="../../assets/image/undraw_proud_coder_re_exuy.svg" alt="" style="width: 100%;height: 100%;">
    </div>
  </div>
</template>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.welcome-text {
  font-size: 20pt;
}

.version-text {
  margin-top: 10px;
  font-size: 16pt;
}

.left-img {
  width: 314px;
  height: 336px;
  position: absolute;
  left: 5px;
  bottom: 0;
}

.right-img {
  width: 388px;
  height: 280px;
  position: absolute;
  right: 0;
  bottom: 0;
}
</style>