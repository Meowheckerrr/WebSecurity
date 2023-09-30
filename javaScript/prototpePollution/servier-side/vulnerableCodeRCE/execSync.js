const {execSync} = require('child_process')

try {
    const result = execSync('dir',{encoding:'utf-8'})
    console.log('command output!!')    
    console.log(result)
} catch(error){
    console.error('Error executing command:', error.message)
}

