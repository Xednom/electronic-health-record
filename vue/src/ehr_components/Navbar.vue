<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link class="navbar-brand" :to="{ name: 'Home' }"
      >Electronic Health Records</router-link
    >
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'Home' }"
            >Home</router-link
          >
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Company and Insurance
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link class="dropdown-item" :to="{ name: 'company.list' }"
              >List of Company</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'company.add' }"
              >Add a company</router-link
            >
            <hr>
            <router-link class="dropdown-item" :to="{ name: 'insurance.list' }"
              >List of Insurance</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'insurance.add' }"
              >Add an Insurance</router-link
            >
            <hr>
            <router-link class="dropdown-item" :to="{ name: 'insurance_rep.list' }"
              >List of Insurance Representative</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'insurance_rep.add' }"
              >Add an Insurance Representative</router-link
            >
          </div>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Patient Basic Information
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link class="dropdown-item" :to="{ name: 'patient_contact.list' }"
              >List of Patient Contact</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'patient_contact.add' }"
              >Add a Patient Contact</router-link
            >
            <hr>
            <router-link class="dropdown-item" :to="{ name: 'patient_address.list' }"
              >List of Patient Address</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'patient_address.add' }"
              >Add a Patient Address</router-link
            >
            <hr>
            <router-link class="dropdown-item" :to="{ name: 'patient_phone.list' }"
              >List of Patient Phone</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'patient_phone.add' }"
              >Add a Patient Phone</router-link
            >
          </div>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Patient Extended Information
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link class="dropdown-item" :to="{ name: 'patient_sibling.list' }"
              >List of Patient Sibling</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'patient_sibling.add' }"
              >Add a Patient Sibling</router-link
            >
            <hr>
            <router-link class="dropdown-item" :to="{ name: 'patient_general_question_category.list' }"
              >List of Patient General Question Category</router-link
            >
            <router-link class="dropdown-item" :to="{ name: 'patient_general_question_category.add' }"
              >Add a Patient General Question Category</router-link
            >
          </div>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style scoped>
.nav-item {
  margin: 0 20px 0 0;
}
.dropdown-menu {
  right:0;
  left:auto;
}
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-size: 100%;
}
</style>
