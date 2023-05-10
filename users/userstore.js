import { defineStore } from 'pinia'

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    users: [],
    user: null,
    loading: false,
    error: null
  }), 
  actions: {
    async fetchUsers() {
      this.users = []
      this.loading = true
      try {
        this.users = await fetch('http://127.0.0.1:8000/users')
        .then((response) => response.json()) 
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },
    async fetchUser(id) {
      this.user = null
      this.loading = true
      try {
        this.post = await fetch(`http://127.0.0.1:8000/users/${id}`)
        .then((response) => response.json())
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    }
  }
})