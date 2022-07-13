<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container">
        <span @click="cancel()">
          <CloseIcon class="closeicon" />
        </span>
        <div class="modal-box">
          <img class="img-fluid img-100" :src="$config.baseURL + imageValue" alt=""
            v-if="imageValue !== '/media/null' && imageValue" />
          <img v-else class="img-fluid img-100" src="~/assets/images/noimage.jpg" alt=""
            style="max-height: 500px !important" />
          <div class="modal-footer mt-8">
            <slot name="footer">
              <b-button class="mx-2 button-format" @click="cancel()">Close</b-button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import CloseIcon from '~/components/icons/close'
export default {
  components: { CloseIcon },
  data() {
    return {
      showNoItem: false,
      show: false,
      variant: 'info',
      dataTable: [],
    }
  },
  methods: {
    cancel() {
      this.$emit('close')
    },
  },
  props: ['imageValue', 'noImageDisplay'],
}
</script>
<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  max-width: 950px;
  width: 100%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.anulla {
  width: 140px;
  color: #fff;
  background-color: #c2c2c2;
  border-radius: 8px;
  text-transform: uppercase;
  border: none;
  padding: 0.375rem 0.75rem;
  font-size: 0.9rem;
  line-height: 1.6;
  border-radius: 0.25rem;
}

.salva {
  width: 140px;
  color: #fff;
  background-color: #ce4600;
  border-radius: 8px;
  text-transform: uppercase;
  border: none;
  padding: 0.375rem 0.75rem;
  font-size: 0.9rem;
  line-height: 1.6;
  border-radius: 0.25rem;
}

.modal-body-custom {
  padding: 0 1rem;
  background-color: #f5f6fa;
  border: 1px solid #ce4600;
  border-radius: 0px;
  padding-top: 0.75rem;
}

.modal-footer {
  padding-left: 0;
  padding-right: 0;
  padding-top: 50px !important;
  border-top: unset !important;
}

.modal-header {
  text-align: center;
  font-size: 28px;
  line-height: 32px;
  font-weight: bold;
  background-color: #181824;
  color: #fff;
  margin-bottom: 0.75rem;
  border-radius: 0;
  border: none;
  display: block;
  text-transform: uppercase;
}

.modal-body-custom label {
  display: block;
}

.error {
  color: red;
  font-weight: 500;
  font-size: 14px;
}

.forma {
  width: 50%;
}

.forma input {
  width: 100%;
  border-radius: 4px;
  height: 35px;
}

@media (max-width: 400px) {
  .anulla {
    width: 50%;
    max-width: 100px;
  }

  .salva {
    width: 50%;
    max-width: 100px;
  }

  .modal-header {
    font-size: 22px;
    line-height: 28px;
  }
}
</style>