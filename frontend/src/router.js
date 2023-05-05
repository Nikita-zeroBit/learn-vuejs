import { createRouter, createWebHistory } from 'vue-router'
import AddUser from "./components/AddUser"
import Users from "./components/Users"
import AddBook from "./components/AddBook"
import Books from "./components/Books"

export default createRouter({
    history: createWebHistory(),
    base: __dirname,
    routes: [
        {
            path: '/users',
            component: Users,
            name: 'users'
        },
        {
            path: '/add-user',
            component: AddUser,
            name: 'add-user'
        },
        {
            path: '/add-book',
            component: AddBook,
            name: 'add-book'
        },
        {
            path: '/books',
            component: Books,
            name: 'books'
        },
    ]
});