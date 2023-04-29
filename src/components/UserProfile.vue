<!-- viewing another users' profile -->

<template>

  <div class="col-md-4" v-for="user in users" :key="user.id">
    <div class="card">

      <img :src="user.profile_photo" class="card-img-top" id="profile-picture" alt="profile-picture">

      <div class="card-body">
        <p class="card-title">{{ user.firstname }}</p>
        <p class="card-title">{{ user.lastname }}</p>

        <div class="row mb-3">
          <div class="col-md-4">{{ user.location }}</div>
        </div>

        <div class="row mb-3">
          <div class="col-md-4">Joined On:</div>
          <div class="col-md-8">{{ user.joined_on }}</div>
        </div>

        <div class="row mb-3">
          <div class="col-md-8">{{ user.biography }}</div>
        </div>

        <div class="row mb-3">
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
        getCsrfToken()
    })
   
  
  
</script>