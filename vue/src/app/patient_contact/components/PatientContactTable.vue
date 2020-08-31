<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'patient_contact.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Patient Contact</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Email Address</th>
              <th scope="col">First name</th>
              <th scope="col">Middle name</th>
              <th scope="col">Last name</th>
              <th scope="col">Gender</th>
              <th scope="col">Birthdate</th>
            </tr>
          </thead>
          <tbody v-if="!loading">
            <tr v-for="item in patientContacts" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'patient_contact.edit', params: { id: item.id } }"
                  >{{ item.email_address }}</router-link
                >
              </td>
              <td>{{ item.first_name }}</td>
              <td>{{ item.middle_name }}</td>
              <td>{{ item.last_name }}</td>
              <td>{{ item.gender }}</td>
              <td>{{ item.birthdate }}</td>
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

import { FETCH_PATIENT_CONTACTS } from "@/store/actions.type";

export default {
  name: "PatientContactTable",
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {
  },
  computed: {
    ...mapGetters(["patientContacts", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_CONTACTS);
  }
};
</script>
