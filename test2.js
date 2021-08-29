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