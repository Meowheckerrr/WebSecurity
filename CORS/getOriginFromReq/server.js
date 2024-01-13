const express = require ('express')
const app =express()

app.use((req,res,next)=>{

    //get the origin value from reqeust 
    const origin = req.get('Origin') // return header value 

    //check whether the origin header exists or not 
    if(origin){
        res.header('Access-Control-Allow-Origin', origin)
        console.log("get the origin successful")
    }
    // proccess the next reqeust!!

    // can recevie the client credentials and send the specific use credential
    res.header('Access-Control-Allow-Credentials', true);
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');


    // pre-flight reqeust 
    if (req.method === 'OPTIONS') {
        return res.status(204).end();
    }
    const cookieValue = req.get('meowCookie')

    next()
})
app.get('/', (req, res) => {
    res.cookie('meowCookie', 'cookieValue', { httpOnly: true, sameSite: 'strict' });
    res.send('Hello, World!');
  });

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
