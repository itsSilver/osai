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
                  Manage Access
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
                New User
              </li>
              <li
                role="button"
                class="mx-2 button-format"
                @click="updateDocument()"
              >
                <i class="fas fa-edit pr-2"></i>
                Update User
              </li>
              <li
                role="button"
                class="mx-2 button-format"
                @click="deleteDocument()"
              >
                <i class="fas fa-trash pr-2"></i>
                Delete User
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
              <b-dropdown
                class="m-2 table-filter-cols"
                id="dropdown-form"
                text="Select fields to display"
                ref="dropdown"
              >
                <b-dropdown-form>
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusUserId"
                    value="1"
                    unchecked-value="0"
                    >Id User</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusName"
                    value="1"
                    unchecked-value="0"
                    >Name</b-form-checkbox
                  >
                  <b-form-checkbox
                    class="table-checkbox mb-3"
                    v-model="statusEmail"
                    value="1"
                    unchecked-value="0"
                    >Email</b-form-checkbox
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
              <UsersTable
                :dataTable="dataTable"
                :statusUserId="statusUserId"
                :statusName="statusName"
                :statusEmail="statusEmail"
                :statusCreationDate="statusCreationDate"
                :statusUpdateDate="statusUpdateDate"
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
import UsersTable from '~/components/tables/UsersTable.vue'
export default {
  components: {
    Nav,
    UsersTable,
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
      statusUserId: '1',
      statusName: '1',
      statusEmail: '1',
      statusCreationDate: '1',
      statusUpdateDate: '0',
    }
  },
  methods: {
    idToDelete(val) {
      this.selectedId = val
    },
    redirectCreate() {
      this.$router.push(`/manage-access/create`)
    },
    updateDocument() {
      if (this.selectedId.length === 0) {
        this.$bvModal.msgBoxOk(`Please select one of the Users for updating!`, {
          title: `Attention`,
          size: 'md',
          buttonSize: 'md',
          okVariant: 'danger',
          okTitle: `Ok`,
          headerClass: 'p-2 border-bottom-0',
          footerClass: 'p-2 border-top-0',
          centered: true,
        })
        return
      }
      if (this.selectedId.length > 1) {
        this.$bvModal.msgBoxOk(
          `Please select only one of the Users for updating!`,
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
      this.$router.push(`/manage-access/update/${this.selectedId[0]}`)
    },
    deleteDocument() {
      if (this.selectedId.length === 0) {
        this.$bvModal.msgBoxOk(`Please select one of the Users for deleting!`, {
          title: `Attention`,
          size: 'md',
          buttonSize: 'md',
          okVariant: 'danger',
          okTitle: `Ok`,
          headerClass: 'p-2 border-bottom-0',
          footerClass: 'p-2 border-top-0',
          centered: true,
        })
        return
      }
      if (this.selectedId.length > 1) {
        this.$bvModal.msgBoxOk(
          `Please select only one of the Users for deleting!`,
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
              .post(`/user/remove/${this.selectedId[0]}`, {
                headers: {
                  Authorization: `Token ${this.$auth.strategy.token.get()}`,
                  'Content-Type': 'application/json',
                },
              })
              .then(() => {
                this.variant = 'danger'
                this.dataCreated = 'User deleted Succesfully'
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
    let response = await $axios.get(`/user/users-list`)
    let dataTable = response.data
    return {
      dataTable,
    }
  },
}
</script>
<style scoped>
</style>
