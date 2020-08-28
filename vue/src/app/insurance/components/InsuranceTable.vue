<template>
  <div class="container">
    <div class="mt-5">
      <router-link :to="{ name: 'insurance.add' }">Add</router-link>
    </div>
    <div class="card mt-5">
      <div class="card-header">Manage Insurances</div>
      <div class="card-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">Address 1</th>
              <th scope="col">Address 2</th>
              <th scope="col">City</th>
              <th scope="col">State</th>
              <th scope="col">Zip code</th>
              <th scope="col">Phone</th>
            </tr>
          </thead>
          <tbody v-if="!loading">
            <tr v-for="item in insurances" :key="item.id">
              <td>
                <router-link
                  :to="{ name: 'insurance.edit', params: { id: item.id } }"
                  >{{ item.address_1 }}</router-link
                >
              </td>
              <td>{{ item.address_2 }}</td>
              <td>{{ item.city }}</td>
              <td>{{ item.state }}</td>
              <td>{{ item.zip_code }}</td>
              <td>{{ item.phone }}</td>
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

import { FETCH_INSURANCES } from "@/store/actions.type";

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
    ...mapGetters(["insurances", "loading"])
  },
  mounted() {
    this.$store.dispatch(FETCH_INSURANCES);
  }
};
</script>
