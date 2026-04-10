# 函数
# 关键字参数标识  *
# 指定位置参数标识 /
# ---------------------------------------------------------函数定义与参数传递
def max(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b

print(max(1,2))

# python 函数的参数传递：
# 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。
# 如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
# 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

# 不可变类型
def fun(a):
    print(id(a))
    a = a + 1   # 新生成一个 a 的对象。
    print(id(a))

a = 1
fun(a)
print(a)

# 可变类型
def mutable_test(b:list):
    print("mutable_test",id(b)) # mutable_test 1722262839872
    b = [2,3,4,5]  # 重新赋值（Re-assignment）操作，肯定会创建一个新对象
    print("mutable_test",id(b)) # mutable_test 1722262989888

b = [1,2,3,4]
mutable_test(b)

def mutable_test2(c:list):
    print("mutable_test2",id(c)) # mutable_test2 1722262989888
    c.append(5)  # 这种是修改对象本身
    print("mutable_test2",id(c)) # mutable_test2 1722262989888
    return c
# 这两次的地址一样，纯粹是时间差导致的巧合。前一个对象刚刚“寿终正寝”把坑位让出来，后一个对象立刻“拎包入住”占了这个坑位。
# 它们在时间上从来没有同时存在过。这说明 CPython 的内存分配效率很高。
c = [1,2,3]
print(mutable_test2(c))


#-----------------------------------------------------------参数类型
# 必需参数 这种必须传入两个参数
def fun(a,b): # 同名的方法只有一个能存活（也就是最后定义的那一个），无论它们的参数列表是否相同。
    return a+b  # 因为在 Python 中，函数名本质上只是一个变量，它指向内存中的一个“函数对象”。 如果你写了两次 def fun(...)，就相当于对同一个变量进行了重新赋值
# 关键字参数
def printinfo( name, age = 18 ):  # 默认参数
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
printinfo( age=50, name="runoob" )

# 不定长参数 
# # 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)  # 70
   print (vartuple) # (60, 50)
 
printinfo( 70, 60, 50 )

# 加了两个星号 ** 的参数会以字典的形式导入。
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1) # 1
   print (vardict) # {'a': 2, 'b': 3}

printinfo(1, a=2,b=3)

# 声明函数时，参数中星号 * 可以单独出现，例如:
# 强制关键字参数 *
# *args：接收任意数量的位置参数（打包成元组）。
# 单独的 *：不接收任何参数，只起到一个隔断/标记的作用。
# 它告诉 Python 解释器：“从这里开始，后面定义的参数不能通过位置传递，必须显式地写出参数名（即关键字传递）”。
def f(a,b,*,c):
    return a+b+c
# 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
# f(1,2,3)   # 报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: f() takes 2 positional arguments but 3 were given
f(1,2,c=3) # 正常
# 6


# ---------------------------------------------------------匿名函数
# Python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
# lambda 语法格式如下：
# lambda [参数1, 参数2, ...]: 表达式   
# 参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，
# 内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。

# 1. 简单的 lambda 函数
add = lambda x, y: x + y
print(add(2, 3))  # 输出 5

# 2. lambda 函数作为参数传递
def apply_operation(a, b, op):
    return op(a, b)

result = apply_operation(10, 5, lambda x, y: x - y)
print(result)  # 输出 5

# 3. lambda 结合 sorted() 进行自定义排序
students = [('Alice', 20), ('Bob', 18), ('Charlie', 22)]
# 按年龄排序
# key 需要接收一个函数。
# sorted() 在排序前，会把列表里的每一个元素都扔进这个 key 函数里跑一遍，然后用函数的返回值来作为排序的实际依据。
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # [('Bob', 18), ('Alice', 20), ('Charlie', 22)]

# 使用 lambda 就是为了把这种**“用完即弃，极其简单的一句话逻辑”**在一行内优雅地写完。


# ----------------------------------------------------------return函数
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的 return 语句返回 None。


# ----------------------------------------------------------强制位置参数
# Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，
# c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# 1. 最小强制：c 和 d 也使用位置传参
f(1,2,3,4,e=5,f=6) # 正常
# 2. 混合传参：c 和 d 使用关键字传参
f(1,2,c=3,d=4,e=5,f=6) # 正常
# 1 2 3 4 5 6
# f(a=1,b=2,c=3,d=4,e=5,f=6) # 报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: f() got some positional-only arguments passed as keyword arguments: 'a, b'

# 隐藏实现细节：比如底层的 C 语言接口，或者你未来可能会修改参数 a、b 的变量名。如果不加 /，用户可能会写 f(a=1, b=2...)，当你把参数名优化重构成 x, y 后，用户的代码就挂了。加上 / 后，用户根本无法通过变量名调用，你可以随意修改参数的内部命名。
# 跟 Python 内置方法统一：像 len(obj) 或者 sum(iterable) 这样的内部函数，其实是不允许写成 len(obj=[1,2]) 这种形态的。/ 语法让普通开发者也能编写跟系统原生的底层函数保持一样行为风格的 API。