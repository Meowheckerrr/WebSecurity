const express = require("express");
const bodyParse = require("body-parser")
const contentType = require('content-type');
const read = require('read');

const app = express()
const port = process.env.PORT || 8001

//middleWare 

//Parse the reqeust

    //paser application/x-www-form-urlencoded"
    app.use(bodyParse.urlencoded({ extended: false }))

    //paser JSON data to js object 
    app.use(bodyParse.json())

    app.use((err, req, res, next) => {
        console.error('Error:', err);
        res.status(500).send('Internal Server Error');
    });


function getCharset(req){
    try {
        //get the contentType of charest property 
        return (contentType.parse(req).parameters.charset || "").toLowerCase()
    }
    catch(error){
        console.log(error)
        return undefined
    }
}

app.post('/api/post1',(req,res)=>{
    const requestBodyObj  = req.body
    console.log(requestBodyObj)
    res.json({message:'Received data !!'})
})

//charset
app.post('/api/post2',(req,res)=>{
    // get the charset form HTTP header (Content-Type:)
    const charset = getCharset(req) || "utf-8" 

    const readOption = {
        //encoding -> Inform the server to use a specific character encoding for decoding when reading data.
        encoding: charset
        // //compose data 
        // inflate: inflate,
        // //Maximum string length.
        // limit: limit,
        // verify: verify
    }

    //read the data: parse request -> to data 
    //Read function have BUG
    read(req,res,(err,data)=>{
        if(err){
            console.error('Error reading request:', err);
            res.status(500).send('Internal Server Error');
        }else{
            console.log(data)
            // res.json({message:'Received data !!'})
            res.send('Request data received successfully!');
        }
    },readOption)
})


app.listen(port,()=>{
    console.log(`Server is running on port ${port}`);
    console.log(`http://127.0.0.1:${port}`)
})