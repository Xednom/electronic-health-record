<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'patient_phone.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Patient Phone</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Patient Contact</th>
              <th scope="col">Phone</th>
              <th scope="col">Phone type</th>
              <th scope="col">Primary</th>
            </tr>
          </thead>
          <tbody v-if="!loading">
            <tr v-for="item in patientPhones" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'patient_phone.edit', params: { id: item.id } }"
                >{{ item.patient_contact }}</router-link>
              </td>
              <td>{{ item.phone }}</td>
              <td>{{ item.phone_type }}</td>
              <template v-if="item.primary">
                <td>
                  <i class="fa fa-check"></i>
                </td>
              </template>
              <template v-else-if="!item.primary">
                <td>
                  <i class="fa fa-times"></i>
                </td>
              </template>
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

import { FETCH_PATIENT_PHONES } from "@/store/actions.type";

export default {
  name: "PatientPhoneTable",
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {},
  computed: {
    ...mapGetters(["patientPhones", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_PHONES);
  }
};
</script>
