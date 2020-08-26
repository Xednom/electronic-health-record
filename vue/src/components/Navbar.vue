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
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'About' }"
            >About</router-link
          >
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="navbarDropdownMenuLink"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
            ><i class="fa fa-user"></i
          ></a>
          <!-- uncomment this when the login system is present -->
          <!-- <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <hr />
            <a class="dropdown-item" href="/accounts/logout/">Logout</a>
          </div> -->
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

<style>
.nav-item {
  margin: 0 20px 0 0;
}
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-size: 100%;
}
</style>
