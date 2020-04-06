#!python

import pickle
import socket
# to test latency
from directkeys import PressKey, W, A, S, D,ReleaseKey

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
        temp = CSocket.recv(100)
        if not temp:
            break
        else:
            #fh.write(data+'-'+str(dt.minute)+':'+str(dt.second)+'\n')
            data = pickle.loads(temp)
            r_v = int(data['Y'])
            #find alternative to press keys

            if r_v < 0:
                r_v = (-1*r_v)
                if data['T'] and data['B']:
                    PressKey(W)
                    PressKey(S)
                    PressKey(A)
                    ReleaseKey(W)
                    ReleaseKey(S)

                elif data['T']:
                    PressKey(W)
                    PressKey(A)
                    ReleaseKey(W)
                    ReleaseKey(A)

                elif data['B']:
                    PressKey(S)
                    PressKey(A)
                    ReleaseKey(S)
                    ReleaseKey(A)
                else:
                    PressKey(A)
                    ReleaseKey(A)
            elif r_v > 0:
                if data['T'] and data['B']:
                    PressKey(W)
                    PressKey(S)
                    PressKey(D)
                    ReleaseKey(W)
                    ReleaseKey(S)
                    ReleaseKey(D)

                elif data['T']:
                    PressKey(W)
                    PressKey(D)
                    ReleaseKey(W)
                    ReleaseKey(D)
                elif data['B']:
                    PressKey(S)
                    PressKey(D)
                    ReleaseKey(S)
                    ReleaseKey(D)
                else:
                    PressKey(D)
                    ReleaseKey(D)
            else:
                if data['T'] and data['B']:
                    PressKey(W)
                    PressKey(S)
                    ReleaseKey(W)
                    ReleaseKey(S)
                elif data['T']:
                    PressKey(W)
                    ReleaseKey(W)
                elif data['B']:
                    PressKey(S)
                    ReleaseKey(S)



    choice = input('Do you Want shut Down Server . (y/n):')
    if choice == 'y':
        break
        fh.close()
    else:
        continue
CSocket.close()
