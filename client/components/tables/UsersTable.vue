<template>
  <b-overlay :show="show" rounded="sm">
    <b-table-simple
      class="table table-bordred table-striped text-center table-desktop"
    >
      <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th v-if="statusUserId === '1'">Id User</b-th>
        <b-th v-if="statusName === '1'">Name</b-th>
        <b-th v-if="statusEmail === '1'">Email</b-th>
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
          <b-td v-if="statusUserId === '1'">{{ data.id }}</b-td>
          <b-td v-if="statusName === '1'">{{ data.name }}</b-td>
          <b-td v-if="statusEmail === '1'">{{ data.email }}</b-td>
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
          ><i class="fa-solid fa-arrow-down-short-wide"></i>Id Solution</b-th
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
          <div class="respo-after-tr" v-if="statusUserId === '1'">
            <b-td class="td-respo-title" v-if="statusUserId === '1'"
              >Id User</b-td
            >
            <b-td class="td-respo-data">{{ data.id }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusName === '1'">
            <b-td class="td-respo-title">Name</b-td>
            <b-td class="td-respo-data">{{ data.name }}</b-td>
          </div>
          <div class="respo-after-tr" v-if="statusEmail === '1'">
            <b-td class="td-respo-title">Email</b-td>
            <b-td class="td-respo-data">{{ data.email }}</b-td>
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
          <b-td style="width: 1000px !important"> </b-td>
        </b-tr>
      </b-tbody>
    </b-table-simple>
    <div class="no-data" v-if="dataTable.length === 0">
      <NoUserItem v-if="showNoItem" />
    </div>
  </b-overlay>
</template>
<script>
import NoUserItem from '~/components/nodata/NoUserItem'
export default {
  components: {
    NoUserItem,
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
  },
  props: [
    'dataTable',
    'statusUserId',
    'statusName',
    'statusEmail',
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