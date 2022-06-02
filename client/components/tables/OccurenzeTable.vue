<template>
  <b-overlay :show="show" rounded="sm">
    <b-table-simple
      class="table table-bordred table-striped text-center table-desktop"
    >
      <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th v-if="statusIdoccurrence === '1'"
          ><i
            class="fa-solid fa-arrow-down-short-wide"
            style="cursor: pointer"
            @click="orderAscDesc()"
          ></i
          >Id occurrence
        </b-th>
        <b-th v-if="statusIdsignal === '1'">Id signal </b-th>
        <b-th v-if="statusIdsolution === '1'">Id solution </b-th>
        <b-th v-if="statusTitle === '1'">Title </b-th>
        <b-th v-if="statusMachine === '1'">Machine order </b-th>
        <b-th v-if="statusTicket === '1'">Ticket </b-th>
        <b-th v-if="statusVersion1 === '1'">Version sw 1 </b-th>
        <b-th v-if="statusVersion2 === '1'">Version sw 2 </b-th>
        <b-th v-if="statusOccurrenceDate === '1'">Occurrence date </b-th>
        <b-th v-if="statusOccurrenceStatus === '1'">Occurrence status </b-th>
        <b-th v-if="statusCreationDate === '1'">Creation date </b-th>
        <b-th v-if="statusUpdateDate === '1'">Update date </b-th>
      </b-thead>
      <b-tbody v-if="dataTable">
        <b-tr v-for="data in dataTable" :key="data.id">
          <b-td>
            <input
              type="checkbox"
              class="checkthis"
              v-model="selectedId"
              :id="data.id"
              :value="data.id"
              @change="changeValue"
            />
          </b-td>
          <b-td v-if="statusIdoccurrence === '1'">{{ data.id }}</b-td>
          <b-td v-if="statusIdsignal === '1'">{{ data.segnalazione }}</b-td>
          <b-td v-if="statusIdsolution === '1'">{{
            data.soluzioni_id[0]
          }}</b-td>
          <b-td v-if="statusTitle === '1'">{{ data.titolo }}</b-td>
          <b-td v-if="statusMachine === '1'">{{ data.commessa_macchina }}</b-td>
          <b-td v-if="statusTicket === '1'">{{ data.rif_ticket }}</b-td>
          <b-td v-if="statusVersion1 === '1'">{{ data.versione_sw_1 }}</b-td>
          <b-td v-if="statusVersion2 === '1'">{{ data.versione_sw_2 }}</b-td>
          <b-td v-if="statusOccurrenceDate === '1'">{{
            data.data_occorrenza
          }}</b-td>
          <b-td v-if="statusOccurrenceStatus === '1'">{{
            data.stato_occorrenza
          }}</b-td>
          <b-td v-if="statusCreationDate === '1'">{{
            formatDate(data.created_at)
          }}</b-td>
          <b-td v-if="statusUpdateDate === '1'">{{
            formatDate(data.updated_at)
          }}</b-td>
        </b-tr>
      </b-tbody>
    </b-table-simple>
    <b-table-simple
      class="table table-bordred table-striped text-center table-respo"
    >
      <!-- <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th
          >Id solution</b-th
        >

        <b-th>Rank</b-th>
        <b-th>Settore riferimento</b-th>
        <b-th>Id stato soluzione</b-th>
        <b-th>Creation date</b-th>
        <b-th>Update date</b-th>
      </b-thead> -->
      <b-tbody v-if="dataTable">
        <b-tr class="respo-tr" v-for="data in dataTable" :key="data.id">
          <div class="respo-after-tr">
            <b-td class="td-respo-title"></b-td>
            <b-td class="td-respo-data">
              <input
                type="checkbox"
                class="checkthis"
                v-model="selectedId"
                :id="data.id"
                :value="data.id"
                @change="changeValue"
            /></b-td>
          </div>
          <div class="respo-after-tr" v-if="statusIdoccurrence === '1'">
            <b-td class="td-respo-title">Id occurrence</b-td>
            <b-td class="td-respo-data">{{ data.id }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusIdsignal === '1'">
            <b-td class="td-respo-title">Id signal</b-td>
            <b-td class="td-respo-data">{{ data.segnalazione }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusIdsolution === '1'">
            <b-td class="td-respo-title">Id solution</b-td>
            <b-td class="td-respo-data">{{ data.soluzioni_id[0] }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusTitle === '1'">
            <b-td class="td-respo-title">Title</b-td>
            <b-td class="td-respo-data">{{ data.titolo }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusMachine === '1'">
            <b-td class="td-respo-title">Machine order</b-td>
            <b-td class="td-respo-data">{{ data.commessa_macchina }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusTicket === '1'">
            <b-td class="td-respo-title">Machine order</b-td>
            <b-td class="td-respo-data">{{ data.rif_ticket }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusVersion1 === '1'">
            <b-td class="td-respo-title">Version sw 1</b-td>
            <b-td class="td-respo-data">{{ data.versione_sw_1 }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusVersion2 === '1'">
            <b-td class="td-respo-title">Version sw 2</b-td>
            <b-td class="td-respo-data">{{ data.versione_sw_2 }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusOccurrenceDate === '1'">
            <b-td class="td-respo-title">Occurrence date</b-td>
            <b-td class="td-respo-data">{{ data.data_occorrenza }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusOccurrenceStatus === '1'">
            <b-td class="td-respo-title">Occurrence status</b-td>
            <b-td class="td-respo-data">{{ data.stato_occorrenza }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusCreationDate === '1'">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">{{ formatDate(data.created_at) }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusUpdateDate === '1'">
            <b-td class="td-respo-title">Update date</b-td>
            <b-td class="td-respo-data">{{ formatDate(data.updated_at) }}</b-td>
          </div>
        </b-tr>
        <b-tr>
          <b-td style="width: 1000px !important">
            <!-- <b-td style="float: left">test</b-td>
            <b-td style="float: right">test</b-td> -->
          </b-td>
        </b-tr>
      </b-tbody>
    </b-table-simple>
    <div class="no-data" v-if="dataTable.length === 0">
      <NoOccorrenzeItems v-if="showNoItem" />
    </div>
  </b-overlay>
</template>
<script>
import NoOccorrenzeItems from '~/components/nodata/NoOccorrenzeItems'
import { format, parseISO } from 'date-fns'
export default {
  components: {
    NoOccorrenzeItems,
  },
  data() {
    return {
      showNoItem: true,
      show: false,
      selectedId: [],
    }
  },
  methods: {
    formatDate(val) {
      if (val) {
        return format(parseISO(val), 'dd-MM-yyyy')
      }
    },
    changeValue() {
      this.$emit('get-new-delete-id', this.selectedId)
      this.selectedId = []
    },
    orderAscDesc() {
      this.$emit('order-asc-desc')
    },
  },
  props: [
    'dataTable',
    'statusIdoccurrence',
    'statusIdsignal',
    'statusTitle',
    'statusIdsolution',
    'statusMachine',
    'statusTicket',
    'statusVersion1',
    'statusVersion2',
    'statusOccurrenceDate',
    'statusOccurrenceStatus',
    'statusCreationDate',
    'statusUpdateDate',
  ],
}
</script>
<style scoped>
.table > :not(caption) > * > * {
  box-shadow: unset !important;
}
td {
  border: unset !important;
}
</style>