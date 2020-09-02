import PatientSiblingAdd from "@/app/patient_sibling/components/PatientSiblingAdd.vue";
import PatientSiblingDetail from "@/app/patient_sibling/components/PatientSiblingEditor.vue";
// import PatientContactList from "@/app/insurance/views/ListPage.vue";
import PatientSiblingIndex from "@/app/patient_sibling/views/IndexPage.vue";

export default [
  {
    path: "/patient-sibling/add",
    name: "patient_sibling.add",
    component: PatientSiblingAdd
  },
  {
    path: "/patient-sibling/list",
    name: "patient_sibling.list",
    component: PatientSiblingIndex
  },
  {
    path: "/patient-sibling/edit/:id",
    name: "patient_sibling.edit",
    component: PatientSiblingDetail
  },
];