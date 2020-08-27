<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'company.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Company</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-12">
              <label for="inputEmail4">Name</label>
              <text-field v-model="newCompany.name"></text-field>
            </div>
            <div class="form-group col-md-12">
              <label for="inputEmail4">Address 1</label>
              <textarea class="form-control" rows="3" v-model="newCompany.address_1"></textarea>
            </div>
            <div class="form-group col-md-12">
              <label for="inputEmail4">Address 1</label>
              <textarea class="form-control" rows="3" v-model="newCompany.address_2"></textarea>
            </div>
            <div class="form-group col-md-4">
              <label for="inputEmail4">City</label>
              <text-field v-model="newCompany.city"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label for="inputEmail4">State</label>
              <text-field v-model="newCompany.state"></text-field>
            </div>
            <div class="form-group col-md-4">
              <label for="inputPassword4">Zip Code</label>
              <number-field v-model="newCompany.zip_code"></number-field>
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
  name: "CompanyAdd",
  components: {
    NumberField,
    TextField
  },
  data() {
    return {
      saving: false,
      success: false,
      companies: {},
      currentItem: {},
      newCompany: {
        name: "",
        address_1: "",
        address_2: "",
        city: "",
        state: "",
        zip_code: ""
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/company/";
      let method = "POST";
      apiService(endpoint, method, this.newCompany)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "company.edit",
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
