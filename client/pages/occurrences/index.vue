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
                <li class="nav-actions-color mx-2">
                  <i class="fas fa-bars pr-2 fas-main-color"></i>
                  Occurrences
                </li>
              </ul>
            </div>
            <ul
              class="d-flex justify-content-around align-content-center m-0 p-0"
              style="list-style: none"
            >
              <li
                role="button"
                class="mx-2 button-format"
                @click="redirectCreate()"
              >
                <i class="fas fa-plus pr-2"></i>
                New Occurrence
              </li>
            </ul>
            <!-- End here -->
          </div>
          <div class="vertical-line"></div>
          <div
            class="
              nav-actions
              d-flex
              justify-content-between
              align-items-center
              mb-2
              navtop
              second-nav-option
            "
          >
            <!-- Second Nav -->
            <div class="d-flex gap-4 second-d-flex-left">
              <b-input-group class="mt-3">
                <b-form-input
                  class="input-search"
                  placeholder="Search"
                  style="height: 40px !important"
                ></b-form-input>
                <b-input-group-append>
                  <b-button class="button-format">
                    <i class="fas fa-search pr-2"></i>Search</b-button
                  >
                </b-input-group-append>
              </b-input-group>
            </div>
            <div
              class="
                d-flex
                justify-content-around
                align-content-center
                m-0
                p-0
                second-d-flex-right
              "
            >
              <b-form-select
                class="number-rows"
                v-model="selected"
                :options="options"
              ></b-form-select>
            </div>
            <!-- End here -->
          </div>
          <div class="table-space">
            <OccurenzeTable />
          </div>
        </div>
      </div>
    </client-only>
  </div>
</template>

<script>
import Nav from '~/components/Nav'
import OccurenzeTable from '~/components/tables/OccurenzeTable.vue'
export default {
  components: {
    Nav,
    OccurenzeTable,
  },
  data() {
    return {
      selected: null,
      options: [
        { value: null, text: '10' },
        { value: '15', text: '15' },
        { value: '20', text: '20' },
        { value: '25', text: '25' },
        { value: '30', text: '30', disabled: true },
      ],
    }
  },
  methods: {
    redirectCreate() {
      this.$router.push(`/occurrences/create`)
    },
  },
}
</script>
<style scoped>
</style>
