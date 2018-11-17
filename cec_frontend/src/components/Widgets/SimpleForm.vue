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
    :size='formUI.size'
    :class="{centerForm: form.divType}">
    <template v-if='form.divType'>
      <template v-for='(item, itemIndex) in form.items'>
        <!-- <div v-if="item.children && JSON.stringify(item.children) !='[]'"> -->

        <div class="el-form_header">
          {{item.titleName}}
        </div>
        <div>
          <template v-for='(child, childIndex) in item.children'>
            <simple-form-item v-if='child.formVisible'
              :key='childIndex'
              :prop="'props.'+itemIndex+'.'+childIndex+'.editValue'"
              :formItemUI='child.formItemUI'>
              <template v-if="child.customType != null || child.customType"
                :slot="'props.'+itemIndex+'.'+childIndex+'.editValue'">
                <slot :name="child.customUI.componentName"></slot>
              </template>
              <DynamicEditor v-else
                class="dynamicEditor"
                :slot="'props.'+itemIndex+'.'+childIndex+'.editValue'"
                :editorUI='child.editorUI'
                :editorInfo='child'
                :editorModel='formData.props[itemIndex][childIndex]'
                @modelChanged='(val)=>{__handleFormDataModified(val, childIndex)}' />
            </simple-form-item>
          </template>
        </div>

      </template>
    </template>
    <!-- </div> -->

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
    <template v-else
      v-for='(item, index) in form.items'>
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
            fieldName: xxx,         // 可选，属性的属性名
            comparison: 'xxx'       // 可选，默认为exact，操作符，具体参照django的Fields的lookup分词
            formVisible: false,     // 可选，默认为不显示，列是否可展示  

            // 2、可选 表单内表单项对象
            formItemUI: {
              // el-form-item的属性，参见element-ui组件
            },
            // 3、可选 表单内表单项控件对象
            DynamicEditor控件的editorInfo的多个属性内容，参见DynamicEditor.editorInfo

            // 4、可选 孩子
            children:[{}],
          },{
            ...
        }],
      }
     */
    form: {
      type: Object,
      required: true,
    },
    /**
     * formmodel数据，参见资源描述对象
     */
    formModel: {
      type: Array,
      default: function () { return [] },
    },
  },
  data: function () {
    var tempFormData = []
    if (this.formModel && this.formModel.length !== 0) {
      tempFormData = JSON.parse(JSON.stringify(this.formModel))
    } else {
      tempFormData = utils_resource.generateProperties(this._getLeafColumns(this.form.items))
    }

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
      var tempFormData = utils_resource.generateProperties(this._getLeafColumns(this.form.items))
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
<style scoped>
.el-form_header {
  height: 48px;
  line-height: 48px;
  background-color: #fff;
  color: #303133;
  cursor: pointer;
  border-bottom: 1px solid #abb2c7;
  outline: none;
  margin-bottom: 10px;
}
.centerForm {
  margin: 0 auto;
  width: 35%;
}
.dynamicEditor {
  width: 100%;
  padding: 0px;
}
</style>
