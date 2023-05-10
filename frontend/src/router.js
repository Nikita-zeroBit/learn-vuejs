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
            path: '/',
            name: 'HomePage',
            component: () => import('./components/Home.vue'),
            meta: {layout: 'basic-layout'}
        },
        {
            path: '/users',
            component: Users,
            meta: {layout: 'basic-layout'},
            name: 'users'
        },
        {
            path: '/add-user',
            component: AddUser,
            meta: {layout: 'basic-layout'},
            name: 'add-user'
        },
        {
            path: '/add-book',
            component: AddBook,
            meta: {layout: 'basic-layout'},
            name: 'add-book'
        },
        {
            path: '/books',
            component: Books,
            meta: {layout: 'basic-layout'},
            name: 'books'
        },
    ]
});