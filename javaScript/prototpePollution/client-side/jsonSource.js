const objectLiteral = {__proto__:{admin:"Ture"}}
const objectFromJson = JSON.parse('{"__proto__":{"admin":"Ture"}}')


console.log(objectLiteral.hasOwnProperty('__proto__'))
console.log(objectFromJson.hasOwnProperty('__proto__'))