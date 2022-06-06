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
                  <VueEditor v-model="form.descrizione" />
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
                  <VueEditor v-model="form.descrizione_allarme" />
                </div>
              </div>
              <!-- <div class="form-group row">
                <label for="immag1" class="col-sm-2 col-form-label create-label"
                  >Image 1</label
                >
                <div class="col-sm-10">
                  <input type="file" @change="fileChange" />
                </div>
              </div> -->
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
                  <VueEditor v-model="form.note" />
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
                  >
                  </b-form-select>
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
export default {
  components: {
    Nav,
    FindOccurrence,
  },
  data() {
    return {
      show: false,
      file1: null,
      file2: null,
      file3: null,
      showFindOccurrence: false,
      dataCreated: '',
      variant: 'info',
      showTitleSignalError: null,
      form: {
        titolo: '',
        descrizione: '',
        note: '',
        descrizione_allarme: '',
        id_allarme: '',
        famiglia_macchina: null,
        sottofamiglia_macchina: null,
        rif_ticket: '',
        immagine_1: null,
      },
      tempimmagine_1: null,
      tempimmagine_2: null,
      tempimmagine_3: null,
      famiglia_macchina_options: [
        { value: null, text: 'Select' },
        { value: 'std_npm:Neo Place Modula', text: 'std_npm:Neo Place Modula' },
        { value: 'std_nmt:Neo Mark Twin', text: 'std_nmt:Neo Mark Twin' },
        { value: 'std_npl:Neo Place', text: 'std_npl:Neo Place' },
        { value: 'std_ncx:Neo Cut', text: 'std_ncx:Neo Cut' },
        { value: 'std_fnw:FineWeld', text: 'std_fnw:FineWeld' },
        { value: 'std_fnx:FineCut', text: 'std_fnx:FineCut' },
        { value: 'std_dm1:Dm1', text: 'std_dm1:Dm1' },
        { value: 'std_dm2:Dm2', text: 'std_dm2:Dm2' },
        { value: 'std_shp:Neo Cut Shape', text: 'std_shp:Neo Cut Shape' },
        { value: 'std_nme:Neo Mark Easy', text: 'std_nme:Neo Mark Easy' },
        {
          value: 'std_npt:Neo place Sold Top',
          text: 'std_npt:Neo place Sold Top',
        },
        { value: 'std_nth:Neo Thermostep', text: 'std_nth:Neo Thermostep' },
        {
          value: 'std_nrm:Neo Router Modula',
          text: 'std_nrm:Neo Router Modula',
        },
        {
          value: 'std_nhm:Neo Handler Modula',
          text: 'std_nhm:Neo Handler Modula',
        },
        { value: 'std_alt:Altro Standard', text: 'std_alt:Altro Standard' },
        {
          value: 'spl_galt:Sistema Generico Speciale',
          text: 'spl_galt:Sistema Generico Speciale',
        },
        { value: 'spl_nef:Neo Feeder', text: 'spl_nef:Neo Feeder' },
        { value: 'spl_nol:Neo Inline', text: 'spl_nol:Neo Inline' },
        { value: 'spl_nin:Neo Inwork', text: 'spl_nin:Neo Inwork' },
        {
          value: 'spl_nlu:Neo Loader/Unloader',
          text: 'spl_nlu:Neo Loader/Unloader',
        },
        { value: 'spl_nfo:Neo Flip Over', text: 'spl_nfo:Neo Flip Over' },
        { value: 'spl_nll:Neo Line Lifter', text: 'spl_nll:Neo Line Lifter' },
        { value: 'spl_ntu:Neo Turn', text: 'spl_ntu:Neo Turn' },
        { value: 'spl_alt:Altro Speciale', text: 'spl_alt:Altro Speciale' },
        { value: 'R_LASER:LASER', text: 'R_LASER:LASER' },
        { value: 'R_SC:Semiconduttori', text: 'R_SC:Semiconduttori' },
        { value: 'R_STD: Standard', text: 'R_STD: Standard' },
        { value: 'R_Linea: Linee/Speciale', text: 'R_Linea: Linee/Speciale' },
        {
          value: 'R_altro: Non Identificabile',
          text: 'R_altro: Non Identificabile',
        },
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
      if (this.form.id_allarme === null || this.form.id_allarme === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Alarm Id!'
        this.toggleToaster()
        return
      }

      const data = new FormData()
      data.append('titolo', this.form.titolo)
      data.append('descrizione', this.form.descrizione)
      data.append('immagine_1', this.tempimmagine_1)
      data.append('immagine_2', this.tempimmagine_2)
      data.append('immagine_3', this.tempimmagine_3)
      data.append('settore_riferimento', 'test test')
      data.append('note', this.form.note)
      data.append('rif_ticket', this.form.rif_ticket)
      data.append('descrizione_allarme', this.form.descrizione_allarme)
      data.append('id_allarme', this.form.id_allarme)
      data.append('famiglia_macchina', this.form.famiglia_macchina)
      data.append('sottofamiglia_macchina', this.form.sottofamiglia_macchina)

      this.$axios
        .post(`/api/segnalazioni/create`, data, {
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
          this.dataCreated = error.response.data.message[0]
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
