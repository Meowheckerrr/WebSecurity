const errorObj = new Error("Meowhecker error message")

errorObj.status = 404

function createError(status, message) {
    const error = new Error(message);
    error.status = status;
    return error;
}

function processError(errObj){
    const status = 500
    const error = createError(status,errObj)
    console.error(error)
}


processError(errorObj)
Object.prototype.status = 300
