#!python

import socket
# to test latency
#import datetime
#fh = open(r'm:/serverlog.txt','a')
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
byname = socket.gethostname()
#print(byname)
host = socket.gethostbyname(byname)

port = 9999

print('Host Name : %s Port Number : %d'%(str(host),port))

#BInding To Port...

server_socket.bind((host,port))
#server_socket.listen(1)
while True:
    server_socket.listen(1)
    CSocket,addr = server_socket.accept()
    print('Client IP : %s Port Number : %d'%(str(addr),port))

    #ask server to send directory Data
    #CSocket.send(str('dir').encode())
    while True:
        #dt = datetime.datetime.now()
        data = CSocket.recv(100).decode()
        if not data:
            break
        else:
            #fh.write(data+'-'+str(dt.minute)+':'+str(dt.second)+'\n')
            print(data)

    '''
    while True:
        if not (CSocket.recv(1000).decode()):
            time.sleep(3)
    #CSocket.send(str(input()).encode('utf-8'))
    '''
    choice = input('Do you Want shut Down Server . (y/n):')
    if choice == 'y':
        break
        fh.close()
    else:
        continue
CSocket.close()
