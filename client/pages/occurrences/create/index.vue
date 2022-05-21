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
          <form class="create-solution-form">
            <div class="form-group row">
              <label
                for="id-occorrenza"
                class="col-sm-2 col-form-label create-label"
                >Id occurrence</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="id-occorrenza"
                  placeholder="Id occurrence"
                />
              </div>
            </div>
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
                  placeholder="Title"
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
                <b-form-textarea
                  class="input-create"
                  id="textarea-small"
                  size="lg"
                  rows="10"
                  max-rows="11"
                ></b-form-textarea>
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
                <input
                  type="text"
                  class="form-control input-create"
                  id="data-occorrenza"
                  placeholder="Occurrence date"
                />
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
                  placeholder="Occurrence status"
                />
              </div>
            </div>
            <div class="form-group row">
              <label for="note" class="col-sm-2 col-form-label create-label"
                >Note</label
              >
              <div class="col-sm-10">
                <b-form-textarea
                  class="input-create"
                  id="note"
                  size="lg"
                  rows="10"
                  max-rows="11"
                ></b-form-textarea>
              </div>
            </div>
            <div class="form-group row">
              <label class="col-sm-2 col-form-label create-label"
                >Creation Date</label
              >
              <div class="col-sm-10">
                <b-form-datepicker
                  id="example-datepicker"
                  v-model="creationDate"
                  class="mb-2 date-choose"
                ></b-form-datepicker>
              </div>
            </div>
            <div class="form-group row">
              <label class="col-sm-2 col-form-label create-label"
                >Update Date</label
              >
              <div class="col-sm-10">
                <b-form-datepicker
                  id="example-datepicker"
                  v-model="updateDate"
                  class="mb-2 date-choose"
                ></b-form-datepicker>
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
      creationDate: '',
      updateDate: '',
    }
  },
}
</script>
<style scoped>
/* .form-group {
  width: 100% !important;
} */
</style>
