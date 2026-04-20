# 面向对象
class FirstPythonObject:

    attribute_1 = "attribute_1" # 类属性 (Class Attribute)属于类本身，所有实例共享同一份，可以通过类名直接访问
    # （双下划线前缀）在 Python 中代表私有属性，但严格来说是通过**名称改写（Name Mangling）**机制实现的。
    __attribute_2 = "attribute_2" # 私有属性 (Private Attribute)属于实例本身，每个实例独有，只能通过实例名调用
    
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

# 在 Python中，self 是一个惯用的名称，用于表示类的实例（对象）自身。
# 它是一个指向实例的引用，使得类的方法能够访问和操作实例的属性。

# 继承 
class DerivedClassName(FirstPythonObject):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

derivedClassName = DerivedClassName("John", 30, "Male")
print(derivedClassName)
# Python 实际将其改写为 _FirstPythonObject__attribute_2
print(derivedClassName._FirstPythonObject__attribute_2)


# 多继承 class DerivedClassName(Base1, Base2, Base3):
# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
# python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

class Base1:
    def __init__(self):
        self.name = "Base1"
    def __str__(self):
        return f"Name: {self.name}"

class Base2:
    def __init__(self):
        self.name = "Base2"
    def __str__(self):
        return f"Name: {self.name}"

class Base3:
    def __init__(self):
        self.name = "Base3"
    def __str__(self):
        return f"Name: {self.name}"

class MultiDerivedClassName(Base1, Base2, Base3):
    def __init__(self, name, age, gender):
        super().__init__()  # Base1/Base2/Base3 的 __init__ 只接受 self，不能传额外参数
        self.name = name    # 子类自行覆盖父类设置的 self.name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

multiDerivedClassName = MultiDerivedClassName("John", 30, "Male")
print(multiDerivedClassName)


# 方法重新
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
# Child 当前子类（从哪个类开始向上查找父类）
# c Child 实例
# myMethod 要调用的方法
# super(Child, c) 返回一个代理对象，它会跳过 Child 这一层，
# 直接去 Child 的 MRO（方法解析顺序）中查找下一个类（即 Parent），并以 c 作为 self 来调用方法。
# 从哪个类开始往上搜索父类
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法,需要明确指定从哪个类开始查找时使用用这个
# super().myMethod() # ❌ super() 无参数版本只能在类方法内部使用，类外部会报错


# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方