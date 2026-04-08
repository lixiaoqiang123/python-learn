# 列表
list_one = [1,2,3,4,'5']
# ----------------------------------------------列表脚本操作符
# 长度
print(len(list_one))
# 组合
print(list_one + [6,7,8])
# 重复
print(list_one * 2)
# 元素是否在列表中 
print(1 in list_one)
print(9 not in list_one)
# 迭代
for i in list_one:
    print(i,end=' ')


# ----------------------------------------------嵌套列表
list_two = [[1,2,3],[4,5,6],[7,8,9]]
print(list_two[0]) # [1,2,3]
print(list_two[0][1]) # 2


# ----------------------------------------------列表比较
list_three = [1,2,3]
list_four = [1,2,3]
# == 用于比较两个对象的值是否相等，而 is 用于检查两个对象是否是同一个内存对象（身份相同）
print(list_three == list_four) # True
print(list_three is list_four) # False
# operator.eq(a, b) 等同于 a == b，用于比较两个对象的值是否相等
import operator
print("operator.eq(a,b): ", operator.eq(list_three,list_four))


# ----------------------------------------------列表函数&方法

# 1. list.append(obj) — 在列表末尾添加新的对象
list_append = [1, 2, 3]
list_append.append(4)
print("append:", list_append)  # [1, 2, 3, 4]

# 2. list.count(obj) — 统计某个元素在列表中出现的次数
list_count = [1, 2, 2, 3, 2, 4]
print("count(2):", list_count.count(2))  # 3

# 3. list.extend(seq) — 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list_extend = [1, 2, 3]
list_extend.extend([4, 5, 6])
print("extend:", list_extend)  # [1, 2, 3, 4, 5, 6]

# 4. list.index(obj) — 从列表中找出某个值第一个匹配项的索引位置
list_index = [1, 2, 3, 2, 4]
print("index(2):", list_index.index(2))  # 1

# 5. list.insert(index, obj) — 将对象插入列表指定位置
list_insert = [1, 2, 4]
list_insert.insert(2, 3)
print("insert:", list_insert)  # [1, 2, 3, 4]

# 6. list.pop([index=-1]) — 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list_pop = [1, 2, 3, 4]
pop_val = list_pop.pop()
print("pop():", pop_val, list_pop)  # 4 [1, 2, 3]
pop_val2 = list_pop.pop(0)
print("pop(0):", pop_val2, list_pop)  # 1 [2, 3]

# 7. list.remove(obj) — 移除列表中某个值的第一个匹配项
list_remove = [1, 2, 3, 2, 4]
list_remove.remove(2)
print("remove(2):", list_remove)  # [1, 3, 2, 4]

# 8. list.reverse() — 反向列表中元素
list_reverse = [1, 2, 3, 4]
list_reverse.reverse()
print("reverse:", list_reverse)  # [4, 3, 2, 1]

# 9. list.sort(key=None, reverse=False) — 对原列表进行排序
list_sort = [3, 1, 4, 1, 5, 9, 2, 6]
list_sort.sort()
print("sort:", list_sort)  # [1, 1, 2, 3, 4, 5, 6, 9]
list_sort.sort(reverse=True)
print("sort(reverse=True):", list_sort)  # [9, 6, 5, 4, 3, 2, 1, 1]
# key参数：按指定规则排序
list_key = ['apple', 'pie', 'a', 'longword']
list_key.sort(key=len)
print("sort(key=len):", list_key)  # ['a', 'pie', 'apple', 'longword']

# 10. list.clear() — 清空列表
list_clear = [1, 2, 3]
list_clear.clear()
print("clear:", list_clear)  # []

# 11. list.copy() — 复制列表（浅拷贝）
list_copy = [1, 2, 3]
list_copied = list_copy.copy()
print("copy:", list_copied)  # [1, 2, 3]
# 验证是不同的对象
print("copy is same object:", list_copy is list_copied)  # False
