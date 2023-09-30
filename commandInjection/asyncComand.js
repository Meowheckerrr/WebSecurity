const { exec } =require('child_process')


let command = "dir"
console.log("Cmd Execut start")

exec(command,(error,stdout,stderr)=>{
    if(error){
        console.error(`Error Message:${error}`)
        return
    }
    
    console.log('command comlete!');
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
})

console.log('exeucting...');