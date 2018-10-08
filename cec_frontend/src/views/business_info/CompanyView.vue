<template>
    <div class="app-container">
        <el-row :gutter="10" type="flex">
            <el-col :span='6'>
                <div>
                    <el-input placeholder="输入关键字进行过滤" v-model="filterText">
                    </el-input>
                    <!-- <el-tree :id='elTree' node-key="id" accordion class="filter-tree" :data="data2" :props="defaultProps" :default-expanded-keys="[-1]" :filter-node-method="filterNode" ref="tree2" v-loading="treeInfo.isLoading" :element-loading-text="treeInfo.loadingText"> -->
                    <el-tree :id='treeInfo.id' node-key="id" accordion class="filter-tree" :data="data2" :props="defaultProps" :default-expanded-keys="[-1]" :filter-node-method="filterNode" ref="tree2" v-loading="treeInfo.isLoading" :element-loading-text="treeInfo.loadingText">

                    </el-tree>
                </div>
            </el-col>
  
        </el-row>
    </div>
</template>

<script>
import { getTreeList } from "@/api/tree";
import { Message, Input, Checkbox, Select } from "element-ui";
//import { on, off } from "wind-dom/src/event";
import emitter from "../../mixins/emitter";
import Vue from "vue";
export default {
  watch: {
    filterText(val) {
      this.$refs.tree2.filter(val);
    }
  },

  methods: {
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    },
    fetchData() {
      this.treeInfo.isLoading = true;
      // 过滤未输入的查询条件
      var conditions = JSON.parse(JSON.stringify(this.filterConditions));
      getTreeList(conditions)
        .then(responseData => {
          // 遍历表列，赋值表数
          let dataList = [];
          var father = new Array();
          var arr = {};
          responseData.forEach(record => {
            if (record.upper_dept_id != null) {
              if (arr[record.upper_dept_id + ""]) {
                arr[record.upper_dept_id + ""].push({
                  id: record.dept_id,
                  label: record.dept_name
                });
              } else {
                arr[record.upper_dept_id + ""] = [
                  { id: record.dept_id, label: record.dept_name }
                ];
              }
            } else {
              dataList.push({ id: record.dept_id, label: record.dept_name });
            }
          });
          for (var i = 0; i < dataList.length; i++) {
            dataList[i].children = this.makeChildrenTreen(
              dataList[i].id + "",
              arr
            );
          }
          this.data2 = [{ id: -1, label: "车属单位", children: dataList }];
          this.treeInfo.isLoading = false;
        })
        .catch(function(error) {
          this.$message(error);
        });
    },
    makeChildrenTreen(fatherId, arrLst) {
      if (arrLst[fatherId]) {
        for (var i = 0; i < arrLst[fatherId].length; i++) {
          arrLst[fatherId][i].children = this.makeChildrenTreen(
            arrLst[fatherId][i].id + "",
            arrLst
          );
        }
        return arrLst[fatherId];
      } else {
        return [];
      }
    }
  },

  data() {
    return {
      treeInfo: {
        id: "RsDept",
        fatherIdCol: "upper_dept_id",
        idCol: "dept_id",
        labelCol: "dept_name",
        isLoading: false,
        loadingText: "加载中"
      },
      filterText: "",
      data2: [],
      defaultProps: {
        children: "children",
        label: "label"
      },
      filterConditions: {
        dept_name: "",
        dept_id: ""
      }
    };
  },
  created() {
    this.fetchData();
  }
};
</script>
