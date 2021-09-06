(index.js)

import { Provider } from 'react-redux'
import { createStore } from 'redux'


let 초기값 = [
  { id : 0, name : '멋진신발', quan : 2 },
  { id : 1, name : '멋진신발2', quan : 1 }
]

function reducer(state = 초기값, 액션) {  // 여기서 등호가 들어가는 문법은 default parameter 문법(ES6 문법)
  if (액션.type === '수량증가') {
    
    let copy = [...state]
    copy[0].quan++

    return copy
  } else {
    return state
  }
}

let store = createStore(reducer)

// reducer는 별거 아니고 그냥 수정된 state를 뱉는 함수