<template>
    <patient-phone-list />
</template>

<script>
import PatientPhoneList from "@/app/patient_phone/components/PatientPhoneTable.vue";

export default {
    name: 'patient-phone-index',
    components: {
        PatientPhoneList
    }
}
</script>