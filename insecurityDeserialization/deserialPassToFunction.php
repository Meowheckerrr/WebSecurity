<?php


class User {
    public $id;
    public $username;
    public $email;

    public function __construct($id,$username,$email)
    {
        $this->id = $id;
        $this->username = $username;
        $this->email = $email;
    
    }
    public function deleteUser(){
        echo "Deleting user: " . $this->username;

        // delete User Code
    }

}

$serializedUser = $_COOKIE['session'];

$user = unserialize($serializedUser);

$user->deleteUser();

?>