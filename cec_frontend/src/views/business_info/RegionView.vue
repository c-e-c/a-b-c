<template>
  <div>
    <SimpleTable :tableFilters="tableFilters"
      :tableFiltersModel="tableFiltersData"
      :tableInfo="tableInfo"
      :tableHeader="tableHeader"
      :tableInfoModel="tableInfoData"
      @cellClickedEvent="showParamFromChild"></SimpleTable>

  </div>
</template>

<script>
import SimpleTable from "@/components/Widgets/SimpleTable";

const dropdownRegionLevel = [
  {
    text: "省级",
    value: "1"
  },
  {
    text: "地级",
    value: "2"
  },
  {
    text: "县级",
    value: "3"
  },
  {
    text: "乡级",
    value: "4"
  },
  {
    text: "村级",
    value: "5"
  }
]

export default {
  data() {
    return {
      tableFilters: {
        form: {
          inline: true,
        },
        formItems: {
          region_code: {
            label: "区域编号:",
          },
          region_name: {
            label: "区域名称:",
          },
        },
        itemEditors: {
          region_code: {
            placeHolder: "区域编号",
          },
          region_name: {
            placeHolder: "区域名称",
          },
        },
      },

      tableFiltersData: {
        uri: "",
        props: {
          region_code: {
            editorType: "el-input",
            editValue: "",
            comparison: "contains",
          },
          region_name: {
            editorType: "el-input",
            editValue: "",
            comparison: "contains",
          }
        }
      },

      // 表信息
      tableInfo: {
        // elementui-table
        border: true,
        highlightCurrentRow: true,
        size: "medium",
      },
      // 表头列信息
      tableHeader: {
        columns: {
          selection: {
            // 表列需要的列
            align: "center",
            showOverflowTooltip: true,
            type: "selection",
          },
          // pk:{
          //   align: "center",
          //   showOverflowTooltip: true,
          //   label: "序号",
          //   sortable: true,
          //   width: 70,
          // },          
          pk: {
            align: "center",
            showOverflowTooltip: true,
            label: "序号",
            sortable: true,
            type: "index",
            width: 70,
          },
          region_code: {
            align: "center",
            showOverflowTooltip: true,
            label: "区域编号",
            sortable: true,
          },
          region_name: {
            align: "center",
            showOverflowTooltip: true,
            label: "区域名称",
            sortable: true,
          },
          region_level: {
            align: "center",
            showOverflowTooltip: true,
            prop: "region_level",
            label: "区域等级",
            sortable: true,
            //filters: dropdownRegionLevel,
            filterPlacement: "bottom-end",
            filterMethod: this.filteTag,
          }
        },

        itemEditors: {
          region_level: {
            //selectOptions: dropdownRegionLevel,
            selectClearable: true,
            selectPlaceholder: ""
          }
        },
        formItems: {
          region_code: {
            label: "区域编号:",

          },
          region_name: {
            label: "区域名称:",
          },
        },
      },

      tableInfoData: {
        uri: "Region",
        props: {
          selection: {
            visible: true,
          },
          pk: {
            visible: true
          },
          region_code: {
            visible: true,
            editable: true,    ///有问题，应该是isEditing
            editorType: "el-input",
          },
          region_name: {
            visible: true,
            editable: true,
            editorType: "el-input",
          },
          region_level: {
            visible: true,
            editable: true,
            editorType: "el-select",
          },
        }
      }

    }
  },

  components: {
    SimpleTable
  },

  methods: {
    showParamFromChild(row, column, cell, event) {
      // console.log(cell)
      // console.log("fromParentHandleCellClicked2")
    },
    filteTag(value, row) {
      return row.flag === value;
    }
  }
}
</script>
