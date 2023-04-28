<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">VueJS with Flask</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li v-if="token" class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li v-if="token" class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
            <li v-if="token" class="nav-item">
              <RouterLink class="nav-link" to="/" @click="logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";

let token = ref("");

async function setToken() {
  token.value = localStorage.getItem('user-token')
}

onMounted(() => {
  setToken()
})

function logout() {
  localStorage.removeItem('user-token')
  token.value = null
  window.location.reload()
}

</script>

<style>
/* Add any component specific styles here */
</style>