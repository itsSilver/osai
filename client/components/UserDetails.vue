<template>
  <div>
    <p class="side-menu-title">User Details</p>
    <div class="profile-pic">
      <div class="count-indicator">
        <img class="img-xs rounded-circle" src="@/assets/images/avatar.png" alt="" />
        <!-- <span class="count bg-success"></span> -->
      </div>
      <div class="profile-name">
        <h5 class="mb-0 font-weight-normal user-name">{{ $auth.user.name }}</h5>
        <span class="user-email">{{ $auth.user.email }}</span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
    }
  },
}
</script>
<style scoped>
.img-xs {
  width: 35px !important;
  height: 35px !important;
}

.profile-pic {
  display: flex !important;
  align-items: center !important;
  position: relative;
  bottom: 5px;
}

.profile-name {
  margin-left: 1rem !important;
  line-height: 1 !important;
}

.user-name {
  font-size: 14px !important;
  font-weight: 700 !important;
  white-space: nowrap;
  margin-bottom: 0 !important;
  color: #ffffff !important;
}

.user-email {
  font-size: 12px !important;
  color: #e2e5f0 !important;
  white-space: nowrap !important;
}

.count-indicator {
  position: relative;
  left: 10px;
}
</style>