import fetch from '@/utils/fetch'

export function getList(params) {
  return fetch({
    url: '/table/list',
    method: 'get',
    params
  })
}

import fetch2 from '@/utils/fetch2'

export function getTreeList(params){
    return fetch2({
      baseURL: 'http://127.0.0.1:8000',
      url: '/test/tree/getTreeList/',
      method: 'get',
      params,
    })
  }