<template>
  <div>
    <o-table
      :data="dataTable"
      :bordered="true"
      :striped="true"
      mobile-cards
      paginated
      :per-page="perPage"
      :current-page.sync="currentPage"
      v-if="dataTable.length > 0"
      default-sort="titolo"
      :selected.sync="selected"
    >
      <o-table-column
        field="id"
        label="ID"
        width="40"
        numeric
        v-slot="props"
        :visible="showID"
      >
        {{ props.row.id }}
      </o-table-column>

      <o-table-column
        field="name"
        label="Name"
        v-slot="props"
        searchable
        position="centered"
        sortable
        :visible="showName"
      >
        {{ props.row.name }}
      </o-table-column>
      <o-table-column
        field="email"
        label="Email"
        v-slot="props"
        searchable
        position="centered"
        sortable
        :visible="showEmail"
      >
        {{ props.row.email }}
      </o-table-column>
      <o-table-column
        field="date"
        label="Creation date"
        position="centered"
        v-slot="props"
        searchable
        sortable
        :visible="showCreationDate"
      >
        {{ formatDate(props.row.created_at) }}
      </o-table-column>
      <o-table-column
        field="date"
        label="Update date"
        position="centered"
        v-slot="props"
        searchable
        sortable
        :visible="showUpdateDate"
      >
        {{ formatDate(props.row.updated_at) }}
      </o-table-column>
      <o-table-column
        field="action"
        label="Action"
        position="centered"
        v-slot="props"
        width="180px"
      >
        <b-button
          class="mx-1 view-btn"
          @click="pushRoute(`view/${props.row.id}`)"
        >
          <i class="mdi mdi-eye"></i>
        </b-button>
        <b-button
          class="mx-1 edit-btn"
          @click="pushRoute(`update/${props.row.id}`)"
        >
          <i class="mdi mdi-pencil"></i>
        </b-button>
        <b-button class="mx-1 delete-btn" @click="deleteDocument(props.row.id)">
          <i class="mdi mdi-delete"></i>
        </b-button>
      </o-table-column>
    </o-table>
    <div v-else>
      <NoUserItem v-if="showNoItem" />
    </div>
    <b-toast id="deleted-value" :variant="variant" solid>
      <template #toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">Notification!</strong>
        </div>
      </template>
      {{ dataCreated }}
    </b-toast>
  </div>
</template>
<script>
import NoUserItem from '~/components/nodata/NoUserItem'
import { format, parseISO } from 'date-fns'
export default {
  components: {
    NoUserItem,
  },
  data() {
    return {
      dataCreated: '',
      variant: '',
      currentPage: 1,
      showNoItem: true,
      show: false,
      selectedId: [],
      selected: {},
      perPage: 10,
      showID: false,
      showName: false,
      showEmail: false,
    }
  },
  methods: {
    formatDate(val) {
      if (val) {
        return format(parseISO(val), 'yyyy-MM-dd')
      }
    },
    watchImage(val) {
      this.imageValue = 'http://localhost:8000' + val
      this.showImage = true
    },
    hideModal() {
      this.showImage = false
    },
    pushRoute(route) {
      this.$router.push(`/manage-access/${route}`)
    },
    deleteDocument(id) {
      this.$bvModal
        .msgBoxConfirm('Are you sure you want to delete this User?', {
          title: `Attention`,
          size: 'sm',
          buttonSize: 'sm',
          okVariant: 'danger',
          okTitle: `Yes`,
          cancelTitle: `No`,
          footerClass: 'p-2',
          hideHeaderClose: true,
          centered: true,
        })
        .then((value) => {
          if (value === true) {
            this.show = true
            this.$axios
              .post(`/user/remove/${id}`, {
                headers: {
                  Authorization: `Token ${this.$auth.strategy.token.get()}`,
                  'Content-Type': 'application/json',
                },
              })
              .then((response) => {
                if (response.data.status === 403) {
                  this.variant = 'danger'
                  this.dataCreated = 'The super admin user cannot be deleted!'
                  this.toggleToaster()
                  this.show = false
                  return
                }
                this.variant = 'danger'
                this.dataCreated = 'User deleted Succesfully'
                this.toggleToaster()
                this.show = false
                this.selectedId = []
                this.$emit('reload-data')
                console.log('Passed successfully!')
              })
              .catch((error) => {
                console.log('Cought Error1', error.response.data)
                this.dataCreated = error.response.data.message[0]
                this.show = false
                this.variant = 'danger'
                this.toggleToaster()
                this.selectedId = []
              })
          } else {
            // Empty do nothing
          }
        })
        .catch((err) => {
          // An error occurred
          this.dataCreated = err.response.data.message[0]
        })
    },
    toggleToaster() {
      this.$bvToast.show('deleted-value')
      setTimeout(() => {
        this.$bvToast.hide('deleted-value')
      }, 2000)
    },
  },
  props: ['dataTable', 'dropdown'],
  watch: {
    dropdown: {
      handler(newVal) {
        newVal.forEach((item) => {
          if (item.text === 'ID') {
            this.showID = JSON.parse(item.value)
          } else if (item.text === 'Name') {
            this.showName = JSON.parse(item.value)
          } else if (item.text === 'Email') {
            this.showEmail = JSON.parse(item.value)
          } else if (item.text === 'Creation date') {
            this.showCreationDate = JSON.parse(item.value)
          } else if (item.text === 'Update date') {
            this.showUpdateDate = JSON.parse(item.value)
          }
        })
      },
      immediate: true,
      deep: true,
    },
  },
}
</script>
<style scoped>
.view-btn {
  background-color: unset !important;
  color: #28a745 !important;
  border: unset;
}

.edit-btn {
  background-color: unset !important;
  border: unset;
  color: #ffc107 !important;
}

.delete-btn {
  background-color: unset !important;
  color: #dc3545 !important;
  border: unset;
}

/deep/ .o-table__td {
  vertical-align: middle;
  text-align: left;
}

/deep/ .o-table__tr--selected {
  background-color: #666;
  color: #ffffff;
}
</style>