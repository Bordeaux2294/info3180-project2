<script setup>
import { ref, onMounted } from "vue";
import { default as router } from './../router';
let posts = ref("");
let csrf_token = ref("");
onMounted(() => {
    getCsrfToken()
    getPosts()
})
async function getCsrfToken() {
  await fetch('/api/v1/csrf-token')
    .then(async (response) => await response.json())
    .then(async (data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch(async error => console.log(await error))
}
async function getPosts() {
  fetch('/api/v1/posts', {
    method: "GET",
    headers: {
        'X-CSRFToken':csrf_token.value
    }
  })
  .then(async function (response) {
      if (response.ok) {
        return response.json()
      }
      else if (response.status == 401) {
        localStorage.removeItem('user-token')
        window.location.reload()
      }
    }).then((data) => {
      posts.value = data.posts;
      console.log(posts.value)
    })
    .catch(async function (error) {
      console.log(await error)
    })
}
async function likePost(post_id) {
  fetch('/api/v1/posts/'+post_id+'/like', {
    method: "POST",
    headers: {
      'X-CSRFToken': csrf_token.value,
    }
  })
    .then(async function (response) {
      if (response.ok) {
        getPosts();
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
function newPost() {
  router.push('/posts/new')
}
function userPosts(user_id) {
  router.push('/users/'+user_id)
}
</script>

<template>
  <div class="container">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="posts_container">
        <div v-for="post in posts" class="post">
          <div class="post_title" @click="userPosts(post.user_id)">
            <div class="user_img_container">
               <img :src="post.user_profile" class="user_img"/>
            </div>
            <div class="username">{{post.username}}</div>
          </div>
          <div class="post_img"> 
            <img :src="post.photo" class="img"/>
          </div>
          <div class="post_description">{{ post.caption }}</div>
          <div class="post_footer">
            <span class="like_container" @click="likePost(post.id)"><i class="icons icon_style fa fa-heart-o"></i><div class="post_likes">{{ post.likes }}</div></span>
            <div class="post_date">{{post.created_on}}</div>
          </div>
        </div>
    </div>
    <div class="text-center post_nav">
      <div class="input_div" id="div_button">
          <button type="submit" @click="newPost">New Post</button>
      </div>
    </div>
  </div>
</template>

<style>
.container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: auto;
    height: max-content;
}
.post_title{
  display: flex;
}
.post_title:hover{
  cursor: pointer;
}
.posts_container{
    display: flex;
    flex-direction: column;
    max-width: 450px;
    width: 100%;
    margin-right: 50px;
}
.post{
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 450px;
    border: 1px solid #afafaf;
    border-radius: 4px;
    margin-bottom: 30px;
}
.post_img{
    display: flex;
    width: 450px;
    height: 250px;
    min-width: 200px;
    position: relative;
    overflow: hidden;
}
.post_footer{
  display: flex;
  justify-content: space-between;
}
.like_container{
    display: flex;
    flex-direction: row;
    align-content: flex-start;
    align-items: center;
}
.icon_style{
  font-size: 13px !important ;
  margin-right: 3px;
  margin-left: 3px;
}
.like_container:hover{
  cursor: pointer;
}
.img {
    width: 450px;
    height: 250px;
    object-fit: cover;
    object-position: center center; 
}
.user_img_container{
    display: flex;
    width: 25px;
    height: 25px;
    position: relative;
    overflow: hidden;
    margin: 5px 0;
}
.user_img {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    object-fit: cover;
    object-position: center center; 
}
.username{
  margin: 5px 10px;
}
.form_div {
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


.post_nav{
    min-width: 200px;
    margin-bottom: auto;
    margin-top: 5px;
}
#div_button {
    display: flex;
    align-items: center;
}
#div_button button {
    background-color: rgb(49, 224, 49);
    border: 1px solid rgb(49, 224, 49);
    border-radius: 5px;
    width: 100%;
    height: 10%;
    color: white;
    font-weight: bold;
}
#div_button button:hover {
    background-color: rgb(115, 255, 115);
    border: 1px solid rgb(115, 255, 115);
}
#div_button button:active {
    background-color: rgb(27, 155, 27);
    border: 1px solid rgb(27, 155, 27);
}
</style>


















































<!-- <template>

    <div class="explore_container" v-for="(postData, index) in data" :key="index">
        <div class="posts_container">
            <div>
                <div class="post_title">
                    <img alt="avatar-icon" src="" width="30px" height="30px"/>
                    <p>{{postData.id}}</p>
                </div>
                <div class="post_image" :style="{ backgroundImage: `url(${getUserPhoto(postData.photo)})` }">

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
    </div>
    <div class="new_posts_button_container">
            <button v-on:click="makeNewPost">New Posts</button>
        </div>
</template>


<script setup>
    import {ref, onMounted} from 'vue'
    let data = ref([])
    let csrf_token = ref("")

    function makeNewPost(){
        window.location.href = '/posts/new'
    }

    async function getUserPhoto(nameofphoto){
        let photo = nameofphoto
        let postPhoto = ""
        await fetch(`/api/v1/photos/${photo}`)
            .then(async response => {
                if(response.ok){
                    let blob = await response.blob()
                    return blob
                }else{
                    alert("Could not retrieve post photo")
                }
            })

            .then(async blob => {
                let arrayBuffer = await blob.arrayBuffer()
                let url = URL.createObjectURL(new Blob([arrayBuffer], { type: blob.type }))
                postPhoto = url
                console.log(postPhoto)
            })

            .catch(async error => console.log(await error))
        return postPhoto
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
                    data.value = result
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
    /* background-image: url(../images/fitf.png); */
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


</style> -->