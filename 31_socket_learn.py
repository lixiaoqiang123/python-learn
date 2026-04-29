import socket
# python 网络编程  socket

# 服务端流程： socket() → bind() → listen() → accept() → recv() / send() → close()。

# 客户端流程： socket() → connect() → send() / recv() → close()。

# socket.socket([family[, type[, proto]]])
# family: 套接字家族可以是 AF_UNIX 或者 AF_INET
# type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
# proto: 一般不填默认为0.
# ===================================================================
# 特性	           SOCK_STREAM（TCP）	            SOCK_DGRAM（UDP）
# 协议	                  TCP	                         UDP
# 连接方式	           需要建立连接	                   无连接，直接发
# 数据可靠性	        ✅ 可靠，不丢包	                  ❌ 可能丢包
# 数据顺序	         ✅ 保证顺序	                      ❌ 不保证顺序
# 速度	              较慢（有握手）	                 较快
# 典型应用	           HTTP、FTP、SSH	              视频、DNS、游戏
# ===================================================================


sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和端口
# _Address 里 str 是给谁用的？
# str 类型是专门给 AF_UNIX（Unix 域套接字） 用的，传的是文件路径，不是 IP 地址：
# sc.bind("/tmp/my.sock")   # ✅ 传文件路径字符串
# 套接字类型	_Address 实际传的值	示例
# AF_INET（IPv4）	tuple → (ip, port)	("127.0.0.1", 8080)
# AF_INET6（IPv6）	tuple → (ip, port, flow, scope)	("::1", 8080, 0, 0)
# AF_UNIX（Unix）	str → 文件路径	"/tmp/my.sock"
sc.bind(("127.0.0.1", 8080))
# 监听连接  
# backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
sc.listen(5)
# 接受连接  # accept()会阻塞，直到有客户端连接进来
# sc.accept()

# ===================================================================
# 方法	                 适用对象	                        用途
# bind()	             服务器端	               绑定 IP 和端口
# listen()	             服务器端	               开始监听客户端连接
# accept()	             服务器端	               接收新的客户端连接
# connect()	             客户端	                    主动连接服务器
# send() / sendall()	 双方	                      发送数据
# recv() / recvfrom()	 双方	                     TCP/UDP 接收数据
# close()	             双方	                     关闭连接
# ===================================================================
