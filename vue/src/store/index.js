import Vue from "vue";
import Vuex from "vuex";

import { companies } from "../store/modules/company.js";
import { insurances } from "../store/modules/insurance.js";
import { patientContacts } from "../store/modules/patient_contact.js";
import { patientAddresses } from "../store/modules/patient_address.js";
import { patientPhones } from "../store/modules/patient_phone.js";
import { patientSiblings } from "../store/modules/patient_sibling.js";
import { patientGeneralQuestionCategories } from "../store/modules/patient_general_question.js";


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    companies,
    insurances,
    patientContacts,
    patientAddresses,
    patientPhones,
    patientSiblings,
    patientGeneralQuestionCategories
  }
});
