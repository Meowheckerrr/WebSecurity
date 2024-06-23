<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <?php
    if (isset($_GET['query'])) {
        $query = $_GET['query'];
        echo "<p>Results for: " . $query . "</p>"; // 直接输出用户输入，没有过滤
    } else {
        echo "<p>No search query provided.</p>";
    }
    ?>
    <a href="index.php">Back to Home</a>
</body>
</html>