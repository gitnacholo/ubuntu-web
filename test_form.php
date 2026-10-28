<?php
// Test script using streams instead of cURL
$postData = http_build_query([
    'nom' => 'Test User',
    'email' => 'test@example.com',
    'assumpte' => 'Test',
    'missatge' => 'Test message from PHP form',
    '_subject' => 'Test from PHP form'
]);

$context = [
    'http' => [
        'method' => 'POST',
        'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
        'content' => $postData,
        'timeout' => 10
    ]
];

$context = stream_context_create($context);
$response = file_get_contents('http://localhost:8086/enviar.php', false, $context);
echo "Response: " . $response;
echo "\nDone!";