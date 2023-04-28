<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img alt="photogram logo" class="photogram_logo" src="../images/igicon.svg" width="20px" height="20px"/>
        </a>
        <a class="navbar-brand" href="/">Photogram</a>
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
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/">Logout</RouterLink>
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

.photogram-logo {
  max-height: 30px;
}

.navbar-brand {
  font-family: 'Brush Script MT', cursive;
  font-size: 25px;
  display: flex;
  align-items: center;
}

.navbar-nav {
  margin-left: auto;
}
</style>