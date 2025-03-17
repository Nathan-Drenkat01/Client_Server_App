import socket

# Server's IP address and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # The same port used by the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Start the chat
while True:
    # Get user input (message from the client)
    message = input("You: ")
    
    # Send message to server
    client_socket.sendall(message.encode())

    if message.lower() == 'exit':
        print("Ending chat.")
        break

    # Receive the server's response
    server_response = client_socket.recv(1024).decode()
    print(f"Server: {server_response}")

# Close the connection
client_socket.close()
