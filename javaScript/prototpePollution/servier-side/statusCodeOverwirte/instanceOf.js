class CustomError extends Error {
    constructor(message){
        super(message) //super -> invoke parent constructor function 
        this.name = 'CustomError';

    }
}

const error1 = new Error('This is a standard Error');
const error2 = new CustomError('This is a custom Error');

console.log(error1 instanceof Error); // true，error1 是 Error 类的实例
console.log(error2 instanceof Error); // true，error2 是 Error 类的实例
console.log(error2 instanceof CustomError); // true，error2 也是 CustomError 类的实例