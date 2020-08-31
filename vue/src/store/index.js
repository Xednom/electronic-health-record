import Vue from "vue";
import Vuex from "vuex";

import { companies } from "../store/modules/company.js";
import { insurances } from "../store/modules/insurance.js";
import { patientContacts } from "../store/modules/patient_contact.js";


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    companies,
    insurances,
    patientContacts
  }
});
