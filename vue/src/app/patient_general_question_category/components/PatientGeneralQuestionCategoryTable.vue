<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'patient_general_question_category.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Patient General Question Category</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Description</th>
            </tr>
          </thead>
          <tbody v-if="!loading">
            <tr v-for="item in patientGeneralQuestionCategories" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'patient_general_question_category.edit', params: { id: item.id } }"
                >{{ item.name }}</router-link>
              </td>
              <td>{{ item.description }}</td>
            </tr>
          </tbody>
          <tbody v-else>
            <div class="spinner-border" role="status">
              <span class="sr-only">Loading...</span>
            </div>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import { FETCH_PATIENT_GENERAL_QUESTION_CATEGORIES } from "@/store/actions.type";

export default {
  name: "PatientGeneralQuestionCategoryTable",
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {},
  computed: {
    ...mapGetters(["patientGeneralQuestionCategories", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_GENERAL_QUESTION_CATEGORIES);
  }
};
</script>
