<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'patient_sibling.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Patient Sibling</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
              <label>Patient Sibling</label>
              <select
                class="custom-select"
                v-model="newPatientSibling.patient_contact"
              >
                <option v-for="item in patientContacts" :key="item.id">{{ item.last_name }}</option>
              </select>
          </div>
          <div class="form-row mt-3">
            <div class="form-group col-md-6">
              <label>First name</label>
              <text-field v-model="newPatientSibling.first_name"></text-field>
            </div>
            <div class="form-group col-md-6">
              <label>Middle name</label>
              <text-field v-model="newPatientSibling.middle_name"></text-field>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label>Last name</label>
              <text-field v-model="newPatientSibling.last_name"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label>Relationship</label>
            <select
              class="custom-select"
              v-model="newPatientSibling.relationship"
            >
              <option >Brother</option>
              <option >Sister</option>
            </select>
            </div>
            <div class="form-group col-md-2">
              <label>Age</label>
              <number-field v-model="newPatientSibling.age"></number-field>
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
import { FETCH_PATIENT_CONTACTS } from "@/store/actions.type";

import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";
// import SelectOption from "@/ehr_components/ehr_forms/SelectOption.vue";

export default {
  name: "PatientSiblingAdd",
  components: {
    NumberField,
    TextField
    // SelectOption
  },
  data() {
    return {
      saving: false,
      success: false,
      currentItem: {},
      newPatientSibling: {
        patient_contact_b00_rec: null,
        first_name: "",
        middle_name: "",
        last_name: "",
        relationship: "",
        age: "",
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/patient-sibling-b03/";
      let method = "POST";
      apiService(endpoint, method, this.newPatientSibling)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "patient_sibling.edit",
            params: { id: currentItem.id }
          });
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapGetters(["patientSiblings", "patientContacts", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_CONTACTS);
  }
};
</script>
