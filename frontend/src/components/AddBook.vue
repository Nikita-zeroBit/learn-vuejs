<template>
    <form id="books-form" method="post" @submit.prevent="checkForm" novalidate="true" action="/books">
        <div v-if="books.error" class="form-group mt-1">
            <Message-prime severity="error">{{ books.error }}</Message-prime>
        </div>
        <div v-if="books.message" class="form-group mt-1">
            <Message-prime severity="success">{{ books.message }}</Message-prime>
        </div>
        <Card-prime>
            <template #title> Book Information </template>
            <template #content> 
                <label for="title">Title</label>
                <InputText-prime id="title" type="text" v-model="books.title" placeholder="Enter title of a book"/>
                <label for="title">Description</label>
                <InputText-prime id="description" type="text" v-model="books.description" placeholder="Enter description of a book"/>
                <label for="title">Year</label>
                <InputText-prime id="year" type="number" max=2023 v-model="books.year" placeholder="Enter year of creating"/>
            </template>
            <template #footer>
                <Button-prime type="btn btn-danger" label="Submit" icon="pi">
                    <a class="btn text-white" href="/books" style="text-decoration: none; color: Black">Add book</a>
                </Button-prime>
            </template>
        </Card-prime>
    </form>
</template>

<script>
    export default {
        data() {
            return {
                books: {
                    title: "",
                    description: "",
                    year: 0,
                    error: null,
                    message: null,
                },
            };
        },
        methods: {
            checkForm: async function (e) {
                if (this.books.title && this.books.description) {
                    try {
                        await this.$axios.post("http://0.0.0.0:8000/api/books", {
                            title: this.books.title,
                            description: this.books.description,
                            year: this.books.year,
                        });

                        this.books.title = "";
                        this.books.description = "";
                        this.books.year = 0;

                        this.books.message = "Book added successfully";

                        window.location.href = '/books'

                        return;
                    } catch (error) {
                        this.books.error = error;
                        console.log(error);
                        return;
                    }
                }
                this.books.error = null;
                if (!this.books.title) {
                    this.books.error = "Title is required";
                    return;
                }
                if (!this.books.description) {
                    this.books.error = "Description is required";
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

   #books-form {
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