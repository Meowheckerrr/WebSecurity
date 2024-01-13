var newWindows = window.open("http://meowhecker.com");

// To close the new window after a few seconds

setTimeout(function(){
    newWindows .close();
},5000);