import socket, time, json
from data import SERVER, PORT
from auth import auth

server = (SERVER, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER, 0))
print(f'A connetion with the server has been made: {sock.getsockname()[0]} {sock.getsockname()[1]} ')


while True:
    name = input('Name: ')
    password = input('Password: ')

    if auth(name, password):
        break


while True:
    try:
        message = (f'User {name}: send message ' + str(input('Message: '))).encode()
        sock.sendto(message, server)
        if message.decode('UTF-8').split(':')[1].strip().split(' ')[2] == 'q':
            raise Exception
        print(f'Information "{message.decode()}" in the server.')
        data, addr = sock.recvfrom(1024)
        print(f'Information "{data.decode()}" received from the server.')
    except Exception:
        print(f'Connection with the server {SERVER} {PORT} broke.')
        break
    except KeyboardInterrupt:
        print(f'Connection with the server {SERVER} {PORT} failed. To properly exit, type "q".')
        break
    time.sleep(2)
sock.close()
