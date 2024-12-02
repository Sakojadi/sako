<?php
$conn = new mysqli("localhost", "root", "", "clients");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM clients";
$result = $conn->query($sql);

$clients = array();
while($row = $result->fetch_assoc()) {
    $clients[] = $row;
}

echo json_encode($clients);
$conn->close();
?>
