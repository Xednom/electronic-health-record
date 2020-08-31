import { apiService } from "@/common/api.service.js";
import {
  FETCH_PATIENT_ADDRESSES,
  FETCH_A_PATIENT_ADDRESS,
  FETCH_PATIENT_CONTACTS
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_PATIENT_ADDRESSES,
  SET_PATIENT_CONTACTS,
  SET_A_PATIENT_ADDRESS,
} from "@/store/mutations.type";

const state = {
  // a list of state related to patient_address

  patientAddresses: [],
  patientContacts: [],
  patientAddress: {},
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  patientAddresses: state => {
    return state.patientAddresses;
  },
  patientContacts: state => {
    return state.patientContacts;
  },
  patientAddress: state => {
    return state.patientAddress;
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
  [SET_PATIENT_ADDRESSES](state, pPatientAddresses) {
    state.patientAddresses = pPatientAddresses;
  },
  [SET_A_PATIENT_ADDRESS](state, pPatientAddress) {
    state.patientAddress = pPatientAddress;
  },
  [SET_PATIENT_CONTACTS](state, pPatientContacts) {
    state.patientContacts = pPatientContacts;
  },
};

const actions = {
  // define actions like FETCH_A_PATIENT_ADDRESSES

  [FETCH_PATIENT_ADDRESSES]({ commit }) {
    let endpoint = `/api/v1/patient-address/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_PATIENT_ADDRESSES, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_PATIENT_ADDRESS]({ commit }, payload) {
    commit(FETCH_START);
    const patient_address_id = payload;
    let endpoint = `/api/v1/patient-address/${patient_address_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_PATIENT_ADDRESS, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  },
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
};

export const patientAddresses = {
  state,
  getters,
  mutations,
  actions
};
