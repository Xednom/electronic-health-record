<template>
  <div class="home">
    <main-menu-cards></main-menu-cards>
  </div>
</template>

<script>
// @ is an alias to /src
import MainMenuCards from "@/ehr_components/MainMenu.vue";

export default {
  name: "Home",
  components: {
    MainMenuCards
  }
};
</script>
