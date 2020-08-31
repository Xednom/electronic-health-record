<template>
    <patient-contact-list />
</template>

<script>
import PatientContactList from "@/app/patient_contact/components/PatientContactTable.vue";

export default {
    name: 'patient-contact-index',
    components: {
        PatientContactList
    }
}
</script>