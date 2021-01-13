from socket import *
serverName = '211.222.58.47'
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

message = input('Input lowsercase sentence : ')
clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(1024)
print(modifiedMessage.decode())
clientSocket.close()
