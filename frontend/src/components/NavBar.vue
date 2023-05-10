<template>
  <Menubar-prime  :model=items>
    <template #start>
        <router-link to="/" >
        </router-link>

    </template>
    <template #end>

    </template>

  </Menubar-prime>

</template>


<script>
export default {
  name: "head-menu",
  data() {
    return {
      items: [

        {
          label: 'Home',
          icon: 'pi pi-fw pi-home',
          to: '/',
        },

        {
          label: 'Users',
          icon: 'pi pi-fw pi-user',
          to: '/users',
        },

        {
          label: 'Books',
          icon: 'pi pi-fw pi-book',
          to: '/books',
        }
      ],
    }
  },
  methods: {
  },
  computed:{

  }
}
</script>

<style scoped>

</style>
