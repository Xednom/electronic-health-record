import InsuranceAdd from "@/app/insurance/components/InsuranceAdd.vue";
import InsuranceDetail from "@/app/insurance/components/InsuranceEditor.vue";
// import InsuranceList from "@/app/insurance/views/ListPage.vue";
import InsuranceIndex from "@/app/insurance/views/IndexPage.vue";

export default [
  {
    path: "/Insurance/add",
    name: "insurance.add",
    component: InsuranceAdd
  },
  {
    path: "/insurance/list",
    name: "insurance.list",
    component: InsuranceIndex
  },
  {
    path: "/insurance/edit/:id",
    name: "insurance.edit",
    component: InsuranceDetail
  },
];