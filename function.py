import math
import random
# 函数
# ----------------------------------------------数学函数
# abs() 取绝对值 1
print(abs(-1))
# round() 四舍五入 1.24
print(round(1.23556, 2))
# pow() 求幂 8
print(pow(2, 3))
# ceil(x) 向上取整 2
print(math.ceil(1.23456))
# floor(x) 向下取整 1
print(math.floor(1.23456))
# exp(x) e的x次方
print(math.exp(1))
# log(x) 自然对数
print(math.log(1))
# log10(x) 以10为底的对数
print(math.log10(1))
# fabs(x) 取绝对值 1.0
print(math.fabs(-1)) 
# max(x1, x2,...) 取最大值 3
print(max(1, 2, 3))
# min(x1, x2,...) 取最小值 1
print(min(1, 2, 3))
# sum(iterable) 求和 6
print(sum([1, 2, 3]))
# prod(iterable) 求积 6
print(math.prod([1, 2, 3]))
# modf(x) 返回x的小数部分和整数部分 (0.2345600000000001, 1.0)
print(math.modf(1.23456))
# sqrt(x) 平方根 2.0
print(math.sqrt(4))



# -----------------------------------------------随机数函数
# choice(seq) 从序列中随机选择一个元素
seq = [1,2,3,4,5,6]
print(random.choice(seq))
# randrange ([start,] stop [,step])  从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# start	1	从 1 开始  stop	10	到 10 结束（不包含 10）  step  2	每次步进 2
# start 默认为 0   step 默认为 1
# 1,3,5,7,9
print(random.randrange(1, 10, 2))
# random()  返回一个0.0到1.0之间的随机浮点数
print(random.random())
# seed([x])  初始化随机数生成器  改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# 调试/测试，需要可重复的结果	✅ 用固定 seed
# 正式运行，需要真正随机的结果	❌ 不用 seed（或不传参数）
# 机器学习实验，保证结果可复现	✅ 用固定 seed
# seed(1) 就像给随机数发生器设置了一个固定的"出发点"，每次从同一个点出发，走出的路径自然完全一样。
# random.seed(1)
# shuffle(lst)  将序列随机打乱
random.shuffle(seq)
print(seq)
# uniform(x, y)  返回一个x到y之间的随机浮点数
print(random.uniform(1, 10))



# -----------------------------------------------三角函数
# acos(x)  反余弦
print(math.acos(1))
# asin(x)  反正弦
print(math.asin(1))
# atan(x)  反正切
print(math.atan(1))
# atan2(y, x)  反正切
print(math.atan2(1, 1))
# cos(x)  余弦
print(math.cos(1))
# sin(x)  正弦
print(math.sin(1))
# tan(x)  正切
print(math.tan(1))
# degrees(x)  弧度转换为角度
print(math.degrees(1))
# radians(x)  角度转换为弧度
print(math.radians(1))


# -----------------------------------------------数学常量
pi = math.pi
e = math.e
print(pi)
print(e)