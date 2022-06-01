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
                  Solutions
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
                New Solution
              </li>
              <li
                role="button"
                class="mx-2 button-format"
                @click="updateDocument()"
              >
                <i class="fas fa-edit pr-2"></i>
                Update Solution
              </li>
              <li
                role="button"
                class="mx-2 button-format"
                @click="deleteDocument()"
              >
                <i class="fas fa-trash pr-2"></i>
                Delete Solution
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
                    v-model="statusIdsolution"
                    value="1"
                    unchecked-value="0"
                    >Id Solution</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusTitle"
                    value="1"
                    unchecked-value="0"
                    >Title</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusRank"
                    value="1"
                    unchecked-value="0"
                    >Rank</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusSector"
                    value="1"
                    unchecked-value="0"
                    >Reference Sector</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusIdStSolutions"
                    value="1"
                    unchecked-value="0"
                    >Id Status Solutions</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusImage1"
                    value="1"
                    unchecked-value="0"
                    >Image 1</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusImage2"
                    value="1"
                    unchecked-value="0"
                    >Image 2</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusImage3"
                    value="1"
                    unchecked-value="0"
                    >Image 3</b-form-checkbox
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
              <SolutionsTable
                :dataTable="dataTable"
                :statusIdsolution="statusIdsolution"
                :statusTitle="statusTitle"
                :statusRank="statusRank"
                :statusSector="statusSector"
                :statusIdStSolutions="statusIdStSolutions"
                :statusCreationDate="statusCreationDate"
                :statusUpdateDate="statusUpdateDate"
                :statusImage1="statusImage1"
                :statusImage2="statusImage2"
                :statusImage3="statusImage3"
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
import SolutionsTable from '~/components/tables/SolutionsTable.vue'
export default {
  components: {
    Nav,
    SolutionsTable,
  },
  data() {
    return {
      selected: null,
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
      statusIdsolution: '1',
      statusTitle: '1',
      statusRank: '1',
      statusSector: '1',
      statusIdStSolutions: '0',
      statusCreationDate: '1',
      statusUpdateDate: '1',
      statusImage1: '0',
      statusImage2: '0',
      statusImage3: '0',
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
      this.$router.push(`/solutions/create`)
    },
    onSubmitSearch() {
      this.show = true
      this.$axios
        .get('/api/soluzioni/filter', {
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
        .get('/api/soluzioni/filter', {
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
      // this.$router.push(`/solutions/update/2`)
      if (this.selectedId.length === 0) {
        this.$bvModal.msgBoxOk(
          `Please select one of the Solutions for updating!`,
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
          `Please select only one of the Solutions for updating!`,
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
      this.$router.push(`/solutions/update/${this.selectedId[0]}`)
    },
    deleteDocument() {
      if (this.selectedId.length === 0) {
        this.$bvModal.msgBoxOk(
          `Please select one of the Solutions for deleting!`,
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
          `Please select only one of the Solutions for deleting!`,
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
              .post(`/api/soluzioni/${this.selectedId[0]}/delete`, {
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
    let response = await $axios.get(`/api/soluzioni/retrive_soluzioni`)
    let dataTable = response.data
    return {
      dataTable,
    }
  },
}
</script>
<style scoped>
</style>
