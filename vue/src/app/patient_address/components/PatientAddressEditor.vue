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
          <router-link :to="{ name: 'patient_address.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ patientAddress.patient_contact }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="validationCustom04">Patient Contact</label>
                <select
                  class="custom-select"
                  id="validationCustom04"
                  v-model="patientAddress.patient_contact"
                >
                  <option v-for="item in patientContacts" :key="item.id">{{ item.last_name }}</option>
                </select>
              </div>
              <div class="form-group col-md-8">
                <label for="validationCustom04">Address 2</label>
                <textarea class="form-control" rows="3" v-model="patientAddress.address_2"></textarea>
              </div>
              <div class="form-group col-md-4">
                <label>City</label>
                <text-field v-model="patientAddress.city"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label>State</label>
                <text-field v-model="patientAddress.state"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label>Zip Code</label>
                <text-field v-model="patientAddress.zip_code"></text-field>
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button type="submit" class="btn btn-danger ml-2" @click="deletePatientAddress">Delete</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { mapGetters } from "vuex";
import {
  FETCH_A_PATIENT_ADDRESS,
  FETCH_PATIENT_CONTACTS
} from "@/store/actions.type";

// import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "PatientAddressEditor",
  components: {
    TextField
    // NumberField
  },
  props: {
    id: {
      type: Number
    }
  },
  methods: {
    onSubmit() {
      if (this.patientAddress) {
        let endpoint = `/api/v1/patient-address/${this.patientAddress.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.patientAddress)
          .then(patientAddress => {
            this.$router.push({
              name: "patient_address.edit",
              params: { id: patientAddress.id }
            });
            this.$store.dispatch(
              FETCH_A_PATIENT_ADDRESS,
              this.$route.params.id
            );
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deletePatientAddress() {
      let endpoint = `/api/v1/patient-addressB01-delete/${this.patientAddress.id}/`;
      let method = "PUT";
      this.patientAddress.active_status = false;
      apiService(endpoint, method, this.patientAddress.active_status).then(
        () => {
          this.$router
            .push({
              name: "patient_address.list"
            })
            .catch(err => {
              console.log(err);
            });
        }
      );
    }
  },
  computed: {
    ...mapGetters(["patientAddress", "patientContacts", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_CONTACTS, this.$route.params.id);
    this.$store.dispatch(FETCH_A_PATIENT_ADDRESS, this.$route.params.id);
  }
};
</script>
