<?php
class user{

    private $filePath;
    public function __construct($filePath)
    {
        $this->filePath = $filePath;
        
        echo "Object created </br>";
    }

    public function someTaskPerform(){
        echo "do some tasks </br>";
    }
    public function __destruct()
    {
        $currentDirectory = getcwd();
        echo "Current Directory: " . $currentDirectory . "<br>";
        echo $this->filePath;
        unlink($this->filePath);
    
    }
}

$deleteFilePath = "C:\Users\USER\Desktop\CSIE\WebSecurity\insecurityDeserialization\magicFunction\meowhecker.txt";
$userObject = new user($deleteFilePath);

// $userSerialize = serialize($userObject);
// echo $userSerialize;
?>