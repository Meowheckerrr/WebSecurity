<?php
session_start();

echo "PHP Server Starting~";
// 用于存储消息的简单数组
if (!isset($_SESSION['messages'])) {
    $_SESSION['messages'] = [];
}

// Home 页面
$preFixPath = "/XSS/blindXSS/php/vulnServer.php";

if ($_SERVER['REQUEST_URI'] == $preFixPath . '/') {
    echo '
        <h1>Welcome to the Guestbook</h1>
        <a href="/XSS/blindXSS/php/vulnServer.php/message">Leave a message</a><br>
        <a href="/XSS/blindXSS/php/vulnServer.php/admin">Admin View</a>
    ';
}

// Message 提交页面
if ($_SERVER['REQUEST_URI'] == $preFixPath . '/message') {
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $message = $_POST['message'];
        if ($message) {
            // 将消息存储在 session 中的数组
            $_SESSION['messages'][] = ['message' => $message];
            header('Location: /XSS/blindXSS/php/vulnServer.php/');
            exit();
        } else {
            echo 'Please enter a message.';
        }
    }

    echo '
        <h1>Leave a Message</h1>
        <form action="/XSS/blindXSS/php/vulnServer.php/message" method="post">
            <label for="message">Message:</label><br>
            <textarea id="message" name="message"></textarea><br>
            <input type="submit" value="Submit">
        </form>
        <a href="/XSS/blindXSS/php/vulnServer.php/">Back to Home</a>
    ';
}

// Admin 查看页面
if ($_SERVER['REQUEST_URI'] == $preFixPath .'/admin') {
    $messages_html = '';
    foreach ($_SESSION['messages'] as $msg) {
        // XSS !!!!!!!!!
        $messages_html .= "Message: {$msg['message']}<br><br>";
    }

    echo "
        <h1>Admin View</h1>
        <div>{$messages_html}</div>
        <a href='/XSS/blindXSS/php/vulnServer.php/'>Back to Home</a>
    ";
}
?>