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

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['id'])) {
        $id = $_POST['id'];
        
        // Log the query for debugging purposes
        error_log("Attempting to delete client with ID: $id");

        $query = "DELETE FROM clients WHERE id = ?";
        $stmt = $conn->prepare($query);
        $stmt->bind_param("i", $id);

        if ($stmt->execute()) {
            echo json_encode(["success" => true, "message" => "Client deleted successfully."]);
        } else {
            error_log("Delete query failed: " . $stmt->error); // Log any query execution error
            echo json_encode(["success" => false, "message" => "Failed to delete client."]);
        }

        $stmt->close();
        $conn->close();
    } else {
        echo json_encode(["success" => false, "message" => "No ID provided."]);
    }
}
?>
