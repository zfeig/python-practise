<?php
header("Content-Type:application/json;cahrset=utf-8");
$user= isset($_POST['user'])?$_POST['user'] : 'zfeig';
$pwd = isset($_POST['pwd'])?$_POST['pwd'] : '123456';
$ret = [
 "action" => "POST",
 "user" => $user,
 "pwd" => $pwd
];

echo json_encode($ret,true); 


?>
