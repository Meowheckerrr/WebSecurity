const {execSync} = require('child_process')

try {
    const command = 'grep "meowhecker"'
    const input  = 'hellow meowhecker\n meowmeow\n'
    const result = execSync(command,{shell:'/bin/bash',input})
    //if shell and input didn't defind, we could pollute it 
    console.log("Result:", result.toString())

} catch (error){
    console.error("Error", error.message)
}