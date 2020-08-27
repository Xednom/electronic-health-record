import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

import CompanyAdd from "@/app/company/components/CompanyAdd.vue";
import CompanyDetail from "@/app/company/components/CompanyEditor.vue";
import CompanyList from "@/app/company/views/ListPage.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/company/add",
    name: "company.add",
    component: CompanyAdd
  },
  {
    path: "/company/list",
    name: "company.list",
    component: CompanyList
  },
  {
    path: "/company/:id/",
    name: "company.edit",
    component: CompanyDetail,
    props: true
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

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
