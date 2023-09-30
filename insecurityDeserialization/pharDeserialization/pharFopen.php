<?php

$phar = new Phar('meowhecker.phar');
$phar['index.php'] = "<?php echo 'meowhecker'?>";

$pharFile = 'Phar://meowhecker.phar/index.php';
$fileHandle = fopen($pharFile,'r');

if($fileHandle){
    while(!feof($fileHandle)){
        $line = fgets($fileHandle);
        echo $line;
    }
    fclose($fileHandle);
}
else {
    echo " Phar file read faild !";
}






?>