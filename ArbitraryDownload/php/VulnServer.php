<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];
     echo "Current file path: " . __FILE__;
    echo $file;
    if (file_exists($file)) {
        header('Content-Description: File Transfer');
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="'.basename($file).'"');
        header('Expires: 0');
        header('Cache-Control: must-revalidate');
        header('Pragma: public');
        header('Content-Length: ' . filesize($file));
        flush(); 
        readfile($file);
        echo "File Download Successfully";
        exit;
    } else {
        echo "File does not exist!";
    }
} else {
    echo "No file specified!";
}
?>