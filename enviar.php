<?php
/**
 * enviar.php - Backend PHP para procesar el formulario de contacto
 * Usa PHPMailer con SMTP autenticado (info@associacioubuntu.org)
 * 
 * Requiere: composer require phpmailer/phpmailer
 * O descargar PHPMailer manualmente en vendor/
 */

// Habilitar reporte de errores para debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('log_errors', 1);
ini_set('error_log', __DIR__ . '/php_errors.log');

// Cargar PHPMailer - registrar autoloader PSR-4 ANTES de los use statements
require_once __DIR__ . '/vendor/phpmailer/phpmailer/src/Exception.php';
require_once __DIR__ . '/vendor/phpmailer/phpmailer/src/SMTP.php';
require_once __DIR__ . '/vendor/phpmailer/phpmailer/src/PHPMailer.php';

// Registrar autoloader PSR-4 para PHPMailer
spl_autoload_register(function ($class) {
    $prefix = 'PHPMailer\\PHPMailer\\';
    $base_dir = __DIR__ . '/vendor/phpmailer/phpmailer/src/';
    $len = strlen('PHPMailer\\PHPMailer\\');
    if (strncmp($class, $prefix, $len) !== 0) {
        return;
    }
    $relative_class = substr($class, $len);
    $file = $base_dir . str_replace('\\', '/', $relative_class) . '.php';
    if (file_exists($file)) {
        require_once $file;
    }
});

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

// Configuración SMTP
$config = [
    'host'       => 'mail.associacioubuntu.org',  // Cambia por tu servidor SMTP real
    'port'       => 587,                           // 587 (STARTTLS) o 465 (SSL)
    'username'   => 'hola@associacioubuntu.org',
    'password'   => 'JSPTE2008*',
    'encryption' => 'tls',                         // 'tls' para 587, 'ssl' para 465
    'from_email' => 'info@associacioubuntu.org',
    'from_name'  => 'Associació Ubuntu Web',
    'to_email'   => 'ubuntu@associacioubuntu.org',
    'to_name'    => 'Associació Ubuntu',
];

// Solo permitir POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('Location: ../contacte.html?error=metodo_no_permitido');
    exit;
}

// Validar y sanitizar datos
$nombre = isset($_POST['nom']) ? trim(strip_tags($_POST['nom'])) : '';
$email  = isset($_POST['email']) ? trim(strip_tags($_POST['email'])) : '';
$asunto_form = isset($_POST['assumpte']) ? trim(strip_tags($_POST['assumpte'])) : '';
$mensaje = isset($_POST['missatge']) ? trim(strip_tags($_POST['missatge'])) : '';

// Validación básica
$errores = [];

if (empty($nombre)) {
    $errores[] = "El nombre es obligatorio.";
}

if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errores[] = "El correo electrónico no es válido.";
}

if (empty($mensaje)) {
    $errores[] = "El mensaje es obligatorio.";
}

if (!empty($errores)) {
    $errores_str = implode('|', $errores);
    header("Location: ../contacte.html?error=" . urlencode(implode('; ', $errores)));
    exit;
}

// Asunto del email
$asunto = isset($_POST['_subject']) ? trim(strip_tags($_POST['_subject'])) : "Nuevo contacto desde la web Ubuntu";
if (isset($_POST['assumpte']) && trim($_POST['assumpte']) !== '') {
    $asunto = trim(strip_tags($_POST['assumpte']));
}

// Construir cuerpo del email
$cuerpo = "Nuevo mensaje de contacto desde la web Ubuntu\n";
$cuerpo .= "=====================================\n\n";
$cuerpo .= "Nombre: {$nombre}\n";
$cuerpo .= "Email: {$email}\n";
$cuerpo .= "Asunto: {$asunto}\n\n";
$cuerpo .= "Mensaje:\n{$mensaje}\n\n";
$cuerpo .= "---\n";
$cuerpo .= "Enviado desde: " . $_SERVER['HTTP_HOST'] . "\n";
$cuerpo .= "IP: " . $_SERVER['REMOTE_ADDR'] . "\n";
$cuerpo .= "Fecha: " . date('Y-m-d H:i:s') . "\n";

// Configurar PHPMailer
$mail = new PHPMailer(true);

try {
    // Configuración SMTP
    $mail->isSMTP();
    $mail->Host       = 'mail.associacioubuntu.org';  // CAMBIA por tu servidor SMTP real
    $mail->SMTPAuth   = true;
    $mail->Username   = 'info@associacioubuntu.org';
    $mail->Password   = 'JSPTE2008';
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // 'ssl' para 465, 'tls' para 587
    $mail->Port       = 587;                             // 587 (STARTTLS) o 465 (SSL)
    $mail->CharSet    = 'UTF-8';
    $mail->Encoding   = '8bit';

    // Configuración de envío
    $mail->setFrom('info@associacioubuntu.org', 'Associació Ubuntu Web');
    $mail->addAddress('ubuntu@associacioubuntu.org', 'Associació Ubuntu');
    $mail->addReplyTo($email, $nombre);
    
    // Contenido
    $mail->isHTML(false);
    $mail->Subject = $asunto;
    $mail->Body    = "Nuevo mensaje de contacto desde la web Ubuntu\n";
    $mail->Body    .= "=====================================\n\n";
    $mail->Body    .= "Nombre: {$nombre}\n";
    $mail->Body    .= "Email: {$email}\n";
    $mail->Body    .= "Asunto: {$asunto}\n\n";
    $mail->Body    .= "Mensaje:\n{$mensaje}\n\n";
    $mail->Body    .= "---\n";
    $mail->Body    .= "Enviado desde: " . $_SERVER['HTTP_HOST'] . "\n";
    $mail->Body    .= "IP: " . $_SERVER['REMOTE_ADDR'] . "\n";
    $mail->Body    .= "Fecha: " . date('Y-m-d H:i:s') . "\n";

    // Configuración de depuración (quitar en producción)
    // $mail->SMTPDebug = SMTP::DEBUG_SERVER;
    // $mail->Debugoutput = function($str, $level) { error_log("SMTP: $str"); };

    $mail->send();

    // Éxito - detectar idioma para redirección
    $referer = $_SERVER['HTTP_REFERER'] ?? '';
    if (strpos($referer, '/en/') !== false) {
        header('Location: ../thank-you.html?enviado=1');
    } elseif (strpos($referer, '/es/') !== false) {
        header('Location: ../gracias.html?enviado=1');
    } else {
        header('Location: ../gràcies.html?enviado=1');
    }
    exit;

} catch (Exception $e) {
    error_log("Error enviando email: " . $mail->ErrorInfo);
    header('Location: ../contacte.html?error=error_envio');
    exit;
}