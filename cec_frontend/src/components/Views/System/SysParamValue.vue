<template>
  <SimpleTreeTable ref='treeTable'
    :treeFilter='treeFilter'
    :tree='tree'
    :treeUI='tree.treeUI'
    :tableFilter='tableFilter'
    :table='table'
    tableAssoProp='param_type' />
</template>

<script>
import utils from '@/mixins/utils'
import SimpleTreeTable from '@/components/Widgets/SimpleTreeTable';

export default {
  name: 'SysParamValue',
  mixins: [utils],
  components: { SimpleTreeTable },
  data() {
    return {
      treeFilter: {
        formUI: {
          labelPosition: 'top',
          size: 'mini',
        },
        items: [
          {
            fieldName: 'name',
            comparison: 'contains',
            formVisible: true,
            editorUI: {
              placeHolder: '名称',
            },
          }, {
            fieldName: 'valid_flag',
            editValue: 'Y',
          },
        ]
      },
      tree: {
        // 自定义属性
        tableName: 'SysParamType',
        rootVisible: true,
        rootName: '系统参数类型',
        displayFieldName: 'name',
        treeUI: {
          defaultExpandAll: true,
        },
        items: [
          { fieldName: 'pk' },
          { fieldName: 'name' },
        ],
      },
      tableFilter: {
        formUI: {
          inline: true,
          inlineMessage: true,
          size: 'mini',
        },
        items: [
          {
            fieldName: 'name',
            comparison: 'contains',
            formVisible: true,
            formItemUI: {
              label: '名称:',
            },
            editorUI: {
              placeHolder: '名称',
            },
          }, {
            fieldName: 'code',
            comparison: 'contains',
            formVisible: true,
            formItemUI: {
              label: '编号:',
            },
            editorUI: {
              placeHolder: '编号',
            },
          },
        ],
      },
      // 表信息
      table: {
        tableName: 'SysParamValue',
        parentFieldName: 'param_type',
        items: [
          {
            fieldName: 'pk',
          }, {
            fieldName: 'name',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '名称',
            },
            formItemUI: {
              rules: [
                { required: true, message: '名称不能为空！' },
                {
                  validator: (rule, value, callback) => {
                    this.$refs.treeTable.validateTableCellUnique(rule, value, callback)
                  },
                  trigger: 'blur',
                },
              ],
            },
          }, {
            fieldName: 'code',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '编号',
            },
            formItemUI: {
              rules: [
                { required: true, message: '编号不能为空！' },
                {
                  validator: (rule, value, callback) => {
                    this.$refs.treeTable.validateTableCellUnique(rule, value, callback)
                  },
                  trigger: 'blur',
                },
              ],
            },
          }, {
            fieldName: 'remark',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '备注',
            },
            editorUI: {
              type: 'textarea',
            },
          }, {
            fieldName: 'sn',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '排序号',
            },
          }, {
            fieldName: 'valid_flag',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '有效标志',
            },
            editorType: 'ElSelect',
            editValue: 'Y',
            selectOptions: [{
              options: [{
                value: 'Y',
                label: '是',
              }, {
                value: 'N',
                label: '否',
              }]
            }],
          },
        ],
      },
    }
  },
}
</script>


