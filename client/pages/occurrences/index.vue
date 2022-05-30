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
            <ul
              class="d-flex justify-content-around align-content-center m-0 p-0"
              style="list-style: none"
            >
              <li
                role="button"
                class="mx-2 button-format"
                @click="redirectCreate()"
              >
                <i class="fas fa-plus pr-2"></i>
                New Occurrence
              </li>
              <li
                role="button"
                class="mx-2 button-format"
                @click="updateDocument()"
              >
                <i class="fas fa-edit pr-2"></i>
                Update Occurrence
              </li>
              <li
                role="button"
                class="mx-2 button-format"
                @click="deleteDocument()"
              >
                <i class="fas fa-trash pr-2"></i>
                Delete Occurrence
              </li>
            </ul>
            <!-- End here -->
          </div>
          <div class="vertical-line"></div>
          <div
            class="
              nav-actions
              d-flex
              justify-content-between
              align-items-center
              mb-2
              navtop
              second-nav-option
            "
          >
            <!-- Second Nav -->
            <div class="d-flex gap-4 second-d-flex-left">
              <b-input-group class="mt-3">
                <b-form-input
                  class="input-search"
                  v-model="filterName"
                  placeholder="Search"
                  style="height: 40px !important"
                ></b-form-input>
                <b-input-group-append>
                  <b-button class="button-format" @click="onSubmitSearch()">
                    <i class="fas fa-search pr-2"></i>Search</b-button
                  >
                </b-input-group-append>
              </b-input-group>
            </div>
            <div
              class="
                d-flex
                justify-content-around
                align-content-center
                m-0
                p-0
                second-d-flex-right
              "
            >
              <b-dropdown
                class="m-2 table-filter-cols"
                id="dropdown-form"
                text="Select fields to display"
                ref="dropdown"
              >
                <b-dropdown-form>
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusIdoccurrence"
                    value="1"
                    unchecked-value="0"
                    >Id Occurrence</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusIdsignal"
                    value="1"
                    unchecked-value="0"
                    >Id Signal</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusIdsolution"
                    value="1"
                    unchecked-value="0"
                    >Id Solution
                  </b-form-checkbox>
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusTitle"
                    value="1"
                    unchecked-value="0"
                    >Title</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusMachine"
                    value="1"
                    unchecked-value="0"
                    >Machine order</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusVersion1"
                    value="1"
                    unchecked-value="0"
                    >Version sw 1</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusVersion2"
                    value="1"
                    unchecked-value="0"
                    >Version sw 2</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusOccurrenceDate"
                    value="1"
                    unchecked-value="0"
                    >Occurrence date</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusOccurrenceStatus"
                    value="1"
                    unchecked-value="0"
                    >Occurrence status</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusCreationDate"
                    value="1"
                    unchecked-value="0"
                    >Creation date</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusUpdateDate"
                    value="1"
                    unchecked-value="0"
                    >Update date</b-form-checkbox
                  >
                </b-dropdown-form>
              </b-dropdown>
              <b-form-select
                class="number-rows"
                v-model="selected"
                :options="options"
              ></b-form-select>
            </div>
            <!-- End here -->
          </div>
          <div class="table-space">
            <b-overlay :show="show" rounded="sm">
              <OccurenzeTable
                :dataTable="dataTable"
                :statusIdoccurrence="statusIdoccurrence"
                :statusIdsignal="statusIdsignal"
                :statusIdsolution="statusIdsolution"
                :statusTitle="statusTitle"
                :statusMachine="statusMachine"
                :statusVersion1="statusVersion1"
                :statusVersion2="statusVersion2"
                :statusOccurrenceDate="statusOccurrenceDate"
                :statusOccurrenceStatus="statusOccurrenceStatus"
                :statusCreationDate="statusCreationDate"
                :statusUpdateDate="statusUpdateDate"
                @get-new-delete-id="idToDelete"
                @order-asc-desc="orderAscDesc"
              />
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
      statusVersion1: '0',
      statusVersion2: '0',
      statusOccurrenceDate: '1',
      statusOccurrenceStatus: '1',
      statusCreationDate: '1',
      statusUpdateDate: '1',
      filterName: null,
      idAscDesc: null,
      statusAscDesc: false,
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
        })
    },
    toggleToaster() {
      this.$bvToast.show('deleted')
      setTimeout(() => {
        this.$bvToast.hide('deleted')
      }, 2000)
    },
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
