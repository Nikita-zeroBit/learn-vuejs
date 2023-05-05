<template>
    <div class="books">
        <div class="container">
            <div class="row">
                <div class="col-sm-6 offset-sm-3">

                    <div v-if="books.length == 0">
                        <div class="card mt-2 mb-2">
                            <div class="card-body">
                                <h4 class="card-title">No book saved</h4>
                                <div class="d-flex justify-content-between">
                                    <a class="btn btn-info text-white" href="/add-book">Add book</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div v-else-if="books.length > 0" v-for="book in books" v-bind:key="book.id">
                        <div class="card mt-2 mb-2">
                            <div class="card-body">
                                <h4 class="card-title">{{ book.title }}</h4>
                                <p class="card-text">{{ book.description }}</p>
                                <p class="card-text">{{ book.year }}</p>
                                <div class="d-flex justify-content-between">
                                    <button class="btn btn-danger" @click="deleteBook(book.id)">
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
                books: [],
            };
        },
        methods: {
            async getData() {
                try {
                    const response = await this.$axios.get(
                        "http://0.0.0.0:8000/api/books"
                    );
                    this.books = response.data.results;
                } catch (error) {
                    console.log(error);
                }
            },
            async deleteBook(bookId) {
                let confirmation = confirm("Do you want to delete this book?");

                if (confirmation) {
                    try {
                        await this.$axios.delete(`http://0.0.0.0:8000/api/books/${bookId}`);
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

    .books {
        margin-top: 10px;
    }
</style>