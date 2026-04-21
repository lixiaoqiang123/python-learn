# 标准库
# os time datetime json random math re sys urllib
# os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
# sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。
# time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。
# datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。
# random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。
# math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。
# re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。
# json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。
# urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。


# -------------------------------------------------------------os
import os

# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录:", current_dir)

# 列出目录下的文件
files = os.listdir(current_dir)
print("目录下的文件:", files)

# dir(os) # 查看os模块有哪些函数
# help(os) # 查看os模块的帮助文档

# shutil 模块，其名称是 "Shell Utilities" 的缩写
import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

# --------------------------------------------------------------文件通配符
import glob
print(glob.glob('28*.py'))

# --------------------------------------------------------------命令行参数
import sys
print(sys.argv)
# sys.argv[0]（列表的第一个元素）：永远是当前运行的脚本文件名称（包含路径信息，具体取决于你运行时怎么写的）。就像你在终端看到的输出 ['28_standard_library.py'] 或者 ['.\\28_standard_library.py']。
# sys.argv[1] 及之后的元素：是你在运行脚本时，跟在脚本名字后面输入的附加参数。这些参数默认都是字符串类型。

# --------------------------------------------------------------错误输出重定向和程序终止
# sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。
# sys.exit() 函数可以用来退出程序。
sys.stderr.write('Warning, log file not found starting a new one\n')

# --------------------------------------------------------------字符串正则匹配
# re 模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案
import re
print(re.split(r'\W+', 'Words, words, words.'))

# --------------------------------------------------------------数学运算,详见function.py
import math
print(math.sqrt(16))


# --------------------------------------------------------------随机数,详见function.py
import random
print(random.randint(1, 10))

# --------------------------------------------------------------访问 互联网
import urllib
from urllib.request import urlopen
for line in urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'baidu' in line:
        pass
        # print(line)

# --------------------------------------------------------------日期和时间
import datetime
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# ---------------------------------------------------------------数据压缩
import zlib
print(len(zlib.compress(b'hello world')))
print(len(b'hello world'))
print(zlib.decompress(zlib.compress(b'hello world')))


# ---------------------------------------------------------------测试模块
# doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
# 它的作用是自动提取并运行代码注释（文档字符串 docstrings）中的测试用例。
doctest.testmod()   # 自动验证嵌入测试
# doctest.testmod() 是一种非常轻量、方便的测试方法。它能让你在写函数说明文档的同时，
# 顺便把测试用例也写了，并能一键验证这些例子是否能正确运行。这种做法被称为**“文档即测试”**。