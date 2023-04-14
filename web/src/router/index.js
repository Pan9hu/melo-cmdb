import {createRouter, createWebHistory} from 'vue-router'
import LoginView from "@/views/LoginView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL), routes: [{
        path: '/', component: LoginView
    }, {
        path: '/login', name: "login", component: LoginView
    }, {
        path: '/about', name: 'about', component: () => import('../views/AboutView.vue')
    }, {
        path: "/reset-password",
        name: "reset-password",
        component: () => import('../views/ResetPasswordView.vue'),children:[
            {
                path: "",
                component: () => import('../views/ResetPassword/AuthenticationStep.vue')
            },{
                path: "authentication-step",
                name: "reset-password-authentication-step",
                component: () => import('../views/ResetPassword/AuthenticationStep.vue')
            },{
                path: "reset-step",
                name: "reset-password-reset-step",
                component: () => import('../views/ResetPassword/ResetStep.vue')
            }, {
                path: "reset-success-step",
                name: "reset-password-reset-success-step",
                component: () => import('../views/ResetPassword/ResetSuccessStep.vue')
            }
        ]
    }, {
        path: '/dashboard', component: () => import('../views/DashboardView.vue'), children: [{
            path: '', name: "home", component: () => import('../views/dashboard/HomeView.vue')
        }, {
            path: 'overview', children: [{
                path: "permission",
                name: "overview-permission",
                component: () => import('../views/dashboard/overview/PermissionView.vue')
            }, {
                path: "machine",
                name: "overview-machine",
                component: () => import('../views/dashboard/overview/MachineView.vue')
            }, {
                path: "concept",
                name: "overview-concept",
                component: () => import('../views/dashboard/overview/ConceptView.vue')
            }, {
                path: "repo-config",
                name: "overview-repo-config",
                component: () => import('../views/dashboard/overview/RepoConfigView.vue')
            },]
        }, {
            path: 'permission-control', children: [{
                path: "member-mgmt",
                name: "permission-control-member-mgmt",
                component: () => import('../views/dashboard/permission-control/MemberMgmtView.vue')
            }, {
                path: "group-mgmt",
                name: "permission-control-group-mgmt",
                component: () => import('../views/dashboard/permission-control/GroupMgmtView.vue')
            },]
        }, {
            path: 'biz-concept', children: [{
                path: "machine",
                name: "biz-concept-machine",
                component: () => import('../views/dashboard/biz-concept/MachineView.vue')
            }, {
                path: "group",
                name: "biz-concept-group",
                component: () => import('../views/dashboard/biz-concept/GroupView.vue')
            }, {
                path: "safe-group",
                name: "biz-concept-safe-group",
                component: () => import('../views/dashboard/biz-concept/SafeGroupView.vue')
            }, {
                path: "res-pool",
                name: "biz-concept-res-pool",
                component: () => import('../views/dashboard/biz-concept/ResPoolView.vue')
            },]
        }, {
            path: 'config', children: [{
                path: "repo", name: "config-repo", component: () => import('../views/dashboard/config/RepoView.vue')
            }, {
                path: "vcs",
                name: "config-vcs",
                component: () => import('../views/dashboard/config/VCSView.vue'),children:[
                    {
                        path: "",
                        component: () => import('../views/dashboard/config/vcs/RepoStepView.vue')
                    },{
                        path: "repo-step",
                        name: "config-vcs-repo-step",
                        component: () => import('../views/dashboard/config/vcs/RepoStepView.vue')
                    },{
                        path: "directory-step",
                        name: "config-vcs-directory-step",
                        component: () => import('../views/dashboard/config/vcs/DirectoryStepView.vue')
                    }, {
                        path: "target-step",
                        name: "config-vcs-target-step",
                        component: () => import('../views/dashboard/config/vcs/TargetStepView.vue')
                    },{
                        path: "execute-step",
                        name: "config-vcs-execute-step",
                        component: () => import('../views/dashboard/config/vcs/ExecuteStepView.vue')
                    },{
                        path: "finish-step",
                        name: "config-vcs-finish-step",
                        component: () => import('../views/dashboard/config/vcs/FinishStepView.vue')
                    },
                ]
            },
            ]
        }, {
            path: "audit", name: "audit", component: () => import('../views/dashboard/AuditView.vue')
        }, {
            path: 'about-me', name: 'about-me', component: () => import('../views/dashboard/AboutMeView.vue')
        }]
    },]
})

export default router
