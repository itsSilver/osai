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
          <b-form @submit.prevent="onSubmit" class="create-solution-form">
            <div class="form-group row">
              <label
                for="id-segnalazione"
                class="col-sm-2 col-form-label create-label"
                >Id signal</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="id-segnalazione"
                  v-model="form.segnalazione"
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
                  type="text"
                  class="form-control input-create"
                  id="id-soluzione"
                  v-model="form.soluzione"
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
                  v-model="form.titolo"
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
                  v-model="form.rif_ticket"
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
                  v-model="form.descrizione"
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="machine" class="col-sm-2 col-form-label create-label"
                >Machine order</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="machine"
                  v-model="form.commessa_macchina"
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
                  v-model="form.versione_sw_1"
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
                  v-model="form.versione_sw_2"
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
                  v-model="form.data_occorrenza"
                  class="mb-2 date-choose"
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
                  type="text"
                  class="form-control input-create"
                  id="status-occorrenza"
                  v-model="form.stato_occorrenza"
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
                  v-model="form.note"
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
        this.form.segnalazione === null ||
        this.form.soluzione === null ||
        this.form.titolo === null ||
        this.form.commessa_macchina === null ||
        this.form.versione_sw_1 === null ||
        this.form.versione_sw_2 === null ||
        this.form.rif_ticket === null ||
        this.form.data_occorrenza === '' ||
        this.form.descrizione === '' ||
        this.form.note === '' ||
        this.form.stato_occorrenza === null
      ) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please make sure all the fields are filled!'
        this.toggleToaster()
        return
      }

      this.$axios
        .post(`/api/occorrenze/create`, this.form, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Occurrence created Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/occurrences')
          }, 2000)
        })
        .catch((error) => {
          this.show = false
          this.dataCreated = 'Something went wrong!'
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
