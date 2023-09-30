const vulnerableObject = {}

Object.defineProperty(vulnerableObject,'gadgetProperty',{
    configurable:false,
    writable:false,
    
})

vulnerableObject.gadgetProperty = "meowhacker hacke in"

console.log(vulnerableObject.gadgetProperty)