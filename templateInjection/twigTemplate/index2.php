<?php



require_once './vendor/autoload.php';

$loder = new \Twig\Loader\ArrayLoader([
    'hello'=>"<html>hello . {{name}}</html>",
]);

$twig = new \Twig\Environment($loder);

$name = isset($_GET['name']) ? $_GET['name'] : 'meow';

$data = ['name' => $name];


//render template

$template = $twig->load('hello');
echo $template->render($data);




?>