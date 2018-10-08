<template>
  <el-table-column :type='columnUI.type'
    :index='columnUI.index'
    :column-key='columnKey'
    :label='columnUI.label'
    :prop='prop'
    :width='columnUI.width'
    :min-width='columnUI.minWidth'
    :fixed='columnUI.fixed'
    :render-header='columnUI.renderHeader'
    :sortable='columnUI.sortable ? columnUI.sortable : true'
    :sort-method='columnUI.sortMethod'
    :resizable='columnUI.resizable'
    :formatter='columnUI.formatter'
    :show-overflow-tooltip='columnUI.showOverflowTooltip ? columnUI.showOverflowTooltip : true'
    :align="columnUI.align ? columnUI.align : 'center'"
    :header-align='columnUI.headerAlign'
    :class-name='columnUI.className'
    :label-class-name='columnUI.labelClassName'
    :selectable='columnUI.selectable'
    :reserve-selection='columnUI.reserveSelection'
    :filters='columnUI.filters'
    :filter-placement='columnUI.filterPlacement'
    :filter-method='columnUI.filterMethod'
    :filtered-value='columnUI.filteredValue'>

    <template slot-scope='{ row, column, $index }'>
      <slot :name='prop'
        :row='row'
        :column='column'
        :$index='$index'></slot>
    </template>

  </el-table-column>
</template>
<script>
export default {
  name: 'SimpleTableColumn',
  props: {
    /**
     * table-column的column-key
     * 参见element-ui组件el-table-column的属性
     */
    columnKey: {
      type: String,
      default: '',
    },
    /**
     * table-column的prop
     * 参见element-ui组件el-table-column的属性
     */
    prop: {
      type: String,
      required: true,
    },
    /**
     * table-column ui
     * 参见element-ui组件el-table-column的属性
     */
    columnUI: {
      type: Object,
      default: function () { return {} },
    },
  },
}
</script>