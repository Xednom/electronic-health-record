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
          <router-link :to="{ name: 'company.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ company.name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="inputEmail4">Name</label>
                <text-field v-model="company.name"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Address 1</label>
               <textarea class="form-control" rows="3" v-model="company.address_1"></textarea>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">Address 2</label>
               <textarea class="form-control" rows="3" v-model="company.address_2"></textarea>
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="inputEmail4">City</label>
                <text-field v-model="company.city"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">State</label>
                <text-field v-model="company.state"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputPassword4">Zip code</label>
                <number-field v-model="company.zip_code"></number-field>
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button
              type="submit"
              class="btn btn-danger ml-2"
              @click="deleteCompany"
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
import { FETCH_A_COMPANY } from "@/store/actions.type";

import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "CompanyEditor",
  components: {
    TextField, NumberField
  },
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {
    onSubmit() {
      if (this.company) {
        
        let endpoint = `/api/v1/company/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.company)
          .then(expense => {
            
            this.$router.push({
              name: "company.edit",
              params: { id: expense.id }
            });
            this.$store.dispatch(FETCH_A_COMPANY, this.$route.params.id);
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deleteCompany() {
      let endpoint = `/api/v1/companyb00-delete/${this.id}/`;
      let method = "PUT";
      this.company.active_status = false;
      apiService(endpoint, method, this.company.active_status).then(() => {
        this.$router
          .push({
            name: "company.list"
          })
          .catch(err => {
            console.log(err);
          });
      });
    }
  },
  computed: {
    ...mapGetters(["company", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_A_COMPANY, this.$route.params.id);
  }
};
</script>
