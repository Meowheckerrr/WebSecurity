const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8081 });

wss.on('connection', (ws) => {
    
    console.log('Client connected.');
    ws.on('message', (message) => {
        console.log('Received:', message);
        ws.send(`Echo: ${message}`);
    });

    //socket closed 
    ws.on('close', () => {
        console.log('Client disconnected.');
    });
});