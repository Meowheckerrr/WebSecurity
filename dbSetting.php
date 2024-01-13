<?php

$servername = "localhost";  
$username = "root";        
$password = "root"; 
$dbname = "testdb";       

$conn = new mysqli($servername, $username, $password);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "CREATE DATABASE IF NOT EXISTS testdb";
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully\n";
} else {
    echo "Error creating database: " . $conn->error . "\n";
}

$conn->select_db("testdb");

$sql = "CREATE TABLE IF NOT EXISTS addrbook (
    name VARCHAR(50) NOT NULL,
    phone CHAR(10)
)";

if ($conn->query($sql) === TRUE) {
    echo "Table created successfully\n";
} else {
    echo "Error creating table: " . $conn->error . "\n";
}

$sql = "INSERT INTO addrbook (name, phone) VALUES ('tom', '0912123456'), ('mary', '0912123567')";
if ($conn->query($sql) === TRUE) {
    echo "Data inserted successfully\n";
} else {
    echo "Error inserting data: " . $conn->error . "\n";
}

$conn->close();

?>