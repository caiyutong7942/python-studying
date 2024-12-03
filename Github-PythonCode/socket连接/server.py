import socket
socket_server = socket.socket()

socket_server.bind(("localhost",8888))  #bind((host,port))

socket_server.listen(1)      # 监听端口(最大连接数)默认自动调整

conn,address = socket_server.accept()        # (链接对象，客户端地址信息) 阻塞方法
print(f"接收到了客户端的链接，客户端的信息是:{address}")

while True:
    data: str = conn.recv(1024).decode("UTF-8")  #接受消息
    if data == 'exit':
        break
    print(f"客户端发来的消息是:{data}")
    reply = input("请输入回复消息:").encode("UTF-8")
    conn.send(reply)      # 返回消息

conn.close()
socket_server.close()