# 推导式
# 是 Python 中一种极其优雅且高效的语法糖。它允许你用一行代码从一个可迭代对象（如列表、元组、字典等）创建出一个新的序列。

# 基本语法 
# [表达式 for 变量 in 可迭代对象 if 条件]

# ----------------------------------------------------列表推导式   转换、过滤序列数据
# 传统方式
sequence = [1, 2, 3, 4, 5]
new_sequence = []
for x in sequence:
    if x % 2 == 0:
        new_sequence.append(x * x)
print(new_sequence)
# 推导式
new_sequence = [x * x for x in sequence if x % 2 == 0]
print(new_sequence)


# ----------------------------------------------------字典推导式   映射关系构建、键值互换
# 传统方式
sequence = [1, 2, 3, 4, 5]
new_sequence = {}
for x in sequence:
    if x % 2 == 0:
        new_sequence[x] = x * x
print(new_sequence)
# 推导式
new_sequence = {x: x * x for x in sequence if x % 2 == 0}
print(new_sequence)


# ----------------------------------------------------集合推导式  需要唯一值的序列
# 传统方式
sequence = [1, 2, 3, 4, 5]
new_sequence = set()
for x in sequence:
    if x % 2 == 0:
        new_sequence.add(x * x)
print(new_sequence)
# 推导式
new_sequence = {x * x for x in sequence if x % 2 == 0}
print(new_sequence)


# ----------------------------------------------------元组推导式  处理大数据量，节省内存 生成器表达式
# 元组是不可变的  
# 生成器表达式  元组推导式返回的结果是一个生成器对象。
# 传统方式  元组不可变，所以先用列表收集，最后转为元组
sequence = [1, 2, 3, 4, 5]
new_sequence = []
for x in sequence:
    if x % 2 == 0:
        new_sequence.append(x * x)
new_sequence = tuple(new_sequence)
print(new_sequence)
# 推导式  注意：(expr for x in iter) 返回的是生成器对象，不是元组！需要用 tuple() 包裹
# 生成器是“惰性计算”，只有在需要时才会产生下一个值，非常节省内存。
new_sequence = (x * x for x in sequence if x % 2 == 0)
print(new_sequence)
# 这是因为生成器（Generator）是一次性的（惰性计算且只能遍历一次）。
# 连续调用了两次 next() 之后，生成器里需要计算的数据已经全部被读取完毕并且耗尽（exhausted）了。
# 生成器内部维护着一个状态（指针），被读过的数据就不会再保留在内存里了，并且不能往回走
print(next(new_sequence)) # 4
print(next(new_sequence)) # 16
# tuple() 会尝试去读取 new_sequence 中剩下的所有元素。由于前面的两次 next() 操作已经把所有的元素都拿光了，再也没有下一个元素可以生成，所以最后得到的就是一个空的元组 ()。
print(tuple(new_sequence)) # ()