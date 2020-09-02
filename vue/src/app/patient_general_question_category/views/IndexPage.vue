<template>
    <patient-general-question-category-list />
</template>

<script>
import PatientGeneralQuestionCategoryList from "@/app/patient_general_question_category/components/PatientGeneralQuestionCategoryTable.vue";

export default {
    name: 'PatientGeneralQuestionCategoryIndex',
    components: {
        PatientGeneralQuestionCategoryList
    }
}
</script>