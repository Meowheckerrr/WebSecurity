

<?php

$phar = new Phar('meowhecker.phar');
$phar['index.php'] = "<?php echo 'meowhecker'?>";

$pharFilePath = 'Phar://meowhecker.phar/index.php';


if (file_exists($pharFilePath)) {
    echo "Phar 文件中的文件存在。\n";
} else {
    echo "Phar 文件中的文件不存在。\n";
}
?>
