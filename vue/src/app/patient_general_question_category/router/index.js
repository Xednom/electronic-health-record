import PatientGeneralQuestionCategoryAdd from "@/app/patient_general_question_category/components/PatientGeneralQuestionCategoryAdd.vue";
import PatientGeneralQuestionCategoryDetail from "@/app/patient_general_question_category/components/PatientGeneralQuestionCategoryEditor.vue";
// import PatientContactList from "@/app/patient_general_question_category/views/ListPage.vue";
import PatientGeneralQuestionCategoryIndex from "@/app/patient_general_question_category/views/IndexPage.vue";

export default [
  {
    path: "/patient-general-question-category/add",
    name: "patient_general_question_category.add",
    component: PatientGeneralQuestionCategoryAdd
  },
  {
    path: "/patient-general-question-category/list",
    name: "patient_general_question_category.list",
    component: PatientGeneralQuestionCategoryIndex
  },
  {
    path: "/patient-general-question-category/edit/:id",
    name: "patient_general_question_category.edit",
    component: PatientGeneralQuestionCategoryDetail
  },
];