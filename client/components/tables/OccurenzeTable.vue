<template>
  <div>
    <b-overlay :show="show" rounded="sm">
      <o-table :data="dataTable" :bordered="true" :striped="true" mobile-cards paginated :per-page="perPage"
        :current-page.sync="currentPage" v-if="dataTable.length > 0" default-sort="id" :selected.sync="selected">
        <o-table-column field="id" label="ID" width="40" numeric sortable v-slot="props" :visible="showID">
          {{ props.row.id }}
        </o-table-column>

        <o-table-column field="titolo" label="Title" v-slot="props" searchable position="centered" sortable
          :visible="showTitle">
          {{ props.row.titolo }}
        </o-table-column>
        <o-table-column field="segnalazione" label="Id Signal" v-slot="props" searchable position="centered" sortable
          :visible="showIdSignal">
          {{ props.row.segnalazione }}
        </o-table-column>

        <o-table-column field="soluzioni_id[0]" label="Id Solution" v-slot="props" searchable position="centered"
          sortable :visible="showIdSolution">
          {{ props.row.soluzioni_id[0] }}
        </o-table-column>
        <o-table-column field="commessa_macchina" label="Machine Order" v-slot="props" searchable position="centered"
          sortable :visible="showMachineOrder">
          {{ props.row.commessa_macchina }}
        </o-table-column>
        <o-table-column field="rif_ticket" label="Ticket" v-slot="props" searchable position="centered" sortable
          :visible="showTicket">
          {{ props.row.rif_ticket }}
        </o-table-column>
        <o-table-column field="versione_sw_1" label="Version sw 1" v-slot="props" searchable position="centered"
          sortable :visible="showVersion1">
          {{ props.row.versione_sw_1 }}
        </o-table-column>
        <o-table-column field="versione_sw_2" label="Version sw 2" v-slot="props" searchable position="centered"
          sortable :visible="showVersion2">
          {{ props.row.versione_sw_2 }}
        </o-table-column>
        <o-table-column field="data_occorrenza" label="Occurrence date" v-slot="props" searchable position="centered"
          sortable :visible="showOccurrenceDate">
          {{ props.row.data_occorrenza }}
        </o-table-column>
        <o-table-column field="stato_occorrenza" label="Occurrence status" v-slot="props" searchable position="centered"
          sortable :visible="showOccurrenceStatus">
          <span v-if="props.row.stato_occorrenza === '1'">Open</span>
          <span v-if="props.row.stato_occorrenza === '0'">Close</span>
          <span></span>
        </o-table-column>

        <o-table-column field="created_at" label="Creation date" position="centered" v-slot="props" searchable sortable
          :visible="showCreationDate">
          {{ formatDate(props.row.created_at) }}
        </o-table-column>
        <o-table-column field="updated_at" label="Update date" position="centered" v-slot="props" searchable sortable
          :visible="showUpdateDate">
          {{ formatDate(props.row.updated_at) }}
        </o-table-column>
        <o-table-column field="action" label="Action" position="centered" v-slot="props" width="180px">
          <b-button class="mx-1 view-btn" @click="pushRoute(`view/${props.row.id}`)">
            <i class="mdi mdi-eye"></i>
          </b-button>
          <b-button class="mx-1 edit-btn" @click="pushRoute(`update/${props.row.id}`)">
            <i class="mdi mdi-pencil"></i>
          </b-button>
          <b-button class="mx-1 delete-btn" @click="deleteDocument(props.row.id)">
            <i class="mdi mdi-delete"></i>
          </b-button>
        </o-table-column>
      </o-table>
      <div v-else>
        <NoOccorrenzeItems v-if="showNoItem" />
      </div>
      <SeeImage v-if="showImage" :imageValue="imageValue" @close="hideModal()" />
    </b-overlay>
  </div>
</template>
<script>
import NoOccorrenzeItems from '~/components/nodata/NoOccorrenzeItems'
import { format, parseISO } from 'date-fns'
export default {
  components: {
    NoOccorrenzeItems,
  },
  data() {
    return {
      showNoItem: true,
      show: false,
      showImage: false,
      selected: {},
      currentPage: 1,
      perPage: 10,
      showID: false,
      showIdSignal: false,
      showIdSolution: false,
      showTitle: false,
      showMachineOrder: false,
      showTicket: false,
      showVersion1: false,
      showVersion2: false,
      showOccurrenceDate: false,
      showOccurrenceStatus: false,
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
      this.imageValue = 'http://localhost:8000' + val
      this.showImage = true
    },
    hideModal() {
      this.showImage = false
    },
    pushRoute(route) {
      this.$router.push(`/occurrences/${route}`)
    },
    deleteDocument(id) {
      this.$bvModal
        .msgBoxConfirm('Are you sure you want to delete this Occurrence?', {
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
              .post(`/api/occorrenze/${id}/delete`, {
                headers: {
                  Authorization: `Token ${this.$auth.strategy.token.get()}`,
                  'Content-Type': 'application/json',
                },
              })
              .then(() => {
                this.variant = 'danger'
                this.dataCreated = 'Occurrence deleted Succesfully'
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
          } else if (item.text === 'Id signal') {
            this.showIdSignal = JSON.parse(item.value)
          } else if (item.text === 'Id solution') {
            this.showIdSolution = JSON.parse(item.value)
          } else if (item.text === 'Title') {
            this.showTitle = JSON.parse(item.value)
          } else if (item.text === 'Machine order') {
            this.showMachineOrder = JSON.parse(item.value)
          } else if (item.text === 'Ticket') {
            this.showTicket = JSON.parse(item.value)
          } else if (item.text === 'Version sw 1') {
            this.showVersion1 = JSON.parse(item.value)
          } else if (item.text === 'Version sw 2') {
            this.showVersion2 = JSON.parse(item.value)
          } else if (item.text === 'Occurrence date') {
            this.showOccurrenceDate = JSON.parse(item.value)
          } else if (item.text === 'Occurrence status') {
            this.showOccurrenceStatus = JSON.parse(item.value)
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

/* .view-btn {
  background-color: #28a745;
}

.edit-btn {
  background-color: #ffc107;
}

.delete-btn {
  background-color: #dc3545;
} */

/deep/ .o-table__td {
  vertical-align: middle;
  text-align: left;
}

/deep/ .o-table__tr--selected {
  background-color: #666;
  color: #ffffff;
}
</style>