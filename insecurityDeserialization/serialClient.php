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

$user1 = new user("meowhecker","meoweckerPassword");

$serializedData = serialize($user1);
echo "initial:";
echo $serializedData;
echo "<br>";

// HTTP Network transfer
$options = [
    'http'=>[
        'method'=>'POST',
        'header'=>'Content-type: application/x-www-form-urlencoded',
        'content'=>$serializedData
    ]
];

$context = stream_context_create($options);

$response = file_get_contents('http://127.0.0.1/insecurityDeserialization/serialServer.php', false, $context);

echo "Response:";
echo $response."<br>";


$deserializedData = unserialize($serializedData);
echo $deserializedData->userName."\n";
echo $deserializedData->password;


?>