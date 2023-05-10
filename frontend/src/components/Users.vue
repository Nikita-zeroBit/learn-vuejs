<template>
    <div id="card" v-if="users.length == 0">
      <Card-prime id="no-users-card">
        <template #title> Users not found </template>
        <template #footer>
          <Button-prime id="add-button-card" type="btn btn-danger" label="Add" icon="pi">
            <a id="add-button-card" class="btn text-white" href="/add-user">Add user</a>
          </Button-prime>
        </template>
      </Card-prime>
    </div>
    <div id="cards" v-else>
      <Button-prime id="add-button" type="btn btn-danger" label="Add" icon="pi">
        <a id="add-button" class="btn text-white" href="/add-user">Add user</a>
      </Button-prime>
      <div id="card" v-for="user in users" v-bind:key="user.id">
        <Card-prime>
            <template #title> {{user.name}} </template>
            <template #content> {{user.email}} </template>
            <template #footer><Button-prime type="btn btn-danger" label="Delete" icon="pi pi-times" @click="deleteUser(user.id)"/></template>
        </Card-prime>
      </div>
    </div>
</template>

<script>
  import {useUserStore} from '@/stores/user'
  export default {
    setup() {
      const useUsers = useUserStore()
      return {useUsers}
    },
    data() {
      return {
        users: [],
      };
    },
    methods: {
      async getData() {
        try {
          await this.useUsers.fetchUsers();
          this.users = this.useUsers.users;
        }
        catch (error) {
          console.log(error);
        }
      },
      async deleteUser(userId) {
        try {
          await this.$axios.delete(`http://127.0.0.1:8000/api/users/${userId}`);
          this.getData();
        }
        catch (error) {
          console.log(error);
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

    
    a {
        color: black;
        text-decoration: none;
    }

    .card-body {
        text-align: left;
    }

    .books {
        margin-top: 10px;
    }

    #cards {
      left: 50%;
    }

    #no-users-card {
      left: 50%;
    }

    #card {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding-left: 0;
    }

    .p-card {
        margin: 40px 0 0;
        width: 25em;
        flex: 0 0 0 0.33%
    }

    #add-button {
        margin-top: 2%;
        left: 90%;
    }

    #add-button-card {
        margin-top: 2%;
        width: 100%;
        justify-content: center;
    }

</style>