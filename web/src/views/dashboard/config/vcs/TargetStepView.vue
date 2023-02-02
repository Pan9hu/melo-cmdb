<template>
  <div class="target-step-view">
    <n-card style="width: 100%; height: 100%;">
      <div style="width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: flex-end;">
        <div class="step-form-content">
          <div style="margin-bottom: 25px;">
            <div style="font-size: 15pt; margin-bottom: 10px;">机器:</div>
            <n-input style="width: 100%;" type="textarea"
                     placeholder="请输入机器的UUID, 使用英文半角逗号分割。" rows="10"/>
          </div>
          <div style="margin-bottom: 25px;">
            <div style="font-size: 15pt; margin-bottom: 10px;">群组:</div>
            <n-tree-select multiple cascade checkable :options="targetMachineGroupOptions" :default-value="[]"
                           placeholder="请选择群组"/>
          </div>
          <n-statistic label="你选择了" tabular-nums>
            <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039"/>
            <template #suffix>
              个三级群组,
            </template>
          </n-statistic>
          <n-statistic label="共计 (去重后) 有" tabular-nums>
            <n-number-animation ref="numberAnimationInstRef" :from="0" :to="12039"/>
            <template #suffix>
              台机器。
            </template>
          </n-statistic>
        </div>
        <div class="step-op-area">
          <n-button strong style="margin-right: 10px;">取&nbsp;消</n-button>
          <n-button strong type="primary" @click="handleStepNextButtonClicked">下&nbsp;一&nbsp;步</n-button>
        </div>
      </div>
    </n-card>
  </div>
</template>

<script setup>

import {useRouter} from "vue-router";
import {onMounted, ref} from "vue";

const router = useRouter()
const numberAnimationInstRef = ref(null)
const emit = defineEmits(["update-step-index", "update-step-status"])

let targetMachineGroupOptions = [
  {
    label: 'Rubber Soul',
    key: 'Rubber Soul',
    children: [
      {
        label:
            "Everybody's Got Something to Hide Except Me and My Monkey",
        key: "Everybody's Got Something to Hide Except Me and My Monkey"
      },
      {
        label: 'Drive My Car',
        key: 'Drive My Car',
        disabled: true
      },
      {
        label: 'Norwegian Wood',
        key: 'Norwegian Wood'
      },
      {
        label: "You Won't See",
        key: "You Won't See",
        disabled: true
      },
      {
        label: 'Nowhere Man',
        key: 'Nowhere Man'
      },
      {
        label: 'Think For Yourself',
        key: 'Think For Yourself'
      },
      {
        label: 'The Word',
        key: 'The Word'
      },
      {
        label: 'Michelle',
        key: 'Michelle',
        disabled: true
      },
      {
        label: 'What goes on',
        key: 'What goes on'
      },
      {
        label: 'Girl',
        key: 'Girl'
      },
      {
        label: "I'm looking through you",
        key: "I'm looking through you"
      },
      {
        label: 'In My Life',
        key: 'In My Life'
      },
      {
        label: 'Wait',
        key: 'Wait'
      }
    ]
  },
  {
    label: 'Let It Be',
    key: 'Let It Be Album',
    children: [
      {
        label: 'Two Of Us',
        key: 'Two Of Us'
      },
      {
        label: 'Dig A Pony',
        key: 'Dig A Pony'
      },
      {
        label: 'Across The Universe',
        key: 'Across The Universe'
      },
      {
        label: 'I Me Mine',
        key: 'I Me Mine'
      },
      {
        label: 'Dig It',
        key: 'Dig It'
      },
      {
        label: 'Let It Be',
        key: 'Let It Be'
      },
      {
        label: 'Maggie Mae',
        key: 'Maggie Mae'
      },
      {
        label: "I've Got A Feeling",
        key: "I've Got A Feeling"
      },
      {
        label: 'One After 909',
        key: 'One After 909'
      },
      {
        label: 'The Long And Winding Road',
        key: 'The Long And Winding Road'
      },
      {
        label: 'For You Blue',
        key: 'For You Blue'
      },
      {
        label: 'Get Back',
        key: 'Get Back'
      }
    ]
  }
]

function handleStepNextButtonClicked() {
  router.push({
    path: '/dashboard/config/vcs/execute-step'
  });
}

onMounted(() => {
  emit('update-step-index', 3)
})

</script>

<style scoped>
.target-step-view {
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
