export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'OSAI',
    htmlAttrs: {
      lang: 'en',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['@/assets/css/main.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {
      src: '~/plugins/lodash.client.js',
    },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@oruga-ui/oruga/nuxt',
    'vue2-editor/nuxt',
    'nuxtjs-mdi-font',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: 'http://api.apexroyale.com',
  },
  // Authentication logic here
  auth: {
    strategies: {
      local: {
        token: {
          property: 'token',
          global: true,
          // required: true,
          type: 'Token',
        },
        user: {
          property: '',
          autoFetch: true,
        },
        endpoints: {
          login: {
            url: '/user/login',
            method: 'post',
            propertyName: 'token',
          },
          user: {
            url: 'user/detail',
            method: 'get',
          },
          logout: false,
        },
      },
    },
  },
  build: {},
}
