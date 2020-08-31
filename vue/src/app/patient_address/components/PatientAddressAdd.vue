<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'patient_address.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Patient Contact</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-12">
              <label for="validationCustom04">Patient Contact</label>
              <select class="custom-select" id="validationCustom04"
                v-model="newPatientAddress.patient_contact">
                <option v-for="item in patientContacts" :key="item.id">
                  {{ item.last_name }}
                </option>
              </select>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-6">
              <label for="validationCustom04">Address 1</label>
              <textarea class="form-control" rows="3" v-model="newPatientAddress.address_1"></textarea>
            </div>
            <div class="form-group col-md-6">
              <label for="validationCustom04">Address 2</label>
              <textarea class="form-control" rows="3" v-model="newPatientAddress.address_2"></textarea>
            </div>
            <div class="form-group col-md-4">
              <label>City</label>
              <text-field v-model="newPatientAddress.city"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label>State</label>
              <text-field v-model="newPatientAddress.state"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label>Zip Code</label>
              <text-field v-model="newPatientAddress.zip_code"></text-field>
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

// import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";
// import SelectOption from "@/ehr_components/ehr_forms/SelectOption.vue";

export default {
  name: "PatientAddressAdd",
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
      newPatientAddress: {
        patient_contact: null,
        address_1: "",
        address_2: "",
        city: "",
        state: "",
        zip_code: "",
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/patient-address/";
      let method = "POST";
      apiService(endpoint, method, this.newPatientAddress)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "patient_address.edit",
            params: { id: currentItem.id }
          });
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapGetters(["patientAddresses", "patientContacts", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_CONTACTS);
  }
};
</script>
