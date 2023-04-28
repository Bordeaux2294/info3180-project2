<script setup>
import { ref, onMounted } from "vue";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.")


onMounted(() => {
  getPosts()
})

async function getPosts() {
  fetch('/api/v1/posts', {
    method: "GET",
    headers: {
    Accept: "application/json",
    Authorization: "Bearer " + localStorage.getItem('user-token'),
    "Content-Type": "application/json",
    }
  })
    .then(async function (response) {
      if (response.ok) {
        let result = await response.json()
        console.log(result)
      }
      else if (response.status == 401) {
        localStorage.removeItem('user-token')
        window.location.reload()
      }
    })
    .catch(async function (error) {
      console.log(await error)
    })
}

</script>

<template>
  <div class="container">
    <div class="text-center">
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
      <h1>{{ message }}</h1>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */
</style>