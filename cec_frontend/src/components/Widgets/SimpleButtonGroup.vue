<template>
  <div>
    <template v-for='group in buttonGroup'>
      <el-button-group class='button-group'>
        <el-button v-for='button in group'
          v-if='button.visible'
          :key='button.uri'
          :size='button.buttonUI.size'
          :type='button.buttonUI.type'
          :plain='button.buttonUI.plain'
          :round='button.buttonUI.round'
          :loading='button.buttonUI.loading'
          :disabled='button.buttonUI.disabled'
          :icon='button.buttonUI.icon'
          :autofocus='button.buttonUI.autofocus'
          :native-type='button.buttonUI.nativeType'
          @click.native='button.click'>
          {{ button.name }}
        </el-button>
      </el-button-group>
    </template>
  </div>
</template>

<script>
export default {
  name: 'SimpleButtonGroup',
  components: {
  },
  props: {
    /**
     *  按钮组
      [
        [ // 分组
          {
            uri:'xxx'          // xxx为按钮唯一标示uri
            click:'',          // click为点击事件
            name:'',           // name为按钮名字
            visible: true      // 是否可视
            buttonUI:{
              // 参见element-ui el-button的属性
            },
          },...
        ],
        ...
      ]
     */
    buttonGroup: {
      type: Array,
    },
  },
  data: function () {
    return {
    }
  },
  methods: {
  },
}
</script>

<style scoped>
.button-group {
  margin: 0px 5px 0px 0px;
}
</style>

