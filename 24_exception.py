# 异常
# 语法错误
# 编译器会直接显示出来 

# 运行时错误
# 编译器不会显示出来，只有在运行时才会显示出来
# ZeroDivisionError，NameError 和 TypeError

while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")

# 如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。
# 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
# 处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，
# 例如:except (RuntimeError, TypeError, NameError):

# try/except...else
# try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
# else 子句将在 try 子句没有发生任何异常的时候执行。

# try 块范围精确，只保护真正可能出错的那段代码
# else 块里的异常不会被当前 except 错误拦截，能真实暴露出 bug
try:
    print("try")
except:
    print("except")
else:  # 没有异常时执行else代码
    print("else")


# 抛出异常
# raise 语句用于抛出异常。raise 语句后面可以跟一个异常实例，也可以跟一个异常类。
# raise ValueError("这是一个自定义异常")


# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value # ← 关键：将参数保存为实例属性
    def __str__(self):
        return repr(self.value)
   
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

    # BaseException
    # ├── SystemExit
    # ├── KeyboardInterrupt
    # ├── GeneratorExit
    # └── Exception          ← 通常自定义异常继承这里
    #     ├── ValueError
    #     ├── TypeError
    #     ├── RuntimeError
    #     └── MyError        ← 你的自定义异常
