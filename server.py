import socket
from data import SERVER, PORT

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    try:
        socket.bind((SERVER, 80))
    except PermissionError:
        socket.bind((SERVER, PORT))
        break
print('The server has be launched.')
print(f'Port: {PORT} - bugged')


def server():
    while True:
        data, addr = socket.recvfrom(1024)
        print(f'The client is connected to:  {addr}')
        client = f'ip {addr[0]} port {addr[1]}'
        if data.decode('UTF-8') == 'q':
            print(f'Client {client} - was disconnected.')
            break
        if not data:
            break
        socket.sendto(data.upper(), addr)
        print(f'The information "{data.decode("UTF-8")}" has been sent to the client - {client}')

    print('The server is disconnected.')


server()
