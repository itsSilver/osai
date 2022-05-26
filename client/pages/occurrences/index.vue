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
                  placeholder="Search"
                  style="height: 40px !important"
                ></b-form-input>
                <b-input-group-append>
                  <b-button class="button-format">
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
                @get-new-delete-id="idToDelete"
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
    }
  },
  methods: {
    idToDelete(val) {
      this.selectedId = val
    },
    redirectCreate() {
      this.$router.push(`/occurrences/create`)
    },
    updateDocument() {
      // this.$router.push(`/occorrences/update/2`)
      console.log('Val here to be deleted!', this.selectedId)
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
      console.log('Val here to be deleted!', this.selectedId)
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
