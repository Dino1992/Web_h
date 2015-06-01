import socket 
import os.path

sock = socket.socket() 
sock.bind(('localhost',8000))
sock.listen(5)
buffer_size = 2048

while True:
    connection, address  = sock.accept()
    buffer = connection.recv(buffer_size)
    path = ''
    result = buffer.split('\n')[0].split(' ')[1]
    path = './' + result 
    if not os.path.isfile(path):
            path ='./index.html' 
            
    file = open(path, 'rb')
    connection.send("""HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n""" + file.read())
    file.close()
    connection.close()
sock.close() 