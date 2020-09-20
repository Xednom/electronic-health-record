import { apiService } from "@/common/api.service.js";
import {
  FETCH_PATIENT_GENERAL_QUESTION_CATEGORIES,
  FETCH_A_PATIENT_GENERAL_QUESTION_CATEGORY,
  FETCH_A_PATIENT_GENERAL_QUESTION_B04S,
  FETCH_PATIENT_GENERAL_QUESTIONS_B04S,
  FETCH_A_PATIENT_GENERAL_QUESTION_B04,
  FETCH_PATIENT_GENERAL_QUESTIONS_B04
} from "@/store/actions.type";
import {
  FETCH_START,
  FETCH_END,
  SET_PATIENT_GENERAL_QUESTION_CATEGORIES,
  SET_A_PATIENT_GENERAL_QUESTION_CATEGORY,
  SET_A_PATIENT_GENERAL_QUESTION_B04S,
  SET_PATIENT_GENERAL_QUESTIONS_B04S,
  SET_A_PATIENT_GENERAL_QUESTION_B04,
  SET_PATIENT_GENERAL_QUESTIONS_B04
} from "@/store/mutations.type";

const state = {
  // a list of state related to patient_general_question_category

  patientGeneralQuestionCategories: [],
  patientGeneralQuestionCategory: {},
  patientGeneralQuestionb04s: [],
  patientGeneralQuestionsB04s: {},
  patientGeneralQuestionB04: [],
  patientGeneralQuestionsB04: {},
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
  patientGeneralQuestionsB04s: state => {
    return state.patientGeneralQuestionsB04s;
  },
  patientGeneralQuestionB04s: state => {
    return state.patientGeneralQuestionB04s;
  },
  patientGeneralQuestionsB04: state => {
    return state.patientGeneralQuestionsB04;
  },
  patientGeneralQuestionB04: state => {
    return state.patientGeneralQuestionB04;
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
  [SET_PATIENT_GENERAL_QUESTIONS_B04S](state, pPatientGeneralQuestionsB04s) {
    state.patientGeneralQuestionsB04s = pPatientGeneralQuestionsB04s;
  },
  [SET_A_PATIENT_GENERAL_QUESTION_B04S](state, pPatientGeneralQuestionB04s) {
    state.patientGeneralQuestionB04s = pPatientGeneralQuestionB04s;
  },
  [SET_PATIENT_GENERAL_QUESTIONS_B04](state, pPatientGeneralQuestionsB04) {
    state.patientGeneralQuestionsB04 = pPatientGeneralQuestionsB04;
  },
  [SET_A_PATIENT_GENERAL_QUESTION_B04](state, pPatientGeneralQuestionB04) {
    state.patientGeneralQuestionB04 = pPatientGeneralQuestionB04;
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
  [FETCH_PATIENT_GENERAL_QUESTIONS_B04S]({ commit }) {
    let endpoint = `/api/v1/patient-general-question-b04s/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_PATIENT_GENERAL_QUESTIONS_B04S, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_PATIENT_GENERAL_QUESTION_B04S]({ commit }, payload) {
    commit(FETCH_START);
    const patient_general_question_b04s_id = payload;
    let endpoint = `/api/v1/patient-general-question-b04s/${patient_general_question_b04s_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_PATIENT_GENERAL_QUESTION_B04S, data);
        commit(FETCH_END);
      })
      .catch(err => {
        console.log(err);
      });
  },
  [FETCH_PATIENT_GENERAL_QUESTIONS_B04]({ commit }) {
    let endpoint = `/api/v1/patient-general-question-b04/`;
    commit(FETCH_START);
    apiService(endpoint)
      .then(response => {
        commit(SET_PATIENT_GENERAL_QUESTIONS_B04, response);
        commit(FETCH_END);
      })
      .catch(error => {
        console.log(error);
      });
  },
  [FETCH_A_PATIENT_GENERAL_QUESTION_B04]({ commit }, payload) {
    commit(FETCH_START);
    const patient_general_question_b04_id = payload;
    let endpoint = `/api/v1/patient-general-question-b04/${patient_general_question_b04_id}/`;
    apiService(endpoint)
      .then(data => {
        commit(SET_A_PATIENT_GENERAL_QUESTION_B04, data);
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
