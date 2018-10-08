import Vue from 'vue'
import ElementUI from 'element-ui'

import 'element-ui/lib/theme-chalk/index.css'
//改变 Element 的样式变量
// import './element-variables.scss'
import App from './App'
import router from './router'
import store from './store'
import '@/icons' // icon
import '@/permission' // 权限
// import DialogComponent from './components/Table/DialogComponent'

// const nDialog = Vue.extend(DialogComponent);
// import regionModule from './store/modules/business_info/region.js'

Vue.use(ElementUI)

Vue.config.productionTip = false

//自定义指令回车，换到下一个input
// Vue.directive('focusNextOnEnter', {
//   bind: function(el, {value}, vnode) {   
//     el.addEventListener('keyup', (ev) => {
//       if (ev.keyCode === 13) {
//         let nextInput = vnode.context.$refs[value]
//         if (nextInput && typeof nextInput.focus === 'function') {
//           nextInput.focus()
//           nextInput.select()
//         }
//       }
//     })
//   }
// })

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
  // template: '<App/>',
  // components: { App }
})

// store.registerModule('regionModule')