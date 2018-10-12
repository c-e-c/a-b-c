<template>
	<div class="form">
		<el-button @click="handleClick()"
		 type="primary">保存</el-button>
		<el-button @click="handleClick()"
		 size="small">返回</el-button>
		<!-- <SimpleForm :formUI='formUI'
		 :form='form' /> -->
		<div class="el-form_header">
			账号信息
		</div>
		<el-form :model="form1"
		 label-position="top"
		 class="form">
			<el-form-item label="账号">
				<el-input v-model="form1.user__username"
				 class="input"></el-input>
			</el-form-item>
			<el-form-item label="账号类型">
				<el-input v-model="form1.account_type"
				 class="input"></el-input>
			</el-form-item>
			<div class="el-form_header">
				用户信息
			</div>
			<el-form-item label="当事人ID">
				<el-input v-model="form1.party"
				 class="input"></el-input>
			</el-form-item>
			<el-form-item label="姓名">
				<el-input v-model="form1.head_img"
				 class="input"></el-input>
			</el-form-item>
		</el-form>
		<div class="el-form_header">
			权限
		</div>
		<div>
			<el-transfer v-model="value1"
			 class="transfer"
			 :button-texts="['到左边', '到右边']"
			 :titles="['用户组', 'Target']"
			 :data="data1"></el-transfer>
		</div>
		<el-transfer class="transfer"
		 v-model="value2"
		 :button-texts="['到左边', '到右边']"
		 :titles="['菜单', 'Target']"
		 :data="data2"></el-transfer>

	</div>
</template>

<script>
//import utils from '@/mixins/utils'
import SimpleForm from '@/components/Widgets/SimpleForm'

export default {
	name: 'AccountDetail',
	//mixins: [utils],
	components: { SimpleForm },
	props: {
		formUI: {
			type: Object,
			default: function () { return {} },
		},
		form: {
			type: Object,
			required: true,
		},
	},
	data() {
		return {
			data1: [
				{
					key: 1,
					label: `运营方`,
				}, {
					key: 2,
					label: `买方`,
				}, {
					key: 3,
					label: `卖方`,
				}, {
					key: 4,
					label: `鉴定机构`,
				}
			],
			data2: [
				{
					key: 1,
					label: `艺术品列表`,
				}, {
					key: 2,
					label: `艺术品发布`,
				}, {
					key: 3,
					label: `鉴定审核`,
				}, {
					key: 4,
					label: `订单列表`,
				}
			],
			value1: [1],
			value2: [],
			labelPosition: 'top',
			form1: {
				user__username: '',
				account_type: '',
				party: '',
				head_img: ''
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

