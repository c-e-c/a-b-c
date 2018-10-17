<template>
	<div>
		<el-button @click="handleClick()"
		 type="primary">保存</el-button>
		<el-button @click="handleClick()"
		 size="small">返回</el-button>
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

