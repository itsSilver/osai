<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container">
        <span @click="cancel()">
          <CloseIcon class="closeicon" />
        </span>
        <!-- <div class="modal-header">
          <slot name="header"> Attention </slot>
        </div> -->
        <div class="">
          <b-overlay :show="show" rounded="sm">
            <o-table
              class="occurrence-table-seg"
              :data="dataTable"
              :bordered="true"
              :striped="true"
              mobile-cards
              paginated
              :per-page="perPage"
              :current-page.sync="currentPage"
              v-if="dataTable.length > 0"
              :selected.sync="selected"
              :checked-rows.sync="checkedRows"
              :hoverable="isHoverable"
            >
              <o-table-column
                class="test"
                field="id"
                label="ID"
                width="40"
                numeric
                v-slot="props"
              >
                {{ props.row.id }}
              </o-table-column>

              <o-table-column
                field="titolo"
                label="Title"
                v-slot="props"
                position="centered"
                searchable
              >
                {{ props.row.titolo }}
              </o-table-column>
              <o-table-column
                field="rank"
                label="Rank"
                v-slot="props"
                position="centered"
                searchable
                sortable
              >
                {{ props.row.rank }}
              </o-table-column>

              <o-table-column
                field="settore_riferimento"
                label="Reference sector"
                v-slot="props"
                position="centered"
                searchable
                sortable
              >
                {{ props.row.settore_riferimento }}
              </o-table-column>
              <o-table-column
                label="Add Solution"
                v-slot="props"
                position="centered"
              >
                <b-button class="mx-1 plus-btn" @click="pushId(props.row)">
                  <i class="mdi mdi-plus"></i>
                </b-button>
              </o-table-column>
            </o-table>
            <div style="text-align: center !important" v-else>
              <NoDataItems v-if="dataTable.length === 0" />
            </div>
          </b-overlay>
          <div class="modal-footer mt-8">
            <slot name="footer"> </slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import CloseIcon from '~/components/icons/close'
import NoDataItems from '~/components/nodata/NoDataItems'
import { format, parseISO } from 'date-fns'
export default {
  components: { CloseIcon, NoDataItems },
  data() {
    return {
      showNoItem: false,
      show: false,
      variant: 'info',
      dataTable: [],
      checkedRows: [],
      currentPage: 1,
      perPage: 10,
      selected: {},
      isHoverable: true,
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    pushId(val) {
      this.$emit('data-add-solution', val)
      this.cancel()
    },
    redirectCreate() {
      this.$router.push({
        path: '/signals/create',
      })
    },
    formatDate(val) {
      if (val) {
        return format(parseISO(val), 'yyyy-MM-dd')
      }
    },
    getData() {
      this.show = true
      this.$axios
        .get(`/api/soluzioni/retrive_soluzioni`, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          this.dataTable = response.data
          this.show = false
        })
        .catch((error) => {
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    cancel() {
      this.$emit('close')
    },
  },
  props: ['tableValue'],
}
</script>
<style scoped>
.plus-btn {
  background-color: unset !important;
  color: #28a745 !important;
  border: unset;
}

.modal-mask {
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  max-width: 1200px;
  width: 100%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.anulla {
  width: 140px;
  color: #fff;
  background-color: #c2c2c2;
  border-radius: 8px;
  text-transform: uppercase;
  border: none;
  padding: 0.375rem 0.75rem;
  font-size: 0.9rem;
  line-height: 1.6;
  border-radius: 0.25rem;
}

.salva {
  width: 140px;
  color: #fff;
  background-color: #ce4600;
  border-radius: 8px;
  text-transform: uppercase;
  border: none;
  padding: 0.375rem 0.75rem;
  font-size: 0.9rem;
  line-height: 1.6;
  border-radius: 0.25rem;
}

.modal-body-custom {
  padding: 0 1rem;
  background-color: #f5f6fa;
  border: 1px solid #ce4600;
  border-radius: 0px;
  padding-top: 0.75rem;
}

.modal-footer {
  padding-left: 0;
  padding-right: 0;
  padding-top: 50px !important;
  border-top: unset !important;
}

.modal-header {
  text-align: center;
  font-size: 28px;
  line-height: 32px;
  font-weight: bold;
  background-color: #181824;
  color: #fff;
  margin-bottom: 0.75rem;
  border-radius: 0;
  border: none;
  display: block;
  text-transform: uppercase;
}

.modal-body-custom label {
  display: block;
}

.error {
  color: red;
  font-weight: 500;
  font-size: 14px;
}

.forma {
  width: 50%;
}

.forma input {
  width: 100%;
  border-radius: 4px;
  height: 35px;
}

@media (max-width: 400px) {
  .anulla {
    width: 50%;
    max-width: 100px;
  }

  .salva {
    width: 50%;
    max-width: 100px;
  }

  .modal-header {
    font-size: 22px;
    line-height: 28px;
  }
}
</style>