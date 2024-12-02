<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "clients";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Debug: Print out the POST data for verification
// Uncomment this to see the full POST data in case of errors
// var_dump($_POST); 

if (isset($_POST['name'])) {
    // Get the client name from POST data
    $name = $_POST['name'];

    // Prepare the SQL query to insert a new client
    $sql = "INSERT INTO clients (name) VALUES ('$name')";

    if ($conn->query($sql) === TRUE) {
        echo "New client added successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} else {
    // If 'name' is not set in the POST data, print an error message
    echo "Error: 'name' parameter is missing in the POST request.";
}

$conn->close();
?>
