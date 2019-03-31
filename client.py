# chat_client.py
import sys
import socket
import select
 
def chat_client():
    if(len(sys.argv) < 3) :
        print( 'Usage : python3 chat_client.py hostname port')
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print ('Unable to connect')
        sys.exit()
     
    print ('Connected to remote host. You can start sending messages')
    username = input("Enter Your Username: ")
    sys.stdout.write('<%s> ' %username); sys.stdout.flush()
    s.send(username.encode()) 
    
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets,write_sockets,error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:            
            if sock == s:
                # incoming message from remote server, s
                data = (sock.recv(4096))
                data = data.decode()
                if not data :
                    print('\nDisconnected from chat server')
                    sys.exit()
                else :
                    #print (data)
                    sys.stdout.write(data)
                    sys.stdout.write('<%s> ' %username); sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline().encode()
                s.send(msg)
                sys.stdout.write('<%s> ' %username); sys.stdout.flush() 

if __name__ == "__main__":
    sys.exit(chat_client())

