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
                <li class="nav-actions-color mx-2 px-14-format">
                  <i class="mdi mdi-plus pr-2 fas-main-color"></i>
                  New Solution
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
                  >Title Solution</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="tittle"
                    v-model="form.titolo"
                    placeholder="Please enter Title Solution"
                  />
                </div>
              </div>
              <!-- <div class="form-group row">
                <label for="tittle" class="col-sm-2 col-form-label create-label"
                  >Id Solution</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="tittle"
                    placeholder="Id Solution"
                  />
                </div>
              </div> -->
              <div class="form-group row">
                <label for="rank" class="col-sm-2 col-form-label create-label"
                  >Rank</label
                >
                <div class="col-sm-10">
                  <!-- <input
                    type="text"
                    class="form-control input-create"
                    id="rank"
                    v-model="form.rank"
                    placeholder="Rank"
                  /> -->
                  <b-form-select
                    v-model="form.rank"
                    :options="rank_options"
                  ></b-form-select>
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="description"
                  class="col-sm-2 col-form-label create-label"
                  >Description</label
                >
                <div class="col-sm-10">
                  <VueEditor
                    v-model="form.descrizione"
                    placeholder="Please enter Description"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="immag2" class="col-sm-2 col-form-label create-label"
                  >Image 1</label
                >
                <div class="col-sm-10">
                  <b-form-file
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                    @change="fileChange"
                  ></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="immag2" class="col-sm-2 col-form-label create-label"
                  >Image 2</label
                >
                <div class="col-sm-10">
                  <b-form-file
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                    @change="fileChange2"
                  ></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="immag3" class="col-sm-2 col-form-label create-label"
                  >Image 3</label
                >
                <div class="col-sm-10">
                  <b-form-file
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                    @change="fileChange3"
                  ></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="sector" class="col-sm-2 col-form-label create-label"
                  >Reference sector</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="sector"
                    v-model="form.settore_riferimento"
                    placeholder="Please enter Reference sector"
                  />
                </div>
              </div>
              <!-- <div class="form-group row">
              <label for="solution" class="col-sm-2 col-form-label create-label"
                >Id state solution</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="solution"
                  placeholder="Id state solution"
                />
              </div>
            </div> -->
              <div class="form-group row">
                <label for="note" class="col-sm-2 col-form-label create-label"
                  >Note</label
                >
                <div class="col-sm-10">
                  <VueEditor
                    v-model="form.note"
                    placeholder="Please enter Note"
                  />
                </div>
              </div>
              <div class="form-group row">
                <div class="col-sm-10">
                  <b-button type="submit" class="mx-2 button-format">
                    <i class="mdi mdi-check pr-2"></i>
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
        titolo: null,
        descrizione: '',
        rank: null,
        note: '',
        immagine_1: null,
        immagine_2: null,
        immagine_3: null,
        settore_riferimento: '',
      },
      rank_options: [
        { value: null, text: 'Select' },
        { value: '1', text: '1' },
        { value: '2', text: '2' },
        { value: '3', text: '3' },
        { value: '4', text: '4' },
        { value: '5', text: '5' },
      ],
      tempimmagine_1: null,
      tempimmagine_2: null,
      tempimmagine_3: null,
    }
  },
  methods: {
    fileChange(event) {
      this.tempimmagine_1 = event.target.files[0]
    },
    fileChange2(event) {
      this.tempimmagine_2 = event.target.files[0]
    },
    fileChange3(event) {
      this.tempimmagine_3 = event.target.files[0]
    },
    onSubmit() {
      this.show = true
      if (this.form.titolo === null || this.form.titolo === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Title Signal!'
        this.toggleToaster()
        return
      }

      const data = new FormData()
      data.append('titolo', this.form.titolo)
      data.append('descrizione', this.form.descrizione)
      if (this.tempimmagine_1 !== null) {
        data.append('immagine_1', this.tempimmagine_1)
      }
      if (this.tempimmagine_1 !== null) {
        data.append('immagine_2', this.tempimmagine_2)
      }
      if (this.tempimmagine_1 !== null) {
        data.append('immagine_3', this.tempimmagine_3)
      }
      if (this.form.rank !== null) {
        data.append('rank', this.form.rank)
      }
      data.append('settore_riferimento', this.form.settore_riferimento)
      data.append('note', this.form.note)
      data.append('rif_ticket', this.form.rif_ticket)

      this.$axios
        .post(`/api/soluzioni/create`, data, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Signal created Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/solutions')
          }, 2000)
        })
        .catch((error) => {
          this.show = false
          this.dataCreated = error.response.data.message[0]
          this.variant = 'danger'
          this.toggleToaster()
        })
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
