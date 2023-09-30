userObj = {
    name:"user",
    password:"user123"
}

Object.prototype.meow = "hacker"
console.log(userObj.hasOwnProperty('moew')) //output: false 
console.log(userObj.meow)

console.log("---------------------------------------------------")

//for loop enumerate
console.log("for...loop")
for (propertyKey in userObj){
    console.log(propertyKey)
}