# 服务端
# 流程： socket() → bind() → listen() → accept() → recv() / send() → close()
import socket

# 1. 创建 socket 对象（TCP）
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 端口复用：避免程序重启时出现 "Address already in use" 错误
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2. 绑定 IP 和端口
server.bind(("127.0.0.1", 8080))

# 3. 开始监听，最多允许 5 个连接排队等待
server.listen(5)
print("服务端已启动，等待客户端连接... (127.0.0.1:8080)")

# 4. 阻塞等待客户端连接
# accept() 返回 (conn, addr)
#   conn: 与该客户端通信的新 socket 对象
#   addr: 客户端的 (IP, 端口) 元组
conn, addr = server.accept()
print(f"客户端已连接：{addr}")

# 5. 循环收发消息
while True:
    # recv(1024)：每次最多接收 1024 字节，返回 bytes 类型
    data = conn.recv(1024)

    # 客户端断开时 recv() 返回空字节 b""
    if not data:
        print("客户端已断开连接")
        break

    message = data.decode("utf-8")  # bytes → str
    print(f"收到客户端消息：{message}")

    # 向客户端回复消息
    reply = f"服务端已收到：{message}"
    conn.send(reply.encode("utf-8"))  # str → bytes

# 6. 关闭连接
conn.close()
server.close()
print("服务端已关闭")