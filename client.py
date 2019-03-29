# client.py

import sys, socket, select

def welcome_message():
    print ''
    print "\n\n\t\t\t\tWELCOME TO CHATTY v1.0\t\t\n\t\t\t\t----------------------"
    print "Chatty is an Open Source Python Command Line Chat App Built On Python Web Sockets"
    print 'Author: Amitrajit Bose & Riddhi Nahata at University of Engineering & Management, Kolkata'
    print 'This is a Minor Academic Project and Must Not Be Used For Emergency Communication Purpose'
    print '\n'

def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py HOSTNAME PORT'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
    
    welcome_message()
    print 'Connected to remote host. You can start sending messages'
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:            
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()
            else :
                # user entered a message
                msg = sys.stdin.readline()
                s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush() 

if __name__ == "__main__":
    sys.exit(chat_client())

