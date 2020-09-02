<template>
  <div class="container col-md-4">
    <div class="row">
      <button type="button" class="btn btn-link mt-5 pull-left">
        <router-link :to="{ name: 'patient_general_question_category.list' }">Back</router-link>
      </button>
    </div>
    <div class="card mt-5">
      <div class="card-header">Add Patient Phone</div>
      <div class="card-body">
        <form @submit.prevent="onSubmit">
          <div class="form-row">
            <div class="form-group col-md-12">
              <label>Name</label>
              <text-field v-model="newPatientGeneralQuestion.name"></text-field>
            </div>
          </div>
          <div class="form-row">
            <div class="form-group col-md-12">
              <label>Description</label>
              <textarea class="form-control"
                v-model="newPatientGeneralQuestion.description"
                cols="38" rows="10"></textarea>
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
// import { FETCH_PATIENT_GENERAL_QUESTION_CATEGORIES } from "@/store/actions.type";

// import NumberField from "@/ehr_components/ehr_forms/NumberField.vue";
import TextField from "@/ehr_components/ehr_forms/TextField.vue";
// import SelectOption from "@/ehr_components/ehr_forms/SelectOption.vue";

export default {
  name: "PatientGeneralQuestionCategoryAdd",
  components: {
    // NumberField,
    TextField
    // SelectOption
  },
  data() {
    return {
      saving: false,
      success: false,
      currentItem: {},
      newPatientGeneralQuestion: {
        name: "",
        description: "",
      }
    };
  },
  methods: {
    onSubmit() {
      this.saving = true;
      let endpoint = "/api/v1/patient-general-question-category/";
      let method = "POST";
      apiService(endpoint, method, this.newPatientGeneralQuestion)
        .then(currentItem => {
          this.saving = false;
          this.success = true;
          this.$router.push({
            name: "patient_general_question_category.edit",
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
    // this.$store.dispatch(FETCH_PATIENT_GENERAL_QUESTION_CATEGORIES);
  }
};
</script>
