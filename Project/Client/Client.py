import socket

def connect_to_server(server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))
    return sock

def send_request_to_server(sock, request):
    sock.sendall(request.encode())

def receive_response_from_server(sock):
    return sock.recv(1024).decode()

def connect_to_peer(peer_ip, peer_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((peer_ip, peer_port))
    return sock

def main():
    server_ip = 'server_public_ip'
    server_port = 12345
    request = 'request_to_connect_to_peer'

    server_sock = connect_to_server(server_ip, server_port)
    send_request_to_server(server_sock, request)

    response = receive_response_from_server(server_sock)
    peer_ip, peer_port = response.split(':')
    server_sock.close()

    peer_sock = connect_to_peer(peer_ip, int(peer_port))
    # Now you can communicate with the peer using the `peer_sock` socket