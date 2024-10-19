<?php
$attackPayload = [
    '.htpasswd',
    '../.htpasswd',
    '../../.htpasswd',
    '../../../.htpasswd',
    '../../../../.htpasswd',
    '../../../../../.htpasswd',
    '../../../../../../.htpasswd',
];
foreach ($attackPayload as $file) {
    $filterfile = basename($file);
    echo $filterfile . "<br>";
}
?>