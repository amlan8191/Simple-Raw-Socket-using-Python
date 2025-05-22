import socket
import sys

try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Socket Creation failed")
    print("Reason: %s"%str(err))
    sys.exit()
print("Socket Connected succesfully")
target_host=input("Enter the IP")
target_port=input("Enter the port number")

try:
    sock.connect((target_host,int(target_port)))
    print("Socket connected succesfully to %s and port %s"%target_host,target_port)
    sock.shutdown(2)
except socket.error as err:
    print("Socket connection failed")
    print("Reason: %s"%str(err))
    sys.exit()