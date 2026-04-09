#----------------------------隐式转换
print("----------------------------隐式转换")
num_int = 1
num_float = 2.0
num_sum = num_int + num_float
print(num_sum)
print(type(num_sum))


#----------------------------显式转换
print("----------------------------显式转换")
str_one = "123"
print(int(str_one))
float_one = 1.23
print(int(float_one)) #输出1

str_two = "123.45"
print(float(str_two))
float_two = '1.23'
print(float(float_two))
float_three = 3.0
print(float(float_three))

#整型与字符串相加;这种情况下不会自动转换
num_one = 123
num_str = "123"
print(num_one + int(num_str))
print(type(num_one + int(num_str)))

# 转成字符串
str_one = 123.4
print(str(str_one))
print(type(str(str_one)))

#-----------------------------------------------其他转换
print("-----------------------------------------------其他转换")
# 将对象 x 转换为表达式字符串 repr(x)
x_int = 123
print(repr(x_int))          # 输出: 123
print(type(repr(x_int)))    # 输出: <class 'str'>

x_str = "hello"
print(repr(x_str))          # 输出: 'hello'  (带引号)
print(str(x_str))           # 输出: hello    (不带引号)

x_list = [1, 2, 3]  
print(repr(x_list))         # 输出: [1, 2, 3]

x_float = 3.14
print(repr(x_float))        # 输出: 3.14


# 用来计算在字符串中的有效Python表达式,并返回一个对象 eval(str)
str_eval = "123"
print(eval(str_eval))
print(type(eval(str_eval)))
x = [1, 2, 3]
s = repr(x)      # [1, 2, 3]  对象 → 字符串
print(type(s))
y = eval(s)      # [1, 2, 3]   字符串 → 对象
print(type(y))
print(x == y)    # True
# 计算数学表达式
print(eval("1 + 2 * 3"))        # 7  (int)
print(eval("3.14 * 2"))         # 6.28 (float)

# 还原列表/字典
print(eval("[1, 2, 3]"))        # [1, 2, 3]  (list)
print(eval("{'a': 1, 'b': 2}")) # {'a': 1, 'b': 2} (dict)

# 与 repr() 配合使用
original = (10, 20, 30)
s = repr(original)        # "(10, 20, 30)"
restored = eval(s)        # (10, 20, 30)
print(type(restored))     # <class 'tuple'>
# 危险！eval 会执行任意代码
eval("__import__('os').system('del /f important.txt')")  # 切勿这样用！
# 安全替代品：ast.literal_eval() 只能解析字面量（数字、字符串、列表、字典等），不会执行任意代码，更安全。

# ---------------------------------------将序列 s 转换为一个元组 tuple(s)
tuple_s = (1,2,3)
print(type(tuple_s))
print(type(tuple(tuple_s)))
# ✅ 真正有意义的用法：把其他序列转为元组
# 列表 → 元组
list_s = [1, 2, 3]
print(tuple(list_s)) # (1, 2, 3)  <class 'tuple'>

# 字符串 → 元组（每个字符变成一个元素）
str_s = "hello"
print(tuple(str_s))       # ('h', 'e', 'l', 'l', 'o')

# 集合 → 元组
set_s = {1, 2, 3}
print(tuple(set_s))       # (1, 2, 3)

# range → 元组
print(tuple(range(5)))    # (0, 1, 2, 3, 4)

# ❌ 没意义的用法（你写的这种）
tuple_s = (1, 2, 3)         # 本身已经是元组
print(tuple(tuple_s))       # 原样返回，没有任何变化

# --------------------------------------将序列 s 转换为一个列表 list(s)
list_tuple_one = (1,2,3)
print(list(list_tuple_one))
list_tuple_two = "HelloWorld"
print(list(list_tuple_two))
# 元组 → 列表（让不可变变成可修改）
t = (1, 2, 3)
lst = list(t)
lst.append(4)         # ✅ 列表可以追加
print(lst)            # [1, 2, 3, 4]
# 字符串 → 列表（便于逐字符操作）
s = "hello"
chars = list(s)       # ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'        # 修改某个字符
print(''.join(chars)) # 'Hello'
# 集合 → 列表（集合无序，转列表后可排序）
se = {3, 1, 2}
print(sorted(list(se)))  # [1, 2, 3]
# range → 列表
print(list(range(1, 6))) # [1, 2, 3, 4, 5]

