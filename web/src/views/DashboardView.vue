<script setup>
import {h, onMounted} from "vue";
import {RouterLink, RouterView} from 'vue-router'
import {NIcon} from "naive-ui";
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
import router from "@/router";

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
    label: "概览",
    key: "overview",
    icon: renderIcon(BarChartOutlined),
    children: [
      {
        label: renderRouteLink("/dashboard/overview/permission", {}, "权限"),
        key: "permission-overview",
        icon: renderIcon(DesktopOutlined)
      },
      {
        label: renderRouteLink("/dashboard/overview/machine", {}, "机器"),
        key: "machine-overview",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: renderRouteLink("/dashboard/overview/concept", {}, "业务概念"),
        key: "concept-overview",
        icon: renderIcon(PaperClipOutlined)
      },
      {
        label: renderRouteLink("/dashboard/overview/repo-config", {}, "存储库与配置"),
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
        label: renderRouteLink("/dashboard/permission-control/member-mgmt", {}, "成员"),
        key: "member-mgmt",
        icon: renderIcon(UserOutlined)
      },
      {
        label: renderRouteLink("/dashboard/permission-control/group-mgmt", {}, "组"),
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
        label: renderRouteLink("/dashboard/biz-concept/machine", {}, "机器"),
        key: "machine",
        icon: renderIcon(CloudServerOutlined)
      },
      {
        label: renderRouteLink("/dashboard/biz-concept/group", {}, "群组"),
        key: "group",
        icon: renderIcon(GroupOutlined)
      },
      {
        label: renderRouteLink("/dashboard/biz-concept/safe-group", {}, "安全组"),
        key: "safe-group",
        icon: renderIcon(SafetyOutlined)
      },
      {
        label: renderRouteLink("/dashboard/biz-concept/res-pool", {}, "资源池"),
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
        label: renderRouteLink("/dashboard/config/repo", {}, "存储库"),
        key: "repo",
        icon: renderIcon(DatabaseFilled)
      },
      {
        label: renderRouteLink("/dashboard/config/versions-control", {}, "版本控制"),
        key: "versions-control",
        icon: renderIcon(PartitionOutlined)
      },
    ]
  },
  {
    label: renderRouteLink("/dashboard/audit", {}, "审计"),
    key: "audit",
    icon: renderIcon(AuditOutlined)
  },
  {
    label: renderRouteLink("/dashboard/about-me", {}, "关于我"),
    key: "about-me",
    icon: renderIcon(InfoCircleOutlined)

  }
];


function autoChangeRightContentWidth(collapsed) {
  document.getElementById("right-content").style.width = (collapsed ? window.innerWidth - 64 : window.innerWidth - 240) + "px"
  document.getElementById("logout-button").style.width = (collapsed ? "45px" : "220px")
  document.getElementById("logout-button").innerText = (collapsed ? "X" : "退 出 Melo CMDB")
}

function handleMenuItemClicked(key, item) {
  console.log(key)
  console.log(item)
}

function handleLogoutButtonClicked() {
    router.push({
    path: '/login'
  })
}

onMounted(() => {
  document.title = "Melo CMDB - 具有HA特性的分布式配置管理数据系统"
  document.getElementById("left-menu").style.height = window.innerHeight + 'px'
  document.getElementById("right-content").style.width = window.innerWidth - 240 + 'px'

  window.onresize = () => {
    document.getElementById("left-menu").style.height = window.innerHeight + 'px'
    autoChangeRightContentWidth()
  }


})

</script>


<template>
  <div class="dashboard-view">
      <n-layout has-sider>
        <n-button @click="handleLogoutButtonClicked" id="logout-button" strong secondary style="position: absolute;bottom: 10px;left: 10px; z-index: 99;width: 220px">退&nbsp;出&nbsp;Melo&nbsp;CMDB</n-button>
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
              @update:value="handleMenuItemClicked"
          />
        </n-layout-sider>
        <n-layout-content id="right-content">
          <router-view style="width: 100%; height: 100%;"/>
        </n-layout-content>
      </n-layout>
  </div>
</template>


<style scoped>
.dashboard-view {
  width: 100%;
  height: 100%;
  display: flex;
}
</style>

