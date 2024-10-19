<?php
$allowed_dir = dirname(__FILE__) . '/downloads/';                                                                            //'C:/Users/Meowhecker/Desktop/WebSecurity/ArbitraryDownload/php/downloads/'
$allowed_files = ['test.txt','example.pdf', 'report.docx', 'image.jpg'];

if (isset($_GET['file'])) {
    $file = basename($_GET['file']);
    $file_path = $allowed_dir . $file;

    if (in_array($file, $allowed_files)){
        if (file_exists($file_path)) {
            header('Content-Description: File Transfer');
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename="'.basename($file_path).'"');
            header('Expires: 0');
            header('Cache-Control: must-revalidate');
            header('Pragma: public');
            header('Content-Length: ' . filesize($file_path));
            flush(); 
            readfile($file_path);
            exit;
            
        } else {
            echo "File does not exist!";
        }
    }else {
        echo "Not Allow !!!!!";
    }
    

} else {
    echo "No file specified!";
}
?>