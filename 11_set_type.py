# 集合
# 集合（set）是一个无序的不重复元素序列。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
#set 里面的元素是可变的吗？
#不是，必须是不可变的（确切地说是可哈希的，Hashable）。 因为集合的底层实现是基于哈希表（为了保证极快的去重和查找速度），哈希表要求每个元素必须能算出一个绝对稳定、不可变的哈希值。
#能放进集合里的： 数字 (int, float)、字符串 (str)、元组 (tuple，前提是元组里面也不能有列表)。由于这些数据类型本身是不可变类型，它们放进去后其内部就再也无法被修改了。
#不能放进集合里的： 列表 (list)、字典 (dict)、另一个集合 (set)。如果你尝试运行 my_set = { [1, 2] }，Python 会直接抛出 TypeError: unhashable type: 'list' 的错误。



# 创建集合
set_one = {1,2,3,4,5}
print(set_one)  # 输出: {1, 2, 3, 4, 5}
set_two = set([1,2,3,4])
# set_two = set([1,2,3,4,[123,456]])
# print(set_two) TypeError: unhashable type: 'list'
set_three = set('abcde')
print(set_three)  # 输出: {1, 2, 3, 4, 5}
# 向集合添加元素
set_one.add(6)
print(set_one)  # 输出: {1, 2, 3, 4，5, 6}
# update() 添加多个元素 可以是列表，元组，字典等
set_one.update([7,8,9])
print(set_one)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 删除集合中的元素
set_one.remove(3)  # 如果元素不存在会引发 KeyError
# 移除集合中的元素，且如果元素不存在，不会发生错误
set_one.discard(3)
print(set_one)
# pop() 随机移除集合中的一个元素
# set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
set_one.pop()
print(set_one)
# clear() 清空集合
#set_one.clear()
#print(set_one)  # 打印 set()
# 计算集合元素个数
print(len(set_one))
# 判断元素是否在集合中存在
print(1 in set_one)
# union() 返回两个集合的并集 union
print(set_one.union(set_two))
# symmetric_difference_update()	 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
print(set_one.symmetric_difference_update(set_two))
print(set_one)
# symmetric_difference() 	返回两个集合中不重复的元素集合。
print(set_one.symmetric_difference(set_two))
print(set_one)
# issuperset() 判断该方法的参数集合是否为指定集合的子集
print(set_one.issuperset(set_two))
print(set_one)
# issubset() 判断该方法的参数集合是否为指定集合的父集
print(set_one.issubset(set_two))
print(set_one)
# isdisjoint() 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# 如果没有共同元素，返回 True。如果有共同元素（哪怕只有一个），返回 False。
print(set_two)
print(set_one.isdisjoint(set_two))
print(set_one)

#带有 _update 后缀的方法和没有它的方法（比如 intersection 和 intersection_update、difference 和 difference_update 等）主要区别在于是否修改原集合 以及 返回值。
#总结来说就是一句话：intersection() 是生成并返回一个“新集合”，原集合不变；而 intersection_update() 是“直接在原集合上动刀子把不需要的切掉”，不返回任何结果（返回 None）。

# intersection_update() 返回集合的交集。
print(set_one.intersection_update(set_two))
print(set_one)
# intersection() 返回集合的交集
print(set_one.intersection(set_two))
print(set_one)
# difference_update() 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
print(set_one.difference_update(set_two))
print(set_one)
# difference() 返回两个集合中不重复的元素集合。
print(set_one.difference(set_two))
print(set_one)
# copy() 复制集合
print(set_one.copy())
print(set_one)

# ------------------------------------------------------------集合间运算
print("# ------------------------------------------------------------集合间运算")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# a - b 集合a中包含而集合b中不包含的元素 差集
print(set_a - set_b)
# a | b  集合a或b中包含的所有元素 并集
print(set_a | set_b)
# a & b  集合a和b中都包含了的元素  交集
print(set_a & set_b)
# a ^ b  不同时包含于a和b的元素 对称差集  你有我没有，我没有你有的元素
print(set_a ^ set_b)

# ------------------------------------------------------------集合内置函数
