import PatientContactAdd from "@/app/patient_contact/components/PatientContactAdd.vue";
import PatientContactDetail from "@/app/patient_contact/components/PatientContactEditor.vue";
// import PatientContactList from "@/app/insurance/views/ListPage.vue";
import PatientContactIndex from "@/app/patient_contact/views/IndexPage.vue";

export default [
  {
    path: "/patient-contact/add",
    name: "patient_contact.add",
    component: PatientContactAdd
  },
  {
    path: "/patient-contact/list",
    name: "patient_contact.list",
    component: PatientContactIndex
  },
  {
    path: "/patient-contact/edit/:id",
    name: "patient_contact.edit",
    component: PatientContactDetail
  },
];