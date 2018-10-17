<template>
    <div class="collapse">
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
            <el-collapse v-model="collapse.collapseUI.activeNames"
                :accordion="collapse.collapseUI.accordion">
                <template v-for='(item, index) in collapse.items'>
                    <el-collapse-item :title="item.collapseItemUI.title"
                        :name="item.collapseItemUI.name">
                        <template v-for='(it, ind) in item.children'>
                            <simple-form-item v-if='it.formVisible'
                                :key='ind'
                                :prop="'props.'+index+'.'+ind+'.editValue'"
                                :formItemUI='it.formItemUI'>
                                <template v-if="it.customType"
                                    :slot="'props.'+index+'.'+ind+'.editValue'">
                                    <slot :name="index+'.'+ind"></slot>
                                </template>
                                <DynamicEditor v-else
                                    class="dynamicEditor"
                                    :slot="'props.'+index+'.'+ind+'.editValue'"
                                    :editorUI='it.editorUI'
                                    :editorInfo='it'
                                    :editorModel='formData.props[index][ind]'
                                    @modelChanged='(val)=>{__handleFormDataModified(val, ind)}' />
                            </simple-form-item>
                        </template>
                    </el-collapse-item>
                </template>
            </el-collapse>
        </el-form>
    </div>
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
              collapseUI:{
                  activeNames: xx,
                  accordion: xx,
              }
            // 表单内el-form表单对象
            items:[
              { 
                // 2、可选 表单内表单项对象
                customType:"",
                collapseItemUI: {
                    title: xxx,
                    name: xxx,
                  // collapseItemUI的属性，参见element-ui组件
                },
                // 3、可选 表单内表单项控件对象
                DynamicEditor控件的editorInfo的多个属性内容，参见DynamicEditor.editorInfo
    
                // 4、可选 孩子
                children:[参见SimpleForm中items资源结构],
              },{
                ...
            }],
          }
         */
        collapse: {
            type: Object,
            required: true,
        },
    },
    data: function () {
        /**
        * formData.props[index][in] 
        * {
        * [[{},{}],[],]
        * }
        */
        var tempFormData = []
        this.collapse.items.forEach(element => {
            if (element.children) {
                tempFormData.push(utils_resource.generateProperties(element.children))
            }
        })
        return {
            /**
             * formData为资源描述属性列表props信息，参考资源描述标准。其中每个列表属性需要与form.items的列表一一对应
             * {[[{},{}],[],]}
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
.collapse {
  margin: 0 auto;
  width: 800px;
}
.dynamicEditor {
  width: 300px;
  padding: 0px;
}
.transfer {
  padding: 24px;
}
</style>
