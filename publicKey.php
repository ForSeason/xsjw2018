<?php
header("content-type:text/html;charset=utf-8");
$user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36";

$url = 'http://xsjw2018.scuteo.com/jwglxt/xtgl/login_slogin.html';
$curl = curl_init();
$cookie_jar = @tempnam('./tmp','cookie'); //tempnam--建立一个具有唯一文件名的文件
curl_setopt($curl, CURLOPT_URL, $url);//这里写上处理登录的界面
curl_setopt($curl, CURLOPT_COOKIEJAR, $cookie_jar);//把返回来的cookie信息保存在$cookie_jar文件中
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);//设定返回的数据是否自动显示
curl_setopt($curl, CURLOPT_HEADER, false);//设定是否显示头信息
curl_setopt($curl, CURLOPT_NOBODY, false);//设定是否输出页面内容
$html = curl_exec($curl);//返回结果
curl_close($curl);
$pattern = '/<input type=\"hidden\" id=\"csrftoken\" name=\"csrftoken\" value=\"(.*?)\"\/>/';
preg_match_all($pattern, $html, $arr);
$csrftoken = $arr[1][0];


$url  = 'http://xsjw2018.scuteo.com/jwglxt/xtgl/login_getPublicKey.html?time='.time().'00';
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $url);//这里写上处理登录的界面
curl_setopt($curl, CURLOPT_COOKIEFILE, $cookie_jar);//把返回来的cookie信息保存在$cookie_jar文件中
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);//设定返回的数据是否自动显示
curl_setopt($curl, CURLOPT_HEADER, false);//设定是否显示头信息
curl_setopt($curl, CURLOPT_NOBODY, false);//设定是否输出页面内容
$json = curl_exec($curl);
$arr = json_decode($json, TRUE);
curl_close($curl);
$pw = 'ysy604822';
$command = sprintf('python3 crypto.py %s %s %s', $arr['modulus'], $arr['exponent'], $pw);
unset($output);
exec($command, $output);


$post = array();
$post['csrftoken'] = $csrftoken;
$post['yhm'] = '201830480189';
$post['mm'] = $output[0];
$url  = 'http://xsjw2018.scuteo.com/jwglxt/xtgl/index_initMenu.html';
$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $url);                
curl_setopt($curl, CURLOPT_POST, 1);
curl_setopt($curl, CURLOPT_HEADER, 1);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($curl, CURLOPT_COOKIEFILE, $cookie_jar);
curl_setopt($curl, CURLOPT_POSTFIELDS, $post);
curl_setopt($curl, CURLOPT_USERAGENT,$user_agent);
curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
$html = curl_exec($curl);
curl_close($curl);
var_dump($post);
var_dump($html);
var_dump($cookie_jar);
