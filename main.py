from socket import *  # Import socket does not work...

# Establish a port number for the server process
server_port = 12000

# Create the server socket and bind it to the port
server_socket = socket(AF_INET, SOCK_STREAM)  # Sock stream is used for TCP
server_socket.bind(('', server_port))
server_socket.listen(1)

print('The server is ready to receive')

# Do the following in an infinite loop to allow for arbitrarily many connections
while True:
    # Create a specific server socket for each client connection
    connection_socket, addr = server_socket.accept()

    # Receive a message from the client and uppercase the message
    sentence = connection_socket.recv(1024).decode()

    # Process the received message
    print(f'Received from {addr}: {sentence}')
    capitalized_sentence = sentence.upper()

    # send the uppercase message back to the client
    connection_socket.send(capitalized_sentence.encode())

    # CLose this connection
    connection_socket.close()
