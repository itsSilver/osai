<template>
  <div class="wrapper d-flex align-items-stretch">
    <client-only>
      <Nav />
      <div id="content" class="p-4 p-md-5 pt-5">
        <div class="wrapped-content"></div>
      </div>
    </client-only>
  </div>
</template>

<script>
import Nav from '~/components/Nav'
export default {
  components: {
    Nav,
  },
  mounted() {
    this.$router.push({
      path: '/signals',
    })
  },
}
</script>
