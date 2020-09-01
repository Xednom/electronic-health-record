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
          <router-link :to="{ name: 'patient_phone.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ patientPhone.patient_contact }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="validationCustom04">Patient Contact</label>
                <select
                  class="custom-select"
                  id="validationCustom04"
                  v-model="patientPhone.patient_contact"
                >
                  <option v-for="item in patientContacts" :key="item.id">{{ item.last_name }}</option>
                </select>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Phone</label>
                <number-field v-model="patientPhone.phone"></number-field>
              </div>
              <div class="form-group col-md-4">
                <input class="form-check-input" type="checkbox" value
                v-model="patientPhone.primary"/>
              <label class="form-check-label" for="defaultCheck1">Primary</label>
              </div>
              <div class="form-group col-md-4">
                <label>Phone Type</label>
                <select
                  class="custom-select"
                  v-model="patientPhone.phone_type"
                >
                  <option selected disabled value>Choose...</option>
                  <option>Home</option>
                  <option>Mobile</option>
                  <option>Work</option>
                </select>
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button type="submit" class="btn btn-danger ml-2" @click="deletePatientPhone">Delete</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { mapGetters } from "vuex";
import { FETCH_PATIENT_CONTACTS } from "@/store/actions.type";
import { FETCH_A_PATIENT_PHONE } from "@/store/actions.type";

import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
// import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "PatientPhoneEditor",
  components: {
    // TextField,
    NumberField
  },
  props: {
    id: {
      type: Number,
    }
  },
  methods: {
    onSubmit() {
      if (this.patientPhone) {
        let endpoint = `/api/v1/patient-phone/${this.patientPhone.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.patientPhone)
          .then(patientPhone => {
            this.$router.push({
              name: "patient_phone.edit",
              params: { id: patientPhone.id }
            });
            this.$store.dispatch(
              FETCH_A_PATIENT_PHONE,
              this.$route.params.id
            );
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deletePatientPhone() {
      let endpoint = `/api/v1/patient-phoneB02-delete/${this.patientPhone.id}/`;
      let method = "PUT";
      this.patientPhone.active_status = false;
      apiService(endpoint, method, this.patientPhone.active_status)
        .then(() => {
          this.$router
            .push({
              name: "patient_phone.list"
            })
            .catch(err => {
              console.log(err);
            });
        }
      );
    }
  },
  computed: {
    ...mapGetters(["patientPhone", "patientContacts", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_A_PATIENT_PHONE, this.$route.params.id);
    this.$store.dispatch(FETCH_PATIENT_CONTACTS, this.$route.params.id);
  }
};
</script>
