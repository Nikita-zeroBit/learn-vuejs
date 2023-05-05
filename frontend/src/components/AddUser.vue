<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-6 offset-sm-3">
                <form id="user-form" method="post" @submit.prevent="checkForm" novalidate="true">
                    <div v-if="users.error" class="form-group mt-1">
                        <div class="alert alert-danger">{{ users.error }}</div>
                    </div>
                    <div v-if="users.message" class="form-group mt-1">
                        <div class="alert alert-success">{{ users.message }}</div>
                    </div>
                    <div class="form-group mt-3" style="text-align: left">
                        <label for="title">Name</label>
                        <input v-model="users.name" type="text" class="form-control" id="name"
                            placeholder="Enter user's name" />
                    </div>
                    <div class="form-group mt-3" style="text-align: left">
                        <label for="description">Email</label>
                        <textarea v-model="users.email" class="form-control" name="email" id="email"
                            placeholder="user's email"></textarea>
                    </div>
                    <div class="form-group mt-3" style="text-align: left">
                            <label for="description">Password</label>
                            <textarea v-model="users.password" class="form-control" name="password" id="password"
                                placeholder="user's email"></textarea>
                        </div>
                    <div class="form-group mt-3">
                        <button type="submit" class="btn btn-primary btn-lg btn-block">
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                users: {
                    name: "",
                    email: "",
                    password: "",
                    error: null,
                    message: null,
                },
            };
        },
        methods: {
            checkForm: async function (e) {
                if (this.users.name && this.users.email) {
                    try {
                        await this.$axios.post("http://0.0.0.0:8000/api/users", {
                            name: this.users.name,
                            email: this.users.email,
                            password: this.users.password,
                        });

                        this.users.name = "";
                        this.users.email = "";
                        this.users.password = "";

                        this.users.message = "User added successfully";

                        return;
                    } catch (error) {
                        this.users.error = error;
                        return;
                    }
                }
                this.users.error = null;
                if (!this.users.name) {
                    this.users.error = "Name is required";
                    return;
                }
                if (!this.users.email) {
                    this.users.error = "Email is required";
                    return;
                }
                if (!this.users.password) {
                    this.users.error = "Password is required";
                    return;
                }
                e.preventDefault();
            },
        },
    };
</script>