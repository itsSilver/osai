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
                  New Occurrence
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
                <label
                  for="id-segnalazione"
                  class="col-sm-2 col-form-label create-label"
                  >Id signal</label
                >
                <div class="col-sm-10">
                  <input
                    type="number"
                    class="form-control input-create"
                    id="id-segnalazione"
                    v-model="dataTable.segnalazione"
                    placeholder="Id signal"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="id-soluzione"
                  class="col-sm-2 col-form-label create-label"
                  >Id solution</label
                >
                <div class="col-sm-10">
                  <input
                    type="number"
                    class="form-control input-create"
                    id="id-soluzione"
                    v-model="dataTable.soluzioni_id[0]"
                    placeholder="Id solution"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="tittle" class="col-sm-2 col-form-label create-label"
                  >Title</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="tittle"
                    v-model="dataTable.titolo"
                    placeholder="Title"
                  />
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
                    placeholder="Ticket"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="textarea-small"
                  class="col-sm-2 col-form-label create-label"
                  >Description</label
                >
                <div class="col-sm-10">
                  <ckeditor
                    :editor="editor"
                    :value="value"
                    :config="config"
                    :tagName="tagName"
                    :disabled="disabled"
                    @input="(event) => $emit('input', event)"
                    v-model="dataTable.descrizione"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="machine"
                  class="col-sm-2 col-form-label create-label"
                  >Machine order</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="machine"
                    v-model="dataTable.commessa_macchina"
                    placeholder="Machine order"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="version-1"
                  class="col-sm-2 col-form-label create-label"
                  >Version sw 1</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="version-1"
                    v-model="dataTable.versione_sw_1"
                    placeholder="Version sw 1"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="version-2"
                  class="col-sm-2 col-form-label create-label"
                  >Version sw 2</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="version-2"
                    v-model="dataTable.versione_sw_2"
                    placeholder="Version sw 2"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="data-occorrenza"
                  class="col-sm-2 col-form-label create-label"
                  >Occurrence date</label
                >
                <div class="col-sm-10">
                  <b-form-datepicker
                    id="example-datepicker"
                    v-model="dataTable.data_occorrenza"
                    class="mb-2 date-choose"
                    today-button
                    reset-button
                    close-button
                    selected-variant="primary"
                    today-variant="primary"
                    hide-header
                    label-close-button="Close"
                    label-today-button="Today"
                    label-reset-button="Reset"
                  ></b-form-datepicker>
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="status-occorrenza"
                  class="col-sm-2 col-form-label create-label"
                  >Occurrence status</label
                >
                <div class="col-sm-10">
                  <input
                    type="number"
                    class="form-control input-create"
                    id="status-occorrenza"
                    v-model="dataTable.stato_occorrenza"
                    placeholder="Occurrence status"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="note" class="col-sm-2 col-form-label create-label"
                  >Note</label
                >
                <div class="col-sm-10">
                  <ckeditor
                    :editor="editor"
                    :value="value"
                    :config="config"
                    :tagName="tagName"
                    :disabled="disabled"
                    @input="(event) => $emit('input', event)"
                    v-model="dataTable.note"
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
let ClassicEditor
let CKEditor
if (process.client) {
  ClassicEditor = require('@ckeditor/ckeditor5-build-classic')
  CKEditor = require('@ckeditor/ckeditor5-vue2')
} else {
  CKEditor = { component: { template: '<div></div>' } }
}
export default {
  components: {
    Nav,
    ckeditor: CKEditor.component,
  },
  props: {
    value: {
      type: String,
      required: false,
    },
    tagName: {
      type: String,
      required: false,
      default: 'div',
    },
    disabled: {
      type: Boolean,
      required: false,
    },
    uploadUrl: {
      type: String,
      required: false,
    },
    config: {
      type: Object,
      required: false,
      default: function () {},
    },
  },
  data() {
    return {
      show: false,
      editor: ClassicEditor,
      dataCreated: '',
      variant: 'info',
      creationDate: '',
      updateDate: '',
      form: {
        segnalazione: null,
        soluzione: null,
        titolo: null,
        descrizione: '',
        note: '',
        commessa_macchina: null,
        versione_sw_1: null,
        versione_sw_1: null,
        data_occorrenza: '',
        rif_ticket: null,
        stato_occorrenza: null,
      },
    }
  },
  methods: {
    onSubmit() {
      this.show = true
      if (
        this.dataTable.segnalazione === null ||
        this.dataTable.segnalazione === ''
      ) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Id signal!'
        this.toggleToaster()
        return
      }
      if (this.dataTable.titolo === null || this.dataTable.titolo === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Title!'
        this.toggleToaster()
        return
      }
      if (this.dataTable.data_occorrenza === null) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Occurrence date!'
        this.toggleToaster()
        return
      }

      if (
        this.dataTable.stato_occorrenza === null ||
        this.dataTable.stato_occorrenza === ''
      ) {
        this.dataTable.stato_occorrenza = 0
      }

      let payload = {
        segnalazione: this.dataTable.segnalazione,
        soluzione: this.dataTable.soluzione,
        titolo: this.dataTable.titolo,
        descrizione: this.dataTable.descrizione,
        commessa_macchina: this.dataTable.commessa_macchina,
        versione_sw_1: this.dataTable.versione_sw_1,
        versione_sw_2: this.dataTable.versione_sw_2,
        data_occorrenza: this.dataTable.data_occorrenza,
        stato_occorrenza: this.dataTable.stato_occorrenza,
        rif_ticket: this.dataTable.rif_ticket,
        note: this.dataTable.note,
      }

      this.$axios
        .post(`/api/occorrenze/update/${this.$route.params.id}`, payload, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          console.log(this.dataTable.soluzioni_id)
          if (this.dataTable.soluzioni_id.length !== 0) {
            this.connectNewSolutionID()
          } else {
            this.dataCreated = 'Occurrence Updated Succesfully'
            this.toggleToaster()
            setTimeout(() => {
              this.$router.push('/occurrences')
            }, 3000)
          }

          // this.dataCreated = 'Occurrence Updated Succesfully'
          // this.toggleToaster()

          // setTimeout(() => {
          //   this.$router.push('/occurrences')
          // }, 3000)
        })
        .catch((error) => {
          this.show = false
          this.variant = 'danger'
          this.dataCreated = 'Something went wrong!'
          this.toggleToaster()
        })
    },
    connectNewSolutionID() {
      const value = this.dataTable.soluzioni_id[0]
      const id = parseInt(this.$route.params.id)
      const payload = {
        occorrenze_id: id,
      }
      this.$axios
        .post(`/api/soluzioni/connect/${value}`, payload, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Occurrence Updated Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/occurrences')
          }, 3000)
        })
        .catch((error) => {
          this.show = false
          this.variant = 'danger'
          this.dataCreated = 'Something went wrong!'
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
  async asyncData({ store, $axios, params }) {
    let response = await $axios.get(
      `/api/occorrenze/retrive_occorrenze/${params.id}`
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
