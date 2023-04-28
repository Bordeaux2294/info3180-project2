<template>
    <div class="form_div1">
        <form @submit.prevent="register" id="register_form">
            <div class="input_div">
                <label for="username">Username</label>
                <input type="text" name="username">
            </div>
            <div class="input_div">
                <label for="password">Password</label>
                <input type="text" name="password">
            </div>
            <div class="input_div">
                <label for="firstname">Firstname</label>
                <input type="text" name="firstname">
            </div>
            <div class="input_div">
                <label for="lastname">Lastname</label>
                <input type="text" name="lastname">
            </div>
            <div class="input_div">
                <label for="email">Email</label>
                <input type="text" name="email">
            </div>
            <div class="input_div">
                <label for="location">Location</label>
                <input type="text" name="location">
            </div>
            <div class="input_div">
                <label for="biography">Biography</label>
                <textarea name="biography" id="" cols="10" rows="10"></textarea>
            </div>
            <div class="input_div">
                <label for="photo">Photo</label>
                <input type="file" name="photo">
            </div>
            <div class="input_div" id="input_div_button">
                <button type="submit">Register</button>
            </div>
        </form>
    </div>
</template>

<script setup>

import {ref, onMounted} from 'vue';

let csrf_token = ref("");

async function getCsrfToken() {
        await fetch('/api/v1/csrf-token')
        .then(async (response) => await response.json())
        .then(async (data) => {
        csrf_token.value = data.csrf_token;
        })
        .catch(async error => console.log(await error))
    }


async function register(){

    let register_form = document.getElementById('register_form');
    let form_data = new FormData(register_form);

    fetch('/api/v1/register', {
        method: 'POST',
        body: form_data,
        headers:{
            'X-CSRFToken':csrf_token.value
        }
    })
    .then(async function (response){
        if(response.ok){
            let result = await response.json()
            console.log(result)
            
        }else{
            alert("User could not be registered!")
        }
    })
    .catch (async function (error){
        console.log(await error)
    })

}

onMounted(()=> {
    getCsrfToken()
})



</script>

<style>

.form_div1 {
    border: 0.5px solid grey;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    padding: 15px 15px;
    width: 55%;
    box-shadow: 7px 7px 4px rgba(0, 0, 0, 0.25);
}

.input_div {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    margin-bottom: 5px;
}

.input_div label {
    font-weight: bold;
}

.input_div textarea {
    width: 65%;
}

#input_div_button {
    display: flex;
    align-items: center;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 15px;
}

#input_div_button button {
    background-color: rgb(49, 224, 49);
    border: 1px solid rgb(49, 224, 49);
    border-radius: 5px;
    width: 100%;
    height: 10%;
    color: white;
    font-weight: bold;
}

#input_div_button button:hover {
    background-color: rgb(115, 255, 115);
    border: 1px solid rgb(115, 255, 115);
}

#input_div_button button:active {
    background-color: rgb(27, 155, 27);
    border: 1px solid rgb(27, 155, 27);
}


</style>