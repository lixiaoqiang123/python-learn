# 字典   字典是可变的
# 键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
# 如果键重复，后面的值会覆盖前面的值。{"name":"李晓强","name":18,"weight":70} ——>{'name': 18, 'weight': 70}
dict_one = {"name":"李晓强","age":18,"weight":70}
# --------------------------------
print(dict_one) 
print(dict_one["name"])  # 输出: 李晓强

# 使用内建函数 dict() 创建字典：
dict_two = dict(name="李晓强", age=18, weight=70)
dict_three = dict([('name', '李晓强'), ('age', 18), ('weight', 70)])

# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
dict_one["height"] = 180  # 添加新键/值对
print(dict_one)  # 输出: {'name': '李晓强', 'age': 18, 'weight': 70, 'height': 180}
dict_one["age"] = 19  # 修改已有键/值对
print(dict_one)  # 输出: {'name': '李晓强', 'age': 19, 'weight': 70, 'height': 180}
# del dict_one         # 删除字典
del dict_one["weight"]  # 删除已有键/值对
print(dict_one)  # 输出: {'name': '李晓强', 'age': 19, 'height': 180}

# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 键必须是不可变的对象，且必须是唯一的（在同一个字典中）。因此，可以用数字、字符串或元组充当键，但用列表就不行，因为列表是可变的。
dict_four = {('name', 'age'): '李晓强'}  # 使用元组作为键
print(dict_four)  # 输出: {('name', 'age'): '李晓强


# ----------------------------------------------------------- 字典内置函数
# len(dict) 计算字典元素个数，即键的数量
print(len(dict_two))  # 输出: 3
# str(dict) 输出字典可打印的字符串表示
print(str(dict_two))  # 输出: {'name': '李晓强', 'age': 18, 'weight': 70}
# type(variable) 返回输入的变量类型，如果变量是字典就返回 <class 'dict'>
print(type(dict_two))  # 输出: <class 'dict'>

# ------------------------------------------------------------ 字典内置方法

# 1 dict.clear()  删除字典内所有元素
dict_five = {"name":"李晓强","age":18,"weight":70}
print(dict_five.clear())  # 输出: None 约定返回 `None`
print(dict_five)  # 输出: {}
# 2 dict.copy()  返回一个字典的浅复制 
# 浅复制（shallow copy）是指创建一个新对象，但新对象的元素仍然引用原始对象的元素，而不是复制元素本身。
# 在Python字典中，使用 dict.copy() 方法进行浅复制，会创建一个新的字典对象，但字典中的键和值仍然指向原始字典中的相同对象。
# 如果值是可变对象（如列表或另一个字典），修改这些值会同时影响原始字典和复制的字典。
# 浅复制的“共享”只适用于值是可变对象（如列表或字典）的情况。如果值是不可变对象（如整数、字符串），修改原始字典不会影响复制。
dict_six = dict_two.copy()
print(dict_six)  # 输出: {'name': '李晓强', 'age': 18, 'weight': 70}
dict_two["age"] = 23 # age是不可变的，所以修改dict_two["age"]不会影响dict_six["age"]
print(dict_six)
# 3 dict.fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
dict_seven = dict.fromkeys(['name', 'age', 'weight'], 'unknown')
print(dict_seven)  # 输出: {'name': 'unknown', 'age': '
# 4 dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
print(dict_two.get("name"))  # 输出: 李晓强
# 5 key in dict 如果键在字典dict里返回true，否则返回false
print("name" in dict_two)  # 输出: True
# 6 dict.items() 以列表返回一个视图对象
# 视图对象是一个动态的对象，它会随着字典的变化而变化。当字典被修改时，视图对象会自动更新以反映这些变化。
# 视图实时反映字典的变化，不需要重新调用 `.items()`。  
# `dict_items` 视图对象，不是列表 ； 字典改变时视图自动更新
print(dict_two.items())  # 输出: dict_items([('name', '李晓强'), ('age', 18), ('weight', 70)])
# 7	dict.keys() 返回一个视图对象
print(dict_two.keys())  # 输出: dict_keys(['name', 'age', 'weight'])
# 8	dict.setdefault(key, default=None) 和get()类似,
# 但如果键不存在于字典中，将会添加键并将值设为default
print(dict_two.setdefault("height", 180))  # 输出: 180
# 9	dict.update(dict2) 把字典dict2的键/值对更新到dict里
print(dict_two.update(dict_seven))  # 输出: None 约定返回 `None`
print(dict_two)  # 输出: {'name': 'unknown', 'age': 'unknown
# 10	dict.values() 返回一个视图对象
print(dict_two.values())  # 输出: dict_values(['unknown', 'unknown', 70, 180])
# 11	dict.pop(key[,default]) 删除字典 key（键）所对应的值，返回被删除的值。
print(dict_two.pop("age"))  # 输出: unknown
# 12	dict.popitem() 返回并删除字典中的最后一对键和值。
print(dict_two.popitem())  # 输出: ('height', 180)
print(dict_two)
