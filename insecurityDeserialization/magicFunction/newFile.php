<?php
$fileName = "meowhecker.txt"; 

// 'write modle" 
$file = fopen($fileName, "w");

if ($file) {

    $content = "Hello, World!\nThis is a new file created with PHP.";

    fwrite($file, $content);

    fclose($file);

    echo "File '$fileName' has been created and written successfully.";

} else {

    echo "Unable to create or write to the file.";

}
?>