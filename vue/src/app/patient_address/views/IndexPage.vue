<template>
    <patient-address-list />
</template>

<script>
import PatientAddressList from "@/app/patient_address/components/PatientAddressTable.vue";

export default {
    name: 'patient-contact-index',
    components: {
        PatientAddressList
    }
}
</script>