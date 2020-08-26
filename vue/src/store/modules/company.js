import { apiService } from "@/common/api.service.js";
import {
  FETCH_COMPANIES,
  FETCH_A_COMPANY,
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_COMPANIES,
  SET_A_COMPANY,
} from "@/store/mutations.type";

const state = {
  // a list of state related to company

  companies: [],
  company: {},
  newCompany: {
    name: "",
    address_1: "",
    address_2: "",
    city: "",
    state: "",
    zip_code: "",
  },
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  companies: state => {
    return state.companies;
  },
  company: state => {
    return state.company;
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
  [SET_COMPANIES](state, pCompanies) {
    state.companies = pCompanies;
  },
  [SET_A_COMPANY](state, pCompany) {
    state.company = pCompany;
  },
};

const actions = {
  // define actions like FETCH_A_COMPANY

  [FETCH_COMPANIES]({ commit }) {
    let endpoint = `/api/v1/company/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_COMPANIES, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_COMPANY]({ commit }, payload) {
    commit(FETCH_START);
    const company_id = payload;
    let endpoint = `/api/v1/company/${company_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_COMPANY, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  }
};

export const companies = {
  state,
  getters,
  mutations,
  actions
};
