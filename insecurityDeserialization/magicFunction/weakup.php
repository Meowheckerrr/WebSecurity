<?php

class userObject{

    public $name;

    public function __construct($name)
    {
        $this->name = $name;
    }

    public function __sleep()
    {
        // sleep method -> prisist the data when serialize or unserialized
        return ["name"];
    }

    public function __wakeup()
    {
        echo "Wakeup function start:". $this->name . "</br>";
    }
}
//serialize object
$user = new userObject("meowhecker");
$userSerialize = serialize($user);
echo $userSerialize;
echo "</br>";

//Unserialize object 
$userDeSerialize = unserialize($userSerialize);
echo $userDeSerialize->name;

?>