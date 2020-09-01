import PatientPhoneAdd from "@/app/patient_phone/components/PatientPhoneAdd.vue";
import PatientPhoneDetail from "@/app/patient_phone/components/PatientPhoneEditor.vue";
// import PatientContactList from "@/app/insurance/views/ListPage.vue";
import PatientPhoneIndex from "@/app/patient_phone/views/IndexPage.vue";

export default [
  {
    path: "/patient-phone/add",
    name: "patient_phone.add",
    component: PatientPhoneAdd
  },
  {
    path: "/patient-phone/list",
    name: "patient_phone.list",
    component: PatientPhoneIndex
  },
  {
    path: "/patient-phone/edit/:id",
    name: "patient_phone.edit",
    component: PatientPhoneDetail
  },
];