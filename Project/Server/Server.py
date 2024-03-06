import socket

def start_server(server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((server_ip, server_port))
    sock.listen(1)
    return sock

def handle_client(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print('received request: ' + data.decode())
        # Send the peer's public IP and port as a response
        response = 'peer_public_ip:peer_public_port'
        sock.sendall(response.encode())

def main():
    server_ip = 'server_public_ip'
    server_port = 12345

    server_sock = start_server(server_ip, server_port)
    while True:
        client_sock, client_address = server_sock.accept()
        print('accepted connection from: ' + str(client_address))
        handle_client(client_sock)
        client_sock.close()

if __name__ == '__main__':
    main()