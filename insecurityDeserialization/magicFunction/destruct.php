
<?php
class user{

    public function __construct()
    {
        echo "Object created";
    }

    public function someTaskPerform(){
        echo "do some tasks";
    }
    public function __destruct()
    {
        echo "Object Destruct";
    }

}
$userObject = new user;
$userSerialize = serialize($userObject);

echo $userSerialize;
?>