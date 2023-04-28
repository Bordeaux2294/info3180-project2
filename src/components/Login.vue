<template>
    <div>
        <div class="form_div">
        <form @submit.prevent="login" id="loginForm">
            <div class="form-group mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" name="username" v-model="username" class="form-control" />
            </div>
            <div class="form-group mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" name="password" ref="password" class="form-control" />
            </div>
            
            <button type="submit" id="login-btn" class="btn btn-primary login-btn">Login</button>

        </form>
      </div>
    </div>
</template>


<script setup>

import { ref, onMounted } from 'vue';

let csrf_token = ref("")

// const username = ref('');
// const password = ref('');

async function getCsrfToken() {
        await fetch('/api/v1/csrf-token')
        .then(async (response) => await response.json())
        .then(async (data) => {
        csrf_token.value = data.csrf_token;
        })
        .catch(async error => console.log(await error))
    }

async function login(){
    const form = document.getElementById('loginForm')
    const formObject = new FormData(form)
  fetch('/login',{
    method: 'POST',
    body: formObject,
    headers:{
        'X-CSRFToken':csrf_token.value
    }
  })
  .then(async function (response){
    if(response.ok){
      let result = await response.json()
      console.log(result)
    }else{
        alert("Could not login user!")
    }
  })
}

onMounted(() => {
    getCsrfToken()
})

</script>


<style>

.form_div {
    border: 0.5px solid grey;
    border-radius: 0px;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: space-evenly;
    padding: 15px 15px;
    width: 30%;
    height: 45%;
    box-shadow: 7px 7px 4px rgba(0, 0, 0, 0.25);
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    font-weight: bold;

}

.form-control {
  width: 20rem;
  max-width: 400px;
  border-radius: 0px;
  border: 0.5px solid grey;
}


.login-btn{
    background-color: rgb(58, 221, 58);
    border: 1px solid rgb(71, 207, 71);
    width: 20rem;
    margin-top: 1rem;
    margin-bottom: 1rem;
    max-width: 400px;
    align-items: center;
    border-radius: 0px;
}

.login-btn:hover {
  background-color: rgb(29, 142, 29);
}

</style>