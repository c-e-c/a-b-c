<template>
	<div>
		<el-button @click="handleClick()"
		    type="text"
		    size="mini">返回</el-button>
		<SimpleForm :formUI='formUI'
		    :form='form' />
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

