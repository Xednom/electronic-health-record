import { apiService } from "@/common/api.service.js";
import {
  FETCH_PATIENT_GENERAL_QUESTION_CATEGORIES,
  FETCH_A_PATIENT_GENERAL_QUESTION_CATEGORY
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_PATIENT_GENERAL_QUESTION_CATEGORIES,
  SET_A_PATIENT_GENERAL_QUESTION_CATEGORY,
} from "@/store/mutations.type";

const state = {
  // a list of state related to patient_general_question_category

  patientGeneralQuestionCategories: [],
  patientGeneralQuestionCategory: {},
  loading: false,
  saving: false
};

const getters = {
  // define method to access state value

  patientGeneralQuestionCategories: state => {
    return state.patientGeneralQuestionCategories;
  },
  patientGeneralQuestionCategory: state => {
    return state.patientGeneralQuestionCategory;
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
  [SET_PATIENT_GENERAL_QUESTION_CATEGORIES](state, pPatientGeneralQuestionCategories) {
    state.patientGeneralQuestionCategories = pPatientGeneralQuestionCategories;
  },
  [SET_A_PATIENT_GENERAL_QUESTION_CATEGORY](state, pPatientGeneralQuestionCategory) {
    state.patientGeneralQuestionCategory = pPatientGeneralQuestionCategory;
  },
};

const actions = {
  // define actions like FETCH_A_PATIENT_GENERAL_QUESTION_CATEGORIES

  [FETCH_PATIENT_GENERAL_QUESTION_CATEGORIES]({ commit }) {
    let endpoint = `/api/v1/patient-general-question-category/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_PATIENT_GENERAL_QUESTION_CATEGORIES, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_PATIENT_GENERAL_QUESTION_CATEGORY]({ commit }, payload) {
    commit(FETCH_START);
    const patient_general_question_category_id = payload;
    let endpoint = `/api/v1/patient-general-question-category/${patient_general_question_category_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_PATIENT_GENERAL_QUESTION_CATEGORY, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  },
};

export const patientGeneralQuestionCategories = {
  state,
  getters,
  mutations,
  actions
};
