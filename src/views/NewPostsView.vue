<template>
    <div class="new_post_wrapper">
        <h1>New Post</h1>
        <NewPost />
    </div>
</template>


<script setup>
    import NewPost from '@/components/NewPosts.vue'
</script>


<style>
.new_post_wrapper {
    height: 350px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

</style>