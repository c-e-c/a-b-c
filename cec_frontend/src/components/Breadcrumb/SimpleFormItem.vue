<template>
  <el-form-item :prop='prop'
    :label='formItemUI.label'
    :label-width='formItemUI.labelWidth'
    :required='formItemUI.required'
    :rules='formItemUI.rules'
    :error='formItemUI.error'
    :show-message='formItemUI.showMessage'
    :inline-message='formItemUI.inlineMessage'
    :size='formItemUI.size'>
    <slot :name='prop'></slot>
  </el-form-item>
</template>
<script>
export default {
  name: 'SimpleFormItem',
  props: {
		/**
     * form-item的prop
	   * 参见element-ui组件el-table-column的属性
     */
    prop: {
      type: String,
      required: true,
    },
		/**
     * form-item ui
     * 参见element-ui组件el-form-item的属性
     */
    formItemUI: {
      type: Object,
      default: function () { return {} },
    },
  },
}
</script>