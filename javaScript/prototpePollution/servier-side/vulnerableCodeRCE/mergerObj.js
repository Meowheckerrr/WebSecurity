const target ={a:1,b:2}
const source ={b:3,c:4}


function mergeObject(targer,source){
    for (let key in source){
        targer[key] = source[key]
    }
}

mergeObject(target,source)
console.log(target)
// { a: 1, b: 3, c: 4 }