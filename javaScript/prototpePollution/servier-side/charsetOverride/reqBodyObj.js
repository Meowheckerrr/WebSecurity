const express = require("express");
const bodyParse = require("body-parser")
const app = express()

//middleWare 

//Parse the reqeust

    //paser application/x-www-form-urlencoded"
    app.use(bodyParse.urlencoded())

    //paser JSON data to js object 
    app.use(bodyParse.json())



app.post('/api/meow',(req,res)=>{
    const requestBodyObj  = req.body
    console.log(requestBodyObj)
    res.json({message:'Received data !!'})
})

const port = process.env.PORT || 8001
app.listen(port,()=>{
    console.log(`Server is running on port ${port}`);
    console.log(`http://127.0.0.1:${port}`)
})