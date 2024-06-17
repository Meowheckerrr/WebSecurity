
<?php
// $_GET['str'] = 'Hello%2C%20world%21%20%F0%9F%98%8A';
$str = $_GET['str'];
//$str = isset($_GET['str']) ? htmlspecialchars($_GET['str']) : "";

$str = iconv('Windows-1252', "UTF-8", $str);
echo 'Frist CONV:' . $str .'</br>';

$str = iconv('UTF-8', "ASCII//TRANSLIT", $str);
echo 'SEC CONV:' . $str .'</br>';
echo "String:" . $str .'</br>';
?>