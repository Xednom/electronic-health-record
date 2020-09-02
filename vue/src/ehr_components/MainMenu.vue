<template>
  <div class="container">
    <div class="card-deck">
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Company App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'company.list' }">List of Company</router-link>
            <br />
            <router-link :to="{ name: 'company.add' }">Add a Company</router-link>
          </p>
        </div>
      </div>
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Insurance App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'insurance.list' }">List of Insurance</router-link>
            <br />
            <router-link :to="{ name: 'insurance.add' }">Add an Insurance</router-link>
          </p>
        </div>
      </div>
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Insurance Representative App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'insurance_rep.list' }">List of Insurance Representative</router-link>
            <br />
            <router-link :to="{ name: 'insurance_rep.add' }">Add an Insurance Representative</router-link>
          </p>
        </div>
      </div>
    </div>
    <div class="card-deck">
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Patient Contact App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'patient_contact.list' }">List of Patient Contact</router-link>
            <br />
            <router-link :to="{ name: 'patient_contact.add' }">Add a Patient Contact</router-link>
          </p>
        </div>
      </div>
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Patient Address App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'patient_address.list' }">List of Patient Address</router-link>
            <br />
            <router-link :to="{ name: 'patient_address.add' }">Add a Patient Address</router-link>
          </p>
        </div>
      </div>
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Patient Phone App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'patient_phone.list' }">List of Patient Phone</router-link>
            <br />
            <router-link :to="{ name: 'patient_phone.add' }">Add a Patient Phone</router-link>
          </p>
        </div>
      </div>
    </div>
    <div class="card-deck">
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Patient Sibling App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'patient_sibling.list' }">List of Patient Sibling</router-link>
            <br />
            <router-link :to="{ name: 'patient_sibling.add' }">Add a Patient Sibling</router-link>
          </p>
        </div>
      </div>
      <div class="card border-info mb-3" style="max-width: 18rem;">
        <div class="card-header">Patient General Question Category App</div>
        <div class="card-body">
          <p class="card-link">
            <router-link :to="{ name:'patient_general_question_category.list' }">List of Patient General Question Category</router-link>
            <br />
            <router-link :to="{ name: 'patient_general_question_category.add' }">Add a Patient General Question Category</router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>