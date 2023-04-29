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

        <button v-if="!isFollowing" @click="followUser">Follow</button>
        <button v-else @click="unfollowUser">Unfollow</button>
      </div>
      
    </div>
  </div>

</template>



<script setup>
  import { ref } from 'vue';
   
  
  
</script>