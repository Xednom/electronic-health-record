<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'patient_sibling.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Patient Sibling</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Patient Contact</th>
              <th scope="col">First name</th>
              <th scope="col">Middle name</th>
              <th scope="col">Last name</th>
              <th scope="col">Relationship</th>
              <th scope="col">Age</th>
            </tr>
          </thead>
          <tbody v-if="!loading">
            <tr v-for="item in patientSiblings" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'patient_sibling.edit', params: { id: item.id } }"
                >{{ item.patient_contact_b00_rec }}</router-link>
              </td>
              <td>{{ item.first_name }}</td>
              <td>{{ item.middle_name }}</td>
              <td>{{ item.last_name }}</td>
              <td>{{ item.relationship }}</td>
              <td>{{ item.age }}</td>
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

import { FETCH_PATIENT_SIBLINGS } from "@/store/actions.type";

export default {
  name: "PatientSiblingTable",
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {},
  computed: {
    ...mapGetters(["patientSiblings", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_SIBLINGS);
  }
};
</script>
