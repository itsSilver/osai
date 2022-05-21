<template>
  <b-overlay :show="show" rounded="sm">
    <b-table-simple
      class="table table-bordred table-striped text-center table-desktop"
    >
      <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th><i class="fa-solid fa-arrow-down-short-wide"></i>Id Signal</b-th>

        <b-th>Rank</b-th>
        <b-th>Reference sector</b-th>
        <b-th>Id status solution</b-th>
        <b-th>Creation date</b-th>
        <b-th>Update date</b-th>
      </b-thead>
      <b-tbody v-if="!showNoItem">
        <b-tr>
          <b-td>
            <input type="checkbox" class="checkthis" />
          </b-td>
          <b-td>test</b-td>
          <b-td>test</b-td>
          <b-td>test</b-td>
          <b-td>test</b-td>
          <b-td>test</b-td>
          <b-td>test</b-td>
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

        <b-th>Rank</b-th>
        <b-th>Reference sector</b-th>
        <b-th>Id status solution</b-th>
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
            <b-td class="td-respo-title">Id Signal</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Rank</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Reference sector</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id status solution</b-td>
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
            <b-td class="td-respo-title">Id Signal</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Rank</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Reference sector</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id status solution</b-td>
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
            <b-td class="td-respo-title">Id Signal</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Rank</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Reference sector</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id status solution</b-td>
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
    <div class="no-data">
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
    }
  },
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