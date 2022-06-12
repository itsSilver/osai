<template>
  <div class="wrapper d-flex align-items-stretch">
    <client-only>
      <Nav />
      <div id="content" class="p-4 p-md-5 pt-5">
        <div class="wrapped-content">
          <div
            class="nav-actions d-flex justify-content-between align-items-center mb-2 navtop"
          >
            <!-- First Nav -->
            <div class="d-flex gap-4">
              <ul
                class="d-flex justify-content-around align-content-center m-0 p-0"
                style="list-style: none"
              >
                <li class="nav-actions-color mx-2 px-14-format">
                  <i class="fas fa-eye pr-2 fas-main-color"></i>
                  View Signal
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
            <b-form class="create-solution-form">
              <div class="form-group row">
                <label for="tittle" class="col-sm-2 col-form-label create-label"
                  >Title Signal</label
                >
                <div class="col-sm-10">
                  <input
                    disabled
                    type="text"
                    class="form-control input-create"
                    id="tittle"
                    v-model="dataTable.titolo"
                  />
                </div>
              </div>
              <div class="form-group row">
                <label for="ticket" class="col-sm-2 col-form-label create-label"
                  >Ticket</label
                >
                <div class="col-sm-10">
                  <input
                    disabled
                    type="text"
                    class="form-control input-create"
                    id="ticket"
                    v-model="dataTable.rif_ticket"
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
                  <VueEditor :disabled="true" v-model="dataTable.descrizione" />
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
                    disabled
                    type="number"
                    class="form-control input-create"
                    id="id_alarme"
                    v-model="dataTable.id_allarme"
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
                    :disabled="true"
                    v-model="dataTable.descrizione_allarme"
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
                </div>
              </div>
              <div class="form-group row">
                <label for="note" class="col-sm-2 col-form-label create-label"
                  >Note</label
                >
                <div class="col-sm-10">
                  <VueEditor :disabled="true" v-model="dataTable.note" />
                </div>
              </div>
              <div class="form-group row">
                <label class="col-sm-2 col-form-label create-label"
                  >Family machine</label
                >
                <div class="col-sm-10">
                  <b-form-select
                    disabled
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
                    disabled
                    v-model="dataTable.sottofamiglia_macchina"
                    :options="sottofamiglia_macchina_options"
                  >
                  </b-form-select>
                </div>
              </div>
              <div class="form-group row">
                <div class="col-sm-10">
                  <b-button
                    class="mx-2 button-format"
                    @click="$router.push(`/signals/update/${$route.params.id}`)"
                  >
                    <i class="fas fa-edit pr-2"></i>
                    Edit
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
    watchImage(val) {
      this.imageValue = 'http://api.apexroyale.com' + val
      this.showImage = true
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
