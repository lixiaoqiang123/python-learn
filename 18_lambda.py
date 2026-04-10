# lambda表达式
# lambda arguments: expression
# lambda是 Python 的关键字，用于定义 lambda 函数。
# arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
# expression 是一个表达式，用于计算并返回函数的结果。

# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
# map(..., numbers)
# map 接收两个参数：一个是函数（在这里是前面定义的 lambda），另一个是可迭代对象（在这里是 numbers 列表）。
# 它的工作原理是：遍历 numbers 列表 [1, 2, 3, 4, 5] 中的每一个元素，然后将这个元素传给前面的 lambda 函数执行。
# 它会依次计算：1**2，2**2，3**2，4**2，5**2。
# 注意：在 Python 3 中，map() 返回的是一个迭代器对象（map object），而不是直接返回列表，这样可以节省内存空间。
# 因为 map() 返回的是一个迭代器，为了能够直观地看到结果或者后续像列表那样去操作它，我们使用 list() 函数将这个迭代器中的所有计算结果提取出来，并打包成一个真正的列表 [1, 4, 9, 16, 25]。
print(squared)  # 输出: [1, 4, 9, 16, 25]

# ------- 使用 lambda 函数与 filter() 一起，筛选偶数：------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]

# -------下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：------------

from functools import reduce
 
numbers = [1, 2, 3, 4, 5]
 
# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)
# reduce 顾名思义就是“归约”或“折叠”，它的执行过程正是你写出来的这种**“滚雪球”式（累积）**的计算方式。
# （（（（1*2）*3）*4）*5）
print(product)  # 输出：120