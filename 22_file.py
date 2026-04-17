# 文件方法

# Python open() 方法用于打开一个文件，并返回文件对象。
# 在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# 文件打开模式
# 'r'：读取（默认）
# 'w'：写入（会覆盖原有内容）
# 'a'：追加（在文件末尾添加内容）
# 'x'：创建（如果文件已存在会报错）
# 'b'：二进制模式
# 't'：文本模式（默认）