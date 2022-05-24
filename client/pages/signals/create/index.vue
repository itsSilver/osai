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
          <form class="create-solution-form">
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
              <label for="immag1" class="col-sm-2 col-form-label create-label"
                >Image 1</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="immag1"
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="immag2" class="col-sm-2 col-form-label create-label"
                >Image 2</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="immag2"
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="immag3" class="col-sm-2 col-form-label create-label"
                >Image 3</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="immag3"
                />
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
                  placeholder="Reference sector"
                />
              </div>
            </div>
            <div class="form-group row">
              <div class="col-sm-10">
                <b-button class="mx-2 button-format">
                  <i class="fas fa-download pr-2"></i>
                  Save
                </b-button>
              </div>
            </div>
          </form>
          <!-- End here -->
        </div>
      </div>
    </client-only>
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
      editor: ClassicEditor,
      description: '',
      note: '',
      form: {
        titolo: null,
        descrizione: '',
        id_allarme: null,
        descrizione_allarme: null,
        famiglia_macchina: null,
        sottofamiglia_macchina: null,
        id_stato_segnalazione: null,
      },
    }
  },
}
</script>
<style scoped>
/* .form-group {
  width: 100% !important;
} */
</style>
