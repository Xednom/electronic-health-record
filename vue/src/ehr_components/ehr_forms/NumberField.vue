<template>
  <div>
    <input
      class="form-control"
      v-bind:value="value"
      v-on:input="$emit('input', $event.target.value)"
      @keypress="isNumber($event)"
    />
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
    return {};
  },
  methods: {
    isNumber: function(evt) {
      evt = evt ? evt : window.event;
      var charCode = evt.which ? evt.which : evt.keyCode;
      if (
        charCode > 31 &&
        (charCode < 48 || charCode > 57) &&
        charCode !== 46
      ) {
        evt.preventDefault();
      } else {
        return true;
      }
    }
  }
};
</script>