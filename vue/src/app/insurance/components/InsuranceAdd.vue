<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'insurance.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Insurance</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-12">
              <label>Address 1</label>
              <textarea class="form-control" rows="3" v-model="newInsurance.address_1"></textarea>
            </div>
            <div class="form-group col-md-12">
              <label>Address 1</label>
              <textarea class="form-control" rows="3" v-model="newInsurance.address_2"></textarea>
            </div>
            <div class="form-group col-md-4">
              <label>City</label>
              <text-field v-model="newInsurance.city"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label>State</label>
              <text-field v-model="newInsurance.state"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label>Zip Code</label>
              <number-field v-model="newInsurance.zip_code"></number-field>
            </div>
            <div class="form-group col-md-4">
              <label>Phone</label>
              <text-field v-model="newInsurance.phone"></text-field>
            </div>
          </div>
          <button type="submit" class="btn btn-success">Add</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { mapGetters } from "vuex";

import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "InsuranceAdd",
  components: {
    NumberField,
    TextField
  },
  data() {
    return {
      saving: false,
      success: false,
      insurances: {},
      currentItem: {},
      newInsurance: {
        address_1: "",
        address_2: "",
        city: "",
        state: "",
        zip_code: "",
        phone: ""
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/insurance/";
      let method = "POST";
      apiService(endpoint, method, this.newInsurance)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "insurance.edit",
            params: { id: currentItem.id }
          });
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapGetters(["loading"])
  },
  mounted() {
    
  }
};
</script>