# ----------------------------------------------将序列 s 转换为一个集合 set(s)
# 列表 → 集合（自动去重！）
list_with_dup = [1, 2, 2, 3, 3, 3, 4]
print(set(list_with_dup))       # {1, 2, 3, 4}
# 字符串 → 集合（每个字符，去重）
str_set = "hello"
print(set(str_set))             # {'h', 'e', 'l', 'o'}  'l'只保留一个
# 元组 → 集合
tuple_set = (1, 2, 2, 3)
print(set(tuple_set))           # {1, 2, 3}
# 最常用场景：列表去重（去重后再转回列表）
data = [3, 1, 2, 1, 3, 5, 2]
unique_data = list(set(data))
print(sorted(unique_data))      # [1, 2, 3, 5]
# 列表 → 集合（自动去重！）
list_with_dup = [1, 2, 2, 3, 3, 3, 4]
print(set(list_with_dup))       # {1, 2, 3, 4}  重复元素被去掉

# 字符串 → 集合（每个字符，去重）
str_s = "hello"
print(set(str_s))               # {'h', 'e', 'l', 'o'}  注意'l'只保留一个

# 元组 → 集合
tuple_s = (1, 2, 2, 3)
print(set(tuple_s))             # {1, 2, 3}

# 最常用场景：列表去重（去重后再转回列表）
data = [3, 1, 2, 1, 3, 5, 2]
unique_data = list(set(data))
print(unique_data)              # [1, 2, 3, 5]（顺序可能不同，因集合无序）

# -------------------------------------------------------------将序列 s 转换为一个字典 dict(s)
# 方式1：由键值对组成的列表/元组 → 字典
pairs = [("name", "Alice"), ("age", 25), ("city", "Beijing")]
print(dict(pairs))              # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 方式2：用 zip() 将两个列表合并为字典
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(dict(zip(keys, values)))  # {'a': 1, 'b': 2, 'c': 3}

# 方式3：直接传入关键字参数
print(dict(name="Bob", age=30)) # {'name': 'Bob', 'age': 30}


# -------------------------------------------------------------转换为不可变集合 frozenset(s)
fs = frozenset([1, 2, 2, 3, 3])
print(fs)                   # frozenset({1, 2, 3})  自动去重
print(type(fs))             # <class 'frozenset'>
# ❌ 不可变，不能增删改
# fs.add(4)                 # AttributeError: 'frozenset' object has no attribute 'add'
# ✅ 可以做字典的 key（普通 set 不行）
d = {frozenset([1, 2]): "one-two"}
print(d)                    # {frozenset({1, 2}): 'one-two'}

# ✅ 支持集合运算
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])
print(a & b)                # frozenset({2, 3})  交集
print(a | b)                # frozenset({1, 2, 3, 4})  并集


# -------------------------------------------------------------将一个整数转换为一个字符 chr(x)
# 数字字符：48~57
print(chr(48))   # '0'
print(chr(55))   # '7'  ← 你的例子，55 对应字符 '7'
print(chr(57))   # '9'

# 大写字母：65~90
print(chr(65))   # 'A'
print(chr(90))   # 'Z'

# 小写字母：97~122
print(chr(97))   # 'a'
print(chr(122))  # 'z'

# 中文也有 Unicode 编码
print(chr(20013)) # '中'
print(chr(25991)) # '文'

# -------------------------------------------------------------将一个字符转换为它的整数值 ord(x)
ord_one = "中"
print(ord(ord_one))
# -------------------------------------------------------------将一个整数转换为一个十六进制字符串 hex(x)
hex_one = 255
print(hex(hex_one))
# -------------------------------------------------------------将一个整数转换为一个八进制字符串 oct(x)
oct_one = 255
print(oct(oct_one))
# -------------------------------------------------------------将一个整数转换为一个二进制字符串 bin(x)
bin_one = 255
print(bin(bin_one))