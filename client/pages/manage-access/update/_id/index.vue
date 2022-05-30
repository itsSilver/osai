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
                <li
                  class="nav-actions-color mx-2"
                  v-if="showPermissionList === false"
                >
                  <i class="fas fa-plus pr-2 fas-main-color"></i>
                  New User
                </li>
                <li
                  class="nav-actions-color mx-2"
                  v-if="showPermissionList === true"
                >
                  <i class="fas fa-plus pr-2 fas-main-color"></i>
                  Add the permissions to User
                </li>
              </ul>
            </div>
            <ul
              class="d-flex justify-content-around align-content-center m-0 p-0"
              style="list-style: none"
            ></ul>
            <!-- End here -->
          </div>
          <div class="vertical-line"></div>
          <!-- Form start here -->
          <b-overlay :show="show" rounded="sm">
            <b-form
              @submit.prevent="onSubmitPermission"
              class="create-solution-form"
            >
              <h5 class="text-center">Check the permissions for this user!</h5>
              <div class="form-group row">
                <PermissionsList
                  :dataTable="dataPermission"
                  @data-send="dataSend"
                />
              </div>

              <div class="form-group row">
                <div class="col-sm-10">
                  <b-button type="submit" class="mx-2 button-format">
                    <i class="fas fa-download pr-2"></i>
                    Save
                  </b-button>
                </div>
              </div>
            </b-form>
          </b-overlay>
          <!-- End here -->
        </div>
      </div>
    </client-only>
    <b-toast id="created" :variant="variant" solid>
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
import Nav from '~/components/Nav'
import PermissionsList from '~/components/PermissionsList'
export default {
  components: {
    Nav,
    PermissionsList,
  },
  data() {
    return {
      show: false,
      accountCreated: null,
      dataPermission: [],
      dataCreated: '',
      variant: 'info',
      showTitleSignalError: null,
      form: {
        name: null,
        email: null,
        password: null,
      },
      showPermissionList: false,
      dataTable: [],
      selected: [],
    }
  },
  mounted() {
    this.getPermissionData()
  },
  methods: {
    dataSend(val) {
      this.selected = val
    },
    onSubmit() {
      this.show = true
      if (
        this.dataTable.username === null ||
        this.dataTable.email === null ||
        this.dataTable.password === null ||
        this.dataTable.password.length < 7
      ) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please make sure all the fields are filled!'
        this.toggleToaster()
        return
      }
      this.$axios
        .post(`/user/update/${this.$route.params.id}`, this.dataTable, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'User updated Succesfully'
          //   this.toggleToaster()
          //   setTimeout(() => {
          //     this.$router.push('/manage-access')
          //   }, 2000)
          this.showPermissionList = true
          this.getPermissionData()
        })
        .catch((error) => {
          this.show = false
          this.dataCreated = 'Something went wrong!'
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    async getPermissionData() {
      this.show = true
      await this.$axios
        .get(`/user/permissions`, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.dataPermission = response.data
          this.show = false
        })
        .catch((error) => {
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    onSubmitPermission() {
      const datapayload = {
        permission_id: this.selected,
      }

      this.show = true
      this.$axios
        .post(`/user/add/permission/${this.$route.params.id}`, datapayload, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'User created Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/manage-access')
          }, 2000)
          // this.showPermissionList = true
          // this.getPermissionData()
        })
        .catch((error) => {
          this.show = false
          this.dataCreated = 'Something went wrong!'
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    hideModal() {
      this.showFindOccurrence = false
    },
    toggleToaster() {
      this.$bvToast.show('created')
      setTimeout(() => {
        this.$bvToast.hide('created')
        this.variant = 'info'
      }, 2000)
    },
  },
  async asyncData({ store, $axios, params }) {
    let response = await $axios.get(`/user/id/${params.id}`)
    let dataTable = response.data
    return {
      dataTable,
    }
  },
}
</script>
<style scoped>
/* .form-group {
  width: 100% !important;
} */
</style>
