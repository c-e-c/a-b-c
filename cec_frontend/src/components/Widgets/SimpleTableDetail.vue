<template>
  <div>
    <el-button @click="handleReturnButtonClicked()"
      size="small">返回</el-button>
    <el-button @click="handleClick()"
      type="primary">保存</el-button>

    <SimpleForm :formUI='detailFormUI'
      :form='detailForm'
      :formModel='detailFormModel'>
      <!-- <template v-for='(item, index) in collapse.items'>
        <template v-for='(child, ind) in item.children'>
          <el-transfer v-if="child.customType"
            :slot="child.customUI.componentName"
            v-model="child.customUI.value1"
            :data="child.customUI.data"></el-transfer>
        </template>
      </template> -->
    </SimpleForm>
  </div>
</template>

<script>
//import utils from '@/mixins/utils'
import SimpleForm from '@/components/Widgets/SimpleForm'
import SimpleCollapse from '@/components/Widgets/SimpleCollapse'

export default {
  name: 'SimpleTableDetail',
  //mixins: [utils],
  components: { SimpleForm, SimpleCollapse },
  props: {
    detailFormUI: {
      type: Object,
      default: function () { return {} },
    },
    detailForm: {
      type: Object,
      default: function () { return {} },
    },
    detailFormModel: {
      type: Object,
      default: function () { return {} },
    },
  },
  data() {
    return {
    }
  },
  methods: {
		/**
		 * 点击返回按钮
		 */
    handleReturnButtonClicked() {
			/**
			 * 返回按钮
			 * @event detailReturnClicked
				*/
      this.$emit('detailReturnClicked')
    },
  },
}
</script>
<style scoped>
.el-form_header {
  height: 48px;
  line-height: 48px;
  background-color: #fff;
  color: #303133;
  cursor: pointer;
  border-bottom: 1px solid #abb2c7;
  outline: none;
}
.form {
  margin: 0 auto;
  width: 800px;
}
.input {
  width: 400px;
  padding: 0px;
}
.transfer {
  padding: 24px;
}
</style>

