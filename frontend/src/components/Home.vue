<template>
  <h2>Hello!</h2>
    <div id="objects">
      <books/>
    </div>
</template>

<script>
import Books from "../components/Books.vue"
export default {
  name: 'home-page',
  components: {
    'books': Books,
  }
}
</script>

<style scoped>

</style>