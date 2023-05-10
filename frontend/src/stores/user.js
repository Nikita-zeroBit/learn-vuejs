import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
    state: () => {
        return {
            users: null,
        }
    }, 
    actions: {
        async fetchUsers() {
        this.users = []
        try {
            let res = await fetch("http://127.0.0.1:8000/api/users");
            const results = await res.json()
            console.log(results);
            this.users = await results.results;
        }
        catch (error) {
            this.error = error
        }
        }
    }
})