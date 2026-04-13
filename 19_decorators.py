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
# 函数形式的类装饰器
def log_class(cls):
    """类装饰器，在调用方法前后打印日志"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)  # 实例化原始类
        
        def __getattr__(self, name):
            """拦截未定义的属性访问，转发给原始类"""
            return getattr(self.wrapped, name)
        
        def display(self):
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")
    
    return Wrapper  # 返回包装后的类

@log_class
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")

obj = MyClass()
obj.display()

# 类形式的类装饰器(实现__call__方法)
class SingletonDecorator:
    """类装饰器，使目标类变成单例模式"""
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    
    def __call__(self, *args, **kwargs):
        """拦截实例化过程，确保只创建一个实例"""
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("Database 初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True，说明是同一个实例

# -----------------------------------------------------------内置装饰器

class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# 使用
MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.name = "Alice"
print(obj.name)
# -----------------------------------------------------------多个装饰器的堆叠
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()

# 闭包
# 即使外部函数已经执行完毕，内部函数依然能“记住”并访问外部函数中的变量。

# 闭包产生的三个必要条件
# 要形成一个闭包，必须满足以下三个条件：
# 必须有一个内嵌函数（函数里面定义函数）。
# 内嵌函数必须引用外部函数的变量（非全局变量）。
# 外部函数的返回值必须是这个内嵌函数本身。

# 闭包有什么用？
# 数据隐藏（封装）：闭包可以让你把一些变量“藏”起来，不让外部直接访问，类似于面向对象中的私有属性。
# 减少全局变量：避免为了保存状态而定义过多的全局变量，减少命名污染。
# 装饰器（Decorators）：Python 中极其实用的装饰器语法，本质上就是闭包的高级应用。
def make_multiplier(n): 
    # 外部环境：n (相当于被“藏起来”的私有状态)
    
    def multiplier(x):      # 条件1：必须有一个内嵌函数
        return x * n        # 条件2：内嵌函数必须引用外部函数的变量
        
    return multiplier       # 条件3：外部函数的返回值必须是内嵌函数本身

# 开始使用（闭包的魔力）：
times3 = make_multiplier(3)  # times3 现在是一个函数，并且它“记住”了 n=3
times5 = make_multiplier(5)  # times5 也是一个函数，但它“记住”了属于它自己的 n=5

print(times3(10))  # 输出 30
print(times5(10))  # 输出 50
