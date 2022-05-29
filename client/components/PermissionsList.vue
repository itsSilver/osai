<template>
  <b-container>
    <b-list-group v-for="data in dataTable" :key="data.id">
      <b-list-group-item>
        <b-form-checkbox v-model="selected" :value="data.id">{{
          data.name
        }}</b-form-checkbox>
      </b-list-group-item>
    </b-list-group>
  </b-container>
</template>
<script>
export default {
  data() {
    return {
      selected: [],
    }
  },
  watch: {
    selected: function (val) {
      this.$emit('data-send', val)
    },
  },
  props: ['dataTable'],
}
</script>