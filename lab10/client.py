import socket
msgFromClient="Kindly send the documents professor"
bytesToSend=str.encode(msgFromClient)
serverAddressPort=("127.0.0.1",20001)
bufferSize=1024
UDPClientSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend,serverAddressPort)
msgFromServer=UDPClientSocket.recvfrom(bufferSize)
msg="Message from Server {}".format(msgFromServer[0])
print(msg)