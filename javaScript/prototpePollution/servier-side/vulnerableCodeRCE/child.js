

//Event listener 
//process.on('message', (message) => {...});
// Listener -> Main process
// Event -> Message event
// If the main process receives a message, the function will be triggered.

process.on('message',(message)=>{
    
    console.log(`subMeow received the message form Main process: ${message}`)
    //process.send(`subMeow say: hi`)
    process.send(`current proccess ID:${process.pid}`)
})
