import socket
#simple code for getting ip address of any url
print('****GetIP****') 
host=input('Enter url:')
ip=socket.gethostbyname(host)
print("IP address of {} is {}".format(host,ip))
