<template>
    <insurance-list />
</template>

<script>
import InsuranceList from "@/app/insurance/components/InsuranceTable.vue";

export default {
    name: 'insurance-index',
    components: {
        InsuranceList
    }
}
</script>