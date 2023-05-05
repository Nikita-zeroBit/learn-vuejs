<template>
  <div id="app">
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous" />
        <title>TesProject</title>
    </head>

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="/"> Test app </a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mx-auto">
                <li class="nav-item" :class="home_class">
                    <a class="nav-link" href="/users"> Users </a>
                </li>
                <li class="nav-item" :class="home_class">
                      <a class="nav-link" href="/books"> Books </a>
                  </li>
                <li class="nav-item" :class="add_user_class">
                    <a class="nav-link" href="/add-user"> Add user </a>
                </li>
                <li class="nav-item" :class="add_book_class">
                    <a class="nav-link" href="/add-book"> Add book </a>
                </li>
            </ul>
        </div>
    </nav>

    <router-view> </router-view>
  </div>
</template>
  
<script>
  export default {
    data() {
      return {
        home_class: this.$route.path === "/" ? "active" : "",
        add_user_class: this.$route.path === "/add-user" ? "active" : "",
        add_book_class: this.$route.path === "/add-book" ? "active" : "",
      };
    },
  };
</script>
  
<style>
  #app-app {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>
  