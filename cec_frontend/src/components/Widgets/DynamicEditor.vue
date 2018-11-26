<template>
  <div>
    <template v-if="editorInfo.editorType==='ElSelect'">
      <el-select :class='editorUI.class'
        :style='editorUI.style'
        :multiple='editorUI.multiple'
        :disabled='editorUI.disabled'
        :value-key='editorUI.valueKey'
        v-model='editorData.editValue'
        :size='editorUI.size'
        :clearable='editorUI.clearable'
        :collapse-tags='editorUI.collapseTags'
        :multiple-limit='editorUI.multipleLimit'
        :name='editorUI.name'
        :auto-complete='editorUI.autoComplete'
        :placeholder='editorUI.selectPlaceholder'
        :filterable='editorUI.filterable'
        :allow-create='editorUI.allowCreate'
        :filter-method='editorUI.filterMethod'
        :remote='editorUI.remote'
        :remote-method='editorUI.remoteMethod'
        :loading='editorUI.loading'
        :loading-text='editorUI.loadingText'
        :no-match-text='editorUI.noMatchText'
        :no-data-text='editorUI.noDataText'
        :popper-class='editorUI.popperClass'
        :reserve-keyword='editorUI.reserveKeyword'
        :default-first-option='editorUI.defaultFirstOption'
        :popper-append-to-body='editorUI.popperAppendToBody'
        :automatic-dropdown='editorUI.automaticDropdown'
        @change='change'>
        <el-option-group v-for='group in editorInfo.selectOptions'
          :key='group.label'
          :label='group.label'
          :disabled='group.disabled'>
          <el-option v-for='option in group.options'
            :key='option.value'
            :value='option.value'
            :label='option.label'
            :disabled='option.disabled'>

          </el-option>
        </el-option-group>
      </el-select>
    </template>
    <template v-else>
      <el-input :class="editorUI.class"
        :style='editorUI.style'
        :type='editorUI.type'
        v-model='editorData.editValue'
        :maxlength='editorUI.maxlength'
        :minlength='editorUI.minlength'
        :placeholder='editorUI.placeHolder'
        :clearable='editorUI.clearable?editorUI.clearable:true'
        :disabled='editorUI.disabled'
        :size='editorUI.size'
        :prefixIcon='editorUI.prefixIcon'
        :suffixIcon='editorUI.suffixIcon'
        :rows='editorUI.rows'
        :autosize='editorUI.autosize'
        :autoComplete='editorUI.autoComplete'
        :name='editorUI.name'
        :readonly='editorUI.readonly'
        :max='editorUI.max'
        :min='editorUI.min'
        :step='editorUI.step'
        :resize='editorUI.resize'
        :autofocus='editorUI.autofocus'
        :form='editorUI.form'
        :label='editorUI.label'
        :tabindex='editorUI.tabindex'
        @change='change'>
      </el-input>
    </template>
  </div>
</template>

<script>
import utils from '@/mixins/utils';

export default {
  name: 'DynamicEditor',
  mixins: [utils],
  model: {
    prop: 'editorModel',
    event: 'modelChanged'
  },
  props: {
    /**
     * 控件ui
     * 具体控件属性,例如如果editorType='ElInput'就是el-input的属性
     * 如果是el-select就是el-select的属性
     */
    editorUI: {
      type: Object,
      default: function () { return {} },
    },

    /**
     * 
      {
        // 具体控件属性,例如如果editorType='ElInput'就是el-input的属性
        // 可选 默认为ElInput类型，值为elementui的组件名如ElInput、ElSelect
        editorType: 'ElInput',
        // 可选 设置默认值
        editValue: 'xxx',
        // 可选 如果editorType为ElSelect，则需要按照规则维护
        selectOptions: [
          // 分组
          { 
            label:'xxx',      // 分组的组名
            disabled:false,   // 是否将该分组下所有选项置为禁用
            options: [        // 具体选项
              {
                value:'xxx'     // 选项的值
                label:'xxx',    // 选项的标签，若不设置则默认与 value 相同
                disabled:false, // 是否禁用该选项
              },...
            ]
          },
          ...
        ]

      },
      */
    editorInfo: {
      type: Object,
      default: function () { return {} },
    },

    /**
     * 编辑器的值,为资源描述的属性对象的属性信息，参考资源描述标准
     */
    editorModel: {
      type: Object,
      required: true
    },
  },

  // events
  // modelChanged 编辑器值被改变
  data: function () {
    return {
      editorData: JSON.parse(JSON.stringify(this.editorModel))
    }
  },
  watch: {
    // editorModel: {
    //   handler: function (val) {
    //     this.editorData = JSON.parse(JSON.stringify(val))
    //   },
    //   deep: true,
    // },
    'editorData.editValue': function (val) {
      if (this.editorInfo.editorType === 'ElSelect') {
        this.editorData.displayValue = this._getValueFromDropdownGroup(this.editorInfo, val)
      } else {
        this.editorData.displayValue = val
      }
      /**
       * form表单中得到改变的值.
       *
       * @event modelChanged
       * @type {object}
       */
      this.$emit('modelChanged', JSON.parse(JSON.stringify(this.editorData)))
    },
  },
  methods: {
    change(value) {
      //   if (this.editorInfo.editorType === 'ElSelect') {
      //     this.editorData.displayValue = this._getValueFromDropdownGroup(this.editorInfo, this.editorData.editValue)
      //   } else {
      //     this.editorData.displayValue = this.editorData.editValue
      //   }
      //   /**
      //    * form表单中得到改变的值.
      //    *
      //    * @event modelChanged
      //    * @type {object}
      //    */
      //   this.$emit('modelChanged', JSON.parse(JSON.stringify(this.editorData)))
    },
  },

}
</script>
<style scoped>
/* .dynamiceditor {
  width: 200px;
} */
</style>