# 模块
# 当导入一个模块时，Python 会按照以下顺序查找模块：
# 当前目录。
# 环境变量 PYTHONPATH 指定的目录。
# Python 标准库目录。
# .pth 文件中指定的目录。

import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')


# from fibo import *
# 这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。
# 大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。

# __name__
# 一个模块被另一个程序第一次引入时，其主程序将运行。
# 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行。

# 每个模块都有一个 内置属性 __name__ 属性。
# 如果模块是被直接运行，__name__ 的值为 __main__。
# 如果模块是被导入的，__name__ 的值为模块名。

# 包
# 包（packages）是 Python 中用来组织模块的一种方式。
# 包本质上就是一个包含多个模块的目录。
# 包的结构如下：
# package_name/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage_name/
#         __init__.py
#         module3.py

# __init__.py 文件可以是空的，也可以包含一些代码，用于初始化包。
# 如果一个文件夹里面没有 __init__.py，那它就是个普通文件夹，别当成包去导入它。

# __init__.py 还可以做什么？
# 除了做“门面标志”，如你笔记里所写，它主要用来做“初始化”。当我们导入一个包的时候，__init__.py 里的代码会自动第一步被运行。
# 控制导出内容： 你可以在里面指定 __all__ = ['module1', 'module2']，这样当别人用 from package_name import * 时，就只会把 module1 和 module2 导出去，而不是暴露所有的模块。
# 快捷导入： 假设别人想用 module1 里的 func_a，常常要写 from package_name.module1 import func_a，这很长。如果你在 __init__.py 里提前写上一句 from .module1 import func_a，别人就可以直接优雅地只写 from package_name import func_a。

# import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，抛出一个 :exc:ImportError 异常。