import InsuranceRepAdd from "@/app/insurance_rep/components/InsuranceRepAdd.vue";
import InsuranceRepDetail from "@/app/insurance_rep/components/InsuranceRepEditor.vue";
// import InsuranceList from "@/app/insurance/views/ListPage.vue";
import InsuranceRepIndex from "@/app/insurance_rep/views/IndexPage.vue";

export default [
  {
    path: "/insurance-rep/add",
    name: "insurance_rep.add",
    component: InsuranceRepAdd
  },
  {
    path: "/insurance-rep/list",
    name: "insurance_rep.list",
    component: InsuranceRepIndex
  },
  {
    path: "/insurance-rep/edit/:id",
    name: "insurance_rep.edit",
    component: InsuranceRepDetail
  },
];