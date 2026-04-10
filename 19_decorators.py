# 装饰器
# 装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。
# 相当于Java中的AOP
# 装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。

# 装饰器的语法使用 @decorator_name 来应用在函数或方法上。

# Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。

# 装饰器的应用场景：

# 日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
# 性能分析: 可以使用装饰器来测量函数的执行时间。
# 权限控制: 装饰器可用于限制对某些函数的访问权限。
# 缓存: 装饰器可用于实现函数结果的缓存，以提高性能。

# ----------------------------------------------------------基本语法
# *args (Positional Arguments)：用于接收所有多余的位置参数，并将它们打包成一个元组 (tuple)。
# 例如：你调用 func(1, 2, 3)，那么在函数内部，args 就是 (1, 2, 3)。
# **kwargs (Keyword Arguments)：用于接收所有多余的关键字参数，并将它们打包成一个字典 (dictionary)。
# 例如：你调用 func(name="Alice", age=25)，那么在函数内部，kwargs 就是 {'name': 'Alice', 'age': 25}

def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()
        result = original_function(*args, **kwargs)
        # 这里是在调用原始函数后添加的新功能
        after_call_code()
        return result
    return wrapper

def before_call_code():
    print("函数调用前执行的代码")

def after_call_code():
    print("函数调用后执行的代码")

# 使用装饰器  相当于调用 decorator_function(target_function)
@decorator_function
def target_function(a,*, b):
    print("原始函数被调用")
    return a + b

# 调用装饰后的函数
print(target_function(1, b=2))


# -----------------------------------------------------------
# 装饰器本身也可以接受参数，此时需要额外定义一个外层函数：
# repeat 函数是一个装饰器工厂，它接受一个参数 num_times，返回一个装饰器 decorator。
# decorator 接受一个函数 func，并返回一个 wrapper 函数。
# wrapper 函数会调用 func 函数 num_times 次。使用 @repeat(3) 装饰s ay_hell 函数后，
# 调用 say_hello 会打印 "Hello!" 三次。

# 闭包
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

# -----------------------------------------------------------类装饰器


# -----------------------------------------------------------内置装饰器


# -----------------------------------------------------------多个装饰器的堆叠
