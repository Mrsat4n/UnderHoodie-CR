import socket
import threading
import pyfiglet
from pyfiglet import Figlet
import os


#clear screen
os.system('cls' if os.name == 'nt' else 'clear')




#aTAG LINE
print('''\033[5;31;40m


     _____                                          _____                                         
  __|  _  |__  ____   _  _____   ______  _____   __|  _  |__  _____  _____  _____   ____  ______  
 |  | | |    ||    \ | ||     \ |   ___||     | |  |_| |    |/     \/     \|     \ |    ||   ___| 
 |  |_| |    ||     \| ||      \|   ___||     \ |   _  |    ||     ||     ||      \|    ||   ___| 
 |______|  __||__/\____||______/|______||__|\__\|__| |_|  __|\_____/\_____/|______/|____||______| 
    |_____|                                        |_____|                                        
\033[0;34;40m
\033[5;34;40m
           ______  _______     
         .' ___  ||_   __ \    
 ______ / .'   \_|  | |__) |   SERVER*
|______|| |         |  __ /    
        \ `.___.'\ _| |  \ \_  
         `.____ .'|____| |___| v.BETA
\033[0;31;40m
\033[1;32;40m
                                    -OJASWA RHX V.01 (2021)                                                                            
                                         



#YOUR OWN PRIVATE CHAT ROOMS
\033[0;37;40m
    ''')





#DATA
host="127.0.0.1"

#assign name to server

port=int(input("\033[0;32;40m Enter A Free Port [4444,1500,1604,1716] : \033[0;35;40m"))
servername= (input("\033[0;32;40m ENTER THE SERVER NAME : \033[0;35;40m"))
from pyfiglet import Figlet
rectanglefont = Figlet(font='rectangles')
#delete above
os.system('cls' if os.name == 'nt' else 'clear')


print(rectanglefont.renderText(servername)+"\033[0;32;40m SERVER STARTED \033[5;32;40m  \033[0;37;40m")



#server startup

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
cport=server.getsockname()[1]
print(f"\033[2;32;40m Socket created using [Port] : {cport}\n")
server.listen()
print(f"Start dynamic IP using [ngrok tcp {port}] \033[0;37;40m\n")

#Clients & Names
clients=[]
names=[]
print("\033[5;31;40m  LISTENING.....\033[0;31;40m\n")

#function to send messges to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)
        
#function to handling connected clients over network
def handle(client):
    while True:
        try:
            #broadcast message
            message=client.recv(1024)
            broadcast(message)
        except:
            #if client gets diconnected
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            broadcast('\033[1;35;40m {} \033[5;31;40m left! \033[0;31;40m'.format(name).encode('ascii'))
            print(f"\033[1;35;40m {name} \033[5;34;40m LEFT SERVER! \033[0;34;40m")
            names.remove(name)
            break
            
            
            
#recieving /listening adding clients
def receive():
    while True:
        
        #Accept Entry
        client,address=server.accept()
        print(f"\033[1;33;40m Connected with {str(address)}\033[0;37;40m")


        
        #implementing and storing names
        client.send("HOODIE".encode("ascii"))
        name=client.recv(1024).decode("ascii")
        names.append(name)
        clients.append(client)
        
        
        #broadcast names
        print(f"\033[1;31;40m {name} \033[0;37;40m \033[5;31;40m CONNECTED ! \033[0;31;40m")
        broadcast("\033[1;33;40m {} joined !\033[2;32;40m".format(name).encode('ascii'))
        client.send("\033[5;31;40m Connected to server! \033[0;31;40m \033[0;37;40m ".encode("ascii"))
        client.send(rectanglefont.renderText(servername).encode("ascii"))
        client.send("Ctrl+C/Z/X To leave the server ! ".encode("ascii"))

        
        #handling Thread for clients
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

receive()
        
        

