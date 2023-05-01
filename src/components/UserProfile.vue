<!-- viewing another users' profile -->

<template>

  <div class="user-card">
    <div class="card mx-auto">

      
      <div class="card-body">
        <img :src="users.profile_photo" class="card-img-top" id="profile-picture" alt="profile-picture" width="110px" height="130px">

        
        <div class ="card-user-info">
        <p class="card-title">{{ users.firstname }} {{ users.lastname }}</p>
        <p class="card-location">{{ users.location }}</p>
        <p class="card-member-since"> Member since {{ users.joined_on }}</p>
        <p class="card-biography">{{ users.biography }}</p>
        </div>


        <div class="card-follow-post-info">

        <div class="card-fol">
          <div class="card-followers-count">{{ users.followers }}</div>
          <div class="card-followers">Followers</div>
        </div>

        <div>
          <div class="card-post-count">{{ users.posts }}</div>
          <div class="card-posts">Posts</div>
        </div>

        <div class="card-button-follow">
       
        <button v-if="isFollowing" @click="followUser(users.id)" id="follow-button">Follow</button>
        <button v-else @click="unfollowUser" id="follow-button">Unfollow</button>
      
        </div>
        </div>
    </div>

      </div>
  </div>

      <div class="photo-grid">
        <img v-for="photo in photos.posts" :key="photo.id" :src="photo.photo" alt="photo" class="photo-post" height="80px" width="80px">
      </div>
      


</template>



<script setup>

    import { ref, onMounted } from 'vue';

    let user_data = sessionStorage.getItem('current_user')
    let current_user = JSON.parse(user_data)

    let csrf_token = ref("");
    const isFollowing = ref(false);
    let users = ref({
      id:1,
      profile_photo:"",
      firstname:"Allah",
      lastname:"Donkey",
      location:"St.Catherine",
      joined_on:"24 Apr 2023",
      biography:"I am a boy",
      followers:10

    })

    let photos = ref([])

    async function getCsrfToken() {
        await fetch('/api/v1/csrf-token')
        .then(async (response) => await response.json())
        .then(async (data) => {
        csrf_token.value = data.csrf_token;
        })
        .catch(async error => console.log(await error))
    }

    async function followUser(id) {
    try {
        const response = await fetch(`/api/v1/users/${id}/follow`, {
        method: 'POST',
        body: id,
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


    async function getProfile(){
      const user_id = window.location.pathname.split('/').pop()
      await fetch(`/api/v1/get_profile/${user_id}`,{
        method:'GET',
        headers:{
          'X-CSRFTOKEN': csrf_token.value
        }
      })
        .then(async response => {
            if(response.status){
              let result = await response.json()
              console.log(result)
              users.value = result
            }else{
              alert("Could not get User Profile!")
            }
        })

        .catch(async error => {
          console.log(await error)
        })
    }

    async function fetchPhotos(id) {
    try {
        const id = window.location.pathname.split('/').pop()
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
        // console.log(photos.value.posts[0].photo)
    } catch (error) {
        console.error(error);
    }
    }



    onMounted(() =>{
        getCsrfToken()
        getProfile()
        if(users.value.followers > 0){
          isFollowing.value = true
          const button = document.getElementById('follow-button');
          button.innerHTML = 'Following';
        }
        fetchPhotos(current_user.id)
    })
   
  
  
</script>


<style>

.card {
  width: 1200px;
  margin: 0 auto;
  margin-top: 10px;
}

.card-body{
  display: flex;
  border-radius: 10px;
  box-shadow: 0px 3px 2px rgba(0, 0, 0, 0.2);
}



.card-body img {
  width: 110px;
  height: 130px;
  border-radius: 0;
  border: 1px solid green;
  margin-right: 3rem;
}

.card-title {
  margin-bottom: 10px;
  font-weight: bold;
}

.card-user-info{
  margin-right: 3rem;
  margin-left: 10px;
}

.card-location,
.card-biography,
.card-member-since,
.card-followers{
  color: grey;
}

.card-biography{
  margin-top: 10px;
}


.card-button-follow{
  margin-top: 5rem;
}


#follow-button{

  background-color: rgb(87, 87, 239);
  color: white;
  padding: 0.8rem 1rem;;
  border-radius: 5px;
  border: none;
  margin-bottom: 1rem;
  height: 2.5rem;
  margin-left: -5rem;

}

.card-followers-count{
  font-weight: bold;
}


.card-follow-post-info {
  display: flex;
  margin-left: 7rem;
  margin-top: 0rem;
  justify-content: center;
}


.card-posts {
  display: inline-block;
  margin-left: 1rem;
  margin-top: 0rem;
}

.photo-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
  justify-content: center;
  margin-top: 50px;
}

.photo-grid img{
  width: 110px;
  height: 130px;
  border-radius: 0;
  margin-right: 3rem;
  margin-left: 10.5rem;

}



</style>



