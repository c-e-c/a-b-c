<template>
	<div>
		<el-button @click="handleClick()"
		 type="primary">保存</el-button>
		<el-button @click="handleClick()"
		 size="small">返回</el-button>

		<SimpleForm :form='form'>
			<!-- <template v-for='(item, index) in collapse.items'>
        <template v-for='(child, ind) in item.children'>
          <el-transfer v-if="child.customType"
            :slot="child.customUI.componentName"
            v-model="child.customUI.value1"
            :data="child.customUI.data"></el-transfer>
        </template>
      </template> -->
		</SimpleForm>
	</div>
</template>

<script>
//import utils from '@/mixins/utils'
import SimpleForm from '@/components/Widgets/SimpleForm'
import SimpleCollapse from '@/components/Widgets/SimpleCollapse'

export default {
	name: 'AccountDetail',
	//mixins: [utils],
	components: { SimpleForm, SimpleCollapse },
	props: {
		collapse: {
			type: Object,
			required: true,
		},
	},
	data() {
		return {
			/**
			 *测试数据 
			 *  */
			form: {
				divType: true,
				items: [
					{
						titleName: "账号信息",
						children: [
							{
								fieldName: 'user__username',
								titleName: "账号信息",
								formVisible: true,
								formItemUI: {
									label: '账号:',
								},
								editorUI: {
									placeHolder: '账号',
								},
							}, {//account_type
								fieldName: 'account_type',
								formVisible: true,
								editable: true,
								formItemUI: {
									label: '账号类型',
								},
								editorUI: {
									placeHolder: '账号类型',
								},
							},
						]
					}, {
						titleName: "用户信息",
						children: [
							{//party
								fieldName: 'party',
								formVisible: true,
								editable: true,
								formItemUI: {
									label: '当事人ID',
								},
							}, {//head_img
								fieldName: 'head_img',
								formVisible: true,
								editable: true,
								formItemUI: {
									label: '头像',
								},
							},
						]
					},
				]
			}

		}
	},
	methods: {
		handleClick() {
			/**
			 * 表保存后
			 * @event detailReturn
				*/
			this.$emit('detailReturn')
		},
	},
}
</script>
<style scoped>
.el-form_header {
  height: 48px;
  line-height: 48px;
  background-color: #fff;
  color: #303133;
  cursor: pointer;
  border-bottom: 1px solid #abb2c7;
  outline: none;
}
.form {
  margin: 0 auto;
  width: 800px;
}
.input {
  width: 400px;
  padding: 0px;
}
.transfer {
  padding: 24px;
}
</style>

