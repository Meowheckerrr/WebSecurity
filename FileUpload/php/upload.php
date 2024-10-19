<?php
//Upload Path ! 
$target_dir = "uploads/";
if (!is_dir($target_dir)) {
    mkdir($target_dir, 0755, true);
}

//Upload File Information
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$fileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

Check

//Only Allow Picture 
if (isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if ($check !== false) {
        echo "File is a Picture - " . $check["mime"] . "。";
        $uploadOk = 1;
    } else {
        echo "FIle is not a Picture 。";
        $uploadOk = 0;
    }
}

// Check duplicate files 
if (file_exists($target_file)) {
    echo "Sorry, File exists。";
    $uploadOk = 0;
}

// Limit FIle Size 500KB
if ($_FILES["fileToUpload"]["size"] > 500000) {
    echo "Sorry, File to BiGGGGGGGGGGGG。";
    $uploadOk = 0;
}

// Limit Upload File type
if ($fileType != "jpg" && $fileType != "png" && $fileType != "jpeg" && $fileType != "gif") {
    echo "Sorry，only Alow JPG, JPEG, PNG & GIF Files!。";
    $uploadOk = 0;
}

// Upload File 
if ($uploadOk == 0) {
    echo "Not Allow to Upload";
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "File:" . basename($_FILES["fileToUpload"]["name"]) . " Upload Successfully";
    } else {
        echo "Sorry, Upload Failed!";
    }
}
?>


