<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'insurance_rep.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Insurance Representative</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-6">
              <label>First name</label>
              <text-field v-model="newInsuranceRep.first_name"></text-field>
            </div>
            <div class="form-group col-md-6">
              <label>Last name</label>
              <text-field v-model="newInsuranceRep.last_name"></text-field>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label>Phone 1</label>
              <number-field v-model="newInsuranceRep.phone_1"></number-field>
            </div>
            <div class="form-group col-md-6">
              <label>Phone 2</label>
              <number-field v-model="newInsuranceRep.phone_2"></number-field>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-12">
              <label>Email Address</label>
              <text-field v-model="newInsuranceRep.email_address"></text-field>
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
  name: "InsuranceRepAdd",
  components: {
    NumberField,
    TextField
  },
  data() {
    return {
      saving: false,
      success: false,
      insuranceReps: {},
      currentItem: {},
      newInsuranceRep: {
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
      let endpoint = "/api/v1/insurance-rep/";
      let method = "POST";
      apiService(endpoint, method, this.newInsuranceRep)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "insurance_rep.edit",
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
