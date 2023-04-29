<template>

    <div class="explore_container" v-for="(postData, index) in data" :key="index">
        <div class="posts_container">
            <div>
                <div class="post_title">
                    <img alt="avatar-icon" src="../images/black_guy.webp" width="30px" height="30px"/>
                    <p>{{postData.user_id}}</p>
                </div>
                <div class="post_image">

                </div>
                <div class="post_body">
                    {{postData.caption}}
                </div>
                <div class="post_footer">
                    <p><img alt="heart-icon" src="../images/unliked.svg" width="20px" height="20px">{{postData.likes}} Likes</p>
                    <p>{{postData.created_on}}</p>
                </div>
            </div>
        </div>
        <div class="new_posts_button_container">
            <button v-on:click="makeNewPost">New Posts</button>
        </div>
    </div>
</template>


<script setup>
    import {ref, onMounted} from 'vue'
    let data = ref([])
    let csrf_token = ref("")

    function makeNewPost(){
        window.location.href = '/posts/new'
    }

    async function getCsrfToken() {
        await fetch('/api/v1/csrf-token')
        .then(async (response) => await response.json())
        .then(async (data) => {
        csrf_token.value = data.csrf_token;
        })
        .catch(async error => console.log(await error))
    }

    async function getPosts(){
        await fetch('/api/v1/posts', {
            method: 'GET',
            headers:{
                'X-CSRFToken':csrf_token.value
            }

        })
            .then(async response => {
                if(response.status){
                    let result = await response.json()
                    console.log(result)
                }

            })
            .catch(async error => {
                console.log(await error)
            })
    }

    onMounted(()=>{
        getCsrfToken()
        getPosts()
    })

</script>

<style>
.explore_container {
    display: flex;
    margin-right: 10px;
}

.posts_container {
    width: 80%;
    height: fit-content;
    display: flex;
    flex-direction: column;
    border: 0.5px solid grey;
    border-radius: 5px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.new_posts_button_container {
    width: 20%;
    text-align: center;
}

.post_title {
    display: flex;
    padding-top: 10px;
}

.post_title img {
    margin-left: 5px;
    margin-right: 8px;
    border-radius: 50%;
}

.post_image {
    height: 500px;
    background-image: url(../images/fitf.png);
    background-repeat: no-repeat;
    background-size: cover;
}

.post_body {
    padding: 10px 5px;
}

.post_footer {
    /* border: 1px solid red; */
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 25px;
    padding: 5px 5px;
    font-weight: bold;
}

.post_footer img{
    margin-right: 5px;
}


.new_posts_button_container button{
    background-color: rgb(59, 59, 250);
    border: 1px solid rgb(59, 59, 250);
    color: white;
    border-radius: 5px;
    margin-top: 5px;
}


</style>