<template>
  <b-overlay :show="show" rounded="sm">
    <b-table-simple
      class="table table-bordred table-striped text-center table-desktop"
    >
      <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th
          ><i class="fa-solid fa-arrow-down-short-wide"></i>Id Solution</b-th
        >
        <b-th>Title</b-th>
        <b-th>Rank</b-th>
        <b-th>Reference sector</b-th>
        <b-th>Id Status Solution</b-th>
        <b-th>Creation date</b-th>
        <b-th>Update date</b-th>
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
          <b-td>{{ data.titolo }}</b-td>
          <b-td>{{ data.rank }}</b-td>
          <b-td>{{ data.settore_riferimento }}</b-td>
          <b-td></b-td>
          <b-td>{{ data.created_at }}</b-td>
          <b-td>{{ data.updated_at }}</b-td>
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
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id Solution</b-td>
            <b-td class="td-respo-data">{{ data.id }}</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Title</b-td>
            <b-td class="td-respo-data">{{ data.titolo }}</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Rank</b-td>
            <b-td class="td-respo-data">{{ data.rank }}</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Reference sector</b-td>
            <b-td class="td-respo-data">{{ data.settore_riferimento }}</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id Status Solution</b-td>
            <b-td class="td-respo-data"></b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">{{ data.created_at }}</b-td>
          </div>
          <div class="respo-after-tr">
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
      <NoSolutionItems v-if="showNoItem" />
    </div>
  </b-overlay>
</template>
<script>
import NoSolutionItems from '~/components/nodata/NoSolutionItems'
export default {
  components: {
    NoSolutionItems,
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