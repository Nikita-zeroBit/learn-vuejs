<template>
    <Button-prime id="add-button" type="btn btn-danger" label="Add" icon="pi">
        <a class="btn text-white" href="/add-book">Add book</a>
    </Button-prime>
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
    <div id="cards" v-else-if="books.length > 0" v-for="book in books" v-bind:key="book.id">
        <Card-prime>
            <template #title> {{book.title}}, {{book.year}} </template>
            <template #content> {{book.description}} </template>
            <template #footer><Button-prime type="btn btn-danger" label="Delete" icon="pi pi-times" @click="deleteBook(book.id)"/></template>
        </Card-prime>
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
                try {
                    await this.$axios.delete(`http://0.0.0.0:8000/api/books/${bookId}`);
                    this.getData();
                } catch (error) {
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

</style>