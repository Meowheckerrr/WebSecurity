<?php
$filePath = "./meowhecker.txt"; // 要删除的文件的路径

if (unlink($filePath)) {
    echo "File '$filePath' has been deleted successfully.";
} else {
    echo "Failed to delete the file.";
}
?>
