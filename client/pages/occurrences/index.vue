<template>
  <div class="wrapper d-flex align-items-stretch">
    <client-only>
      <Nav />
      <div id="content" class="p-4 p-md-5 pt-5">
        <div class="wrapped-content">
          <div
            class="
              nav-actions
              d-flex
              justify-content-between
              align-items-center
              mb-2
              navtop
              respo-nav-top
            "
          >
            <!-- First Nav -->
            <div class="d-flex gap-4">
              <ul
                class="
                  d-flex
                  justify-content-around
                  align-content-center
                  m-0
                  p-0
                "
                style="list-style: none"
              >
                <li class="nav-actions-color mx-2">
                  <i class="fas fa-bars pr-2 fas-main-color"></i>
                  Occurrences
                </li>
              </ul>
            </div>
            <div
              class="
                d-flex
                justify-content-around
                align-content-center align-items-center
              "
            >
              <button
                role="button"
                class="mx-2 button-format"
                @click="redirectCreate()"
                style="height: 40px"
              >
                <i class="mdi mdi-plus pr-2"></i>
                New Occurrence
              </button>

              <b-dropdown
                class="m-2 table-filter-cols"
                id="dropdown-form"
                text="Select fields to display"
                ref="dropdown"
              >
                <b-dropdown-form>
                  <b-form-checkbox
                    v-for="(drop, index) in dropdown"
                    :key="index"
                    class="table-checkbox mb-3"
                    v-model="drop.value"
                    value="true"
                    unchecked-value="false"
                    @change="dropDownChange(drop)"
                    >{{ drop.text }}
                  </b-form-checkbox>
                </b-dropdown-form>
              </b-dropdown>
            </div>
            <!-- End here -->
          </div>
          <div class="vertical-line"></div>

          <div class="table-space">
            <b-overlay :show="show" rounded="sm">
              <OccurenzeTable :dataTable="dataTable" :dropdown="dropdown" />
            </b-overlay>
          </div>
        </div>
      </div>
      <b-toast id="deleted" :variant="variant" solid>
        <template #toast-title>
          <div class="d-flex flex-grow-1 align-items-baseline">
            <strong class="mr-auto">Notification!</strong>
          </div>
        </template>
        {{ dataCreated }}
      </b-toast>
    </client-only>
  </div>
</template>

