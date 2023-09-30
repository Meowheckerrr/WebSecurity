
<?php
class User {
    
    public $username;
    public $access_token;

    public function __construct($username,$access_token)
    {
        $this->username = $username;
        $this->access_token = $access_token;
    }
}

$User = new User("administrator",0);

echo serialize(($User));
?>