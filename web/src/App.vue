<script setup>
import {h, onMounted, ref} from "vue";
import {RouterLink, RouterView} from 'vue-router'
import {NIcon, darkTheme} from "naive-ui";
import {
  UsergroupAddOutlined,
  UserOutlined,
  ControlOutlined,
  DesktopOutlined,
  BarChartOutlined,
  PaperClipOutlined,
  CloudServerOutlined,
  GroupOutlined,
  BoxPlotOutlined,
  SafetyOutlined,
  FileSyncOutlined,
  PartitionOutlined,
  CloudSyncOutlined,
  DatabaseFilled,
  AuditOutlined,
  InfoCircleOutlined
} from "@vicons/antd";

function renderIcon(icon) {
  return () => h(NIcon, null, {default: () => h(icon)});
}

function renderRouteLink(path, params, label) {
  return () =>
      h(
          RouterLink, {
            to: {
              path: path,
              params: params,
            }
          },
          {default: () => label}
      )
}

const menuOptions = [
  {
    label: renderRouteLink("/dashboard/overview", {}, "概览"),
    key: "overview",
    icon: renderIcon(BarChartOutlined),
    children: [
      {
        label: renderRouteLink("/dashboard/overview/PermissionOverview", {}, "权限"),
        key: "permission-overview",
        icon: renderIcon(DesktopOutlined)
      },
      {
        label: renderRouteLink("/dashboard/overview/MachineOverview", {}, "机器"),
        key: "machine-overview",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: "业务概念",
        key: "concept-overview",
        icon: renderIcon(PaperClipOutlined)
      },
      {
        label: "存储库与配置",
        key: "repo-config-overview",
        icon: renderIcon(CloudSyncOutlined)
      },
    ]
  },
  {
    label: "权限控制",
    key: "permission-control",
    icon: renderIcon(ControlOutlined),
    children: [
      {
        label: "成员",
        key: "member-mgmt",
        icon: renderIcon(UserOutlined)
      },
      {
        label: "组",
        key: "group-mgmt",
        icon: renderIcon(UsergroupAddOutlined)
      },
    ]
  },
  {
    label: "业务概念",
    key: "biz-concept",
    icon: renderIcon(PaperClipOutlined),
    children: [
      {
        label: "机器",
        key: "machine",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: "群组",
        key: "group",
        icon: renderIcon(GroupOutlined)
      },
      {
        label: "安全组",
        key: "safe-group",
        icon: renderIcon(SafetyOutlined)
      },
      {
        label: "资源池",
        key: "res-pool",
        icon: renderIcon(BoxPlotOutlined)
      },
    ]
  },
  {
    label: "配置",
    key: "config",
    icon: renderIcon(FileSyncOutlined),
    children: [
      {
        label: "存储库",
        key: "repo",
        icon: renderIcon(DatabaseFilled)
      },
      {
        label: "版本控制",
        key: "versions-control",
        icon: renderIcon(PartitionOutlined)
      },
      {
        label: "审计",
        key: "audit",
        icon: renderIcon(AuditOutlined)
      },
    ]
  },
  {
    label: "关于",
    key: "about",
    icon: renderIcon(InfoCircleOutlined)

  }
];


function autoChangeRightContentWidth(collapsed) {
  document.getElementById("right-content").style.width = (collapsed ? window.innerWidth - 64 : window.innerWidth - 240) + "px"
}

function handleMenuItemClicked(key, item) {
  console.log(key)
  console.log(item)
}

let useDarkTheme = ref(false)

onMounted(() => {
  document.getElementById("left-menu").style.height = window.innerHeight + 'px';
  document.getElementById("right-content").style.width = window.innerWidth - 240 + "px";
  window.onresize = () => {
    document.getElementById("left-menu").style.height = window.innerHeight + 'px';
    autoChangeRightContentWidth()
  }

  let systemDarkModeMedia = window.matchMedia('(prefers-color-scheme:dark)');

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
    <n-config-provider :theme="useDarkTheme ? darkTheme : null">
      <n-space vertical>
        <n-layout has-sider style="height: 100%; display: flex;">
          <n-layout-sider
              id="left-menu"
              bordered
              show-trigger
              collapse-mode="width"
              :collapsed-width="64"
              :width="240"
              :native-scrollbar="false"
              :on-update:collapsed="autoChangeRightContentWidth"
          >
            <n-menu
                :collapsed-width="64"
                :collapsed-icon-size="22"
                :options="menuOptions"
            />
          </n-layout-sider>
          <n-layout-content id="right-content" content-style="padding: 24px;" style="background: gray">
            content
          </n-layout-content>
        </n-layout>
      </n-space>
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
