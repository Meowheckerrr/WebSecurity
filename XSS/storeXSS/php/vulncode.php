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
} catch (PDOException $e) {

}
// Exploit bid=1 UNION ALL SELECT NULL,NULL,CONCAT(0x7171786b71,0x7065724158775947494875744f6a6458475944476961446a5869656358616968765143625a645643,0x716a786271),NULL-- -
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
</head>
<body>

<h1>Blog Posts</h1>

<?php if (!empty($posts)): ?>
    <?php foreach ($posts as $post): ?>
        <div class="blog-post">
            <?= phpinfo(); ?> 
            <h2><a href="blog.php?bid=<?= $post['bid']; ?>"><?= htmlspecialchars($post['title']); ?></a></h2>
            <p><?= htmlspecialchars($post['content']); ?></p>
            <p><small>Posted on <?= htmlspecialchars($post['created_at']); ?></small></p>
        </div>
        <hr>
    <?php endforeach; ?>
<?php else: ?>
    <p>No posts found.</p>
<?php endif; ?>

</body>
</html>