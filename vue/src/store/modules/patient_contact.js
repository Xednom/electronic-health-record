import { apiService } from "@/common/api.service.js";
import {
  FETCH_PATIENT_CONTACTS,
  FETCH_A_PATIENT_CONTACT,
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_PATIENT_CONTACTS,
  SET_A_PATIENT_CONTACT,
} from "@/store/mutations.type";

const state = {
  // a list of state related to patient_contact

  patientContacts: [],
  patientContact: {},
  newPatientContact: {
    first_name: "",
    middle_name: "",
    last_name: "",
    email_address: "",
    gender: "",
    birthdate: null,
    contact_type: "",
    patient_relationship: "",

  },
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  patientContacts: state => {
    return state.patientContacts;
  },
  patientContact: state => {
    return state.patientContact;
  },
  loading: state => {
    return state.loading;
  }
};

const mutations = {
  // define mutations to redefine state value

  [FETCH_START](state) {
    state.loading = true;
  },
  [FETCH_END](state) {
    state.loading = false;
  },
  [SET_PATIENT_CONTACTS](state, pPatientContacts) {
    state.patientContacts = pPatientContacts;
  },
  [SET_A_PATIENT_CONTACT](state, pPatientContact) {
    state.patientContact = pPatientContact;
  },
};

const actions = {
  // define actions like FETCH_A_PATIENT_CONTACTS

  [FETCH_PATIENT_CONTACTS]({ commit }) {
    let endpoint = `/api/v1/patient-contact/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_PATIENT_CONTACTS, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_PATIENT_CONTACT]({ commit }, payload) {
    commit(FETCH_START);
    const patient_contact_id = payload;
    let endpoint = `/api/v1/patient-contact/${patient_contact_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_PATIENT_CONTACT, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  }
};

export const patientContacts = {
  state,
  getters,
  mutations,
  actions
};
