<template>
  <b-overlay :show="show" rounded="sm">
    <b-table-simple
      class="table table-bordred table-striped text-center table-desktop"
    >
      <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th v-if="statusIdsignal === '1'"
          ><i
            class="fa-solid fa-arrow-down-short-wide"
            style="cursor: pointer"
            @click="orderAscDesc()"
          ></i
          >Id Signal</b-th
        >

        <b-th v-if="statusTicket === '1'">Ticket</b-th>
        <b-th v-if="statusAlarm === '1'">Id Alarm</b-th>
        <b-th v-if="statusSector === '1'">Reference sector</b-th>
        <b-th v-if="statusMachine === '1'">Family machine</b-th>
        <b-th v-if="statusUnderMachine === '1'">Under Family machine</b-th>
        <b-th v-if="statusCreationDate === '1'">Creation date</b-th>
        <b-th v-if="statusUpdateDate === '1'">Update date</b-th>
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
          <b-td v-if="statusIdsignal === '1'">{{ data.id }}</b-td>
          <b-td v-if="statusTicket === '1'">{{ data.rif_ticket }}</b-td>
          <b-td v-if="statusAlarm === '1'">{{ data.id_allarme }}</b-td>
          <b-td v-if="statusSector === '1'"></b-td>
          <b-td v-if="statusMachine === '1'">{{ data.famiglia_macchina }}</b-td>
          <b-td v-if="statusUnderMachine === '1'">{{
            data.sottofamiglia_macchina
          }}</b-td>
          <b-td v-if="statusCreationDate === '1'">{{ data.created_at }}</b-td>
          <b-td v-if="statusUpdateDate === '1'">{{ data.updated_at }}</b-td>
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
          ><i class="fa-solid fa-arrow-down-short-wide"></i>Id Signal</b-th
        >

        <b-th>Ticket</b-th>
        <b-th>Reference sector</b-th>
        <b-th>Id status solution</b-th>
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
          <div class="respo-after-tr" v-if="statusIdsignal === '1'">
            <b-td class="td-respo-title">Id Signal</b-td>
            <b-td class="td-respo-data">{{ data.id }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusTicket === '1'">
            <b-td class="td-respo-title">Ticket</b-td>
            <b-td class="td-respo-data">{{ data.rif_ticket }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusAlarm === '1'">
            <b-td class="td-respo-title">Id Alarm</b-td>
            <b-td class="td-respo-data">{{ data.id_allarme }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusSector === '1'">
            <b-td class="td-respo-title">Reference sector</b-td>
            <b-td class="td-respo-data"></b-td>
          </div>
          <div class="respo-after-tr" v-if="statusMachine === '1'">
            <b-td class="td-respo-title">Family machine</b-td>
            <b-td class="td-respo-data">{{ data.famiglia_macchina }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusUnderMachine === '1'">
            <b-td class="td-respo-title">Under Family machine</b-td>
            <b-td class="td-respo-data">{{ data.sottofamiglia_macchina }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusCreationDate === '1'">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">{{ data.created_at }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusUpdateDate === '1'">
            <b-td class="td-respo-title">Update date</b-td>
            <b-td class="td-respo-data">{{ data.updated_at }}</b-td>
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
      <NoSignalItems v-if="showNoItem" />
    </div>
  </b-overlay>
</template>
<script>
import NoSignalItems from '~/components/nodata/NoSignalItems'
export default {
  components: {
    NoSignalItems,
  },
  data() {
    return {
      showNoItem: true,
      show: false,
      selectedId: [],
    }
  },
  methods: {
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
    'statusTicket',
    'statusIdsignal',
    'statusAlarm',
    'statusMachine',
    'statusSector',
    'statusUnderMachine',
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