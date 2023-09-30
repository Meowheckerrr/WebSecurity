<?php 
function compare1(){
    if (1 == "1"){
        return 'compare1 is true';
    }
    else{
        return 'compare1 is false';
    }
}

function compare2(){
    if (0 == ""){
        return 'compare2 is true';
    }
    else{
        return 'compare2 is false';
    }
}

echo compare1() . "<br>";
echo compare2();

?>