const {fork} = require('child_process')

const execArgsOptions=[
    "--inspect=9926",
    "--eval=require('child_process').execSync('curl http://127.0.0.1:8000')"
]

const options ={
    //property 
    execArgv:execArgsOptions
}
const mainProcess = fork('child.js',[],options)

mainProcess.on('message',(message)=>{
    console.log(`Main process received message from child: ${message}`);
})
mainProcess.send("I'm your father!! MEOW FATHER")