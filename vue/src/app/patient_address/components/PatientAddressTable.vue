<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'patient_address.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Patient Address</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Patient Contact</th>
              <th scope="col">City</th>
              <th scope="col">State</th>
              <th scope="col">Zip Code</th>
            </tr>
          </thead>
          <tbody v-if="!loading">
            <tr v-for="item in patientAddresses" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'patient_address.edit', params: { id: item.id } }"
                  >{{ item.patient_contact }}</router-link
                >
              </td>
              <td>{{ item.city }}</td>
              <td>{{ item.state }}</td>
              <td>{{ item.zip_code }}</td>
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

import { FETCH_PATIENT_ADDRESSES } from "@/store/actions.type";

export default {
  name: "PatientAddressTable",
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {
  },
  computed: {
    ...mapGetters(["patientAddresses", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_PATIENT_ADDRESSES);
  }
};
</script>
