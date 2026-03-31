#----------------------------------基本数据类型
# 不可变类型：字符串、数字、元组
# 可变类型：列表、字典、集合

# 字符串
my_str = "hello"
# 数字:int float complex
num = 1
print(isinstance(num, int))
# 布尔类型 bool
# isinstance(对象, 类型) 的第二个参数必须是一个类型（如 int、bool、str），而不是一个值。
# 同样的问题也存在于 str、tuple、list、set、dict，它们都是 Python 内置类型，被你的变量名覆盖了。
my_bool = True
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
print(isinstance(my_bool, int))
# 元组,不可变
my_tuple = (1, 2, 3)
# 列表，可变
my_list = [1, 2, 3]
# 集合，可变
my_set = {1, 2, 3}
# 字典，可变
my_dict = {"name": "hello", "age": 18}



#----------------------------Tuple 元组; # 修改元组元素的操作是非法的 tuple_two[0] = 1
tuple_two = (1,2,3,4)
print(tuple_two[0:2])
print(tuple_two)
print(tuple_two[0])
print(tuple_two[0:])
# 会输出（1，） 这是 Python 区分单元素元组和普通括号的特殊设计。
# (1,) 中的逗号是 Python 用来表示"这是一个元组"的标志。
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(tuple_two[0:2:2])
print(tuple_two * 2)
print(tuple_two + (5,6))
# ()空元组   (1,)一个元素加逗号
print(type(()))


#----------------------------set 集合
# set集合是无序的，不重复的，可变的；
# 可以进行交集、并集、差集
set_one = {3,2,1,3}
set_two = {6,4,5}
# 输出{1, 2, 3}
print(set_one)
# 交集: 两个集合共同拥有的元素
print(set_one & set_two)
# 并集:两个集合合并在一起（去重）
print(set_one | set_two)
#差集:属于左边，但不属于右边的元素
print(set_one - set_two)
#对称差集:两个集合中不共同拥有的元素
print(set_one ^ set_two)
#子集
print(set_one.issubset(set_two))
#父集
print(set_one.issuperset(set_two))
#不相交:两个集合没有共同元素
print(set_one.isdisjoint(set_two))


#-----------------------------------dict 字典
dict_one = {"name":"小强","age":18,"gender":"男"}
print(dict_one)
print(dict_one["name"])
print(dict_one.get("name"))
dict_one['age'] = 19
print(dict_one)
print(dict_one['gender'])
print(dict_one.keys())
print(dict_one.values())
dict_two = dict([("name","小强"),("age",18),("gender","男")])
print(dict_two)
dict_three = dict(name="小强",age=18,gender="男")
print(dict_three)

#------------------------------------bytes 类型
# bytes 类型是不可变的；
# bytes("Hello") 必须指定编码，否则不知道用什么规则转换
byte_one = bytes("Hello",encoding="utf-8")
print(byte_one)
x = byte_one[0:1]
print(x)
y = byte_one+b"world"
print(y)
print(len(y))
# ord() 函数用于将字符转换为相应的整数值。
if x[0] == ord("H"):
    print("The first element is 'H'")

#-------------------------------------数据类型转换
