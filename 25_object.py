# 面向对象
class FirstPythonObject:

    attribute_1 = "attribute_1" # 类属性 (Class Attribute)属于类本身，所有实例共享同一份，可以通过类名直接访问

    def __init__(self, name, age): # 构造方法
        self.name = name # 实例属性 (Instance Attribute)属于实例本身，每个实例独有，只能通过实例名调用
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


firstPythonObject = FirstPythonObject("John", 30)
print(firstPythonObject)
print(FirstPythonObject.attribute_1) # 类属性可以通过类名直接访问

# self 代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