<script>
import Nav from '~/components/Nav'
import OccurenzeTable from '~/components/tables/OccurenzeTable.vue'
export default {
  components: {
    Nav,
    OccurenzeTable,
  },
  data() {
    return {
      selected: null,
      dataTable: [],
      selectedId: [],
      dataCreated: '',
      variant: '',
      show: false,
      options: [
        { value: null, text: '10' },
        { value: '15', text: '15' },
        { value: '20', text: '20' },
        { value: '25', text: '25' },
        { value: '30', text: '30', disabled: true },
      ],
      statusIdoccurrence: '1',
      statusIdsignal: '1',
      statusIdsolution: '1',
      statusTitle: '1',
      statusMachine: '0',
      statusTicket: '0',
      statusVersion1: '0',
      statusVersion2: '0',
      statusOccurrenceDate: '1',
      statusOccurrenceStatus: '1',
      statusCreationDate: '1',
      statusUpdateDate: '1',
      filterName: null,
      idAscDesc: null,
      statusAscDesc: false,
      dropdown: [
        {
          text: 'ID',
          value: true,
        },
        {
          text: 'Id signal',
          value: true,
        },
        {
          text: 'Id solution',
          value: true,
        },
        {
          text: 'Title',
          value: true,
        },
        {
          text: 'Machine order',
          value: true,
        },
        {
          text: 'Ticket',
          value: true,
        },
        {
          text: 'Version sw 1',
          value: true,
        },
        {
          text: 'Version sw 2',
          value: true,
        },
        {
          text: 'Occurrence date',
          value: true,
        },
        {
          text: 'Occurrence status',
          value: true,
        },
        {
          text: 'Creation date',
          value: true,
        },
        {
          text: 'Update date',
          value: true,
        },
      ],
    }
  },
  methods: {
    orderAscDesc() {
      this.statusAscDesc = !this.statusAscDesc
      if (this.statusAscDesc === true) {
        this.idAscDesc = '-id'
      } else {
        this.idAscDesc = 'id'
      }
      this.onSubmitAscDesc()
    },
    idToDelete(val) {
      this.selectedId = val
    },
    redirectCreate() {
      this.$router.push(`/occurrences/create`)
    },
    onSubmitSearch() {
      this.show = true
      this.$axios
        .get('/api/occorrenze/filter', {
          params: {
            search: this.filterName,
          },
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
        })
        .then((response) => {
          this.dataTable = response.data
          this.show = false
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    onSubmitAscDesc() {
      this.show = true
      this.$axios
        .get('/api/occorrenze/filter', {
          params: {
            ordering: this.idAscDesc,
          },
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
        })
        .then((response) => {
          this.dataTable = response.data
          this.show = false
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    updateDocument() {
      // this.$router.push(`/occorrences/update/2`)
      console.log(this.selectedId)
      if (this.selectedId.length === 0) {
        this.$bvModal.msgBoxOk(
          `Please select one of the occurrences for updating!`,
          {
            title: `Attention`,
            size: 'md',
            buttonSize: 'md',
            okVariant: 'danger',
            okTitle: `Ok`,
            headerClass: 'p-2 border-bottom-0',
            footerClass: 'p-2 border-top-0',
            centered: true,
          }
        )
        return
      }
      if (this.selectedId.length > 1) {
        this.$bvModal.msgBoxOk(
          `Please select only one of the occurrences for updating!`,
          {
            title: `Attention`,
            size: 'md',
            buttonSize: 'md',
            okVariant: 'danger',
            okTitle: `Ok`,
            headerClass: 'p-2 border-bottom-0',
            footerClass: 'p-2 border-top-0',
            centered: true,
          }
        )
        return
      }
      this.$router.push(`/occurrences/update/${this.selectedId[0]}`)
    },
    deleteDocument() {
      if (this.selectedId.length === 0) {
        this.$bvModal.msgBoxOk(
          `Please select one of the occurrences for deleting!`,
          {
            title: `Attention`,
            size: 'md',
            buttonSize: 'md',
            okVariant: 'danger',
            okTitle: `Ok`,
            headerClass: 'p-2 border-bottom-0',
            footerClass: 'p-2 border-top-0',
            centered: true,
          }
        )
        return
      }
      if (this.selectedId.length > 1) {
        this.$bvModal.msgBoxOk(
          `Please select only one of the occurrences for deleting!`,
          {
            title: `Attention`,
            size: 'md',
            buttonSize: 'md',
            okVariant: 'danger',
            okTitle: `Ok`,
            headerClass: 'p-2 border-bottom-0',
            footerClass: 'p-2 border-top-0',
            centered: true,
          }
        )
        return
      }

      this.$bvModal
        .msgBoxConfirm('Are you sure you want to delete this occurrence?', {
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
              .post(`/api/occorrenze/${this.selectedId[0]}/delete`, {
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
    dropDownChange(val) {
      const indexArray = this.dropdown.findIndex((e) => e.text === val.text)
      this.dropdown[indexArray].value = val.value
      localStorage.setItem('occurrenceTable', JSON.stringify(this.dropdown))
    },
  },
  mounted() {
    if (process.client) {
      let occurrenceTable = localStorage.getItem('occurrenceTable')
      if (occurrenceTable) {
        this.dropdown = JSON.parse(occurrenceTable)
      } else {
        localStorage.setItem('occurrenceTable', JSON.stringify(this.dropdown))
      }
    }
  },
  async asyncData({ store, $axios }) {
    let response = await $axios.get(`/api/occorrenze/retrive_occorrenze`)
    let dataTable = response.data
    return {
      dataTable,
    }
  },
}
</script>
<style scoped>
</style>
