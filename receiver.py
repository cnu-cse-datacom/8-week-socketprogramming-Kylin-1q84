import socket

def socket_recv(server_socket,size):
	recv_size = 0
	recv_data = server_socket.recv(1024)
	if not recv_data:
		return	
	while len(recv_data):
		recv_size += len(recv_data)
		print("current_size / total_size = ",recv_size,"/",size," ",(recv_size/size)*100,"%")
		f.write(recv_data)
		server_socket.sendto("ok".encode(), addr)
		recv_data = server_socket.recv(1024)
		if(recv_data.decode() == "EOF"):
			server_socket.sendto("ok".encode(), addr)
			break

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('',9000))
data, addr = server_socket.recvfrom(2000)
print(data)
print(addr)
print("file recve start from ", addr)
print(data)
f = open(data, 'wb')
print("File Name : ", data)
server_socket.sendto( "ok".encode(), addr)
size,addr = server_socket.recvfrom(2000)
print("File Size : ", int(size))
server_socket.sendto( "ok".encode(), addr)
socket_recv(server_socket,int(size))

