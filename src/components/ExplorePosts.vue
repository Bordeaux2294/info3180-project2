<template>
    <div class="explore_container">
        <div class="posts_container">
            <div>
                <div class="post_title">
                    <img alt="avatar-icon" src="../images/black_guy.webp" width="30px" height="30px"/>
                    <p>User Name</p>
                </div>
                <div class="post_image">

                </div>
                <div class="post_body">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus repudiandae dolore totam, ipsum impedit consequuntur facere quae odio ut aut?
                </div>
                <div class="post_footer">
                    <p><img alt="heart-icon" src="../images/unliked.svg" width="20px" height="20px">10 Likes</p>
                    <p>24 Apr 2018</p>
                </div>
            </div>
        </div>
        <div class="new_posts_button_container">
            <button>New Posts</button>
        </div>
    </div>
</template>



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