import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to bind the server

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (max 1 client in this example)
server_socket.listen(1)
print(f"Server is listening on {HOST}:{PORT}...")

# Accept the incoming connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Default responses
default_responses = {
    "hello": "Hello, how can I help you today?",
    "how are you": "I'm just a server, but I'm doing fine! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that. Can you try something else?"
}

# Begin the chat
while True:
    # Receive the client's message
    client_message = client_socket.recv(1024).decode()
    
    if client_message.lower() == 'exit':
        print("Client has ended the chat.")
        break

    print(f"Client: {client_message}")
    
    # Get the server's response based on the message
    response = default_responses.get(client_message.lower(), default_responses["default"])
    
    # Send the response to the client
    client_socket.sendall(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
