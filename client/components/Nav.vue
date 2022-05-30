<template>
  <nav id="sidebar" v-bind:class="{ closedsidebar: isClosedOpened }">
    <div class="custom-menu">
      <button
        type="button"
        id="sidebarCollapse"
        class="btn respo-button"
        @click="openSideMenu()"
      >
        <i class="fa fa-bars"></i>
        <!-- <span class="sr-only">Toggle Menu</span> -->
      </button>
    </div>
    <p class="side-menu-title">CONTENT</p>
    <ul class="list-unstyled components">
      <li class="active">
        <nuxt-link tag="a" to="/signals" class="text-white"
          ><i class="fa-regular fa-gem mr-3"></i> Signals</nuxt-link
        >
      </li>
      <li>
        <nuxt-link tag="a" to="/solutions" class="text-white"
          ><i class="fa fa-ghost mr-3"></i> Solutions</nuxt-link
        >
      </li>

      <li>
        <nuxt-link tag="a" to="/occurrences" class="text-white"
          ><i class="fa-regular fa-gem mr-3"></i> Occurrences</nuxt-link
        >
      </li>
      <!-- <li>
        <a class="text-white" href="#"
          ><i class="fa fa-ghost mr-3"></i> Status Solutions</a
        >
      </li>
      <li>
        <a class="text-white" href="#"
          ><i class="fa fa-droplet mr-3"></i> Status Signals</a
        >
      </li> -->
    </ul>
    <p class="side-menu-title">SETTINGS</p>
    <ul class="list-unstyled components">
      <li>
        <nuxt-link tag="a" to="/manage-access" class="text-white"
          ><i class="fa fa-ghost mr-3"></i> Manage access</nuxt-link
        >
      </li>
      <!-- <li>
        <a class="text-white" href="#"
          ><i class="fa fa-location-dot mr-3"></i> Translations</a
        >
      </li> -->
    </ul>
  </nav>
</template>
<script>
export default {
  name: 'Nav',
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
