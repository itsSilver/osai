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
                  New Signal
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
                    v-model="form.titolo"
                    placeholder="Title Signal"
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
                    v-model="form.rif_ticket"
                    placeholder="Ticket"
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
                <label
                  for="id_alarme"
                  class="col-sm-2 col-form-label create-label"
                  >Id alarm</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="id_alarme"
                    v-model="form.id_allarme"
                    placeholder="Id alarm"
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
                  <ckeditor
                    :editor="editor"
                    :value="value"
                    :config="config"
                    :tagName="tagName"
                    :disabled="disabled"
                    @input="(event) => $emit('input', event)"
                    v-model="form.descrizione_allarme"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="immag1" class="col-sm-2 col-form-label create-label"
                  >Image 1</label
                >
                <div class="col-sm-10">
                  <input type="file" @change="fileChange" />
                </div>
              </div>
              <!-- <div class="form-group row">
                <label for="immag2" class="col-sm-2 col-form-label create-label"
                  >Image 2</label
                >
                <div class="col-sm-10">
                  <b-form-file
                    v-model="form.file2"
                    :state="Boolean(form.file2)"
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                  ></b-form-file>
                </div>
              </div> -->
              <!-- <div class="form-group row">
                <label for="immag3" class="col-sm-2 col-form-label create-label"
                  >Image 3</label
                >
                <div class="col-sm-10">
                  <b-form-file
                    v-model="form.file3"
                    :state="Boolean(form.file3)"
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                  ></b-form-file>
                </div>
              </div> -->
              <div class="form-group row">
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
                <label class="col-sm-2 col-form-label create-label"
                  >Family machine</label
                >
                <div class="col-sm-10">
                  <b-form-select
                    v-model="form.famiglia_macchina"
                    :options="famiglia_macchina_options"
                  ></b-form-select>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-2 col-form-label create-label"
                  >Under Family machine</label
                >
                <div class="col-sm-10">
                  <b-form-select
                    v-model="form.sottofamiglia_macchina"
                    :options="sottofamiglia_macchina_options"
                  ></b-form-select>
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
      <FindOccurrence v-if="showFindOccurrence" @close="hideModal()" />
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
import FindOccurrence from '~/components/popup/FindOccurrence'
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
    FindOccurrence,
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
      file1: null,
      file2: null,
      file3: null,
      showFindOccurrence: false,
      editor: ClassicEditor,
      dataCreated: '',
      variant: 'info',
      showTitleSignalError: null,
      form: {
        titolo: null,
        descrizione: '',
        note: '',
        descrizione_allarme: '',
        id_allarme: null,
        famiglia_macchina: null,
        sottofamiglia_macchina: null,
        rif_ticket: null,
        immagine_1: null,
        // file2: null,
        // file3: null,
        // id_stato_segnalazione: null,
      },
      tempimmagine_1: null,
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
    }
  },
  methods: {
    fileChange(event) {
      this.form.immagine_1 = event.target.files[0]
      this.tempimmagine_1 = new FormData()
      this.tempimmagine_1.append('image', this.form.immagine_1)
    },
    onSubmit() {
      let payload = {
        titolo: this.form.titolo,
        descrizione: this.form.descrizione,
        id_allarme: this.form.id_allarme,
        immagine_1: this.tempimmagine_1,
        descrizione_allarme: this.form.descrizione_allarme,
        famiglia_macchina: this.form.famiglia_macchina,
        sottofamiglia_macchina: this.form.sottofamiglia_macchina,
        rif_ticket: this.form.rif_ticket,
      }

      console.log(payload)

      this.show = true
      if (
        this.form.titolo === null ||
        this.form.descrizione === '' ||
        this.form.descrizione_allarme === '' ||
        this.form.id_allarme === null ||
        this.form.famiglia_macchina === null ||
        this.form.sottofamiglia_macchina === null ||
        this.form.rif_ticket === null
      ) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please make sure all the fields are filled!'
        this.toggleToaster()
        return
      }
      this.$axios
        .post(`/api/segnalazioni/create`, payload, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'multipart/form-data',
          },
        })
        .then(() => {
          this.dataCreated = 'Signal created Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/signals')
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
