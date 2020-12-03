<?php
error_reporting(-1);

/* データベース設定 */
define('DB_DNS', 'mysql:host=localhost; dbname=cri_sortable; charset=utf8');
define('DB_USER', 'root');
define('DB_PASSWORD', 'root');

/* データベースへ接続 */
try {
  $dbh = new PDO(DB_DNS, DB_USER, DB_PASSWORD);
  $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
} catch (PDOException $e){
    echo $e->getMessage();
    exit;
}

/* データベースへ登録 */
if(!empty($_POST['inputName'])){
  try{
    $sql  = 'INSERT INTO sortable(name) VALUES(:ONAMAE)';
    $stmt = $dbh->prepare($sql);

    $stmt->bindParam(':ONAMAE', $_POST['inputName'], PDO::PARAM_STR);
    $stmt->execute();

    header('location: http://localhost:8001/');
    exit();
  } catch (PDOException $e) {
      echo 'データベースにアクセスできません！'.$e->getMessage();
  }
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>8001-cri-sortable</title>
  <link href="css/style.css" rel="stylesheet">
</head>
<body>
<div id="wrapper">

<div id="input_form">
  <form action="index.php" method="POST">
    <input type="text" name="inputName">
    <input type="submit" value="登録">
  </form>
</div>

<div id="drag-area">
<?php
$sql = 'SELECT * FROM sortable';
$stmt = $dbh->query($sql);
foreach ($stmt as $result)){
  echo '  <div class="drag" data-num="'.$result['id'].'" style="left:'.$result['left_x'].'px; top:'.$result['top_y'].'px;">'.PHP_EOL;
  echo '    <p><span class="name">'.$result['id'].' '.$result['name'].'</span></p>'.PHP_EOL;
  echo '  </div>'.PHP_EOL;
}
?>
</div>

</div>
</body>
</html>
