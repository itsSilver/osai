import Vue from 'vue'
import VueLodash from 'vue-lodash'
import chunk from 'lodash/chunk'

Vue.use(VueLodash, { lodash: { chunk } })
