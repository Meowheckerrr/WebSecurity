<?php 

require './vendor/autoload.php';

$loader = new \Twig\Loader\FilesystemLoader('views');
$twig = new \Twig\Environment($loader, [
 
]);

$lexer = new \Twig\Lexer($twig, array(
    'tag_block' => array('{','}'),
    'tag_variable' => array('{{$','}}')
));

$twig->setLexer($lexer);

echo $twig->render("");