<?php 
	session_start();

	$filename = $_SESSION['filename'];
	$path = "./uploads/";
	$mailto = "info@csaconsultants.in";
	$subject = "CV";
	$message = "CV sent via csaconsultants.in";
	$from_name="CSA cv";
	$from_mail="info@csaconsultants.in";
	$file = $path.$filename;
    $file_size = filesize($file);
    $handle = fopen($file, "r");
    $content = fread($handle, $file_size);
    //die($content);
    fclose($handle);
    $content = chunk_split(base64_encode($content));
    $uid = md5(uniqid(time()));
    $header = "From: ".$from_name." <".$from_mail.">\r\n";
    $header .= "MIME-Version: 1.0\r\n";
    $header .= "Content-Type: multipart/mixed; boundary=\"".$uid."\"\r\n\r\n";
    $header .= "This is a multi-part message in MIME format.\r\n";
    $header .= "--".$uid."\r\n";
    $header .= "Content-type:text/plain; charset=iso-8859-1\r\n";
    $header .= "Content-Transfer-Encoding: 7bit\r\n\r\n";
    $header .= $message."\r\n\r\n";
    $header .= "--".$uid."\r\n";
    $header .= "Content-Type: application/octet-stream; name=\"".$filename."\"\r\n"; // use different content types here
    $header .= "Content-Transfer-Encoding: base64\r\n";
    $header .= "Content-Disposition: attachment; filename=\"".$filename."\"\r\n\r\n";
    $header .= $content."\r\n\r\n";
    $header .= "--".$uid."--";
    if (mail($mailto, $subject, "", $header)) {
        $msg = "Your CV has been received. We will get back to you shortly.";
        $_SESSION['flag']=true;
    } else {
        $msg="Sorry, your file was not uploaded. Please send a mail to info@csaconsultants.in.";
        $_SESSION['flag']=false;
    }
    $_SESSION['msg']="<center><code>".$msg."</code></center>";
    header('Location:career.php');

// // send email
// if(mail("abhinavagrawal1995@gmail.com","My subject","test"))
// 	echo "sent";


?>