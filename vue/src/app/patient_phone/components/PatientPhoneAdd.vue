<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'patient_phone.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Patient Phone</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <label>Patient Contact</label>
            <select
              class="custom-select"
              v-model="newPatientPhone.patient_contact"
            >
              <option v-for="item in patientContacts" :key="item.id">{{ item.last_name }}</option>
            </select>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label>Phone</label>
              <number-field v-model="newPatientPhone.phone"></number-field>
            </div>
            <div class="form-group col-md-6">
              <label>Phone Type</label>
              <select
                class="custom-select"
                id="validationCustom04"
                v-model="newPatientPhone.phone_type"
              >
                <option>Home</option>
                <option>Mobile</option>
                <option>Work</option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-3">
              <input class="form-check-input" type="checkbox" value
                v-model="newPatientPhone.primary"/>
              <label class="form-check-label" for="defaultCheck1">Primary</label>
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
// import TextField from "@/ehr_components/ehr_forms/TextField.vue";
// import SelectOption from "@/ehr_components/ehr_forms/SelectOption.vue";

export default {
  name: "PatientPhoneAdd",
  components: {
    NumberField,
    // TextField
    // SelectOption
  },
  data() {
    return {
      saving: false,
      success: false,
      currentItem: {},
      newPatientPhone: {
        patient_contact: null,
        phone: "",
        phone_type: "",
        primary: null
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/patient-phone/";
      let method = "POST";
      apiService(endpoint, method, this.newPatientPhone)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "patient_phone.edit",
            params: { id: currentItem.id }
          });
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapGetters(["patientPhones", "patientContacts", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_CONTACTS);
  }
};
</script>
