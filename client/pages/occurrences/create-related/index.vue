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
                  >Alarm ID</label
                >
                <div class="col-sm-10">
                  <input
                    type="number"
                    class="form-control input-create"
                    id="id-segnalazione"
                    v-model="alarmId"
                    placeholder="Alarm ID"
                    readonly
                    @click="showTableSignals()"
                    :disabled="alarmId"
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
                  <VueEditor
                    v-model="form.descrizione"
                    placeholder="Please enter Description"
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
                    today-button
                    reset-button
                    close-button
                    selected-variant="primary"
                    today-variant="primary"
                    hide-header
                    label-close-button="Close"
                    label-today-button="Today"
                    label-reset-button="Reset"
                  >
                  </b-form-datepicker>
                </div>
              </div>
              <div class="form-group row">
                <label
                  for="status-occorrenza"
                  class="col-sm-2 col-form-label create-label"
                  >Occurrence status</label
                >
                <div class="col-sm-10">
                  <b-form-select
                    v-model="form.stato_occorrenza"
                    :options="stato_occorrenza_macchina_options"
                  >
                  </b-form-select>
                </div>
              </div>
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
                <label
                  for="id-soluzione"
                  class="col-sm-2 col-form-label create-label"
                  >Solution
                </label>
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    v-model="solutionTitle"
                    placeholder="Select an solution"
                    readonly
                    @click="showTableSolutions()"
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
    <SeeSignals
      v-if="showModalSignals"
      @data-add-signal="dataAddSignal"
      @close="hideModal()"
    />
    <SeeSolutions
      v-if="showModalSolutions"
      @data-add-solution="dataAddSolution"
      @close="hideModal()"
    />
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
import SeeSignals from '~/components/popup/SeeSignals'
import SeeSolutions from '~/components/popup/SeeSolutions'
export default {
  components: {
    Nav,
    SeeSignals,
    SeeSolutions,
  },
  data() {
    return {
      stato_occorrenza_macchina_options: [
        { value: null, text: 'Select' },
        { value: 1, text: 'Open' },
        { value: 0, text: 'Close' },
      ],
      show: false,
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
        commessa_macchina: '',
        versione_sw_1: '',
        versione_sw_2: '',
        data_occorrenza: null,
        rif_ticket: '',
        stato_occorrenza: null,
      },
      showModalSignals: false,
      showModalSolutions: false,
      solutionTitle: null,
      alarmId: null,
    }
  },
  mounted() {
    if (this.$route.query.id_occurrence) {
      this.duplicateId = this.$route.query.id_occurrence
      this.getOcurrenceDuplicate()
    }
    this.alarmId = this.$route.query.id_alarm
  },
  methods: {
    dataAddSignal(val) {
      this.form.segnalazione = val
    },
    dataAddSolution(val) {
      this.solutionTitle = val.titolo
      this.form.soluzione = val.id
    },
    showTableSignals() {
      this.showModalSignals = true
    },
    showTableSolutions() {
      this.showModalSolutions = true
    },
    onSubmit() {
      this.show = true
      if (this.form.segnalazione === null || this.form.segnalazione === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Id signal!'
        this.toggleToaster()
        return
      }
      if (this.form.titolo === null || this.form.titolo === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Title!'
        this.toggleToaster()
        return
      }
      if (this.form.data_occorrenza === null) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Occurrence date!'
        this.toggleToaster()
        return
      }

      if (
        this.form.stato_occorrenza === null ||
        this.form.stato_occorrenza === ''
      ) {
        this.form.stato_occorrenza = 0
      }
      if (this.form.soluzione === '') {
        this.form.soluzione = null
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
          this.show = false
          setTimeout(() => {
            this.$router.push('/occurrences')
          }, 2000)
        })
        .catch((error) => {
          this.show = false
          this.dataCreated = error.response.data.message
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    getOcurrenceDuplicate() {
      this.show = true
      this.$axios
        .get(`/api/occorrenze/retrive_occorrenze/${this.duplicateId}`, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.form = response.data[0]
          this.show = false
        })
        .catch((error) => {
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
      this.showModalSignals = false
      this.showModalSolutions = false
    },
  },
}
</script>
<style scoped>
/* .form-group {
  width: 100% !important;
} */
</style>
