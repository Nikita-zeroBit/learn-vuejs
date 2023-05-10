<template>

    <div>
        <head-menu/>
        <router-view/>
    </div>

</template>

<script>
import HeadMenu from '../components/NavBar.vue'

export default {
  name: 'basic',
  components: {
    'head-menu': HeadMenu,
  }
}
</script>

<style scoped>

</style>