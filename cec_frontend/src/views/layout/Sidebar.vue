<template>
  <el-menu mode="vertical" background-color="#324157" text-color="#EEF1F6" :default-active="$route.path">
    <sidebar-item :routes='permission_routers'></sidebar-item>
  </el-menu>
</template>

<script>
import { mapGetters } from 'vuex'
import SidebarItem from './SidebarItem'
export default {
  components: { SidebarItem },
  computed: {
    ...mapGetters([
      'permission_routers'
    ])
  }
}
</script>

<style scoped>
.el-menu {
  min-height: 100%;
}
</style>
