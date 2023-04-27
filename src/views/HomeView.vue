<script setup>
import { ref } from "vue";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.")

</script>

<template>
    <div class="container">
        <div class="photogram_photo_div">
          <!-- <img alt="Photogram photo" class="photogram_photo" src="../images/under_pier.jpg" width="200px" height="200px" /> -->
        </div>
        <div class="login_div">
          <div class="title">
            <img alt="photogram logo" class="photogram_logo" src="../images/igicon.svg" width="20px" height="20px"/>
            <h1 class="login_title">Photogram</h1>
          </div>
          <div class="body">
            <p>Share photos of your favourite moments with friends, family and the world
            </p>
            <div class="body_buttons">
              <button id="register_button">Register</button>
              <button id="login_button">Login</button>
            </div>
          </div>
        </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
.container {
  border: 1px solid red;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  height: 250px;
}

.photogram_photo_div {
  border: 1px solid red;
  width: 25%;
  height: 90%;
  background-image: url(../images/under_pier.jpg);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}

.login_div {
  border: 1px solid grey;
  border-radius: 10px;
  background-color: white;
  width: 45%;
  height: 90%;
  box-shadow: 7px 7px 4px rgba(0, 0, 0, 0.25);
}

.title {
  border: 1px solid green;
  display: flex;
  justify-content: center;
  /* align-items: center; */
  padding-top: 5px;
}

.title h1 {
  font-size: 16px;
  font-family: fantasy;
}

.body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.body_buttons {
  border: 1px solid red;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 5px 5px;
  width: 50%;
}

.body_buttons button {
  width: 70px;
  height: 30px;
  color: white;
  font-weight: bold;
  font-size: 14px;
  border-radius: 5px;
  text-align: center;
}

#register_button {
  background-color: rgb(40, 197, 40);
  border: 1px solid rgb(40, 197, 40);
}

#login_button {
  background-color: rgb(63, 63, 184);
  border: 1px solid rgb(63, 63, 184);
}



</style>