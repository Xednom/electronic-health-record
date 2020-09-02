<template>
    <patient-sibling-list />
</template>

<script>
import PatientSiblingList from "@/app/patient_sibling/components/PatientSiblingTable.vue";

export default {
    name: 'PatientSiblingIndex',
    components: {
        PatientSiblingList
    }
}
</script>