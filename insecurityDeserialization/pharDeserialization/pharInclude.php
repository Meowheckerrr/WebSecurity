<?php 

$phar = new Phar('meowhecker.phar'); // phar -打包的php
$phar['index.php'] = "<?php echo 'meowhecker'; ?>";

//Access PHP file by unpacket the Phar
$indextContent = file_get_contents('phar://meowhecker.phar/index.php');
echo "parse phar file :" . $indextContent . "\n";

//Rungin the php script!!
echo "Running the php script from the phar file:\n";
include('phar://meowhecker.phar/index.php'); // or include 'phar://meowhecker.phar/index.php' ;
?>