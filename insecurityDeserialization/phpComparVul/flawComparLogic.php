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
if (isset($_COOKIE['login'])){

    try {
        $login = unserialize($_COOKIE['login']);
        // pass the login validation
    }catch (error){
        
    }
}
if ($login['userName'] == $valiUserName && $login['password'] == $valiPassword) {
    $userObj = new user($valiUserName,$valiPassword);
    setcookie('login',serialize($userObj),time()+3600);

    //Redirect 
    header('Location: meowhecker.php');
    exit;
}else {
    $loginError = 'Invalid username or password';
}
?>



