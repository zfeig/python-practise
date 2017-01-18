<?php
  
 
  function returnMsg($msg,$status,$res=[]){
   $ret = [
     'status' => intval($status),
     'msg' => $msg,
     'result' => $res
   ];
   echo json_encode($ret,JSON_UNESCAPED_UNICODE);
   // exit(0);
  }

  
  header("Content-Type:application/json;charset=utf-8");
  
  $raw = json_decode(file_get_contents("php://input"),true);  
  //returnMsg('参数错误！',400,$raw);


  $user = isset($_POST['user']) ? trim($_POST['user']) : $raw['user'];
  $pwd = isset($_POST['pwd']) ? trim($_POST['pwd']) :  $raw['pwd'];

    

  
  if (!$user || !$pwd) {
     returnMsg('参数错误！',400);
  }

  $is_valid_user =  $_COOKIE && $_COOKIE['valid_user'] = 'admin';

  if ($user == 'zfeig' && $pwd == '123456'){
      $role = $is_valid_user ? 'admin':'master';
      returnMsg("登录成功！",200,["info"=>"welcome to {$role}!"]);

  }else{
     returnMsg('登陆失败，请检查！',404,['user'=>$user,'pwd'=>$pwd]);
  }

?>
