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
          <router-link :to="{ name: 'patient_sibling.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ patientSibling.patient_contact }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="validationCustom04">Patient Contact</label>
                <select
                  class="custom-select"
                  id="validationCustom04"
                  v-model="patientSibling.patient_contact_b00_rec"
                >
                  <option v-for="item in patientContacts" :key="item.id">{{ item.last_name }}</option>
                </select>
              </div>
              <div class="form-group col-md-4">
                <label>First name</label>
                <text-field v-model="patientSibling.first_name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label>Middle name</label>
                <text-field v-model="patientSibling.middle_name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label>Last name</label>
                <text-field v-model="patientSibling.last_name"></text-field>
              </div>
              <div class="form-group col-md-2">
                  <label>Relationship</label>
                <select
                  class="custom-select"
                  v-model="patientSibling.relationship"
                >
                  <option >Brother</option>
                  <option >Sister</option>
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
import { FETCH_A_PATIENT_SIBLING } from "@/store/actions.type";

// import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "PatientSiblingEditor",
  components: {
    TextField,
    // NumberField
  },
  props: {
    id: {
      type: Number,
    }
  },
  methods: {
    onSubmit() {
      if (this.patientSibling) {
        let endpoint = `/api/v1/patient-sibling-b03/${this.patientSibling.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.patientSibling)
          .then(patientSibling => {
            this.$router.push({
              name: "patient_sibling.edit",
              params: { id: patientSibling.id }
            });
            this.$store.dispatch(
              FETCH_A_PATIENT_SIBLING,
              this.$route.params.id
            );
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deletePatientPhone() {
      let endpoint = `/api/v1/patient-sibling-b03-delete/${this.patientSibling.id}/`;
      let method = "PUT";
      this.patientSibling.active_status = false;
      apiService(endpoint, method, this.patientSibling.active_status)
        .then(() => {
          this.$router
            .push({
              name: "patient_sibling.list"
            })
            .catch(err => {
              console.log(err);
            });
        }
      );
    }
  },
  computed: {
    ...mapGetters(["patientSibling", "patientContacts", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_A_PATIENT_SIBLING, this.$route.params.id);
    this.$store.dispatch(FETCH_PATIENT_CONTACTS, this.$route.params.id);
  }
};
</script>
