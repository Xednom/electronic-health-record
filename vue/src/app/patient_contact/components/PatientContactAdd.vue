<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'patient_contact.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Patient Contact</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-4">
              <label>First name</label>
              <text-field v-model="newPatientContact.first_name"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label>Middle name</label>
              <text-field v-model="newPatientContact.middle_name"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label>Last name</label>
              <text-field v-model="newPatientContact.last_name"></text-field>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="validationCustom04">Gender</label>
              <select class="custom-select" id="validationCustom04"
                v-model="newPatientContact.gender">
                <option selected disabled value>Choose...</option>
                <option>Male</option>
                <option>Female</option>
              </select>
            </div>
            <div class="form-group col-md-6">
              <label for="validationCustom04">Patient Relationship</label>
              <select class="custom-select" id="validationCustom04"
                v-model="newPatientContact.patient_relationship">
                <option selected disabled value>Choose...</option>
                <option>Self</option>
                <option>Father</option>
                <option>Mother</option>
                <option>Guardian</option>
              </select>
            </div>
            <div class="form-group col-md-6">
              <label>Birthdate</label>
              <input type="date" class="form-control"
                v-model="newPatientContact.birthdate">
            </div>
            <div class="form-group col-md-6">
              <label for="validationCustom04">Contact Type</label>
              <select class="custom-select" id="validationCustom04"
                v-model="newPatientContact.contact_type">
                <option selected disabled value>Choose...</option>
                <option>Patient</option>
                <option>Relative</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-12">
              <label>Email Address</label>
              <text-field v-model="newPatientContact.email_address"></text-field>
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
// import { FETCH_PATIENT_CONTACTS } from "@/store/actions.type";

// import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";
// import SelectOption from "@/ehr_components/ehr_forms/SelectOption.vue";

export default {
  name: "PatientContactAdd",
  components: {
    // NumberField,
    TextField,
    // SelectOption
  },
  data() {
    return {
      saving: false,
      success: false,
      currentItem: {},
      newPatientContact: {
        first_name: "",
        middle_name: "",
        last_name: "",
        email_address: "",
        gender: "",
        birthdate: null,
        contact_type: "",
        patient_relationship: ""
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/patient-contact/";
      let method = "POST";
      apiService(endpoint, method, this.newPatientContact)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "patient_contact.edit",
            params: { id: currentItem.id }
          });
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapGetters(["patientContacts", "loading"])
  },
  mounted() {
    // this.$store.dispatch(FETCH_PATIENT_CONTACTS);
  }
};
</script>
