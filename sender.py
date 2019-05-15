import socket
import os

def socket_recv(client_socket,size):
	print("File Transmit Start....")
	send_size = 0	
	send_data = f.read(1024)
	while send_data:
		send_size += len(send_data)
		print("current_size / total_size = ",send_size,"/",size," ",(send_size/size)*100,"%")
		client_socket.sendto(send_data.encode(), (ip_addr,port))
		data = client_socket.recvfrom(2000)
		send_data = f.read(1024)
	client_socket.sendto("EOF".encode(), (ip_addr,port))
	print("ok")
	print("file_send_end")
	
	
	

file_name = input("Input your file name : ")
f = open(file_name, 'r')

ip_addr = "192.168.0.55"
port = 9000


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto( file_name.encode(), (ip_addr,port))
data = client_socket.recvfrom(2000)
size = os.path.getsize(file_name)
client_socket.sendto( (str(size)).encode(), (ip_addr,port))
data = client_socket.recvfrom(2000)
socket_recv(client_socket,size)

