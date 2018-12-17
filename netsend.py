import socket

host, port = '127.0.0.1', 25001
data = 'this is a test string blah' # String of gods

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((host, port))
    sock.send(b'this is a test string')#.sendall(data.encode('utf-8'))
    new_data = sock.recv(1024).decode('utf-8')
    print(new_data)
finally:
    sock.close()
