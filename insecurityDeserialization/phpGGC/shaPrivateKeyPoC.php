<?php

//Store on php service
$secrekey = "meowheckerKey";

//Hash data (payload)

$data = "meowhecker";
//hash_hmac

$hash1 = hash_hmac('sha1',$data,$secrekey); //順序有差
$hash2 = hash_hmac('sha1',$secrekey,$data);
echo "Generated Hash1:" . $hash1. "\n";
echo "Generated Hash2:" . $hash2;
?>


