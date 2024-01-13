const myObject = {
    apple: 'red',
    abaa:'meow',
    banana: 'yellow',
    cherry: 'red',
    date: 'brown'
  };

const firstField_0 = Object.keys(myObject)[0] // first property -> apple 
const firstField_1 = Object.keys(myObject)[1] // 
const firstField_2 = Object.keys(myObject)[2] // 
const firstField_3 = Object.keys(myObject)[3] // 

console.log("^.{0}a.*",firstField_0.match('^.{0}a.*'))
console.log("^.{1}a.*",firstField_0.match('^.{1}a.*'))
console.log("^.{1}a.*",firstField_1.match('^.{2}a.*'))