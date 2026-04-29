# 客户端
# 流程： socket() → connect() → send() / recv() → close()
import socket

# 1. 创建 socket 对象（TCP）
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 连接服务器（IP, 端口）
client.connect(("127.0.0.1", 8080))
print("已连接到服务端 (127.0.0.1:8080)")
print("提示：输入消息后按 Enter 发送，输入 'quit' 退出\n")

# 3. 循环发送和接收消息
while True:
    message = input("请输入消息：")

    if message.lower() == "quit":
        print("断开连接，退出客户端")
        break

    # send()：将字符串编码为 bytes 后发送
    client.send(message.encode("utf-8"))

    # recv(1024)：接收服务端返回的数据，最多 1024 字节
    data = client.recv(1024)

    # 服务端断开时 recv() 返回空字节 b""
    if not data:
        print("服务端已断开连接")
        break

    print(f"服务端回复：{data.decode('utf-8')}\n")

# 4. 关闭连接
client.close()
print("客户端已关闭")
