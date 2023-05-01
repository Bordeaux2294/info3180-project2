<template>

    <div class="new_post_container">
        <form @submit.prevent="makeNewPost" id="new_post_form" enctype="multipart/form-data">
            <label for="photo">Photo</label>
            <input type="file" name="photo">
            <label for="caption">Caption</label>
            <input type="text" name="caption">
            <button type="submit">Submit</button>
        </form>
    </div>

</template>


<script setup>
    import {ref, onMounted} from 'vue'


    let user_data = sessionStorage.getItem('current_user')

    let csrf_token = ref("");
    let current_user = ref(JSON.parse(user_data))


    async function getCsrfToken() {
            await fetch('/api/v1/csrf-token')
            .then(async (response) => await response.json())
            .then(async (data) => {
            csrf_token.value = data.csrf_token;
            })
            .catch(async error => console.log(await error))
        }

    function makeNewPost(){
        const form = document.getElementById('new_post_form')
        const formData = new FormData(form)

        // console.log(current_user.value['message'])
        fetch(`/api/v1/users/${current_user.value['id']}/posts`, {
        method: 'POST',
        body: formData,
        headers:{
            'X-CSRFToken':csrf_token.value
        }
            })
            .then(async function (response){
                if(response.ok){
                    let result = await response.json()
                    alert(result['message'])
                    window.location.href = '/explore'
                    
                }else{
                    alert("New post could not be created!")
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
.new_post_container {
    border: 1px solid grey;
    border-radius: 10px;
    background-color: burlywood;
    display: flex;
    height: 80%;
}

.new_post_container form {
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    padding: 5px 5px;
}

.new_post_container label {
    margin-top: 20px;
}

.new_post_container button {
    width: 45%;
    height: 30px;
    color: white;
    background-color: rgb(34, 212, 34);
    border: 1px solid rgb(34, 212, 34);
    border-radius: 5px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 25px;
}

</style>