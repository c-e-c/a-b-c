<template>
    <div class="app-container">
        <div>
            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                <el-form-item label="区域编号">
                     <!-- <slot name="nn"></slot> -->
                    <el-input v-model="formInline.id" placeholder="区域编号"></el-input>
                </el-form-item>
                <el-form-item label="站点名称">
                    <el-input v-model="formInline.name" placeholder="站点名称"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSearch">查询</el-button>
                    <el-button type="primary" @click="add">增加</el-button>
                    <el-button type="primary" @click="remove">删除</el-button>
                    <el-button type="primary" @click="save">保存</el-button>
                </el-form-item>
            </el-form>
        </div>

        <div>
            <el-table :data="clientlist" border fit highlight-current-row stripe @select="handleSelectionChange">
                <el-table-column type="selection" width="55">
                </el-table-column>
                <el-table-column align="center" label='序号' width="70">
                    <template slot-scope="scope">
                        <span>{{ scope.$index+1 }}</span>
                    </template>
                </el-table-column>
                <el-table-column align="center" label='区域编号' sortable>
                    <template slot-scope="scope">
                        <el-input v-show="scope.row.edit" autofocus size="small" v-model="scope.row.station_code" @focus="click1"></el-input>
                        <span v-show="!scope.row.edit" @dblclick='scope.row.edit=!scope.row.edit'>{{ scope.row.station_code }}</span>
                    </template>
                </el-table-column>
                <el-table-column align="center" label='区域名称' prop="station_name" sortable>
                </el-table-column>
                <el-table-column align="center" label='区域拼音' prop="region_spell">
                </el-table-column>
                <el-table-column align="center" label='地址' prop="address">
                </el-table-column>
                <el-table-column align="center" label="编辑" width="120">
                    <template slot-scope="scope">
                        <el-button :type="scope.row.edit?'success':'primary'" @click='scope.row.edit=!scope.row.edit' size="small" icon="edit">{{scope.row.edit?'完成':'编辑'}}</el-button>
                    </template>
                </el-table-column>
                <el-table-column prop="flag" label="使用标志" :filters="[{ text: '是', value: '是' }, { text: '否', value: '否' }]" :filter-method="filteTag" filter-placement="bottom-end">
                    <template slot-scope="scope">
                        <el-tag :type="scope.row.flag === '是' ? 'primary' : 'success'" close-transition>{{scope.row.flag}}</el-tag>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <div>
            <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page.sync="listQuery.page" :page-sizes="[10,20,30, 50]" :page-size="listQuery.limit" layout="total, sizes, prev, pager, next, jumper" :total="total">
            </el-pagination>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            serverLists: [{
                station_code: '11',
                station_name: '陈江',
                region_spell: '',
                address: '陈江',
                edit: false,
                flag: '否'
            }, {
                station_code: '2',
                station_name: '北仑',
                region_spell: '',
                address: '北仑',
                edit: false,
                flag: '是'
            }, {
                station_code: '31',
                station_name: '曲阜',
                region_spell: '',
                address: '曲阜',
                edit: false,
                flag: '是'
            }, {
                station_code: '41',
                station_name: '泰安',
                region_spell: '',
                address: '泰安',
                edit: false,
                flag: '是'
            }, {
                station_code: '51',
                station_name: '三海关',
                region_spell: '',
                address: '三海关',
                edit: false,
                flag: '是'
            }, {
                station_code: '61',
                station_name: '葫芦岛',
                region_spell: '',
                address: '葫芦岛',
                edit: false,
                flag: '是'
            }, {
                station_code: '71',
                station_name: '陈江',
                region_spell: '',
                address: '陈江',
                edit: false,
                flag: '否'
            }, {
                station_code: '881',
                station_name: '北仑',
                region_spell: '',
                address: '北仑',
                edit: false,
                flag: '是'
            }, {
                station_code: '991',
                station_name: '曲阜',
                region_spell: '',
                address: '曲阜',
                edit: false,
                flag: '是'
            }, {
                station_code: '10',
                station_name: '泰安',
                region_spell: '',
                address: '泰安',
                edit: false,
                flag: '是'
            }, {
                station_code: '11',
                station_name: '三海关',
                region_spell: '',
                address: '三海关',
                edit: false,
                flag: '是'
            }, {
                station_code: '12',
                station_name: '葫芦岛',
                region_spell: '',
                address: '葫芦岛',
                edit: false,
                flag: '是'
            }, {
                station_code: '13',
                station_name: '陈江',
                region_spell: '',
                address: '陈江',
                edit: false,
                flag: '否'
            }, {
                station_code: '14',
                station_name: '北仑',
                region_spell: '',
                address: '北仑',
                edit: false,
                flag: '是'
            }, {
                station_code: '15',
                station_name: '曲阜',
                region_spell: '',
                address: '曲阜',
                edit: false,
                flag: '是'
            }, {
                station_code: '16',
                station_name: '泰安',
                region_spell: '',
                address: '泰安',
                edit: false,
                flag: '是'
            }, {
                station_code: '17',
                station_name: '三海关',
                region_spell: '',
                address: '三海关',
                edit: false,
                flag: '是'
            }, {
                station_code: '18',
                station_name: '葫芦岛',
                region_spell: '',
                address: '葫芦岛',
                edit: false,
                flag: '是'
            }, {
                station_code: '19',
                station_name: '陈江',
                region_spell: '',
                address: '陈江',
                edit: false,
                flag: '否'
            }, {
                station_code: '20',
                station_name: '北仑',
                region_spell: '',
                address: '北仑',
                edit: false,
                flag: '是'
            }, {
                station_code: '21',
                station_name: '曲阜',
                region_spell: '',
                address: '曲阜',
                edit: false,
                flag: '是'
            }, {
                station_code: '22',
                station_name: '泰安',
                region_spell: '',
                address: '泰安',
                edit: false,
                flag: '是'
            }, {
                station_code: '23',
                station_name: '三海关',
                region_spell: '',
                address: '三海关',
                edit: false,
                flag: '是'
            }, {
                station_code: '24',
                station_name: '葫芦岛',
                region_spell: '',
                address: '葫芦岛',
                edit: false,
                flag: '是'
            }, {
                station_code: '25',
                station_name: '葫芦岛',
                region_spell: '',
                address: '葫芦岛',
                edit: false,
                flag: '是'
            }],
            total: null,
            listQuery: {
                page: 1,
                limit: 10,
            },
            clientlist: [],
            selected: [], //已选择项
            temporaryData: [],//临时数据
            deletedData: [],
            addedData: [],
            number: 1,
            click1: this.test,
            formInline: {
                id: '',
                name: '',
            }
        }
    },
    created() {
        this.getList()
        this.temporaryData = this.clientlist
    },
    // computed: {
    // getIndex(index)
    //     {   
    //         // let number = this.number
    //         // number++
    //                    console.log(index)
    //          return index
    //         // if(number > listQuery.limit)
    //         // {number += listQuery.limit}
    //     }
    // },
    methods: {
        getList() {
            let array = [], startNum = 0, endNum = 0
            var id = this.formInline.id
            var name = this.formInline.name
            if (id || name) {
                if (id) {
                    array = this.search(id)
                } else if (name) {
                    array = this.search(name)
                }
                this.total = array.length
                array = this.page(this.listQuery.page, this.listQuery.limit, this.total, array)
            } else {
                this.total = this.serverLists.length
                array = this.page(this.listQuery.page, this.listQuery.limit, this.total, this.serverLists)
            }
            this.setSlist(array)
        },
        page(a, b, c, d) {
            let array = [], startNum = 0, endNum = 0
            startNum = (a - 1) * b
            if (a * b < c) {
                endNum = a * b
            } else {
                endNum = c;
            }
            return array = d.slice(startNum, endNum)
        },
        search(formInline) {
            return this.serverLists.filter(function(list) {
                return Object.keys(list).some(function(key) {
                    return String(list[key]).toLowerCase().indexOf(formInline) > -1
                })
            })
        },
        handleSizeChange(val) {
            this.listQuery.limit = val
            this.getList()
        },
        handleCurrentChange(val) {
            this.listQuery.page = val
            this.getList()
        },
        test() { console.log("获得焦点") },
        handleSelectionChange(val, row) {
            this.selected = val
        },
        onSearch() {
            this.listQuery.page = 1
            this.getList()
        },
        add() {
            this.clientlist.push({
                station_code: ' ',
                station_name: '',
                region_spell: '',
                address: '',
                edit: false,
                flag: '是'
            })
        },
        remove() {
            if (confirm("你确定删除吗？")) {
                let clientlist = this.clientlist
                let deletedData
                this.selected.forEach(function(select, i) {
                    clientlist.forEach(function(list, index) {
                        if (select.station_code === list.station_code) {
                            deletedData = select
                            clientlist.splice(index, 1)
                        }
                    })
                })
                this.deletedData = deletedData
            }
            else {
             this.$message({
              message: "区域名称不能为空",
              type: "warning"
            });
            }
        },
        save() {
            var deletedData = this.deletedData
            var serverLists = this.serverLists
            console.log(deletedData)
            if (deletedData) {
                serverLists.forEach(function(list, index) {
                    if (list.station_code == deletedData.station_code) {
                        serverLists.splice(index, 1)
                    }
                })
            }

        },
        setSlist(arr) {
            // this.slist = JSON.parse(JSON.stringify(arr));
            this.clientlist = arr
        },
        filteTag(value, row) {
            return row.flag === value;
        }
    }
}
</script>
