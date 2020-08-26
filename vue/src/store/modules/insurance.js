import { apiService } from "@/common/api.service.js";
import {
  FETCH_INSURANCES,
  FETCH_INSURANCE_REPS,
  FETCH_AN_INSURANCE,
  FETCH_AN_INSURANCE_REP
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_INSURANCES,
  SET_INSURANCE_REPS,
  SET_AN_INSURANCE 
} from "@/store/mutations.type";

const state = {
  // a list of state related to insurance

  insurances: [],
  insuranceReps: [],
  insurance: {},
  insuranceRep: {},
  newInsurance: {
    address_1: "",
    address_2: "",
    city: "",
    state: "",
    zip_code: "",
    phone: ""
  },
  newInsuranceRep: {
    insurance: null,
    first_name: "",
    last_name: "",
    phone_1: "",
    phone_2: "",
    email_address: ""
  },
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  insurances: state => {
    return state.insurances;
  },
  insuranceReps: state => {
    return state.insuranceReps;
  },
  insurance: state => {
    return state.insurance;
  },
  insuranceRep: state => {
    return state.insuranceRep;
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
  [SET_INSURANCES](state, pInsurances) {
    state.insurances = pInsurances;
  },
  [SET_INSURANCE_REPS](state, pInsuranceReps) {
    state.insuranceReps = pInsuranceReps;
  },
  [SET_AN_INSURANCE](state, pInsurance) {
    state.insurance = pInsurance;
  },
  [SET_AN_INSURANCE_REPS](state, pInsuranceRep) {
    state.insuranceRep = pInsuranceRep;
  },
};

const actions = {
  // define actions like FETCH_AN_INSURANCE

  [FETCH_INSURANCES]({ commit }) {
    let endpoint = `/api/v1/insurance/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_INSURANCES, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_INSURANCE_REPS]({ commit }) {
    let endpoint = `/api/v1/insurance-rep/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_INSURANCE_REPS, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_AN_INSURANCE]({ commit }, payload) {
    commit(FETCH_START);
    const insurance_id = payload;
    let endpoint = `/api/v1/insurance/${insurance_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_AN_INSURANCE, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  },
  [FETCH_AN_INSURANCE_REP]({ commit }, payload) {
    commit(FETCH_START);
    const insurance_rep_id = payload;
    let endpoint = `/api/v1/insurance-rep/${insurance_rep_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_AN_INSURANCE_REP, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  }
};

export const insurances = {
  state,
  getters,
  mutations,
  actions
};
