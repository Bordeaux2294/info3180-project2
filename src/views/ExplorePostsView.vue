<template>
    <div class="explore_posts_container">
        <Explore />
    </div>
</template>


<script setup>
    import Explore from '@/components/ExplorePosts.vue'
</script>

<style>

.explore_posts_container {
    border: 1px solid red;
    display: flex;
    height: 900px;
    justify-content: center;
}

</style>