function createError(arg,status){
    // initial Status 

    status = status || 500

    // object
    if (typeof arg === 'object' && arg instanceof Error){
        status = arg.status || arg.statusCode || status
    }else if (arg === 'number'){
        status = arg;
    }
    const error = new Error(`Custom Error with Status Code${status}`)
    error.status = status
    
    return error
}


const error1 = createError(404); // 创建一个状态码为 404 的错误对象
console.error(error1);

const customError = new Error('This is a custom error');
customError.status = 418;

const error2 = createError(customError); // 从现有的 Error 对象中提取状态码
console.error(error2);