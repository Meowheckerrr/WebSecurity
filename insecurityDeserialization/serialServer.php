<?php


class user {
    public $userName;
    public $password;

    public function __construct($userName,$password)
    {
        $this->userName = $userName;
        $this->password = $password;
    }
}

//capture reqeust 
$rawData = file_get_contents('php://input');

// echo $rawData; //(urlEncoded)
$decodedRawData = urldecode($rawData);
echo $decodedRawData;
echo "<br>";

$deserializeData = unserialize($decodedRawData);
//Check if unserialize was successful
if ($deserializeData !== false){
    echo "unserialize was successful";
    echo "User Name: " . $deserializeData->userName . "\n";
    echo "Password: " . $deserializeData->password;
    $deserializeData->userName="meowHacker";
}else{
    // Failed to unserialize
    echo "Failed to unserialize the data.";
}

?>