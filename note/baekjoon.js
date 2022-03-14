// 2588
const fs = require('fs'); 
const input = fs.readFileSync("/dev/stdin").toString().split("\n").map(Number); 

const num1 = input[0]
const num2 = input[1]

const oneNum = num2 % 10
const tenNum = Math.floor((num2 % 100)/10)
const hundredNum = Math.floor(num2/100)

console.log(num1 * oneNum)
console.log(num1 * tenNum)
console.log(num1 * hundredNum)
console.log(num1 * num2)

// 10430
const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number)

const a = input[0]
const b = input[1]
const c = input[2]

console.log((a+b)%c)
console.log(((a%b) + (b%c))%c)
console.log((a*b)%c)
console.log(((a%c) * (b%c))%c)

// if
// 1330
const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number)

const [a, b] = inputData

if (a > b) {
  console.log('>')
} else if (a < b) {
  console.log('<')
} else {
  console.log('==')
}

// 9498
const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number)

const num = inputData[0]

if ( 90 <= num && num <= 100) {
  console.log('A')
} else if ( 80 <= num && num <= 89 ) {
  console.log('B')
} else if ( 70 <= num && num <= 79 ) {
  console.log('C')
} else if ( 60 <= num && num <= 69 ) {
  console.log('D')
} else {
  console.log('F')
}

// 2753
let input = require("fs").readFileSync("/dev/stdin").toString().split(" ");
const A = Number(input[0]);


if ((A % 4 === 0 && A % 100 !== 0) || A % 400 === 0) {
  console.log("1")
} else {
  console.log("0")
}

// 2884
const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number)

const [H, M] = inputData

if (M > 45 && M < 60) {
  console.log(H, M - 45)
} else {
  if (H == 0) {
    console.log(23, M + 15)
  } else {
    console.log(H - 1, M + 15)
  }
}


// 2739
const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number)

const N = inputData[0]

for (let i = 1; i < 10; i++) {
  console.log(` ${N} * ${i} =`,N*i)
}

// 10950
let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

for (let i = 1; i <= input[0]; i++) {
    let numbers = input[i].split(' ')
    
    console.log(Number(numbers[0]) + Number(numbers[1]))
}

// 8393
const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(Number)

let result = 0

for (let i = 1; i <= inputData[0]; i++) {
  result += i
}

console.log(result)

// 15552

// 2741
