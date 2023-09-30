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

//echo $user1;
//Fatal error: Uncaught Error: Object of class user could not be converted to string

//serialized "object" to "string"
$serializeUser = serialize($user1);
echo $serializeUser;
echo "<br>";


$deserializedUser = unserialize($serializeUser);
echo "Persisted Property<br>";
echo "Deserialized User: Name = " . $deserializedUser->userName . ", Password = " . $deserializedUser->password;

?>