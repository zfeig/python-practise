<?php
header("Content-Type:application/json;cahrset=utf-8");
$user= isset($_GET['user'])?$_GET['user'] : 'zfeig';
$pwd = isset($_GET['pwd'])?$_GET['pwd'] : '123456';
$ret = [
 "action" => "GET",
 "user" => $user,
 "pwd" => $pwd
];

echo json_encode($ret,true); 


?>
