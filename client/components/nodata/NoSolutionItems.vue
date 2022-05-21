<template>
  <div>
    <i class="fas fa-search"></i>
    <div style="padding-top: 20px">
      <h6 class="text-dark fw-bold">Could not find any items</h6>
      <p>Try changing the filters or add a new one</p>
      <b-button class="mx-2 button-format" @click="redirectCreate()">
        <i class="fas fa-plus pr-2"></i>
        New Solution
      </b-button>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    redirectCreate() {
      this.$router.push(`/solutions/create`)
    },
  },
}
</script>
<style scoped>
.fa-search {
  font-size: 120px !important;
  color: #d7d7db;
}
</style>