<template>
  <div class="users">
    <div class="container">
      <div class="row">
        <div class="col-sm-6 offset-sm-3">

          <div v-if="users.length == 0">
            <div class="card mt-2 mb-2">
              <div class="card-body">
                <h4 class="card-title">No user saved</h4>
                <div class="d-flex justify-content-between">
                  <a class="btn btn-info text-white" href="/add-user">Add user</a>
                </div>
              </div>
            </div>
          </div>

          <div v-else-if="users.length > 0" v-for="user in users" v-bind:key="user.id">
            <div class="card mt-2 mb-2">
              <div class="card-body">
                <h4 class="card-title">{{ user.name }}</h4>
                <p class="card-text">{{ user.email }}</p>
                <div class="d-flex justify-content-between">
                  <button class="btn btn-danger" @click="deleteUser(user.id)">
                    Delete
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        users: [],
      };
    },
    methods: {
      async getData() {
        try {
          const response = await this.$axios.get(
            "http://0.0.0.0:8000/api/users"
          );
          this.users = response.data.results;
        } catch (error) {
          console.log(error);
        }
      },
      async deleteUser(userId) {
        let confirmation = confirm("Do you want to delete this user?");

        if (confirmation) {
          try {
            await this.$axios.delete(`http://0.0.0.0:8000/api/users/${userId}`);
            this.getData();
          } catch (error) {
            console.log(error);
          }
        }
      },
    },

    created() {
      this.getData();
    },
  };
</script>

<style scoped>
  h3 {
    margin: 40px 0 0;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  .card-body {
    text-align: left;
  }

  .users {
    margin-top: 10px;
  }
</style>