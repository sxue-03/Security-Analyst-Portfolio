import socket
target = input('enter ip address to scan:')
for port in range(1, 6463):
    s = socket.socket()
    s.settimeout(0.1)
    result = s.connect_ex((target,port))
    if result == 0:
        print('port', port, 'is open')
    s.close()
