<template>
  <el-form ref='elForm'
    :model='formData'
    :rules='formUI.rules'
    :inline='formUI.inline'
    :label-position='formUI.labelPosition'
    :label-width="formUI.labelWidth ? formUI.labelWidth : '80px'"
    :label-suffix='formUI.labelSuffix'
    :show-message='formUI.showMessage'
    :inline-message='formUI.inlineMessage'
    :status-icon='formUI.statusIcon'
    :size='formUI.size'>
    <template v-for='(item, index) in form.items'>
      <simple-form-item v-if='item.formVisible'
        :key='index'
        :prop="'props.'+index+'.editValue'"
        :formItemUI='item.formItemUI'>
        <DynamicEditor :slot="'props.'+index+'.editValue'"
          :editorUI='item.editorUI'
          :editorInfo='item'
          :editorModel='formData.props[index]'
          @modelChanged='(val)=>{__handleFormDataModified(val, index)}' />
      </simple-form-item>
      <!-- <el-form-item :key='item.uri'
        :prop="
          'props.'+index+
          '.editValue'
          "
        :label='item.formItemUI.label'
        :label-width='item.formItemUI.labelWidth'
        :required='item.formItemUI.required'
        :rules='item.formItemUI.rules'
        :error='item.formItemUI.error'
        :show-message='item.formItemUI.showMessage'
        :inline-message='item.formItemUI.inlineMessage'
        :size='item.formItemUI.size'>
        <DynamicEditor :editorUI='item.editorUI'
          :editorInfo='item'
          v-model='formData.props[index]' />
      </el-form-item> -->
    </template>
  </el-form>
</template>

<script>
import * as utils_resource from '@/utils/resource'
import utils from '@/mixins/utils'
import SimpleFormItem from '@/components/Widgets/SimpleFormItem'
import DynamicEditor from '@/components/Widgets/DynamicEditor'

/**
 * 简单的表单
 */
export default {
  name: 'SimpleForm',
  components: { DynamicEditor, SimpleFormItem },
  mixins: [utils],
  // model: {
  //   prop: 'formModel',
  //   event: 'modelChanged'
  // },
  props: {
    /**
     * 表ui
     * 参见element-ui组件el-form的属性
     */
    formUI: {
      type: Object,
      default: function () { return {} },
    },

    /**
     * 
      {
        // 表单内el-form表单对象
        items:[
          {
            // 1、自定义部分
            fieldName: xxx,         // 必须，属性的属性名
            comparison: 'xxx'       // 可选，默认为exact，操作符，具体参照django的Fields的lookup分词
            formVisible: false,         // 可选，默认为不显示，列是否可展示  

            // 2、可选 表单内表单项对象
            formItemUI: {
              // el-form-item的属性，参见element-ui组件
            },
            // 3、可选 表单内表单项控件对象
            DynamicEditor控件的editorInfo的多个属性内容，参见DynamicEditor.editorInfo

            // 4、 可选 孩子
            formChildren:[{}],
          },{
            ...
        }],
      }
     */
    form: {
      type: Object,
      required: true,
    },
  },
  data: function () {
    var tempFormData = utils_resource.generateProperties(this.form.items)

    return {
      /**
       * formData为资源描述属性列表props信息，参考资源描述标准。其中每个列表属性需要与form.items的列表一一对应
      */
      formData: { props: tempFormData },
    }
  },
  watch: {
    // // 外界数据被修改，直接深拷贝数据，暂时先写成JSON形式转换
    // formModel: {
    //   handler: function (val) {
    //     this.formData = JSON.parse(JSON.stringify(val))
    //   },
    //   deep: true,
    // },
    // // 内部数据被修改
    // formData: {
    //   handler: function (val) {
    //     /**
    //      * form表单中得到改变的值.
    //      *
    //      * @event modelChanged
    //      * @type {object}
    //      */
    //     this.$emit('modelChanged', JSON.parse(JSON.stringify(val)))
    //   },
    //   deep: true,
    // }
  },
  methods: {
    /**
     * 清除表单数据
     */
    reset() {
      // 清除数据
      var tempFormData = utils_resource.generateProperties(this.form.items)
      this.formData = { props: tempFormData }
      // 清除界面
      this.$refs.elForm.resetFields()
    },

    /**
     * 获取表单数据
     */
    getFormData() {
      return JSON.parse(JSON.stringify(this.formData.props))
    },

    __handleFormDataModified(val, index) {
      this.formData.props[index] = val
      /**
       * form表单中得到改变的值.
       *
       * @event modelChanged
       * @type {object}
       */
      this.$emit('modelChanged', JSON.parse(JSON.stringify(val)))
    }


    // keyEvent(ev, v) {
    //   if (ev.keyCode == 13) {
    //     this.$refs[v].$el.querySelector('input').focus()
    //   } else if (ev.keyCode == 112) {
    //     this.saveData()
    //   }
    // }
  },

}
</script>
