<template>
  <div class="finish-step-view">
    <n-card style="width: 100%; height: 100%;">
      <div style="width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
        <div class="step-form-content">
          <div>
            <n-statistic label="你一共处理了" tabular-nums>
              <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039"/>
              <template #suffix>
                台机器，
              </template>
            </n-statistic>
            <n-statistic label="其中有" tabular-nums>
              <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12030"/>
              <template #suffix>
                台成功完成了变更任务，
              </template>
            </n-statistic>
            <n-statistic label="但是还有" tabular-nums>
              <n-number-animation ref="numberAnimationInstRef" :from="0" :to="9"/>
              <template #suffix>
                台操作失败。
              </template>
            </n-statistic>
            <n-divider title-placement="left">详细的错误信息如下:</n-divider>
          </div>
          <div style="flex: 1; display: flex; padding-bottom: 15px">
            <n-log id="log-content" style="width: 100%; height: 350px;" :loading="logAreaLoading" :log="logContent"/>
          </div>
        </div>
        <div class="step-op-area">
          <n-button strong type="warning" @click="handleCopyToClipBoardButtonClicked" style="margin-right: 10px;">
            拷贝到剪贴板
          </n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked">好</n-button>
        </div>
      </div>
    </n-card>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";
import { useMessage } from 'naive-ui'

const message = useMessage()
const router = useRouter()
const numberAnimationInstRef = ref(null)
const emit = defineEmits(["update-step-index", "update-step-status"])

let logAreaLoading = ref(false)

let demoLog = "2023-02-02T07:00:48Z DDEBUG Extra commands: [u'makecache', u'--timer']\n" +
    "2023-02-02T07:00:48Z DEBUG docker-ce-stable: has expired and will be refreshed.\n" +
    "2023-02-02T07:00:48Z DEBUG epel: has expired and will be refreshed.\n" +
    "2023-02-02T07:00:48Z DEBUG updates: has expired and will be refreshed.\n" +
    "2023-02-02T07:00:48Z DEBUG base: has expired and will be refreshed.\n" +
    "2023-02-02T07:00:48Z DEBUG extras: has expired and will be refreshed.\n" +
    "2023-02-02T07:00:48Z DEBUG reviving: 'docker-ce-stable' can be revived - repomd matches.\n" +
    "2023-02-02T07:00:48Z DEBUG not found other for: Docker CE Stable - x86_64\n" +
    "2023-02-02T07:00:48Z DEBUG not found modules for: Docker CE Stable - x86_64\n" +
    "2023-02-02T07:00:48Z DEBUG not found deltainfo for: Docker CE Stable - x86_64\n" +
    "2023-02-02T07:00:48Z DEBUG docker-ce-stable: using metadata from Tue 31 Jan 2023 12:00:37 AM CST.\n" +
    "2023-02-02T07:00:48Z DEBUG reviving: failed for 'epel', mismatched repomd.\n" +
    "2023-02-02T07:00:48Z DEBUG repo: downloading from remote: epel\n" +
    "2023-02-02T07:00:49Z DEBUG not found other for: Extra Packages for Enterprise Linux 7 - x86_64\n" +
    "2023-02-02T07:00:49Z DEBUG not found modules for: Extra Packages for Enterprise Linux 7 - x86_64\n" +
    "2023-02-02T07:00:54Z DEBUG epel: using metadata from Thu 02 Feb 2023 10:42:01 AM CST.\n" +
    "2023-02-02T07:00:54Z DEBUG reviving: 'updates' can be revived - repomd matches.\n" +
    "2023-02-02T07:00:54Z DEBUG not found other for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found modules for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found deltainfo for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found updateinfo for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG updates: using metadata from Sat 28 Jan 2023 03:32:29 AM CST.\n" +
    "2023-02-02T07:00:54Z DEBUG reviving: 'base' can be revived - repomd matches.\n" +
    "2023-02-02T07:00:54Z DEBUG not found other for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found modules for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found deltainfo for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found updateinfo for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG base: using metadata from Fri 30 Oct 2020 04:03:00 AM CST.\n" +
    "2023-02-02T07:00:54Z DEBUG reviving: 'extras' can be revived - repomd matches.\n" +
    "2023-02-02T07:00:54Z DEBUG not found other for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found modules for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found deltainfo for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG not found updateinfo for: CentOS-7\n" +
    "2023-02-02T07:00:54Z DEBUG extras: using metadata from Wed 05 Oct 2022 01:24:54 AM CST.\n" +
    "2023-02-02T07:00:54Z DEBUG No module defaults found\n" +
    "2023-02-02T07:00:54Z DDEBUG timer: sack setup: 6339 ms\n" +
    "2023-02-02T07:00:54Z INFO Metadata cache created.\n" +
    "2023-02-02T07:00:54Z DDEBUG Cleaning up.\n"

let logContent = ref(demoLog)


function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs'
  });
}

function handleCopyToClipBoardButtonClicked() {
  const clipboard = navigator.clipboard
  if (clipboard !== undefined){
    // 浏览器支持 Clipboard API
    clipboard.writeText(logContent.value).then(() => {
        message.success(
            "内容已经拷贝到剪贴板。"
        );
    }).catch(()=>{
      message.error(
          "拷贝内容到剪贴板失败。"
      );
    })
  } else {

  }
}

onMounted(() => {
  emit('update-step-index', 5)
  numberAnimationInstRef.value?.play()
})


</script>

<style scoped>
.finish-step-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding-top: 25px;
}

.step-form-content {
  flex: 1;
  display: flex;
  flex-direction: column;

}

.step-op-area {
  display: flex;
  justify-content: flex-end;
}
</style>