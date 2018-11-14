<template>
  <div class='simpletable'>
    <!-- 工具栏按钮 -->
    <SimpleButtonGroup ref='simpleButtonGroup'
      class='simplebuttongroup'
      :buttonGroup='buttonGroupData' />
    <!-- 查询条件 -->
    <SimpleForm v-if='tableFilterVisible'
      ref='simpleFilter'
      class='simplefilter'
      :formUI='tableFilter.formUI'
      :form='tableFilter' />
    <!-- 表 -->
    <el-form ref='elForm'
      :model='tableData'
      inlineMessage>
      <el-table ref='elTable'
        :height='tableUI.height'
        :maxHeight='tableUI.maxHeight'
        :stripe='tableUI.stripe'
        :border='tableUI.border?tableUI.border:true'
        :size='tableUI.size'
        :max-length='tableUI.maxLength'
        :fit='tableUI.fit'
        :show-header='tableUI.showHeader'
        :highlight-current-row='tableUI.highlightCurrentRow'
        :current-row-key='tableUI.currentRowKey'
        :row-class-name='tableUI.rowClassName ? tableUI.rowClassName : __tableRowClassName'
        :row-style='tableUI.rowStyle'
        :cell-class-name='tableUI.cellClassName'
        :cell-style='tableUI.cellStyle'
        :header-row-class-name='tableUI.headerRowClassName'
        :header-row-style='tableUI.headerRowStyle'
        :header-cell-class-name='tableUI.headerCellClassName'
        :header-cell-style='tableUI.headerCellStyle'
        :row-key='tableUI.rowKey'
        :empty-text='tableUI.emptyText'
        :default-expand-all='tableUI.defaultExpandAll'
        :expand-row-keys='tableUI.expandRowKeys'
        :default-sort='tableUI.defaultSort'
        :tooltip-effect='tableUI.tooltipEffect'
        :show-summary='tableUI.showSummary'
        :sum-text='tableUI.sumText'
        :summary-method='tableUI.summaryMethod'
        :span-method='tableUI.spanMethod'
        :data='tableData.rows'
        @selection-change='__handleTableSelectionChanged'>
        <!-- <el-table-column type='expand' fixed>
          <template slot-scope='props'>
            <el-form-item>
            </el-form-item>
          </template>
        </el-table-column> -->
        <el-table-column type='index'
          fixed
          width='42px'
          align='center'>
          <el-form-item>
          </el-form-item>
        </el-table-column>
        <el-table-column type='selection'
          fixed
          align='center'>
          <el-form-item>
          </el-form-item>
        </el-table-column>
        <template v-for='(item, index) in table.items'>
          <simple-table-column v-if='item.columnVisible'
            :key='index'
            :column='item'
            :columnUI='item.columnUI'>
          </simple-table-column>
        </template>
        <el-table-column v-if='table.hasOperatingColumn'
          fixed='right'
          label='操作'
          align='center'>
          <template slot-scope='{ row, column, $index }'>
            <el-form-item size='mini'>
              <slot name='operating_column'
                :row='row'
                :column='column'
                :$index='$index'></slot>
            </el-form-item>
          </template>
        </el-table-column>

      </el-table>
    </el-form>
    <!-- 传入elementui的page-total属性不起作用 -->
    <SimplePagination ref='simplePagination'
      class='simplepagination'
      :changePageSize='__handlePaginationSizeChanged'
      :changeCurrentPage='__handlePaginationCurrentChanged'>
    </SimplePagination>
  </div>
</template>

<script>
import * as api_gda from '@/api/gda'
import * as utils_resource from '@/utils/resource'
import * as utils_ui from '@/utils/ui'
import utils from '@/mixins/utils'
import SimpleButtonGroup from '@/components/Widgets/SimpleButtonGroup'
import SimpleTableColumn from '@/components/Widgets/SimpleTableColumn'
import SimpleForm from '@/components/Widgets/SimpleForm'
import SimplePagination from '@/components/Widgets/SimplePagination'
// import DynamicEditor from '@/components/Widgets/DynamicEditor'

