import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import { useAuthStore } from "@/stores/auth";
import { accessTokenService } from "@/services/accessTokenService";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/job/:id",
      name: "job",
      component: () => import("../views/JobView.vue"),
    },
    {
      path: "/search/",
      name: "search",
      component: () => import("../views/SearchView.vue"),
    },
    {
      path: "/login/",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/register/",
      name: "register",
      component: () => import("../views/RegisterView.vue"),
    },
    {
      path: "/profile/",
      name: "profile",
      meta: { requiresAuth: true },
      component: () => import("../views/ProfileView.vue"),
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ],
});

router.beforeEach((to, from, next) => {
  // const useAuth = useAuthStore();
  const accessToken = accessTokenService.get();
  if (to.meta.requiresAuth && !accessToken) {
    next("/login");
  } else {
    next();
  }
});

export default router;
