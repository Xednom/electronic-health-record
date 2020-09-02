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
          <router-link :to="{ name: 'patient_general_question_category.list' }">Back</router-link>
        </button>
      </div>
      <div class="card mt-5">
        <div class="card-header">
          Edit
          <strong>{{ patientGeneralQuestionCategory.name }}</strong> records
        </div>
        <div class="card-body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="inputEmail4">Name</label>
                <text-field v-model="patientGeneralQuestionCategory.name"></text-field>
              </div>
              <div class="form-group col-md-12">
                <label>Description</label>
                <textarea class="form-control"
                  v-model="patientGeneralQuestionCategory.description" id="" cols="30" rows="10"></textarea>
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
import { FETCH_A_PATIENT_GENERAL_QUESTION_CATEGORY } from "@/store/actions.type";

// import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";

export default {
  name: "PatientGeneralQuestionCategoryEditor",
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
      if (this.patientGeneralQuestionCategory) {
        let endpoint = `/api/v1/patient-general-question-category/${this.patientGeneralQuestionCategory.id}/`;
        let method = "PUT";
        apiService(endpoint, method, this.patientGeneralQuestionCategory)
          .then(patientGeneralQuestionCategory => {
            this.$router.push({
              name: "patient_general_question_category.edit",
              params: { id: patientGeneralQuestionCategory.id }
            });
            this.$store.dispatch(
              FETCH_A_PATIENT_GENERAL_QUESTION_CATEGORY,
              this.$route.params.id
            );
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    deletePatientPhone() {
      let endpoint = `/api/v1/patient-general-question-category-delete/${this.patientGeneralQuestionCategory.id}/`;
      let method = "PUT";
      this.patientGeneralQuestionCategory.active_status = false;
      apiService(endpoint, method, this.patientGeneralQuestionCategory.active_status)
        .then(() => {
          this.$router
            .push({
              name: "patient_general_question_category.list"
            })
            .catch(err => {
              console.log(err);
            });
        }
      );
    }
  },
  computed: {
    ...mapGetters(["patientGeneralQuestionCategory", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_A_PATIENT_GENERAL_QUESTION_CATEGORY, this.$route.params.id);
  }
};
</script>
