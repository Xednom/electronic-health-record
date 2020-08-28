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
          <router-link :to="{ name: 'insurance.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ insurance.name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-6">
                <label for="inputEmail4">Address 1</label>
               <textarea class="form-control" rows="3" v-model="insurance.address_1"></textarea>
              </div>
              <div class="form-group col-md-6">
                <label for="inputEmail4">Address 2</label>
               <textarea class="form-control" rows="3" v-model="insurance.address_2"></textarea>
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="inputEmail4">City</label>
                <text-field v-model="insurance.city"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputEmail4">State</label>
                <text-field v-model="insurance.state"></text-field>
              </div>
              <div class="form-group col-md-4">
                <label for="inputPassword4">Zip code</label>
                <number-field v-model="insurance.zip_code"></number-field>
              </div>
            </div>
            <button type="submit" class="btn btn-info">Update</button>
            <button
              type="submit"
              class="btn btn-danger ml-2"
              @click="deleteInsurance"
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
import { FETCH_AN_INSURANCE } from "@/store/actions.type";

import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "InsuranceEditor",
  components: {
    TextField, NumberField
  },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  methods: {
    onSubmit() {
      if (this.insurance) {
        
        let endpoint = `/api/v1/insurance/${this.insurance.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.insurance)
          .then(insurance => {
            
            this.$router.push({
              name: "insurance.edit",
              params: { id: insurance.id }
            });
            this.$store.dispatch(FETCH_AN_INSURANCE, this.$route.params.id);
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deleteInsurance() {
      let endpoint = `/api/v1/insuranceB00-delete/${this.id}/`;
      let method = "PUT";
      this.insurance.active_status = false;
      apiService(endpoint, method, this.insurance.active_status).then(() => {
        this.$router
          .push({
            name: "insurance.list"
          })
          .catch(err => {
            console.log(err);
          });
      });
    }
  },
  computed: {
    ...mapGetters(["insurance", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_AN_INSURANCE, this.$route.params.id);
  }
};
</script>
