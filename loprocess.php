
<?php
 $conn=mysqli_connect('localhost','root','','ants');
 if($conn==false){
    echo'Server-Not-Respned!';
 }else{
    echo'...';
 }

 $value1=$_REQUEST['first-name'];
 $value2=$_REQUEST['last-name'];
 $value3=$_REQUEST['u-comment'];

 $sql="INSERT INTO `users-ajax`(`f-name`,`l-name`,`userc`) VALUES('$value1','$value2','$value3')";
 $fbdata=mysqli_query($conn,$sql);
 if($fbdata==false){
    echo'Database-Not-Responed!';
 }else{
    echo'...';
 }





?>