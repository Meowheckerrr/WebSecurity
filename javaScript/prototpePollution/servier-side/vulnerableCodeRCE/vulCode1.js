//PP2RCE

const { execSync, fork } = require('child_process');
const { is } = require('express/lib/request');
// child_process -> module 
// execSync ->　exec command
// fork -> create sub proccess !!

var object = {
    name:"test"
}

function f1(){
    console.log('Im funciotn')
}

function isObject(obj){
    console.log(typeof obj);
    return typeof obj === 'function' || typeof obj ==='object'
}
//console.log(isObject(f1))
//function
//true

//如果invoke f1() f1 沒有return -> defautl "undefined" !!

function mergeObject(targer,source){
    for(let key in source){
        if(isObject(targer[key])&&isObject(source[key])){
            mergeObject(targer[key],source[key])
        }
        else{
            targer[key] = source[key]
        }
    }
    return targer
}


function cloneObj(targerObj){
    mergeObject({},targerObj)
}

// user object -> source 
clone(USERINPUT);

var MainProcess = fork('execFileEcho.js')
// echo meow>execFileEcho : execSync 