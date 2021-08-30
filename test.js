const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number)

let result = 1

for (let i = 2; i <= inputData[0]; i++) {
  result += i
}

console.log(result)