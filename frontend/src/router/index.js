import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: "/About",
      name: "About",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/Assess",
      name: "Assess",
      component: () => import("../views/Assess.vue"),
    },
    {
      path: "/Results",
      name: "Results",
      component: () => import("../views/Results.vue"),
    },
    {
      path: "/Enrichment",
      name: "Enrichment",
      component: () => import("../views/Enrichment.vue"),
    },
    {
      path: "/Feedback",
      name: "Feedback",
      component: () => import("../views/Feedback.vue"),
    },
    {
      path: "/Survey",
      name: "Survey",
      component: () => import("../views/Survey.vue"),
    },
    {
      path: "/InternalError",
      name: "500",
      component: () => import("../views/500.vue"),
    },
    {
      path: "/:pathMatch(.*)",
      name: "NotFound",
      component: () => import("../views/NotFound.vue"),
    },
  ],
});

// Handle the case of fair assessment in progress and user leaves.
router.beforeEach((to, from, next) => {
  const isProcessing = sessionStorage.getItem("isProcessing") === "true";
  // Check if current route is results and request is processing
  if (from.path === "/Results" && isProcessing) {
    const confirmNavigation = window.confirm(
      "The request is still processing. Are you sure you want to leave?"
    );
    if (confirmNavigation) {
      sessionStorage.setItem("isProcessing", "false"); // Clear the state
      next();
    } else {
      next(false); // Prevent navigation
    }
  } else {
    next();
  }
});

export default router;
