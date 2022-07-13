<template></template>

<script>
export default {
  async created() {
    await this.$axios.get('/user/logout', {
      headers: {
        Authorization: `Token ${this.$auth.strategy.token.get()}`,
        Accept: 'application/json',
      },
    }).then((res) => {
      console.log('res logout', res)
      this.$auth.strategy.token.set(null)
      this.$axios.setHeader('Authorization', false)
      this.$auth.logout({
        headers: {
          Authorization: `Token ${this.$auth.strategy.token.get()}`,
          Accept: 'application/json',
        },
      })
    })

  },
}
</script>