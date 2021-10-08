#!/bin/sh

#import
import socket
import threading
import pyfiglet
from pyfiglet import Figlet
import os

#clear screen
os.system('cls' if os.name == 'nt' else 'clear')


#aTAG LINE
print('''\033[5;34;40m


     _____                                          _____                                         
  __|  _  |__  ____   _  _____   ______  _____   __|  _  |__  _____  _____  _____   ____  ______  
 |  | | |    ||    \ | ||     \ |   ___||     | |  |_| |    |/     \/     \|     \ |    ||   ___| 
 |  |_| |    ||     \| ||      \|   ___||     \ |   _  |    ||     ||     ||      \|    ||   ___| 
 |______|  __||__/\____||______/|______||__|\__\|__| |_|  __|\_____/\_____/|______/|____||______| 
    |_____|                                        |_____|                                        
\033[0;31;40m
\033[5;31;40m
           ______  _______     
         .' ___  ||_   __ \    
 ______ / .'   \_|  | |__) |   
|______|| |         |  __ /    
        \ `.___.'\ _| |  \ \_  
         `.____ .'|____| |___| v.BETA    
\033[0;34;40m
\033[1;32;40m
                                    -OJASWA RHX  (2021)                                                                            
                                         



#YOUR OWN PRIVATE CHAT ROOMS
\033[0;37;40m
    ''')




#VALIDATE


#enter IP address
adress=input("\033[0;32;40m Enter received address  : \033[0;35;40m " )
port=int(input(" \033[0;32;40m Enter received port (DIGITS) :  \033[0;35;40m"))


#choose name
name=input("\033[0;32;40m Enter Your Code name :  \033[0;35;40m")
#delete above
os.system('cls' if os.name == 'nt' else 'clear')




#Connect to server
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((adress,port))
# Listening to Server and Sending name
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'HOODIE' Sendname
            message = client.recv(1024).decode('ascii')
            if message == 'HOODIE':
                client.send(name.encode('ascii'))
            else:
                print("\033[1;36;40m---------------------------------------------------------------------------------------\033[0;37;40m")
                print(message)
        except:
            # Close Connection When Error
            print("\033[5;31;40m ERROR FOUND ! \033[0;31;40m")
            client.close()
            break
# Sending Messages To Server
def write():
    while True:
        message = ' \033[1;35;40m {}  \033[1;34;40m >> \n \033[0;37;40m  {}'.format(name, input('-'))
        client.send(message.encode('ascii'))
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
