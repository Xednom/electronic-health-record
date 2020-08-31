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
          <router-link :to="{ name: 'patient_contact.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ patientContact.first_name }} {{ patientContact.last_name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="inputEmail4">First name</label>
                <text-field v-model="patientContact.first_name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Middle name</label>
                <text-field v-model="patientContact.middle_name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Last name</label>
                <text-field v-model="patientContact.last_name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Email Address</label>
                <text-field v-model="patientContact.email_address"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputPassword4">Gender</label>
                <select
                  class="custom-select"
                  id="validationCustom04"
                  v-model="patientContact.gender"
                >
                  <option selected disabled value>Choose...</option>
                  <option>Male</option>
                  <option>Female</option>
                </select>
              </div>
              <div class="form-group col-md-4">
                <label for="validationCustom04">Patient Relationship</label>
                <select
                  class="custom-select"
                  id="validationCustom04"
                  v-model="patientContact.patient_relationship"
                >
                  <option selected disabled value>Choose...</option>
                  <option>Self</option>
                  <option>Father</option>
                  <option>Mother</option>
                  <option>Guardian</option>
                </select>
              </div>
              <div class="form-group col-md-4">
              <label for="validationCustom04">Contact Type</label>
              <select class="custom-select" id="validationCustom04"
                v-model="patientContact.contact_type">
                <option selected disabled value>Choose...</option>
                <option>Patient</option>
                <option>Relative</option>
              </select>
            </div>
              <div class="form-group col-md-4">
                <label>Birthdate</label>
                <input type="date" class="form-control" v-model="patientContact.birthdate" />
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button type="submit" class="btn btn-danger ml-2" @click="deleteInsuranceRep">Delete</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { mapGetters } from "vuex";
import { FETCH_A_PATIENT_CONTACT } from "@/store/actions.type";

// import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "InsuranceRepEditor",
  components: {
    TextField
    // NumberField
  },
  props: {
    id: {
      type: Number,
    }
  },
  methods: {
    onSubmit() {
      if (this.patientContact) {
        let endpoint = `/api/v1/patient-contact/${this.patientContact.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.patientContact)
          .then(patientContact => {
            this.$router.push({
              name: "patient_contact.edit",
              params: { id: patientContact.id }
            });
            this.$store.dispatch(
              FETCH_A_PATIENT_CONTACT,
              this.$route.params.id
            );
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deleteInsuranceRep() {
      let endpoint = `/api/v1/patient-contactB00-delete/${this.patientContact.id}/`;
      let method = "PUT";
      this.patientContact.active_status = false;
      apiService(endpoint, method, this.patientContact.active_status)
        .then(() => {
          this.$router
            .push({
              name: "patient_contact.list"
            })
            .catch(err => {
              console.log(err);
            });
        }
      );
    }
  },
  computed: {
    ...mapGetters(["patientContact", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_A_PATIENT_CONTACT, this.$route.params.id);
  }
};
</script>
