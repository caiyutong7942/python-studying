import socket
socket_client = socket.socket()

socket_client.connect(("localhost",8888))  #(host,port)

socket_client.listen(1)      # 监听端口(最大连接数)默认自动调整

while True:
    send_msg = input("请输入要发送的消息")
    if send_msg == 'exit':
        break
    socket_client.send(send_msg.encode("UTF-8"))   # 发送消息
    recv_data = socket_client.recv(1024)  #缓冲区大小
    print(f"服务端回复的消息是:{recv_data.decode('UTF-8')}")

socket_client.close()