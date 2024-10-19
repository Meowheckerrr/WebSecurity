<?php
// 定義一個包含允許文件名的白名單數組
$allowed_files = ['example.txt', 'report.pdf', 'image.jpg'];

// 模擬用戶輸入的文件名
$file = 'report.pdf/2312e';

// 使用 in_array() 檢查用戶輸入的文件名是否在白名單中
if (in_array($file, $allowed_files)) {
    echo "File '$file' is allowed for download.";
} else {
    echo "File '$file' is not allowed.";
}
?>