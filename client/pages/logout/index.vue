<template></template>

<script>
export default {
  created() {
    this.$auth.strategy.token.set(null)
    this.$axios.setHeader('Authorization', false)
    this.$auth.logout({
      headers: {
        Authorization: `Token ${this.$auth.strategy.token.get()}`,
        Accept: 'application/json',
      },
    })
  },
}
</script>