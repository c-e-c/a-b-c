<template>
  <div>
    <SimpleButtonGroup class='simplebuttongroup'
      :buttonGroup='toolButtonGroupData' />
    <template v-if="detailStyle === 'collapsestyle'">

    </template>
    <template v-else>
      <SimpleForm ref='elForm'
        class='simpleform'
        :formUI='detailFormUI'
        :form='detailForm'
        :formModel='detailFormModel'>
      </SimpleForm>
    </template>
    <slot name='customdetail' />
  </div>
</template>

<script>
import * as api_gda from '@/api/gda'
import * as utils_resource from '@/utils/resource'
import * as utils_ui from '@/utils/ui'
//import utils from '@/mixins/utils'
import SimpleButtonGroup from '@/components/Widgets/SimpleButtonGroup'
import SimpleForm from '@/components/Widgets/SimpleForm'

export default {
  name: 'SimpleTableDetail',
  //mixins: [utils],
  components: {
    SimpleForm,
    SimpleButtonGroup,
  },
  props: {
    /**
     * 明细样式：包含formstyle,collapsestyle。默认为form
     */
    detailStyle: {
      type: String,
      default: 'formstyle'
    },

    /**
     * 详情formUI数据,参见SimpleForm的formUI属性
     */
    detailFormUI: {
      type: Object,
      default: function () { return {} }
    },
    /**
     * 详情form数据,参见SimpleForm的form属性
     */
    detailForm: {
      type: Object,
      default: function () { return {} }
    },
    /**
     * 详情form数据Model,参见SimpleForm的formModel属性
     */
    detailFormModel: {
      type: Object,
      default: function () { return {} },
    },
    /**
     * 要替换的工具按钮组，已有按钮组，包含uri: return,save
     * 这些可以被替代默认设置，也可以自定义值，
        [
          {
            uri:'xxx'          // xxx为按钮唯一标示uri
            click:'',          // click为点击事件
            name:'',           // name为按钮名字
            buttonUI:{
              // 参见element-ui el-button的属性
            },
          },...
        ]
     */
    defaultDetailToolButtonGroup: {
      type: Array,
      default: function () { return [] },
    },
  },
  data() {
    return {
      // 工具按钮组
      toolButtonGroupData: this.__getDetailToolButtonGroup(),
    }
  },
  methods: {
		/**
		 * 点击返回按钮
		 */
    __handleReturnButtonClicked() {
			/**
			 * 返回按钮
			 * @event detailReturnClicked
				*/
      this.$emit('detailReturnClicked')
    },
    __handleSaveButtonClicked() {
      // 校验form
      this.$refs.elForm.validate((valid, obj) => {
        if (valid) {
          // 调用接口
          var diffModel = utils_resource.getDifferenceModel([this.$refs.elForm.getFormResData()])
          if (!diffModel) {
            return
          }
          api_gda.saveData(this.table.tableName, diffModel).then((responseData) => {
            this.$message({ message: '保存成功', type: 'success' })
          }).catch((error) => {
            // 设置界面
            utils_ui.showErrorMessage(error)
          })
        } else {
          let msg = ''
          Object.keys(obj).forEach(key => {
            obj[key].forEach(element => {
              msg += element.field + ':' + element.message // todo element.field 细化扩展修改
            })
          })
          utils_ui.showErrorMessage({ message: msg })
          return
        }
      })

    },
    __getDetailToolButtonGroup() {
      // 设置已有toolbuttongroup数据
      var tempToolButtonGroup = [
        [
          {
            uri: 'return',
            name: '返回',
            click: this.__handleReturnButtonClicked,
            visible: true,
            buttonUI: {
              type: 'primary',
              size: 'mini',
              icon: 'el-icon-search',
            },
          },
        ], [
          {
            uri: 'save',
            name: '保存',
            click: this.__handleSaveButtonClicked,
            visible: true,
            buttonUI: {
              type: 'primary',
              size: 'mini',
              icon: 'el-icon-tickets',
            }
          },
        ], [
          {
            uri: 'import',
            name: '导入',
            visible: true,
            buttonUI: {
              type: 'primary',
              size: 'mini',
              icon: 'el-icon-upload2',
            }
          }, {
            uri: 'export',
            name: '导出',
            visible: true,
            buttonUI: {
              type: 'primary',
              size: 'mini',
              icon: 'el-icon-download',
            }
          }, {
            uri: 'print',
            name: '打印',
            visible: true,
            buttonUI: {
              type: 'primary',
              size: 'mini',
              icon: 'el-icon-printer',
            }
          },
        ]
      ]
      if (this.defaultDetailToolButtonGroup && this.defaultDetailToolButtonGroup.length !== 0) {
        this.defaultDetailToolButtonGroup.forEach(button => {
          var tempButton = this.__findButtonGroup(tempToolButtonGroup, button.uri)
          if (tempButton) {
            Object.keys(button).forEach(prop => {
              tempButton[prop] = button[prop]
            })
          }
        })
      }
      return tempToolButtonGroup
    },
  },
}
</script>
<style scoped>
.simplebuttongroup {
  padding: 5px 10px 5px 10px;
}
.simpleform {
  padding: 0px 10px 0px 10px;
}
</style>

