<!-- Please remove this file from your project -->
<template>
  <section class="h-100 gradient-form" style="background-color: #eee">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-xl-10">
          <div class="card rounded-3 text-black">
            <div class="row g-0">
              <div class="col-lg-6">
                <div class="card-body p-md-5 mx-md-4">
                  <div class="text-center">
                    <img
                      src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                      style="width: 185px"
                      alt="logo"
                    />
                    <h4 class="mt-1 mb-5 pb-1">OSAI</h4>
                  </div>

                  <b-form @submit.prevent="submitForm">
                    <p>Please login to your account</p>

                    <div class="form-outline mb-4">
                      <b-form-input
                        type="email"
                        id="form2Example11"
                        class="form-control"
                        placeholder="Phone number or email address"
                        v-model="form.email"
                      />
                      <label class="form-label" for="form2Example11"
                        >Username</label
                      >
                    </div>

                    <div class="form-outline mb-4">
                      <b-form-input
                        type="password"
                        id="form2Example22"
                        class="form-control"
                        placeholder="Password"
                        v-model="form.password"
                      />
                      <label class="form-label" for="form2Example22"
                        >Password</label
                      >
                    </div>

                    <div class="text-center pt-1 mb-5 pb-1">
                      <button
                        class="
                          btn btn-primary btn-block
                          fa-lg
                          gradient-custom-2
                          mb-3
                          login-button
                        "
                        type="submit"
                      >
                        Log in
                      </button>
                      <a class="text-muted" href="#!">Forgot password?</a>
                    </div>
                  </b-form>
                </div>
              </div>
              <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                  <h4 class="mb-4">Welcome to Osai!</h4>
                  <p class="small mb-0">Osai make your job easier.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  middleware: 'auth',
  auth: 'guest',
  layout: 'login',
  name: 'login',
  data() {
    return {
      form: {
        email: null,
        password: null,
      },
      errors: {
        email: false,
        password: false,
      },
      token: null,
    }
  },
  methods: {
    async submitForm() {
      await this.$axios
        .post('/user/login', this.form)
        .then((response) => {
          this.token = response.data.token
          this.$auth.strategy.token.set(this.token)
          this.redirectPage()
        })
        .catch((err) => {})
    },
    redirectPage() {
      this.$router.go(this.$router.currentRoute)
    },
    // await this.$axios
    //     .post('/login', this.form)
    //     .then((response) => {
    //       this.token = response.data.token
    //       this.$auth.strategy.token.set(this.token)
    //       this.showModalCompany = true
    //     })
    //     .catch((err) => {
    //       this.show = false
    //       this.error_server = err.response.data.error
    //     })
  },
}
</script>
<style scoped>
.login-button {
  width: 100%;
}
.gradient-custom-2 {
  background: #485679;
}

@media (min-width: 768px) {
  .gradient-form {
    height: 100vh !important;
  }
}
@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}
</style>
