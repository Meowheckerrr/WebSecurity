const customerHeader = {
    headers:{
    'Content-Type': 'application/json',
    'Authorization': 'meowhecker secret-token',
    'testing':undefined
    }
}

const response ={
    __proto__:customerHeader
}

console.log(response.headers);  // 输出 customProto 中的 headers 对象
console.log(response.__proto__.headers);  // 也可以访问
console.log(response.__proto__.headers['Content-Type']);  // 访问特定的头部值