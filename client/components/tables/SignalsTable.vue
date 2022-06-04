<template>
  <div>
    <o-table :data="dataTable" :bordered="true" :striped="true" mobile-cards paginated :per-page="perPage"
      :current-page.sync="currentPage" v-if="dataTable.length > 0" default-sort="titolo" :selected.sync="selected">
      <o-table-column field="id" label="ID" width="40" numeric v-slot="props" :visible="showID">
        {{ props.row.id }}
      </o-table-column>

      <o-table-column field="titolo" label="Title" v-slot="props" searchable position="centered" sortable
        :visible="showTitle">
        {{ props.row.titolo }}
      </o-table-column>
      <o-table-column field="rif_ticket" label="Ticket" v-slot="props" searchable position="centered" sortable
        :visible="showTicket">
        {{ props.row.rif_ticket }}
      </o-table-column>

      <o-table-column field="id_allarme" label="Id Alarm" v-slot="props" searchable position="centered" sortable
        :visible="showAlarm">
        {{ props.row.id_allarme }}
      </o-table-column>
      <o-table-column field="famiglia_macchina" label="Family machine" v-slot="props" searchable position="centered"
        sortable :visible="showFamily">
        {{ props.row.famiglia_macchina }}
      </o-table-column>
      <o-table-column field="sottofamiglia_macchina" label="Under Family machine" v-slot="props" searchable
        position="centered" sortable :visible="showUnderFamily">
        {{ props.row.sottofamiglia_macchina }}
      </o-table-column>
      <o-table-column field="immagine_1" label="Image 1" v-slot="props" position="centered" :visible="showImage1">
        <b-button class="mx-2 button-format file-button" @click="watchImage(props.row.immagine_1)">Image 1</b-button>
      </o-table-column>
      <o-table-column field="immagine_2" label="Image 2" v-slot="props" position="centered" :visible="showImage2">
        <b-button class="mx-2 button-format file-button" @click="watchImage(props.row.immagine_2)">Image 2</b-button>
      </o-table-column>
      <o-table-column field="immagine_3" label="Image 3" v-slot="props" position="centered" :visible="showImage3">
        <b-button class="mx-2 button-format file-button" @click="watchImage(props.row.immagine_3)">Image 3</b-button>
      </o-table-column>

      <o-table-column field="date" label="Creation date" position="centered" v-slot="props" searchable sortable
        :visible="showCreationDate">
        {{ new Date(props.row.created_at).toLocaleDateString() }}
      </o-table-column>
      <o-table-column field="date" label="Update date" position="centered" v-slot="props" searchable sortable
        :visible="showUpdateDate">
        {{ new Date(props.row.updated_at).toLocaleDateString() }}
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
      <NoSignalItems v-if="showNoItem" />
    </div>
    <SeeImage v-if="showImage" :imageValue="imageValue" @close="hideModal()" />
  </div>
</template>

<script>
import NoSignalItems from '~/components/nodata/NoSignalItems'
import SeeImage from '~/components/popup/SeeImage'
export default {
  components: {
    NoSignalItems,
    SeeImage,
  },
  data() {
    return {
      showNoItem: true,
      show: false,
      showImage: false,
      selected: {},
      currentPage: 1,
      perPage: 2,
      showID: false,
      showTitle: false,
      showTicket: false,
      showAlarm: false,
      showFamily: false,
      showUnderFamily: false,
      showImage1: false,
      showImage2: false,
      showImage3: false,
      showCreationDate: false,
      showUpdateDate: false,
    }
  },
  methods: {
    watchImage(val) {
      this.imageValue = 'http://localhost:8000' + val
      this.showImage = true
    },
    hideModal() {
      this.showImage = false
    },
    pushRoute(route) {
      this.$router.push(`/signals/${route}`)
    },
    deleteDocument(id) {
      this.$bvModal
        .msgBoxConfirm('Are you sure you want to delete this Signal?', {
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
              .post(`/api/segnalazioni/${id}/delete`, {
                headers: {
                  Authorization: `Token ${this.$auth.strategy.token.get()}`,
                  'Content-Type': 'application/json',
                },
              })
              .then(() => {
                this.variant = 'danger'
                this.dataCreated = 'Signal deleted Succesfully'
                this.toggleToaster()
                this.$nuxt.refresh()
                this.show = false
                this.selectedId = []
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
  props: [
    'dataTable',
    'dropdown'
  ],
  watch: {
    dropdown: {
      handler(newVal) {
        newVal.forEach((item) => {
          if (item.text === 'ID') {
            this.showID = JSON.parse(item.value);
          } else if (item.text === 'Title') {
            this.showTitle = JSON.parse(item.value);
          } else if (item.text === 'Ticket') {
            this.showTicket = JSON.parse(item.value);
          } else if (item.text === 'Alarm') {
            this.showAlarm = JSON.parse(item.value);
          } else if (item.text === 'Family machine') {
            this.showFamily = JSON.parse(item.value);
          } else if (item.text === 'Under Family machine') {
            this.showUnderFamily = JSON.parse(item.value);
          } else if (item.text === 'Image 1') {
            this.showImage1 = JSON.parse(item.value);
          } else if (item.text === 'Image 2') {
            this.showImage2 = JSON.parse(item.value);
          } else if (item.text === 'Image 3') {
            this.showImage3 = JSON.parse(item.value);
          } else if (item.text === 'Creation date') {
            this.showCreationDate = JSON.parse(item.value);
          } else if (item.text === 'Update date') {
            this.showUpdateDate = JSON.parse(item.value);
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
  background-color: #28a745;
}

.edit-btn {
  background-color: #ffc107;
}

.delete-btn {
  background-color: #dc3545;
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