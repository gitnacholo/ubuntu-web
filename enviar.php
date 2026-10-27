<?php
/**
 * enviar.php - Backend PHP para procesar el formulario de contacto
 * Envía los datos del formulario a ubuntu@associacioubuntu.org
 * 
 * Requiere: PHP con mail() habilitado o configuración SMTP en php.ini
 * Para producción, configurar SMTP en php.ini o usar PHPMailer
 */

// Configuración
$destinatario = "ubuntu@associacioubuntu.org";
$asunto_defecto = "Nuevo contacto desde la web Ubuntu";

// Solo permitir POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('Location: ../contacte.html?error=metodo_no_permitido');
    exit;
}

// Validar y sanitizar datos
$nombre = isset($_POST['nom']) ? trim(strip_tags($_POST['nom'])) : '';
$email = isset($_POST['email']) ? trim(strip_tags($_POST['email'])) : '';
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
    // Redirigir con errores
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

// Headers del email
$headers = "From: {$nombre} <{$email}>\r\n";
$headers .= "Reply-To: {$email}\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

// Enviar email
$enviado = mail($destinatario, $asunto, $cuerpo, $headers);

// Redireccionar
if ($enviado) {
    // Éxito - redirigir a página de gracias
    // Detectar idioma desde la URL de origen o usar por defecto catalán
    $referer = $_SERVER['HTTP_REFERER'] ?? '';
    if (strpos($referer, '/en/') !== false) {
        header('Location: ../thank-you.html?enviado=1');
    } elseif (strpos($referer, '/es/') !== false) {
        header('Location: ../gracias.html?enviado=1');
    } else {
        header('Location: ../gràcies.html?enviado=1');
    }
} else {
    // Error al enviar
    header('Location: ../contacte.html?error=error_envio');
}
exit;