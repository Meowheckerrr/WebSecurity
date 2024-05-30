<?php
$maliciousInput = "`whomai`";
$inquiryId = preg_replace('/[\$<>;|&{}\(\)\[\]\'\"]/', '', $maliciousInput);
$contents = shell_exec("dir /var/www/mailroom/inquiries/$inquiryId.html");
echo $contents
?>