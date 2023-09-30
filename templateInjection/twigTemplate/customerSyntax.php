<?php

// load twig template!! 
require './vendor/autoload.php';

$loader = new \Twig\Loader\FilesystemLoader('views');
$twig = new \Twig\Environment($loader, [
    // 'cache' => '/path/to/compilation_cache',
]);

$lexer = new \Twig\Lexer($twig, array(
    'tag_block' => array('{','}'),
    'tag_variable' => array('{{$','}}')
));

$twig->setLexer($lexer);

$output = $twig->render("customerSyntax.html",array(
    'name'=>'meowhecker',
    'age'=>'18',
    'badStuff'=>$_GET['badStuff'],//Vulnerable Code 
    'users' => array(
        array('name'=>"meow1", 'age'=>'20'),
        array('name'=>"meow2", 'age'=>'30'),
        array('name'=>"meow3", 'age'=>'40'),
    )
));
echo $output;
?>