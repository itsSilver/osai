<template>
  <b-overlay :show="show" rounded="sm">
    <b-table-simple
      class="table table-bordred table-striped text-center table-desktop"
    >
      <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th>Id occurrence </b-th>
        <b-th>Id signal </b-th>
        <b-th>Id soluzione </b-th>
        <b-th>Title </b-th>
        <b-th>Machine order </b-th>
        <b-th>Version sw 1 </b-th>
        <b-th>Version sw 2 </b-th>
        <b-th>Occurrence date </b-th>
        <b-th>Occurrence status </b-th>
        <b-th>Creation date </b-th>
        <b-th>Update date </b-th>
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
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
          <b-td>{{ data.id }}</b-td>
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
          >Id soluzione</b-th
        >

        <b-th>Rank</b-th>
        <b-th>Settore riferimento</b-th>
        <b-th>Id stato soluzione</b-th>
        <b-th>Creation date</b-th>
        <b-th>Update date</b-th>
      </b-thead> -->
      <b-tbody v-if="!showNoItem">
        <b-tr class="respo-tr">
          <div class="respo-after-tr">
            <b-td class="td-respo-title"></b-td>
            <b-td class="td-respo-data">
              <input type="checkbox" class="checkthis" id="checkall"
            /></b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id occurrence</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id signal</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id soluzione</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Title</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Machine order</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Version sw 1</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Version sw 2</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Occurrence date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Occurrence status</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Update date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
        </b-tr>
        <b-tr class="respo-tr">
          <div class="respo-after-tr">
            <b-td class="td-respo-title"></b-td>
            <b-td class="td-respo-data">
              <input type="checkbox" class="checkthis" id="checkall"
            /></b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id occurrence</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id signal</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id soluzione</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Title</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Machine order</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Version sw 1</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Version sw 2</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Occurrence date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Occurrence status</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Update date</b-td>
            <b-td class="td-respo-data">test</b-td>
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
    changeValue() {
      this.$emit('get-new-delete-id', this.selectedId)
      this.selectedId = []
    },
  },
  props: ['dataTable'],
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