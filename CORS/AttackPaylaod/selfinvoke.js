
urlarray =[]
for (var i = 0;i<10;i++){
    urlarray.push((function(index){
        url = 'http://meowhecker/page'+index ; 
        return url;
    })(i))
}
console.log(urlarray)
