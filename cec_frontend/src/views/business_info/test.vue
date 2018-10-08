<template>
<SimpleTree :treeInfo="treeInfo" :treeInfoModel="treeInfoData" :treeHeader="treeHeader" 
    prop="region_name"  :isLazy="false"  :isExistRoot="true" :treeFiltersModel="treeFiltersData"
></SimpleTree>
</template>

<script>
import SimpleTree from "@/components/Widgets/SimpleTree";
export default {
  components: {
    SimpleTree
  },
  data() {
    return {
      treeInfo: {
        emptyText: "内容为空",
        nodekey: "id",
        highlightCurrent: true,
        defaultExpandAll: false,
        expandOnClickNode: true,
        autoExpandParent: false,
        showCheckbox: true,
        checkStrictly: false,
        accordion: true,
      },
      treeInfoData: {
        uri: "Region"
      },
      treeHeader: {
        columns: {
          // 表列需要的列
          parent: {
            align: "center",
            showOverflowTooltip: true,
            label: "区域编号",
            sortable: true
          },
          pk: {
            align: "center",
            showOverflowTooltip: true,
            label: "序号",
            sortable: true,
            type: "index",
            width: 70
          },
          region_code: {
            align: "center",
            showOverflowTooltip: true,
            label: "区域编号",
            sortable: true
          },
          region_name: {
            align: "center",
            showOverflowTooltip: true,
            label: "区域名称",
            sortable: true
          }
        }
      },
      treeFiltersData: {
        props: {
          region_name: {
            editValue: "",
            comparison: "contains",
          }
        }
      }
    }
  }
};
</script>
<style>
.container {
  text-align: center;
  margin: 10px auto;
  width: 750px;
}
.container > div {
  border: 1px solid rgba(0, 0, 0, 0.3);
  text-align: left;
  /*设置 HTML 组件的 width 属性包括边框*/
  box-sizing: border-box;
  background-color: #96ff6b;
  padding: 5px;
}
div .left {
  width: 300px;
  height: 230px;
  float: left;
}
div .main {
  width: 450px;
  height: 230px;
  float: left;
  /*这里不采用 clearfix 的用法了,直接 clear */
  clear: right;
}
div .right {
  width: 750px;
  float: left;
}

@media screen and (min-width: 1000px) {
  .container {
    text-align: center;
    margin: 10px auto;
    width: 960px;
  }
  .container > div {
    border: 1px solid rgba(0, 0, 0, 0.3);
    /*设置 HTML 组件的 width 属性包括边框*/
    box-sizing: border-box;
    background-color: #96ff6b;
    padding: 5px;
  }
  div .left {
    width: 240px;
    height: 240px;
    float: left;
  }
  div .main {
    width: 460px;
    height: 240px;
    float: left;
  }
  div .right {
    width: 260px;
    height: 240px;
    float: left;
  }
}
@media screen and (min-width: 180px) and (max-width: 500px) {
  .container {
    text-align: center;
    margin: 10px auto;
    width: 450px;
  }
  .container > div {
    border: 1px solid rgba(0, 0, 0, 0.3);
    /*设置 HTML 组件的 width 属性包括边框*/
    box-sizing: border-box;
    background-color: #96ff6b;
    padding: 5px;
  }
  div .left {
    width: 450px;
    height: 240px;
    float: left;
  }
  div .main {
    width: 450px;
    height: 240px;
    float: left;
  }
  div .right {
    width: 450px;
    height: 240px;
    float: left;
  }
}
</style>

