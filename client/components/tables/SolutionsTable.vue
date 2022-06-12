<template>
  <div>
    <b-overlay :show="show" rounded="sm">
      <o-table
        :data="dataTable"
        :bordered="true"
        :striped="true"
        mobile-cards
        paginated
        :per-page="perPage"
        :current-page.sync="currentPage"
        v-if="dataTable.length > 0"
        default-sort="id"
        default-sort-direction="desc"
      >
        <o-table-column
          field="id"
          label="ID"
          width="40"
          numeric
          v-slot="props"
          :visible="showID"
          sortable
        >
          {{ props.row.id }}
        </o-table-column>

        <o-table-column
          field="titolo"
          label="Title"
          v-slot="props"
          searchable
          position="centered"
          sortable
          :visible="showTitle"
        >
          {{ props.row.titolo }}
        </o-table-column>
        <o-table-column
          field="rif_ticket"
          label="Ticket"
          v-slot="props"
          searchable
          position="centered"
          sortable
          :visible="showTicket"
        >
          {{ props.row.rif_ticket }}
        </o-table-column>

        <o-table-column
          field="rank"
          label="Rank"
          v-slot="props"
          searchable
          position="centered"
          sortable
          :visible="showRank"
        >
          {{ props.row.rank }}
        </o-table-column>
        <o-table-column
          field="settore_riferimento"
          label="Reference sector"
          v-slot="props"
          searchable
          position="centered"
          sortable
          :visible="showReferenceSector"
        >
          {{ props.row.settore_riferimento }}
        </o-table-column>
        <o-table-column
          field="immagine_1"
          label="Image 1"
          v-slot="props"
          position="centered"
          :visible="showImage1"
        >
          <b-button
            class="mx-2 button-format file-button-table"
            @click="watchImage(props.row.immagine_1)"
            >Image 1
          </b-button>
        </o-table-column>
        <o-table-column
          field="immagine_2"
          label="Image 2"
          v-slot="props"
          position="centered"
          :visible="showImage2"
        >
          <b-button
            class="mx-2 button-format file-button-table"
            @click="watchImage(props.row.immagine_2)"
            >Image 2
          </b-button>
        </o-table-column>
        <o-table-column
          field="immagine_3"
          label="Image 3"
          v-slot="props"
          position="centered"
          :visible="showImage3"
        >
          <b-button
            class="mx-2 button-format file-button-table"
            @click="watchImage(props.row.immagine_3)"
            >Image 3
          </b-button>
        </o-table-column>

        <o-table-column
          field="user_id"
          label="User Id"
          position="centered"
          v-slot="props"
          searchable
          sortable
          :visible="showUserId"
        >
          {{ props.row.user_id }}
        </o-table-column>
        <o-table-column
          field="created_at"
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
          field="updated_at"
          label="Update date"
          position="centered"
          v-slot="props"
          searchable
          sortable
          :visible="showUpdateDate"
        >
          <!-- {{ new Date(props.row.updated_at).toLocaleDateString() }} -->
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
          <b-button
            class="mx-1 delete-btn"
            @click="deleteDocument(props.row.id)"
          >
            <i class="mdi mdi-delete"></i>
          </b-button>
        </o-table-column>
      </o-table>
      <div v-else>
        <NoSolutionItems v-if="showNoItem" />
      </div>
      <SeeImage
        v-if="showImage"
        :imageValue="imageValue"
        @close="hideModal()"
      />
    </b-overlay>
  </div>
</template>
<script>
import NoSolutionItems from '~/components/nodata/NoSolutionItems'
import SeeImage from '~/components/popup/SeeImage'
import { format, parseISO } from 'date-fns'
export default {
  components: {
    NoSolutionItems,
    SeeImage,
  },
  data() {
    return {
      showNoItem: true,
      show: false,
      showImage: false,
      currentPage: 1,
      perPage: 10,
      showID: false,
      showTitle: false,
      showTicket: false,
      showRank: false,
      showReferenceSector: false,
      showStatusSolution: false,
      showUserId: false,
      showImage1: false,
      showImage2: false,
      showImage3: false,
      showCreationDate: false,
      showUpdateDate: false,
    }
  },
  methods: {
    formatDate(val) {
      if (val) {
        return format(parseISO(val), 'yyyy-MM-dd')
      }
    },
    watchImage(val) {
      this.imageValue = 'http://api.apexroyale.com' + val
      this.showImage = true
    },
    hideModal() {
      this.showImage = false
    },
    pushRoute(route) {
      this.$router.push(`/solutions/${route}`)
    },
    deleteDocument(id) {
      this.$bvModal
        .msgBoxConfirm('Are you sure you want to delete this Solution?', {
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
              .post(`/api/soluzioni/${id}/delete`, {
                headers: {
                  Authorization: `Token ${this.$auth.strategy.token.get()}`,
                  'Content-Type': 'application/json',
                },
              })
              .then(() => {
                this.variant = 'danger'
                this.dataCreated = 'Solution deleted Succesfully'
                this.toggleToaster()
                this.$nuxt.refresh()
                this.show = false
                this.selectedId = []
                this.$emit('value-deleted')
              })
              .catch((error) => {
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
      this.$bvToast.show('deleted')
      setTimeout(() => {
        this.$bvToast.hide('deleted')
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
          } else if (item.text === 'Title') {
            this.showTitle = JSON.parse(item.value)
          } else if (item.text === 'Ticket') {
            this.showTicket = JSON.parse(item.value)
          } else if (item.text === 'Rank') {
            this.showRank = JSON.parse(item.value)
          } else if (item.text === 'Reference sector') {
            this.showReferenceSector = JSON.parse(item.value)
          } else if (item.text === 'Id Status Solution') {
            this.showStatusSolution = JSON.parse(item.value)
          } else if (item.text === 'Image 1') {
            this.showImage1 = JSON.parse(item.value)
          } else if (item.text === 'Image 2') {
            this.showImage2 = JSON.parse(item.value)
          } else if (item.text === 'Image 3') {
            this.showImage3 = JSON.parse(item.value)
          } else if (item.text === 'User Id') {
            this.showUserId = JSON.parse(item.value)
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
