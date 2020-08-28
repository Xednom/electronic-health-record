import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

import CompanyRoutes from "@/app/company/router";
import InsuranceRoutes from "@/app/insurance/router";

Vue.use(VueRouter);

const baseRoutes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: '*',
    redirect: { name: 'Home' },
  },
  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // }
];

const routes = baseRoutes.concat(CompanyRoutes, InsuranceRoutes);

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
