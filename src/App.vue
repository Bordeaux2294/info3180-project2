<script setup>
import { ref } from "vue";
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";


let token = ref("");

</script>

<template>
  <AppHeader />

  <main>
    <RouterView />
  </main>
  
  <AppFooter />
</template>

<style>
body {
  padding-top: 75px;
}
</style>