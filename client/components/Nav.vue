<template>
  <nav id="sidebar" v-bind:class="{ closedsidebar: isClosedOpened }">
    <div class="custom-menu">
      <button type="button" id="sidebarCollapse" class="btn respo-button" @click="openSideMenu()">
        <i class="mdi mdi-menu mr-3"></i>
        <!-- <span class="sr-only">Toggle Menu</span> -->
      </button>
    </div>
    <UserDetails />
    <p class="side-menu-title">CONTENT</p>
    <ul class="list-unstyled components">
      <li class="active" v-permission="'Can view segnalazioni'">
        <nuxt-link tag="a" to="/signals" class="text-white px-14-format">
          <i class="mdi mdi-alarm-light mr-3"></i> Signals
        </nuxt-link>
      </li>
      <li v-permission="'Can view occorrenze'">
        <nuxt-link tag="a" to="/occurrences" class="text-white px-14-format">
          <i class="mdi mdi-repeat mr-3"></i>
          Occurrences
        </nuxt-link>
      </li>
      <li v-permission="'Can view soluzioni'">
        <nuxt-link tag="a" to="/solutions" class="text-white px-14-format">
          <i class="mdi mdi-lightbulb mr-3"></i> Solutions
        </nuxt-link>
      </li>
    </ul>
    <p class="side-menu-title" v-permission="'Can view users'">SETTINGS</p>
    <ul class="list-unstyled components">
      <li v-permission="'Can view users'">
        <nuxt-link tag="a" to="/manage-access" class="text-white px-14-format">
          <i class="mdi mdi-account-group mr-3"></i>
          Manage access
        </nuxt-link>
      </li>
    </ul>
    <div data-v-1165e0b7="" class="
        infos
        px-4
        py-1
        bg-primary
        text-right
        position-absolute
        bottom-0
        w-100
        logout-row
      ">
      <nuxt-link tag="a" to="/logout" class="text-white text-uppercase font-weight-bold logout-btn">
        <i class="mdi mdi-logout mr-1"></i>
        Logout
      </nuxt-link>
    </div>
  </nav>
</template>
<script>
import UserDetails from '~/components/UserDetails'
export default {
  name: 'Nav',
  components: { UserDetails },
  data() {
    return {
      isClosedOpened: false,
    }
  },
  methods: {
    openSideMenu() {
      this.isClosedOpened = !this.isClosedOpened
    },
  },
}
</script>
<style scoped>
.logout-row {
  background-color: #485679 !important;
}

.logout-row>a {
  background-color: #4373fb !important;
  border-radius: 0.25rem !important;
  padding: 0.2rem 0.4rem !important;
}
</style>
