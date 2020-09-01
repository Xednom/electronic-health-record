import { apiService } from "@/common/api.service.js";
import {
  FETCH_PATIENT_PHONES,
  FETCH_A_PATIENT_PHONE,
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_PATIENT_PHONES,
  SET_A_PATIENT_PHONE,
} from "@/store/mutations.type";

const state = {
  // a list of state related to patient_phone

  patientPhones: [],
  patientPhone: {},
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  patientPhones: state => {
    return state.patientPhones;
  },
  patientPhone: state => {
    return state.patientPhone;
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
  [SET_PATIENT_PHONES](state, pPatientPhones) {
    state.patientPhones = pPatientPhones;
  },
  [SET_A_PATIENT_PHONE](state, pPatientPhone) {
    state.patientPhone = pPatientPhone;
  },
};

const actions = {
  // define actions like FETCH_A_PATIENT_PHONES

  [FETCH_PATIENT_PHONES]({ commit }) {
    let endpoint = `/api/v1/patient-phone/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_PATIENT_PHONES, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_PATIENT_PHONE]({ commit }, payload) {
    commit(FETCH_START);
    const patient_phone_id = payload;
    let endpoint = `/api/v1/patient-phone/${patient_phone_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_PATIENT_PHONE, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  },
};

export const patientPhones = {
  state,
  getters,
  mutations,
  actions
};
