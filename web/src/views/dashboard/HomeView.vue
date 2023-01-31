<template>
  <div class="home-view">
    <div class="welcome-text">欢迎使用 Melo CMDB</div>
    <div class="version-text">v1.0.0</div>
    <div class="left-img">
      <img src="../../assets/image/undraw_ideas_re_7twj.svg" alt=" ">
    </div>
    <div class="right-img">
      <img src="../../assets/image/undraw_proud_coder_re_exuy.svg" alt=" ">
    </div>
  </div>
</template>

<style>
.home-view{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  width: 100%;
  height: 100%;
}
.welcome-text{
  font-size: 20pt;
}
.version-text{
  margin-top: 10px;
  font-size: 16pt;
}
.left-img{
  width: 54px ;
  height: 59px;
  position: absolute;
  left: 5px;
  border: 0;
}
.right-img{
  width: 70px;
  height: 65px;
  position: absolute;
  right: 0px;
  border: 0;
}
</style>