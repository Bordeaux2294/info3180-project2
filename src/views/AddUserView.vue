<template>
    <div class="register_container">
      <h1>Register</h1>
      <RegisterForm />
    </div>
  </template>
  
<script setup>
    import RegisterForm from '@/components/RegisterForm.vue'
</script>

<style>
.register_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 15px 15px;
}
</style>
  