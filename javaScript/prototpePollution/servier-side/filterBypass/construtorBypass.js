// Create a constructor function
function LocalObj() {
    name:"local object"
}

// Add a property to the prototype(global testing)
Object.prototype.property = "meow adding form Global Obj";

// Create an instance of MyObject
const myInstance = new LocalObj();

// Access the property on the instance
console.log(myInstance.property); // This will output "meow"
