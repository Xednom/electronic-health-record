<template>
  <div>
    <input v-bind:value="value"
      class="form-control"
      v-on:input="$emit('input', $event.target.value)" />
    <!-- <div class="mt-2">Value: {{ value }}</div> -->
  </div>
</template>

<script>
  export default {
    props: {
        value: {
            type: String
        }
    },
    data() {
      return {
      }
    }
  }
</script>