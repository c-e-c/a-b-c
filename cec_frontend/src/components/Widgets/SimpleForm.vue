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
    <!-- :class="{centerForm: form.divType}" -->
    <template v-for='(item, itemIndex) in form.items'>
      <template v-if='item.formVisible'>
        <template v-if='item.children && item.children.length>0'>
          <!-- 增加分组头部 -->
          <div class="el-form_header">
            {{ item.formItemUI.label }}
          </div>
          <!-- 增加分组内容 -->
          <template v-for='(child, childIndex) in item.children'>
            <el-form-item v-if='child.formVisible'
              :prop="'props.'+child.itemKey+'.editValue'"
              :label='child.formItemUI.label'
              :label-width='child.formItemUI.labelWidth'
              :required='child.formItemUI.required'
              :rules='child.formItemUI.rules'
              :error='child.formItemUI.error'
              :show-message='child.formItemUI.showMessage'
              :inline-message='child.formItemUI.inlineMessage'
              :size='child.formItemUI.size'>

              <!-- <template v-if="child.customType != null || child.customType"
                :slot="'props.'+child.itemKey+'.editValue'">
                <slot :name="child.customUI.componentName"></slot>
              </template> -->
              <!-- class="dynamicEditor" -->
              <DynamicEditor :editorUI='child.editorUI'
                :editorInfo='child'
                :editorModel='formData.props[child.itemKey]'
                @modelChanged='(val)=>{__handleFormDataModified(val, child.itemKey)}' />
            </el-form-item>
          </template>
        </template>
        <template v-else>
          <el-form-item :key='itemIndex'
            :prop="'props.'+itemIndex+'.editValue'"
            :label='item.formItemUI?item.formItemUI.label:undefined'
            :label-width='item.formItemUI?item.formItemUI.labelWidth:undefined'
            :required='item.formItemUI?item.formItemUI.required:undefined'
            :rules='item.formItemUI?item.formItemUI.rules:undefined'
            :error='item.formItemUI?item.formItemUI.error:undefined'
            :show-message='item.formItemUI?item.formItemUI.showMessage:undefined'
            :inline-message='item.formItemUI?item.formItemUI.inlineMessage:undefined'
            :size='item.formItemUI?item.formItemUI.size:undefined'>
            <DynamicEditor :editorUI='item.editorUI'
              :editorInfo='item'
              :editorModel='formData.props[itemIndex]'
              @modelChanged='(val)=>{__handleFormDataModified(val, itemIndex)}' />
          </el-form-item>
        </template>
      </template>
    </template>

    <!-- <template v-else
      v-for='(item, index) in form.items'>
      <el-form-item v-if='item.formVisible'
        :key='index'
        :prop="'props.'+index+'.editValue'"
        :label='item.formItemUI.label'
        :label-width='item.formItemUI.labelWidth'
        :required='item.formItemUI.required'
        :rules='item.formItemUI.rules'
        :error='item.formItemUI.error'
        :show-message='item.formItemUI.showMessage'
        :inline-message='item.formItemUI.inlineMessage'
        :size='item.formItemUI.size'>
        <DynamicEditor :slot="'props.'+index+'.editValue'"
          :editorUI='item.editorUI'
          :editorInfo='item'
          :editorModel='formData.props[index]'
          @modelChanged='(val)=>{__handleFormDataModified(val, index)}' />
      </el-form-item>
    </template> -->
  </el-form>
</template>

<script>
import * as utils_resource from '@/utils/resource'
import utils from '@/mixins/utils'
import DynamicEditor from '@/components/Widgets/DynamicEditor'

/**
 * 简单的表单
 */
export default {
  name: 'SimpleForm',
  components: { DynamicEditor },
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

            // 4、可选 孩子,目前只支持一层孩子，总共两层
            children:[{}],
            // itemKey此字段SimpleForm初始化时自动生成
            // itemKey: 'xxx',             
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
      type: Object,
      default: function () { return {} },
    },
  },
  data: function () {
    var tempFormData = {}
    if (this.formModel && Object.keys(this.formModel).length !== 0) {
      tempFormData = JSON.parse(JSON.stringify(this.formModel))
    } else {
      tempFormData = {
        props: utils_resource.generateProperties(this._getLeafItems(this.form.items))
      }
    }
    return {
      /**
       * formData为资源描述属性列表props信息，参考资源描述标准。其中每个列表属性需要与form.items的列表一一对应
      */
      formData: tempFormData,
    }
  },
  created() {
    this._setLeafItems(this.form.items)
  },
  methods: {
    /**
     * 清除表单数据
     */
    reset() {
      // 清除数据
      var tempFormData = utils_resource.generateProperties(this._getLeafItems(this.form.items))
      this.formData = {
        props: tempFormData
      }
      // 清除界面
      this.$refs.elForm.resetFields()
    },
    /**
     * 获取表单数据
     */
    getFormProps() {
      return JSON.parse(JSON.stringify(this.formData.props))
    },

    /**
     * 获取表单资源数据
     */
    getFormResData() {
      return JSON.parse(JSON.stringify(this.formData))
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
  margin: 0 auto 0 0;
  width: 50%;
}
</style>
