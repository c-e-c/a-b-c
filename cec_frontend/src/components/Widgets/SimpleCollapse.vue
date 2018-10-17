<template>
	<div class="collapse">
		<el-form ref='elForm'
		 :model='formData'
		 label-width="100px">
			<el-collapse v-model="collapse.collapseUI.activeNames"
			 :accordion="collapse.collapseUI.accordion">
				<template v-for='(item, itemIndex) in collapse.items'>
					<el-collapse-item :title="item.collapseItemUI.title"
					 :name="item.collapseItemUI.name">
						<template v-for='(child, childInd) in item.children'>
							<simple-form-item v-if='child.formVisible'
							 :key='childInd'
							 :prop="'props.'+itemIndex+'.'+childInd+'.editValue'"
							 :formItemUI='child.formItemUI'>
								<template v-if="child.customType"
								 :slot="'props.'+itemIndex+'.'+childInd+'.editValue'">
									<slot :name="itemIndex+'.'+childInd"></slot>
								</template>
								<DynamicEditor v-else
								 class="dynamicEditor"
								 :slot="'props.'+itemIndex+'.'+childInd+'.editValue'"
								 :editorUI='child.editorUI'
								 :editorInfo='child'
								 :editorModel='formData.props[itemIndex][childInd]'
								 @modelChanged='(val)=>{__handleFormDataModified(val, childInd)}' />
							</simple-form-item>
						</template>
					</el-collapse-item>
				</template>
			</el-collapse>
		</el-form>
	</div>
</template>

<script>
import * as utils_resource from '@/utils/resource'
import SimpleFormItem from '@/components/Widgets/SimpleFormItem'
import DynamicEditor from '@/components/Widgets/DynamicEditor'

/**
 * 简单的表单
 */
export default {
	name: 'SimpleForm',
	components: { DynamicEditor, SimpleFormItem },
	props: {
		/**
		 * 
			{
				//1、element-ui组件el-collapse的属性
					collapseUI:{					
							activeNames: ["1","2"],  //可选，无默认值，当前激活的面板
							accordion: false,    		 //可选，false，是否手风琴
					}
				// 2、表单内el-form-item表单对象
				items:[
					{ 
						collapseItemUI: {						//element-ui组件el-collapse-Item的属性
								title: "xxx",						//面板标题
								name: "xx",							//唯一标志符
						},
						children:[{	
							formVisible: true,				//form是否可显示，true为显示，不定义和false则不显示	
							customType:"", 						//可选，无默认，为true时，可添加自定义组件。不设定时，默认使用DynamicEditor控件
							formItemUI:{							//可选,参见element-ui组件el-form-items的属性
								label: 'xx',
								rules:[{},],          // 可选，数组中rules的表单验证规则对象，参见element-ui组件el-form-items的rules属性
							}
							editorUI:{								//DynamicEditor控件ui
							},
							}],
					},{
						...
				}],
			}
		 */
		collapse: {
			type: Object,
			required: true,
		},
	},
	data: function () {
		/**
		* formData.props[index][in] 
		* {
		* [[{},{}],[],]
		* }
		*/
		var tempFormData = []
		this.collapse.items.forEach(element => {
			if (element.children) {
				tempFormData.push(utils_resource.generateProperties(element.children))
			}
		})
		return {
			/**
			 * formData为资源描述属性列表props信息，参考资源描述标准。其中每个列表属性需要与form.items的列表一一对应
			 * {[[{},{}],[],]}
			*/
			formData: { props: tempFormData },
		}
	},
	watch: {
	},
	methods: {
		/**
		 * 清除表单数据
		 */
		reset() {
			// 清除数据
			var tempFormData = []
			this.collapse.items.forEach(element => {
				if (element.children) {
					tempFormData.push(utils_resource.generateProperties(element.children))
				}
			})
			//			var tempFormData = utils_resource.generateProperties(this.form.items)
			this.formData = { props: tempFormData }
			// 清除界面
			this.$refs.elForm.resetFields()
		},

		/**
		 * 获取表单数据
		 */
		getFormData() {
			return JSON.parse(JSON.stringify(this.formData.props))
		},

		__handleFormDataModified(val, index) {
			this.formData.props[index] = val
			/**
			 * form表单中得到改变的值.
			 *
			 * @event modelChanged
			 * @type {object}
			 */
			this.$emit('modelChanged', JSON.parse(JSON.stringify(val)))
		}
	},

}
</script>
<style scoped>
.collapse {
  margin: 0 auto;
  width: 75%;
}
.dynamicEditor {
  width: 40%;
}
</style>
