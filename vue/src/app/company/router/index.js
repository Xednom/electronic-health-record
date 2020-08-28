// import CompanyAdd from "@/app/company/components/CompanyAdd.vue";
import CompanyDetail from "@/app/company/components/CompanyEditor.vue";
// import CompanyList from "@/app/company/views/ListPage.vue";
import CompanyIndex from "@/app/company/views/IndexPage.vue";
import CompanyForm from "@/app/company/views/FormPage.vue";

export default [
  {
    path: "/company/add",
    name: "company.add",
    component: CompanyForm
  },
  {
    path: "/company/list",
    name: "company.list",
    component: CompanyIndex
  },
  {
    path: "/company/edit/:id",
    name: "company.edit",
    component: CompanyDetail
  },
];