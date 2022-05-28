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
                <li class="nav-actions-color mx-2">
                  <i class="fas fa-plus pr-2 fas-main-color"></i>
                  New User
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
            <b-form @submit.prevent="onSubmit" class="create-solution-form">
              <div class="form-group row">
                <label for="tittle" class="col-sm-2 col-form-label create-label"
                  >Name</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="tittle"
                    v-model="form.name"
                    placeholder="Name"
                  />
                  <div class="error-show" v-if="showTitleSignalError">
                    Please enter the Title Signal!
                  </div>
                </div>
              </div>
              <div class="form-group row">
                <label for="ticket" class="col-sm-2 col-form-label create-label"
                  >Email</label
                >
                <div class="col-sm-10">
                  <input
                    type="email"
                    class="form-control input-create"
                    id="ticket"
                    v-model="form.email"
                    placeholder="Email"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="ticket" class="col-sm-2 col-form-label create-label"
                  >Password</label
                >
                <div class="col-sm-10">
                  <input
                    type="password"
                    class="form-control input-create"
                    id="ticket"
                    v-model="form.password"
                    placeholder="Password"
                  />
                </div>
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

export default {
  components: {
    Nav,
  },
  data() {
    return {
      show: false,
      dataCreated: '',
      variant: 'info',
      showTitleSignalError: null,
      form: {
        name: null,
        email: null,
        password: null,
      },
    }
  },
  methods: {
    onSubmit() {
      this.show = true
      console.log(this.form.password.length)
      if (
        this.form.name === null ||
        this.form.email === null ||
        this.form.password === null ||
        this.form.password.length < 7
      ) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please make sure all the fields are filled!'
        this.toggleToaster()
        return
      }
      this.$axios
        .post(`/user/register`, this.form, {
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
}
</script>
<style scoped>
/* .form-group {
  width: 100% !important;
} */
</style>
