import Vue from 'vue'
import VueGates from 'vue-gates'

Vue.use(VueGates, {
  // Configuration
  persistent: true,
})

export default (_context, inject) => {
  inject('gates', Vue.prototype.$gates)
}
