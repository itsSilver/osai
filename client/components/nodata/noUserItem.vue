<template>
  <div>
    <i class="mdi mdi-file-document-box-search mr-3"></i>
    <div style="padding-top: 20px">
      <h6 class="text-dark fw-bold">Could not find any items</h6>
      <p>Try changing the filters or add a new one</p>
      <b-button class="mx-2 button-format" @click="redirectCreate()">
        <i class="fas fa-plus pr-2"></i>
        New User
      </b-button>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    redirectCreate() {
      this.$router.push(`/manage-access/create`)
    },
  },
}
</script>
<style scoped>
.mdi-file-document-box-search {
  font-size: 100px !important;
  color: #d7d7db;
}
</style>