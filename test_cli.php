<?php
// Direct test of enviar.php via CLI
$_POST = [
    'nom' => 'Test User',
    'email' => 'test@example.com',
    'assumpte' => 'Test',
    'missatge' => 'Test message from PHP form',
    '_subject' => 'Test from PHP form'
];

require_once 'enviar.php';
echo "Done!\n";