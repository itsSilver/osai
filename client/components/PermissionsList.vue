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
  mounted() {
    this.getDataPermissions()
  },
  methods: {
    getDataPermissions() {
      this.show = true
      this.$axios
        .get(`/user/id/${this.$route.params.id}`, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          if (response) {
            const permissions = response.data.permissions
            const dataPermissions = []
            permissions.forEach((e) => {
              dataPermissions.push(e.id)
            })
            // console.log(permissions)
            this.selected = dataPermissions
          }
          this.show = false
        })
        .catch((error) => {
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
  },
  props: ['dataTable'],
}
</script>