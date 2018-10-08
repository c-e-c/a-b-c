<template>
  <el-row class="content">
    <el-col class="leftBox">
      <el-container style="height: 90%; border: 1px solid #eee">
         <el-aside width="200px" style="height: 50%">              
            <el-input placeholder="输入关键字进行过滤" v-model="filterText">
            </el-input>
            <el-tree :load="loadNode" lazy node-key="id" accordion class="filter-tree" :data="data2" :props="defaultProps" :default-expanded-keys="[-1]" :filter-node-method="filterNode" ref="tree2" v-loading="treeInfo.isLoading" :element-loading-text="treeInfo.loadingText">
            </el-tree>               
         </el-aside>
      </el-container>
    </el-col>
    <el-col class="middleBox">
           地方的广东省告诉对方贵定师范贵定师范广东佛山
      <el-input placeholder="输入关键字进行过滤" v-model="filterText"></el-input>
    </el-col>
  </el-row>
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
    loadNode(node, resolve) {
      if (node.level === 0) {
        return resolve([{ id: -1, label: "车属单位" }]);
      }
      setTimeout(() => {
        if (node.level === 1) {
          this.filterConditions.upper_dept_id = "null";
        } else {
          this.filterConditions.upper_dept_id = node.data.id;
        }

        var conditions = JSON.parse(JSON.stringify(this.filterConditions));
         
        getTreeList(conditions)
          .then(responseData => {
            // 遍历表列，赋值表数
            let dataList = [];
            responseData.forEach(record => {
              dataList.push({ id: record.dept_id, label: record.dept_name });
            });
            resolve(dataList);
          })
          .catch(function(error) {
            this.$message(error);
          });
      }, 200);
    },
    filterNode(value, data) {
      if (!value) return true;
      return data.label.indexOf(value) !== -1;
    }
    // fetchData() {
    //   // 过滤未输入的查询条件
    //   var conditions = JSON.parse(JSON.stringify(this.filterConditions));
    //   getTreeList(conditions)
    //     .then(responseData => {
    //       // 遍历表列，赋值表数
    //       var dataList = [];
    //       responseData.forEach(record => {
    //         dataList.push({ id: record.dept_id, label: record.dept_name });
    //       });
    //       return dataList;
    //     })
    //     .catch(function(error) {
    //       this.$message(error);
    //     });
    // }
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
        dept_id: "",
        upper_dept_id: ""
      },
      treeData: []
    };
  },
  created() {}
};
</script>
<style>
.content {
 height: 100%;
}
 .leftBox {
  float: left;
  width: 200px;
  height: 100%;
  margin: 5px;
  background: #ffffff;
  display: inline;
}
.middleBox {
  float: left;
  width: 50%;
  height: auto;
  margin: 5px;
  background: #b1fffc;
  display: inline;

}

/* @media only screen and (min-width: 1024px) {
  .content {
    width: 1000px;
    margin: auto;
  }
} */
/* @media only screen and (min-width: 400px) and (max-width: 1024px) {
 .leftBox {
    width: 30%;
  }
  .middleBox {
    width: 65%;
  } 
} */
/*
@media only screen and (max-width: 400px) {
  .leftBox,
  .middleBox {
    width: 98%;
    height: 200px;
  }
} */
</style>


