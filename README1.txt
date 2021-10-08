----SERVER STEPS TO FOLLOW-----

Make sure you have ngrok to make it visible on WAN network

1.> python SERVER.py
2.>Enter Free port (1500,etc)
3.>Name your server
4.>If you want server to connect on WAN network use dynamic IP and start is using given command in square brackets [ngrok tcp "port number"]
5.>after ngrok starts 
6.>use Command prommpt and get ip address of your created tunnel ,copy Domain name from forwarding section of ngrok

  tcp://{0.tcp.ngrok.io}.17088 - copy text in curly bracket without curly bracket and in cmd $-ping 0.tcp.ngrok.io

it will give you IP of domain name (Client use this to address connect server and chat) [1]

and share tcp://0.tcp.ngrok.io.{17088} port you got in ngrok to clients to connect (Client use this port to connect server and chat) [2]

7.>make sure to dont stop ngrok
8.> Clients will automaticly connect to the server using ngrok ip [1] and port [2] given to them



---------Client(Hoodie)steps to follow-------------
1.>python HOODIE.py
2.>Enter recieved IP given by server in step 6.>[1]
3.>Enter recieved Port given by server in step 6.>[2]
4.>enter your code name(any name)
5.>now you can chat with others who are connected to same server !
have fun

(WARNING)
USE WISELY


