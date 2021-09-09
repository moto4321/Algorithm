let alert초기값 = true

function reducer2(state = alert초기값, 액션) {
  if (액션.type === 'alert닫기') {
    state = false
    return state 
  } else {
    return state
  }
}

import { createStore, combineReducers } from 'redux'

let store = createStore(combineReducers({reducer,reducer2}))

function state를props화(state){
  return {
    state : state
  }
}

// 위를 아래와 같이 바꿔야한다.

function state를props화(state){
  return {
    state : state.reducer,
    alert : state.reducer2
  }
}