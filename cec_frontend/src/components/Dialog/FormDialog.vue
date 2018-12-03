<template>
  <el-dialog :title="dialogTitle"
    :visible.sync="showFlag"
    :width="dialog.width"
    :fullscreen="dialog.fullscreen"
    :top="dialog.top"
    :modal="dialog.modal"
    :modal-append-to-body="dialog.modalAppendToBody"
    :append-to-body="dialog.appendToBody"
    :lock-scroll="dialog.lockScroll"
    :custom-class="dialog.customClass"
    :close-on-click-modal="dialog.closeOnClickModal"
    :close-on-press-escape="dialog.closeOnPressEscape"
    :show-close="dialog.showClose"
    :center="dialog.center"
    @close="close"
    @open="__open">
    <SimpleForm ref="simpleForm"
      :formInfo="formUI"
      :formModel="formModel"
      @formModelChanged="(val)=>{__storeModifiedFormModel(val)}" />
    <div slot="footer">
      <template v-for="name in Object.keys(dialogButtons)">
        <!-- 关闭按钮直接实现，外部不需要实现 -->
        <template v-if="name==='关闭'">
          <el-button :key="name"
            :size="dialogButtons[name].size"
            :type="dialogButtons[name].type"
            :plain="dialogButtons[name].plain"
            :round="dialogButtons[name].round"
            :loading="dialogButtons[name].loading"
            :disabled="dialogButtons[name].disabled"
            :icon="dialogButtons[name].icon"
            :autofocus="dialogButtons[name].autofocus"
            :native-type="dialogButtons[name].nativeType"
            @click.native="close">
            {{name}}
          </el-button>
        </template>
        <template v-else-if="name==='保存'">
          <el-button :key="name"
            :size="dialogButtons[name].size"
            :type="dialogButtons[name].type"
            :plain="dialogButtons[name].plain"
            :round="dialogButtons[name].round"
            :loading="dialogButtons[name].loading"
            :disabled="dialogButtons[name].disabled"
            :icon="dialogButtons[name].icon"
            :autofocus="dialogButtons[name].autofocus"
            :native-type="dialogButtons[name].nativeType"
            @click.native="__save">
            {{name}}
          </el-button>
        </template>
        <template v-else>
        </template>
      </template>
    </div>
  </el-dialog>
</template>

<script>
import SimpleForm from "@/Widgets/SimpleForm"

