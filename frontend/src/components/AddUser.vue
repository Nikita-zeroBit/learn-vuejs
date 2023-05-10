<template>
    <form id="users-form" method="post" @submit.prevent="checkForm" novalidate="true">
        <div v-if="users.error" class="form-group mt-1">
            <Message-prime severity="error">{{ users.error }}</Message-prime>
        </div>
        <div v-if="users.message" class="form-group mt-1">
            <Message-prime severity="success">{{ users.message }}</Message-prime>
        </div>
        <Card-prime>
            <template #title> User Information </template>
            <template #content> 
                <label for="name">Name</label>
                <InputText-prime id="name" type="text" v-model="users.name" placeholder="Enter username"/>
                <label for="email">Email</label>
                <InputText-prime id="email" type="text" v-model="users.email" placeholder="Enter email"/>
                <label for="password">Password</label>
                <InputText-prime id="password" type="text" v-model="users.pasword" placeholder="Enter password"/>
            </template>
            <template #footer>
                <Button-prime type="submit" label="Submit" icon="pi"/>
            </template>
        </Card-prime>
    </form>
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
                         await this.$axios.post("http://127.0.0.1:8000/api/users", {
                            name: this.users.name,
                            email: this.users.email,
                            password: this.users.password,
                        });

                        this.users.name = "";
                        this.users.email = "";
                        this.users.password = "";

                        this.users.message = "User added successfully";

                        window.location.href = '/users'

                        return;
                    } catch (error) {
                        this.users.error = error;
                        console.log(error);
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

<style>

    a {
        color: black;
        text-decoration: none;
    }

   #users-form {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding-left: 0;
    }

    .p-card {
        margin: 40px 0 0;
        width: 25em;
        left: 50%;
    }

    .p-card-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        flex-wrap: wrap;
    }

    label {
        margin-top: 20px;
    }

    .p-message {
        left: 70%;
    }

</style>