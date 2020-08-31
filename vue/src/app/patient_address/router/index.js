import PatientAddressAdd from "@/app/patient_address/components/PatientAddressAdd.vue";
import PatientAddressDetail from "@/app/patient_address/components/PatientAddressEditor.vue";
// import PatientAddressList from "@/app/insurance/views/ListPage.vue";
import PatientAddressIndex from "@/app/patient_address/views/IndexPage.vue";

export default [
  {
    path: "/patient-address/add",
    name: "patient_address.add",
    component: PatientAddressAdd
  },
  {
    path: "/patient-address/list",
    name: "patient_address.list",
    component: PatientAddressIndex
  },
  {
    path: "/patient-address/edit/:id",
    name: "patient_address.edit",
    component: PatientAddressDetail
  },
];