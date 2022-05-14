<template>
  <b-overlay :show="show" rounded="sm">
    <b-table-simple
      class="table table-bordred table-striped text-center table-desktop"
    >
      <b-thead>
        <b-th>
          <input type="checkbox" class="checkthis" id="checkall" />
        </b-th>
        <b-th>Id occorrenza </b-th>
        <b-th>Id segnalazione </b-th>
        <b-th>Id soluzione </b-th>
        <b-th>Titolo </b-th>
        <b-th>Commessa macchina </b-th>
        <b-th>Versione sw 1 </b-th>
        <b-th>Versione sw 2 </b-th>
        <b-th>Data occorrenza </b-th>
        <b-th>Stato occorrenza </b-th>
        <b-th>Creation date </b-th>
        <b-th>Update date </b-th>
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
            <b-td class="td-respo-title">Id occorrenza</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id segnalazione</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id soluzione</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Titolo</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Commessa macchina</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Versione sw 1</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Versione sw 2</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Data occorrenza</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Stato occorrenza</b-td>
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
            <b-td class="td-respo-title">Id occorrenza</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id segnalazione</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Id soluzione</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Titolo</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Creation date</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Commessa macchina</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Versione sw 1</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Versione sw 2</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Data occorrenza</b-td>
            <b-td class="td-respo-data">test</b-td>
          </div>
          <div class="respo-after-tr">
            <b-td class="td-respo-title">Stato occorrenza</b-td>
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