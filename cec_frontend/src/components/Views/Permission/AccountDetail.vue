<template>
	<div>
		<el-button @click="handleClick()"
		 type="primary">保存</el-button>
		<el-button @click="handleClick()"
		 size="small">返回</el-button>
		<!-- <SimpleForm :formUI='formUI'
		 :form='form' /> -->
		<!-- <el-form :model="form1"
		 label-position="top"
		 class="form">
			<el-collapse v-model="activeNames"
			 @change="handleChange">
				<el-collapse-item title="一致性 Consistency"
				 name="1">
					<div class="el-form_header">
						账号信息
					</div>
					<el-form-item label="账号">
						<el-input class="input"></el-input>
					</el-form-item>
					<el-form-item label="账号类型">
						<el-input v-model="form1.account_type"
						 class="input"></el-input>
					</el-form-item>
				</el-collapse-item>
				<el-collapse-item title="Consistency"
				 name="2">
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
				</el-collapse-item>
				<div>
					<div class="el-form_header">
						权限
					</div>
					<el-form-item label="">
						<el-transfer v-model="value1"
						 class="transfer"
						 :button-texts="['到左边', '到右边']"
						 :titles="['用户组', 'Target']"
						 :data="data1"></el-transfer>
						<el-transfer class="transfer"
						 v-model="value2"
						 :button-texts="['到左边', '到右边']"
						 :titles="['菜单', 'Target']"
						 :data="data2"></el-transfer>
					</el-form-item>
				</div>
			</el-collapse>
		</el-form> -->
		<SimpleCollapse :formUI='formUI'
		 :collapse='collapse'>
			<template v-for='(item, index) in collapse.items'>
				<template v-for='(it, ind) in item.children'>
					<el-transfer :slot="index+'.'+ind"
					 v-model="it.value1"
					 :data="it.data"></el-transfer>
				</template>
			</template>
		</SimpleCollapse>
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
		formUI: {
			type: Object,
			default: function () { return {} },
		},
		collapse: {
			type: Object,
			required: true,
		},
	},
	data() {
		return {
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

