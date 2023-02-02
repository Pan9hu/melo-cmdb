<template>
  <div class="repo-step-view">
    <n-card style="width: 100%; height: 100%;">
      <div style="width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px;">
            <div style="font-size: 15pt; margin-bottom: 10px;">存储库:</div>
            <n-input style="width: 500px;" type="text" placeholder="请输入已经放置到 Melo CMDB 的存储库名称"/>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 15pt; margin-bottom: 10px;">分支:</div>
            <n-input style="width: 150px;" type="text" placeholder="请输入存储库分支"/>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 15pt; margin-bottom: 10px;">标签:</div>
            <n-input style="width: 150px;" type="text" placeholder="请输入存储库标签"/>
          </div>
          <div class="step-form-content">
            <n-alert title="处理中" type="info" :bordered="false" v-if="gitRepoCheckStatus === 'doing'">
              正在检查指定存储库中的配置数据是否可用。
            </n-alert>
            <n-alert title="配置数据可用" type="success" :bordered="false" v-if="gitRepoCheckStatus === 'ok'">
              恭喜, 这个存储库中的配置数据可用被同步到机器或者群组。
            </n-alert>
            <n-alert title="配置数据不可用" type="error" :bordered="false" v-if="gitRepoCheckStatus === 'false'">
              遗憾, 这个存储库出现了一些问题。
            </n-alert>
          </div>
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px;">重&nbsp;做</n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked" :loading="nextButtonLoading">下&nbsp;一&nbsp;步</n-button>
        </div>
      </div>
    </n-card>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";

const router = useRouter()

const emit = defineEmits(["update-step-index", "update-step-status"])


let gitRepoCheckStatus = ref('doing');

let nextButtonLoading = ref(false)

function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs/directory-step'
  });
}

onMounted(() => {
  emit('update-step-index', 1)
})

</script>

<style scoped>
.repo-step-view {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  padding-top: 25px;
}

.step-form-content {
  flex: 1;
}

.step-op-area {
  display: flex;
  justify-content: flex-end;
}
</style>
