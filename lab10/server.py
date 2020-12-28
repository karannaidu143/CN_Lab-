  
import socket
localIP="127.0.0.1"
localPort=20001
bufferSize=1024
msgFromServer="Ready to send the file from professor"
bytesToSend=str.encode(msgFromServer)
UDPServerSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))
print("UDP server up and listening")
while(True):
    bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
    message=bytesAddressPair[0]
    address=bytesAddressPair[1]
    clientMsg="Message from Client:{}".format(message)
    clientIP="Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    UDPServerSocket.sendto(bytesToSend,address)