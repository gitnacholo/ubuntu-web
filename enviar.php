<?php
/**
 * enviar.php — Backend del formulario de contacto
 * Las credenciales SMTP viven en .env (NO en este fichero, NUNCA en git)
 */

error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', __DIR__ . '/../private/php_errors.log');

// ── Cargar .env ────────────────────────────────────────────────
function loadEnv(string $file): array {
    if (!is_readable($file)) {
        throw new RuntimeException(".env no encontrado o no legible");
    }
    $env = [];
    foreach (file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
        $line = trim($line);
        if ($line === '' || $line[0] === '#') continue;
        [$k, $v] = array_pad(explode('=', $line, 2), 2, '');
        $k = trim($k);
        $v = trim($v);
        if (strlen($v) >= 2 && ($v[0] === '"' || $v[0] === "'")) {
            $v = substr($v, 1, -1);
        }
        $env[$k] = $v;
    }
    return $env;
}

try {
    $config = loadEnv(__DIR__ . '/.env');
} catch (Throwable $e) {
    error_log('enviar.php: ' . $e->getMessage());
    header('Location: contacte.html?error=config');
    exit;
}

foreach (['SMTP_HOST','SMTP_PORT','SMTP_USER','SMTP_PASS','MAIL_FROM','MAIL_FROM_NAME','MAIL_TO','MAIL_TO_NAME'] as $k) {
    if (empty($config[$k])) {
        error_log("enviar.php: falta $k en .env");
        header('Location: contacte.html?error=config');
        exit;
    }
}

// ── PHPMailer (instalación manual en vendor/) ─────────────────
require_once __DIR__ . '/vendor/phpmailer/phpmailer/src/Exception.php';
require_once __DIR__ . '/vendor/phpmailer/phpmailer/src/SMTP.php';
require_once __DIR__ . '/vendor/phpmailer/phpmailer/src/PHPMailer.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

// ── Solo POST ─────────────────────────────────────────────────
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    http_response_code(405);
    header('Location: contacte.html?error=metodo_no_permitido');
    exit;
}

// ── Sanitizar ─────────────────────────────────────────────────
$nombre  = trim(strip_tags($_POST['nom']      ?? ''));
$email   = trim(strip_tags($_POST['email']    ?? ''));
$asunto  = trim(strip_tags($_POST['assumpte'] ?? '')) ?: 'Nou contacte des de la web Ubuntu';
$mensaje = trim(strip_tags($_POST['missatge'] ?? ''));

$errores = [];
if ($nombre === '')                                              $errores[] = 'El nombre es obligatorio.';
if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) $errores[] = 'El correo electrónico no es válido.';
if ($mensaje === '')                                             $errores[] = 'El mensaje es obligatorio.';

if ($errores) {
    header('Location: contacte.html?error=' . urlencode(implode('; ', $errores)));
    exit;
}

// ── Cuerpo ────────────────────────────────────────────────────
$cuerpo  = "Nou missatge de contacte des de la web Ubuntu\n";
$cuerpo .= "=====================================\n\n";
$cuerpo .= "Nombre:  {$nombre}\n";
$cuerpo .= "Email:   {$email}\n";
$cuerpo .= "Asunto:  {$asunto}\n\n";
$cuerpo .= "Mensaje:\n{$mensaje}\n\n";
$cuerpo .= "---\n";
$cuerpo .= 'Enviado desde: ' . ($_SERVER['HTTP_HOST'] ?? '-') . "\n";
$cuerpo .= 'IP: '            . ($_SERVER['REMOTE_ADDR'] ?? '-') . "\n";
$cuerpo .= 'Fecha: '         . date('Y-m-d H:i:s') . "\n";

// ── Enviar ────────────────────────────────────────────────────
$mail = new PHPMailer(true);
try {
    $mail->isSMTP();

    $mail->Host       = $config['SMTP_HOST'];
    $mail->SMTPAuth   = true;
    $mail->Username   = $config['SMTP_USER'];
    $mail->Password   = $config['SMTP_PASS'];
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port       = (int) $config['SMTP_PORT'];
    $mail->CharSet    = 'UTF-8';
    $mail->Encoding   = '8bit';

    $mail->setFrom($config['MAIL_FROM'], $config['MAIL_FROM_NAME']);
    $mail->addAddress($config['MAIL_TO'], $config['MAIL_TO_NAME']);
    $mail->addReplyTo($email, $nombre);

    $mail->isHTML(false);
    $mail->Subject = $asunto;
    $mail->Body    = $cuerpo;

    $mail->send();

    header('Location: contacte.html?enviado=1');
    exit;

} catch (Exception $e) {
    error_log('Error enviando email: ' . $mail->ErrorInfo);
    header('Location: contacte.html?error=error_envio');
    exit;
}