export default {
  name: "FormDialog",
  components: {
    SimpleForm,
  },

  model: {
    prop: "visible",
    event: "showChanged",
  },
  props: {
    /**
     * 对话框是否可视
     */
    visible: {
      type: Boolean,
      default: false,
    },

    /**
     * 对话框模式，create模式与update模式
     * create模式给新增数据使用
     * update模式给更新数据使用
     */
    dialogMode: {
      type: String,
      default: "create",// 值为create、update,默认为create
    },

    /**
     * 对话框el-dialog对象
     *
      {
        // el-dialog的属性，参见element-ui组件
        参数	说明	类型	可选值	默认值
        width	Dialog 的宽度	string	—	50%
        fullscreen	是否为全屏 Dialog	boolean	—	false
        top	Dialog CSS 中的 margin-top 值	string	—	15vh
        modal	是否需要遮罩层	boolean	—	true
        modal-append-to-body	遮罩层是否插入至 body 元素上，若为 false，则遮罩层会插入至 Dialog 的父元素上	boolean	—	true
        append-to-body	Dialog 自身是否插入至 body 元素上。嵌套的 Dialog 必须指定该属性并赋值为 true	boolean	—	false
        lock-scroll	是否在 Dialog 出现时将 body 滚动锁定	boolean	—	true
        custom-class	Dialog 的自定义类名	string	—	—
        close-on-click-modal	是否可以通过点击 modal 关闭 Dialog	boolean	—	true
        close-on-press-escape	是否可以通过按下 ESC 关闭 Dialog	boolean	—	true
        show-close	是否显示关闭按钮	boolean	—	true
        center	是否对头部和底部采用居中布局	boolean	—	false
      } 
     *
     */
    dialog: {
      type: Object,
      default: function () {
        return {
          // elementui_dialog
          title: "", width: "50%", fullscreen: false, top: "15vh", modal: true,
          modalAppendToBody: true, appendToBody: false, lockScroll: true,
          customClass: "", closeOnClickModal: false, closeOnPressEscape: true,
          showClose: true, center: false,
          // 自定义
          class: "formDialog", footerClass: "formDialogFooter",
        }
      }
    },

    formUI: {
      type: Object,
    },

    /**
     * 表单数据对象为资源描述对象
     */
    formModel: {
      type: Object,
    },
  },
  data: function () {
    return {
      // 对话框的按钮
      dialogButtons: {
        '保存': {
          type: "primary",
        },
        '关闭': {
          type: "primary",
        }
      },

      // 控制dialog的弹出和关闭
      showFlag: this.visible,
      // title数据
      dialogTitle: this.dialog.title,
      // form表单增量数据
      modifiedFormData: {
      },
    }
  },
  watch: {
    // 外界数据修改
    visible(val) {
      this.showFlag = val
    },
    // 内部数据修改
    showFlag(val) {
      this.$emit("showChanged", val)
    },
  },
  methods: {
    // 获取增量数据并存储到修改模型中
    __storeModifiedFormModel(obj) {
      // 记录每次修改的增量
      Object.keys(obj).forEach((prop) => {
        if (!this.modifiedFormData[prop]) {
          this.modifiedFormData[prop] = {}
        }
        // 如果formModel原数据不存在则表明为新增
        if (!this.formModel[prop]) {
          this.modifiedFormData[prop].editValue = obj[prop].editValue
        } else {
          if (this.formModel[prop].editValue !== obj[prop].editValue && this.formModel[prop].displayValue !== obj[prop].displayValue) {
            // 赋值
            this.modifiedFormData[prop].editValue = obj[prop].editValue
            this.modifiedFormData[prop].displayValue = obj[prop].displayValue
          } else if (this.formModel[prop].editValue !== obj[prop].editValue && this.formModel[prop].displayValue === obj[prop].displayValue) {
            this.modifiedFormData[prop].editValue = obj[prop].editValue
          } else {
            // 删除属性
            delete this.modifiedFormData[prop]
          }
        }
      })
    },

    // 打开界面
    __open() {
      // 打开前设置界面
      if (this.dialogMode === "create") {
        if (!this.dialogTitle) {
          this.dialogTitle = "新增"
        }
      } else if (this.dialogMode === "update") {
        if (!this.dialogTitle) {
          this.dialogTitle = "修改"
        }
      }
    },

    // 关闭界面
    close() {
      // 清空数据
      this.$refs.simpleForm.reset()
      this.dialogTitle = ""
      this.modifiedFormData = {
        uri: "",
        props: {}
      }
      // 关闭界面
      this.showFlag = false
    },
    // 保存信息
    // 根据dialogMode字段判断如果是create则发出create信号，如果是update则发出update信号
    // 如果mode没有设置，则不发信号
    // 参数为[{prop:xxx,value:xxx}]
    __save() {
      // 判断修改的值跟原值是否一样,如果存在需要将this.modifiedFormData相应的值删除
      let obj = _.cloneDeep(this.modifiedFormData)
      if (Object.keys(obj).length === 0) {
        this.close()
        return
      }
      if (this.dialogMode === "create") {
        /**
         * 对话框保存按钮的新增事件
         *
         * @event create
         * @type {object}
         */
        this.$emit("create", obj)
      } else if (this.dialogMode === "update") {
        /**
         * 对话框保存按钮的更新事件
         *
         * @event update
         * @type {object}
         */
        this.$emit("update", obj)
      } else {
        // 不处理
      }
    }
  },
}
</script>