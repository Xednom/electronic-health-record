import { apiService } from "@/common/api.service.js";
import {
  FETCH_PATIENT_SIBLINGS,
  FETCH_A_PATIENT_SIBLING
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_PATIENT_SIBLINGS,
  SET_A_PATIENT_SIBLING,
} from "@/store/mutations.type";

const state = {
  // a list of state related to patient_sibling

  patientSiblings: [],
  patientSibling: {},
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  patientSiblings: state => {
    return state.patientSiblings;
  },
  patientSibling: state => {
    return state.patientSibling;
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
  [SET_PATIENT_SIBLINGS](state, pPatientSiblings) {
    state.patientSiblings = pPatientSiblings;
  },
  [SET_A_PATIENT_SIBLING](state, pPatientSibling) {
    state.patientSibling = pPatientSibling;
  },
};

const actions = {
  // define actions like FETCH_A_PATIENT_SIBLINGS

  [FETCH_PATIENT_SIBLINGS]({ commit }) {
    let endpoint = `/api/v1/patient-sibling-b03/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_PATIENT_SIBLINGS, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_PATIENT_SIBLING]({ commit }, payload) {
    commit(FETCH_START);
    const patient_sibling_id = payload;
    let endpoint = `/api/v1/patient-sibling-b03/${patient_sibling_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_PATIENT_SIBLING, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  },
};

export const patientSiblings = {
  state,
  getters,
  mutations,
  actions
};
