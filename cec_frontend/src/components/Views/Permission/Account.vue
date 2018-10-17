<template>
  <div>
    <SimpleTable v-if='isList'
      ref='simpleTable'
      :tableFilter='tableFilter'
      :table='table'>
      <template slot='operating_column'
        slot-scope='{ row, column, $index }'>
        <el-button @click="handleClick(row)"
          type='text'
          size="mini">查看</el-button>
      </template>
    </SimpleTable>
    <AccountDetail v-else
      :collapse='collapse'
      @detailReturn='()=>isList=true'>
    </AccountDetail>
  </div>
</template>

<script>
import SimpleTable from '@/components/Widgets/SimpleTable'
import AccountDetail from '@/components/Views/Permission/AccountDetail'

export default {
  name: 'Account',
  //mixins: [utils],
  components: { SimpleTable, AccountDetail },
  data() {
    const generateData = _ => {
      const data = [];
      for (let i = 1; i <= 15; i++) {
        data.push({
          key: i,
          label: `备选项 ${i}`,
          disabled: i % 4 === 0
        });
      }
      return data;
    };
    return {
      isList: true,
      tableFilter: {
        formUI: {
          inline: true,
          inlineMessage: true,
          size: 'mini',
        },
        items: [
          {
            fieldName: 'user__username',
            comparison: 'contains',
            formVisible: true,
            formItemUI: {
              label: '账号:',
            },
            editorUI: {
              placeHolder: '账号',
            },
          }, {
            fieldName: 'valid_flag',
            formVisible: true,
            editorType: 'ElSelect',
            editValue: 'Y',
            selectOptions: [{
              options: [{
                value: 'Y',
                label: '是',
              }, {
                value: 'N',
                label: '否',
              }]
            }],
            formItemUI: {
              label: '有效标志:',
            },
            editorUI: {
              clearable: true,
              placeHolder: '有效标志',
            },
          },
        ],
      },
      collapse: {
        collapseUI: {
          activeNames: ['1', '2', '3'],
        },
        items: [
          {
            collapseItemUI: {
              title: "账号信息",
              name: "1",
            },
            children: [
              {//user__username
                fieldName: 'user__username',
                formVisible: true,
                editable: true,
                formItemUI: {
                  label: '账号',
                  // rules: [
                  //   { required: true, message: '账号不能为空！' },
                  // ],
                },
              }, {//account_type
                fieldName: 'account_type',
                formVisible: true,
                editable: true,
                formItemUI: {
                  label: '账号类型',
                },
              },
            ],
          }, {
            collapseItemUI: {
              title: "用户信息",
              name: "2",
            },
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
            ],
          }, {
            collapseItemUI: {
              title: "权限信息",
              name: "3",
            },
            children: [
              {//party
                customType: true,
                data: generateData(),
                value1: [1, 4],
                fieldName: 'party',
                formVisible: true,
                editable: true,
              }, {//head_img
                fieldName: 'head_img',
                formVisible: true,
                //editable: true,
                formItemUI: {
                  label: '头像',
                },
              },
            ],
          },

        ]
      },
      table: {
        tableName: 'Account',
        hasOperatingColumn: true,
        items: [
          {
            fieldName: 'pk',
          }, //////// 账号信息
          {//user__username
            fieldName: 'user__username',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '账号',
              // rules: [
              //   { required: true, message: '账号不能为空！' },
              // ],
            },
            columnUI: {
              label: '账号',
            },
          }, {//account_type
            fieldName: 'account_type',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '账号类型',
            },
            columnUI: {
              label: '账号类型',
            },
          }, //////// 用户信息
          {//party
            fieldName: 'party',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '当事人ID',
            },
            columnUI: {
              label: '当事人ID',
            },
          }, {//head_img
            fieldName: 'head_img',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '头像',
            },
            columnUI: {
              label: '头像',
            },
          }, {//user__first_name
            fieldName: 'user__first_name',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '姓',
            },
            columnUI: {
              label: '姓',
            },
          }, {//user__last_name
            fieldName: 'user__last_name',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '名',
            },
            columnUI: {
              label: '名',
            },
          }, {//user__email
            fieldName: 'user__email',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '电子邮箱',
            },
            columnUI: {
              label: '电子邮箱',
            },
          }, {//email_binding_flag
            fieldName: 'email_binding_flag',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '电子邮箱绑定',
            },
            columnUI: {
              label: '电子邮箱绑定',
            },
          }, {//tel
            fieldName: 'tel',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '手机号',
            },
            columnUI: {
              label: '手机号',
            },
          }, {//tel_binding_flag
            fieldName: 'tel_binding_flag',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '手机号绑定',
            },
            columnUI: {
              label: '手机号绑定',
            },
          }, {//qq_openid
            fieldName: 'qq_openid',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: 'QQopenid',
            },
            columnUI: {
              label: 'QQopenid',
            },
          }, {//qq_binding_flag
            fieldName: 'qq_binding_flag',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: 'QQ绑定',
            },
            columnUI: {
              label: 'QQ绑定',
            },
          }, {//wechat_openid
            fieldName: 'wechat_openid',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '微信openid',
            },
            columnUI: {
              label: '微信openid',
            },
          }, {//wechat_binding_flag
            fieldName: 'wechat_binding_flag',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '微信绑定',
            },
            columnUI: {
              label: '微信绑定',
            },
          },////////// 权限
          {//user__is_active
            fieldName: 'user__is_active',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '激活状态',
            },
            columnUI: {
              label: '激活状态',
            },
          }, {//user__is_staff
            fieldName: 'user__is_staff',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: 'Staff状态',
            },
            columnUI: {
              label: 'Staff状态',
            },
          }, {//user__is_superuser
            fieldName: 'user__is_superuser',
            columnVisible: true,
            editable: true,
            formItemUI: {
              label: '超级用户状态',
            },
            columnUI: {
              label: '超级用户状态',
            },
          }, ////////// 登录信息
          {//user__date_joined
            fieldName: 'user__date_joined',
            columnVisible: true,
            //editable: true,
            formItemUI: {
              label: '注册时间',
            },
            columnUI: {
              label: '注册时间',
            },
          }, {//user__last_login
            fieldName: 'user__last_login',
            columnVisible: true,
            //editable: true,
            columnUI: {
              label: '最近登录时间',
            },
          }, {//current_login_ip
            fieldName: 'current_login_ip',
            columnVisible: true,
            //editable: true,
            columnUI: {
              label: '最近登录IP',
            },
          }, {//current_login_device
            fieldName: 'current_login_device',
            columnVisible: true,
            //editable: true,
            columnUI: {
              label: '最近登录设备',
            },

          },// 其它
          {// remark
            fieldName: 'remark',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '备注',
            },
            editorUI: {
              type: 'textarea',
            },
          }, {//sn
            fieldName: 'sn',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '排序号',
            },
          }, {//valid_flag
            fieldName: 'valid_flag',
            columnVisible: true,
            editable: true,
            columnUI: {
              label: '有效标志',
            },
            editorType: 'ElSelect',
            editValue: 'Y',
            selectOptions: [{
              options: [{
                value: 'Y',
                label: '是',
              }, {
                value: 'N',
                label: '否',
              }]
            }],
          },
        ],
      },
      // formUI: {
      //   //inline: true,
      //   labelWidth: '100px',
      //   //showMessage: true,
      //   // inlineMessage: true,
      // },
    }
  },
  methods: {
    handleClick(row) {
      this.isList = false
    },
  },
}
</script>