export default {
  name: 'SimpleTable',
  components: {
    SimpleButtonGroup,
    SimpleTableColumn,
    SimpleForm,
    SimplePagination,
    // DynamicEditor,
  },
  mixins: [utils],
  props: {
    /**
     * 是否显示表过滤信息
     */
    tableFilterVisible: {
      type: Boolean,
      default: true,
    },
    /**
     * 表过滤条件信息，参见SimpleForm的form属性
     */
    tableFilter: {
      type: Object,
      default: function () { return {} },
    },
    /**
     * 表ui
     * 参见element-ui组件el-table的属性
     */
    tableUI: {
      type: Object,
      default: function () { return {} },
    },

    /**
     * 表信息
      {
        // 1、自定义部分
        tableName: 'xxx',         // 必须，业务表名信息，xxx为业务表名
        parentFieldName: 'xxx'    // 可选，节点的父属性， xxx为列属性
        hasOperatingColumn: false // 可选，不包含，默认为false
        // 2、表列
        items:[                   // 必须
          {
            // 1、表列ui
            columnUI: {           // 必须
              // 参见element-ui组件el-table-column的属性
            },

            // 2、自定义部分
            fieldName: 'xxx',     // 可选，属性的属性名，xxx未业务表字段
            editable: false,      // 可选，列是否可编辑，默认为false不可编辑
            columnVisible:false,  // 可选，列可显示，默认未false不可视
            rules:[{},],          // 可选，数组中rules的表单验证规则对象，参见element-ui组件el-form-items的rules属性

            // 3、单元格控件对象     // 可选
            DynamicEditor控件的editorInfo的多个属性内容，参见DynamicEditor.editorInfo

            // 4、可选 item的孩子,数组中为多个子item对象，当有hasChildren为true时，DynamicEditor属性无效
            hasChildren: false, 
            children:[{},],
            // columnKey此字段SimpleTable初始化时自动生成
            // columnKey: 'xxx', 
          },{
            ...
        }],
      }
     */
    table: {
      type: Object,
      required: true,
    },
    /**
     * 已有按钮组，包含search,add,remove,save,pass,reject,print,import,export
      [
        {
          uri: 'search',
          name: '查询',
          click: this.__handleSearchButtonClicked,
          visible: true,
          buttonUI: {
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-search'
          },
          ...
        }
      ]
     */
    defaultButtonGroup: {
      type: Array,
      default: function () { return [] },
    },
  },
  data: function () {
    var tempButtonGroup = [
      [
        {
          uri: 'search',
          name: '查询',
          click: this.__handleSearchButtonClicked,
          visible: true,
          buttonUI: {
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-search',
          },
        },
      ], [
        {
          uri: 'add',
          name: '增加',
          click: this.__handleAddButtonClicked,
          visible: true,
          buttonUI: {
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-circle-plus-outline',
          }
        }, {
          uri: 'modify',
          name: '修改',
          click: this.__handleModifyButtonClicked,
          visible: true,
          buttonUI: {
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-document',
          }
        }, {
          uri: 'remove',
          name: '删除',
          click: this.__handleDeleteButtonClicked,
          visible: true,
          buttonUI: {
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-remove-outline',
          }
        }, {
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
          uri: 'pass',
          name: '通过',
          visible: true,
          buttonUI: {
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-circle-check-outline',
          }
        }, {
          uri: 'reject',
          name: '驳回',
          visible: true,
          buttonUI: {
            type: 'primary',
            size: 'mini',
            icon: 'el-icon-circle-close-outline',
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
    // 设置已有按钮组数据
    this.defaultButtonGroup.forEach(button => {
      var tempButton = null
      tempButton = this.__findButtonGroup(tempButtonGroup, button.uri)
      if (tempButton) {
        Object.keys(button).forEach(prop => {
          tempButton[prop] = button[prop]
        })
      }
    })

    return {
      // 按钮组
      buttonGroupData: tempButtonGroup,

      // 表数据
      tableData: {
        rows: [],// 资源描述序列
      },
    }
  },
  created() {
    this.__setTableColumnsLeafItems(this.table.items)
  },
  mounted() {
    // 计算elTable的高度
    this.$nextTick(() => {
      window.addEventListener('resize', this.__handleResize)
    })
    this.__handleResize()
  },

  methods: {
    /**
     * 得到过滤器数据
     */
    getFormData() {
      return this.$refs.simpleFilter.getFormData()
    },
    /**
     * 查询过滤条件的数据，offset默认从第0页分页
     */
    fetchData(filters, offset) {
      api_gda.listData(this.table.tableName,
        this._getLeafColumns(this.table.items),
        filters,
        this.$refs.simplePagination.getPageSize(),
        offset
      ).then((responseData) => {
        if (responseData.results) {
          // 生成分页数据
          this.tableData.rows = utils_resource.setResources(responseData.results, this._getLeafColumns(this.table.items),
            this.table.parentUri)
        } else {
          // 生成不分页数据
          this.tableData.rows = utils_resource.setResources(responseData, this._getLeafColumns(this.table.items),
            this.table.parentUri)
        }
        // 设置显示角色
        this._setResourcesDisplayValue(this.tableData.rows, this._getLeafColumns(this.table.items))
        // 设置分页
        this.$refs.simplePagination.setPageTotal(responseData.count)

      }).catch((error) => {
        // 设置界面
        utils_ui.showErrorMessage(error)
      })
    },
    /**
     * 插入一条记录
     */
    insertData(parentUri) {
      // 生成资源
      let rd = utils_resource.generateResource(this._getLeafColumns(this.table.items))
      // 初始化设置资源属性
      utils_resource.setResourceProperties(rd, this._getLeafColumns(this.table.items))
      // 设置资源的父
      utils_resource.setResourceParent(rd, parentUri)
      // 设置显示角色
      this._setResourceDisplayValue(rd, this._getLeafColumns(this.table.items))
      // 设置单元格正在编辑状态
      utils_resource.setResourceEditingState(rd, true)

      // 插入一条资源
      utils_resource.addResource(this.tableData.rows, rd)
    },
    /**
     * 校验单元格的唯一性 
     */
    validateUnique(rule, value, callback) {
      // 表
      var type = this.table.tableName
      var rowIndex = rule.field.split('.')[1]   // rows.x.props.y.editValue
      var fieldIndex = rule.field.split('.')[3]  // rows.x.props.y.editValue
      // 查看当前资源行的差异状态，如果为修改和删除，则不判断唯一性
      var state = utils_resource.getResourceDifferenceState(this.tableData.rows[rowIndex])
      if (state === 'ROW_ADDED') {
        this._validateUnique(rule, value, callback,
          this.table.tableName,
          this.tableData.rows[rowIndex].props[fieldIndex].fieldName)
      } else {
        callback()
      }
    },
    // 点击查询按钮
    __handleSearchButtonClicked() {
      let offset = (this.$refs.simplePagination.getCurrentPage() - 1) * this.$refs.simplePagination.getPageSize()
      this.fetchData(this.$refs.simpleFilter.getFormData(), offset)
    },
    // 处理分页SizeChange事件
    __handlePaginationSizeChanged(size) {
      this.$refs.simplePagination.setPageSize(size)
      this.fetchData(this.$refs.simpleFilter.getFormData(), 0)
    },
    // 处理分页CurrentChange事件
    __handlePaginationCurrentChanged(currentPage) {
      let offset = (currentPage - 1) * this.$refs.simplePagination.getPageSize()
      this.fetchData(this.$refs.simpleFilter.getFormData(), offset)
    },
    // 点击增加按钮
    __handleAddButtonClicked() {
      this.insertData()
    },
    // 表单元格数据变更事件
    __handleTableCellModified(rd, index, prop) {
      utils_resource.modifyResource(rd, index, prop)
    },
    // 表行的选择列被改变事件
    __handleTableSelectionChanged(selection) {
      utils_resource.setResourcesSelectedState(this.tableData.rows, selection)
    },
    // 点击修改按钮
    __handleModifyButtonClicked() {
      utils_resource.setResourcesEditingState(this.tableData.rows, true)
    },
    // 点击删除按钮
    __handleDeleteButtonClicked() {
      if (!utils_resource.hasResourcesSelected(this.tableData.rows)) {
        this.$message({ message: '请选择要删除的记录', type: 'warning' })
        return
      }
      this.$confirm('确认要删除已选的记录吗?', '提示', { type: 'warning' }
      ).then(() => {
        utils_resource.removeResources(this.tableData.rows)
      }).catch(() => {
        this.$message({ message: '取消删除', type: 'info' })
      })
    },
    // 点击保存按钮
    __handleSaveButtonClicked() {
      // 校验form
      this.$refs.elForm.validate((valid, obj) => {
        if (valid) {
          // 调用接口
          var diffModel = utils_resource.getDifferenceModel(this.tableData)
          if (!diffModel) {
            // 设置资源的编辑状态
            utils_resource.setResourcesEditingState(this.tableData.rows, false)
            return
          }
          api_gda.saveData(this.table.tableName, diffModel).then((responseData) => {
            utils_resource.saveResources(this.tableData.rows, responseData)
            // 设置显示角色
            this._setResourcesDisplayValue(this.tableData.rows, this._getLeafColumns(this.table.items))
            // 设置资源的编辑状态
            utils_resource.setResourcesEditingState(this.tableData.rows, false)
            this.$message({ message: '保存成功', type: 'success' })
            /**
             * 表保存后
             * @event tableSave
             */
            this.$emit('tableSave')
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
    __findButtonGroup(buttonGroup, uri) {
      var tempButton = null
      for (var i = 0; i < buttonGroup.length; i++) {
        tempButton = buttonGroup[i].find(element => { return element.uri === uri })
        if (tempButton) {
          break
        }
      }
      return tempButton
    },
    __handleResize() {
      if (this.$refs.elForm) {
        let simpleButtonGroupOffsetHeight = this.$refs.simpleButtonGroup ? this.$refs.simpleButtonGroup.$el.offsetHeight : '0'
        let simpleFilterOffsetHeight = this.$refs.simpleFilter ? this.$refs.simpleFilter.$el.offsetHeight : '0'
        let simplePaginationOffsetHeight = this.$refs.simplePagination ? this.$refs.simplePagination.$el.offsetHeight : '0'

        let dynamicHeight = 'calc(100%' +
          ' - ' + simpleButtonGroupOffsetHeight + 'px' +
          ' - ' + simpleFilterOffsetHeight + 'px' +
          ' - ' + simplePaginationOffsetHeight + 'px' +
          ')'
        this.$refs.elForm.$el.style.height = dynamicHeight
      }

      this.tableUI.height = '100%'
      // this.$refs.elTable.$el.style.height = dynamicHeight
      // this.tableUI.height = dynamicHeight
    },
    __tableRowClassName({ row, rowIndex }) {
      var state = utils_resource.getResourceDifferenceState(row)
      if (state === 'ROW_ADDED') {
        return 'globle-inserted-row'
      } else if (state === 'ROW_REMOVED') {
        return 'globle-removed-row'
      } else if (state === 'ROW_MODIFIED') {
        return 'globle-modified-row'
      } else {
        return ''
      }
    },
    __setTableColumnsLeafItems(items) {
      var leaf = { index: 0 }
      this.__setLeafItems(items, leaf)
    },
    __setLeafItems(items, leaf) {
      if (!items || !leaf || leaf.index < 0) {
        return
      }
      items.forEach(element => {
        if (element.hasChildren) {
          this.__setLeafItems(element.children, leaf)
        } else {
          element.columnKey = leaf.index.toString()
          leaf.index += 1
        }
      })
    },
  },
}
</script>

<style scoped>
.simpletable {
  height: 100%;
}
.simplebuttongroup {
  padding: 5px 10px 5px 10px;
}
.simplefilter {
  padding: 5px 10px 5px 10px;
}
.simplepagination {
  padding: 5px 10px 5px 10px;
}
</style>
