<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-6 offset-sm-3">
                <form id="books-form" method="post" @submit.prevent="checkForm" novalidate="true">
                    <div v-if="books.error" class="form-group mt-1">
                        <div class="alert alert-danger">{{ books.error }}</div>
                    </div>
                    <div v-if="books.message" class="form-group mt-1">
                        <div class="alert alert-success">{{ books.message }}</div>
                    </div>
                    <div class="form-group mt-3" style="text-align: left">
                        <label for="title">Title</label>
                        <input v-model="books.title" type="text" class="form-control" id="title"
                            placeholder="Enter books's title" />
                    </div>
                    <div class="form-group mt-3" style="text-align: left">
                        <label for="description">Description</label>
                        <textarea v-model="books.description" class="form-control" name="description" id="description"
                            placeholder="bookss's email"></textarea>
                    </div>
                    <div class="form-group mt-3" style="text-align: left">
                        <label for="description">Year</label>
                        <textarea v-model="books.year" class="form-control" name="year" id="year"
                            placeholder="books's year"></textarea>
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

                        return;
                    } catch (error) {
                        this.books.error = error;
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