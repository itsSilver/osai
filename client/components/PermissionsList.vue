<template>
  <b-container>
    <b-list-group v-for="data in dataTable" :key="data.name">
      <b-list-group-item>
        <b-form-checkbox value="orange">{{ data.name }}</b-form-checkbox>
      </b-list-group-item>
    </b-list-group>
  </b-container>
</template>
<script>
export default {
  props: ['dataTable'],
}
</script>