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
                  <i class="fas fa-plus pr-2 fas-main-color"></i>
                  Update Signal
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
                  >Title Signal</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="tittle"
                    v-model="dataTable.titolo"
                    placeholder="Please enter Title Signal"
                  />
                  <div class="error-show" v-if="showTitleSignalError">
                    Please enter the Title Signal!
                  </div>
                </div>
              </div>
              <div class="form-group row">
                <label for="ticket" class="col-sm-2 col-form-label create-label"
                  >Ticket</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="ticket"
                    v-model="dataTable.rif_ticket"
                    placeholder="Please enter Ticket"
                  />
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
                    v-model="dataTable.descrizione"
                    placeholder="Please enter Description"
                  />
                </div>
              </div>

              <div class="form-group row">
                <label
                  for="id_alarme"
                  class="col-sm-2 col-form-label create-label"
                  >Id alarm</label
                >
                <div class="col-sm-10">
                  <input
                    type="number"
                    class="form-control input-create"
                    id="id_alarme"
                    v-model="dataTable.id_allarme"
                    placeholder="Please enter Id alarm"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="description"
                  class="col-sm-2 col-form-label create-label"
                  >Description Alarm</label
                >
                <div class="col-sm-10">
                  <VueEditor
                    v-model="dataTable.descrizione_allarme"
                    placeholder="Please enter Description Alarm"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="immag1" class="col-sm-2 col-form-label create-label"
                  >Image 1</label
                >
                <div class="col-sm-10" style="display: flex !important">
                  <b-button
                    class="mx-2 button-format file-button"
                    @click="watchImage(dataTable.immagine_1)"
                    >Image 1
                  </b-button>
                  <b-form-file
                    placeholder="Add new Image or drop it here..."
                    drop-placeholder="Drop file here..."
                    @change="fileChange"
                  ></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="immag2" class="col-sm-2 col-form-label create-label"
                  >Image 2</label
                >
                <div class="col-sm-10" style="display: flex !important">
                  <b-button
                    class="mx-2 button-format file-button"
                    @click="watchImage(dataTable.immagine_2)"
                    >Image 2
                  </b-button>
                  <b-form-file
                    placeholder="Add new Image or drop it here..."
                    drop-placeholder="Drop file here..."
                    @change="fileChange2"
                  ></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="immag3" class="col-sm-2 col-form-label create-label"
                  >Image 3</label
                >
                <div class="col-sm-10" style="display: flex !important">
                  <b-button
                    class="mx-2 button-format file-button"
                    @click="watchImage(dataTable.immagine_3)"
                    >Image 3
                  </b-button>
                  <b-form-file
                    placeholder="Add new Image or drop it here..."
                    drop-placeholder="Drop file here..."
                    @change="fileChange3"
                  ></b-form-file>
                </div>
              </div>
              <!-- <div class="form-group row">
                <label for="sector" class="col-sm-2 col-form-label create-label"
                  >Reference sector</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="sector"
                    placeholder="Reference sector"
                  />
                </div>
              </div> -->
              <div class="form-group row">
                <label for="note" class="col-sm-2 col-form-label create-label"
                  >Note</label
                >
                <div class="col-sm-10">
                  <VueEditor
                    v-model="dataTable.note"
                    placeholder="Please enter Note"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-2 col-form-label create-label"
                  >Family machine</label
                >
                <div class="col-sm-10">
                  <b-form-select
                    v-model="dataTable.famiglia_macchina"
                    :options="famiglia_macchina_options"
                  >
                  </b-form-select>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-2 col-form-label create-label"
                  >Under Family machine</label
                >
                <div class="col-sm-10">
                  <b-form-select
                    v-model="dataTable.sottofamiglia_macchina"
                    :options="sottofamiglia_macchina_options"
                  >
                  </b-form-select>
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
      <SeeImage
        v-if="showImage"
        :imageValue="imageValue"
        @close="hideModal()"
      />
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
import SeeImage from '~/components/popup/SeeImage'
export default {
  components: {
    Nav,
    SeeImage,
  },
  data() {
    return {
      show: false,
      showImage: false,
      dataCreated: '',
      variant: 'info',
      showTitleSignalError: null,
      famiglia_macchina_options: [
        { value: null, text: 'Select' },
        { value: 'Modula', text: 'Modula' },
        { value: 'Easy2', text: 'Easy2' },
        { value: 'Twin Shape 3', text: 'Twin Shape 3' },
      ],
      sottofamiglia_macchina_options: [
        { value: null, text: 'Select' },
        { value: '1', text: '1' },
        { value: '2', text: '2' },
        { value: '3', text: '3' },
      ],
      imageValue: null,
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
    watchImage(val) {
      this.imageValue = 'http://localhost:8000' + val
      this.showImage = true
    },
    onSubmit() {
      // this.show = true
      if (this.dataTable.titolo === null || this.dataTable.titolo === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Title Signal!'
        this.toggleToaster()
        return
      }
      if (
        this.dataTable.id_allarme === null ||
        this.dataTable.id_allarme === ''
      ) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Alarm Id!'
        this.toggleToaster()
        return
      }
      const data = new FormData()

      if (this.tempimmagine_1 !== null) {
        data.append('immagine_1', this.tempimmagine_1)
      }
      if (this.tempimmagine_2 !== null) {
        data.append('immagine_2', this.tempimmagine_2)
      }
      if (this.tempimmagine_3 !== null) {
        data.append('immagine_3', this.tempimmagine_3)
      }
      data.append('titolo', this.dataTable.titolo)
      data.append('descrizione', this.dataTable.descrizione)
      data.append('settore_riferimento', 'test test')
      data.append('note', this.dataTable.note)
      data.append('rif_ticket', this.dataTable.rif_ticket)
      data.append('descrizione_allarme', this.dataTable.descrizione_allarme)
      data.append('id_allarme', this.dataTable.id_allarme)
      data.append('famiglia_macchina', this.dataTable.famiglia_macchina)
      data.append(
        'sottofamiglia_macchina',
        this.dataTable.sottofamiglia_macchina
      )
      this.$axios
        .post(`/api/segnalazioni/update/${this.$route.params.id}`, data, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Signal Updated Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/signals')
          }, 3000)
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
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
    hideModal() {
      this.showImage = false
    },
  },

  async asyncData({ store, $axios, params }) {
    let response = await $axios.get(
      `/api/segnalazioni/retrive_segnalazioni/${params.id}`
    )
    let dataTable = response.data[0]
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
