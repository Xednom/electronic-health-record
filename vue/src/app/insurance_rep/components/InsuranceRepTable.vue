<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'insurance_rep.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Insurance Representatives</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">First name</th>
              <th scope="col">Last name</th>
              <th scope="col">Phone 1</th>
              <th scope="col">Phone 2</th>
              <th scope="col">Email Address</th>
            </tr>
          </thead>
          <tbody v-if="!loading">
            <tr v-for="item in insuranceReps" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'insurance_rep.edit', params: { id: item.id } }"
                  >{{ item.email_address }}</router-link
                >
              </td>
              <td>{{ item.first_name }}</td>
              <td>{{ item.last_name }}</td>
              <td>{{ item.phone_1 }}</td>
              <td>{{ item.phone_2 }}</td>
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

import { FETCH_INSURANCE_REPS } from "@/store/actions.type";

export default {
  name: "InsuranceTable",
  props: {
    id: {
      type: Number,
      default: 0
    }
  },
  methods: {},
  computed: {
    ...mapGetters(["insuranceReps", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_INSURANCE_REPS);
  }
};
</script>
