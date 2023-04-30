<!-- viewing another users' profile -->

<template>

  <div class="col-md-4" v-for="user in users" :key="user.id">
    <div class="card">

      
      <div class="card-body">
        <img :src="user.profile_photo" class="card-img-top" id="profile-picture" alt="profile-picture" width="30px" height="30px">
        <p class="card-title">{{ user.firstname }}</p>
        <p class="card-title">{{ user.lastname }}</p>

        <div class="row">
          <div class="col-md-4 card-location">{{ user.location }}</div>
        </div>

        <div class="row">
          <div class="col-md-4">Joined On:</div>
          <div class="col-md-8">{{ user.joined_on }}</div>
        </div>

        <div class="row">
          <div class="col-md-8">{{ user.biography }}</div>
        </div>

        <div class="row">
          <div class="col-md-4">Followers:</div>
          <div class="col-md-8">{{ user.followers }}</div>
        </div>

        <button v-if="!isFollowing" @click="followUser" id="follow-button">Follow</button>
        <button v-else @click="unfollowUser" id="follow-button">Unfollow</button>

    </div>

    <div class="container">
    <div class="row">
        <div class="col-md-4" v-for="photo in photos" :key="photo.id">
        <img :src="photo.url" alt="photo">
        </div>
    </div>
    </div>
      
    </div>
  </div>

</template>



<script setup>

    import { ref, onMounted } from 'vue';

    let csrf_token = ref("");
    const isFollowing = ref(false);
    let users = ref([{
      id:1,
      profile_photo:"../images/black_guy.webp",
      firstname:"Allah",
      lastname:"Donkey",
      location:"St.Catherine",
      joined_on:"24 Apr 2023",
      biography:"I am a boy",
      followers:10

    }])

    let photos = ref([
      {
        id:1,
        url:"../images/under_pier.jpg"
      }
  ])

    async function getCsrfToken() {
        await fetch('/api/v1/csrf-token')
        .then(async (response) => await response.json())
        .then(async (data) => {
        csrf_token.value = data.csrf_token;
        })
        .catch(async error => console.log(await error))
    }

    async function followUser(id) {
    const formObject = new FormData();
    formObject.append('id', id);
    try {
        const response = await fetch(`/api/users/${id}/follow`, {
        method: 'POST',
        body: formObject,
        headers: {
            'X-CSRFTOKEN': csrf_token.value
        }
        })

        if (response.ok) {
            isFollowing.value = true;
            const button = document.getElementById('follow-button');
            button.textContent = 'Following';
        } else {
            console.log('Failed to follow user');
        }
        } catch (error) {
        console.log(error);
        }
    }

    async function unfollowUser(){

    }


    async function fetchPhotos(id) {
    const formObject = new FormData();
    try {
        const response = await fetch(`/api/v1/users/${id}/posts`, {
        method: 'GET',
        headers: {
            'X-CSRFTOKEN': csrf_token.value
        }
        });

        if (!response.ok) {
        throw new Error('Failed to fetch photos');
        }

        const data = await response.json();
        photos.value = data;
    } catch (error) {
        console.error(error);
    }
    }



    onMounted(() =>{
        // getCsrfToken()
    })
   
  
  
</script>

<style>
.card {
  border: 1px solid red;
  width: 1200px;
}

.card-body{
  border: 1px solid blue;
  display: flex;

}

.card-body img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: 1px solid green;
}

.card-title {
  margin-left: 5px;
}

.row {
  border: 1px solid yellow;
  display: flex;
  width: 40px;
  height: 25px;
  margin: 5px 5px;
}
</style>