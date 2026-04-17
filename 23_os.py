# OS
# os 模块是 Python 标准库中的一个重要模块，它提供了与操作系统交互的功能。
# 通过 os 模块，你可以执行文件操作、目录操作、环境变量管理、进程管理等任务。
import os

# os.getcwd() 返回当前工作目录的路径。
print(os.getcwd())

# os.chdir(path) 函数用于改变当前工作目录。path 是你想要切换到的目录路径。
os.chdir("E:\Python-WorkSpace")
print("新的工作目录:", os.getcwd())

# os.listdir(path) 返回指定目录下的所有文件和目录的名称列表。
print(os.listdir())

os.chdir("E:\Python-WorkSpace\python-learn")

# 创建目录
os.mkdir("test")

# 删除目录
os.rmdir("test")

# 删除文件
# os.remove(path) 函数用于删除一个文件。如果文件不存在，会抛出 FileNotFoundError 异常。
try:
    os.remove("file_to_delete.txt")
except FileNotFoundError:
    print("文件不存在")

#  重命名文件或目录
# os.rename(src, dst) 函数用于重命名文件或目录。src 是原始路径，dst 是新的路径。

# 获取环境变量
# os.getenv(key) 函数用于获取指定环境变量的值。如果环境变量不存在，返回 None。
print(os.getenv("JAVA_HOME"))

# 执行系统命令
# os.system(command) 函数用于在操作系统的 shell 中执行命令。命令执行后，返回命令的退出状态。
# os.system("dir")
