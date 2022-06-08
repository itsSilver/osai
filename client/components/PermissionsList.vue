<template>
  <b-container>
    <b-list-group-item>
      <b-form-checkbox
        class="checkthis"
        id="checkall"
        v-model="selectAll"
        :disabled="viewMode"
        >Select All Permissions</b-form-checkbox
      >
    </b-list-group-item>
    <b-list-group v-for="data in dataTable" :key="data.id">
      <b-list-group-item>
        <b-form-checkbox
          v-model="selected"
          :value="data.id"
          :disabled="viewMode"
          >{{ data.name }}</b-form-checkbox
        >
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
  computed: {
    selectAll: {
      get: function () {
        if (this.dataTable.length != 0) {
          return this.dataTable
            ? this.selected.length == this.dataTable.length
            : false
        }
      },
      set: function (value) {
        var selected = []
        if (value) {
          this.dataTable.forEach(function (user) {
            selected.push(user.id)
          })
        }
        if (this.dataTable.length != 0) {
          this.selected = selected
        }
      },
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
  props: ['dataTable', 'viewMode'],
}
</script>