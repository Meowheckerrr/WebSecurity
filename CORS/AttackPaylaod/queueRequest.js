var queue = [];


queue.push(function(value){
    console.log('function1',value)
})
queue.push(function(value){
    console.log('function2',value)
})
queue.push(function(value){
    console.log('function3',value)
})

for (var i=0;i<=3;i++){
    if(queue.length){
        var func = queue.shift()
        func(i*100)
    }
}