<template>
  <div class="container">
    <div class="mt-5" v-if="loading">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
    <div v-else>
      <div class="row">
        <button type="button" class="btn btn-link mt-5 pull-left">
          <router-link :to="{ name: 'insurance_rep.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ insuranceRep.name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="inputEmail4">First name</label>
                <text-field v-model="insuranceRep.first_name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Last name</label>
                <text-field v-model="insuranceRep.last_name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputPassword4">Phone 1</label>
                <number-field v-model="insuranceRep.phone_1"></number-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputPassword4">Phone 2</label>
                <number-field v-model="insuranceRep.phone_2"></number-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Email Address</label>
                <text-field v-model="insuranceRep.email_address"></text-field>
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button
              type="submit"
              class="btn btn-danger ml-2"
              @click="deleteInsuranceRep"
            >
              Delete
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { mapGetters } from "vuex";
import { FETCH_AN_INSURANCE_REP } from "@/store/actions.type";

import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "InsuranceRepEditor",
  components: {
    TextField, NumberField
  },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  methods: {
    onSubmit() {
      if (this.insuranceRep) {
        
        let endpoint = `/api/v1/insurance-rep/${this.insuranceRep.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.insuranceRep)
          .then(insuranceRep => {
            
            this.$router.push({
              name: "insurance_rep.edit",
              params: { id: insuranceRep.id }
            });
            this.$store.dispatch(FETCH_AN_INSURANCE_REP, this.$route.params.id);
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deleteInsuranceRep() {
      let endpoint = `/api/v1/insuranceRepB00-delete/${this.id}/`;
      let method = "PUT";
      this.insuranceRep.active_status = false;
      apiService(endpoint, method, this.insuranceRep.active_status).then(() => {
        this.$router
          .push({
            name: "insuranceRep.list"
          })
          .catch(err => {
            console.log(err);
          });
      });
    }
  },
  computed: {
    ...mapGetters(["insuranceRep", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_AN_INSURANCE_REP, this.$route.params.id);
  }
};
</script>
