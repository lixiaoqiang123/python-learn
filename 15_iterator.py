# 迭代器与生成器

# ----------------------------------------------------------迭代器
# 迭代器是用于遍历序列或可迭代对象的对象。
# 迭代器可以通过 next() 函数获取下一个元素。
# 迭代器可以通过 iter() 函数获取。
# 超出范围之后会报错  StopIteration
list = [1,2,3,4,5]
# iterator只能遍历一次，因为迭代器内部维护了一个指针，走完就没了，节省内存
iterator = iter(list)
print(next(iterator))

# 使用for遍历迭代器
list_two = [1,2,3,4,5]
for x in iter(list_two):
    print (x, end=" ")

print("\n")
# 使用while遍历迭代器
while True:
    try:
        print(next(iterator),end=" ")
    except StopIteration:
        break


# 创建一个迭代器
# 要把一个类作为一个迭代器使用，需要在类中实现两个方法 __iter__() 与 __next__()。
# __iter__()：返回迭代器对象本身。
# __next__()：返回下一个数据，如果没有数据了则抛出 StopIteration 异常。

class MyNumbers:
    def __iter__(self):
        self.a = 1  # 初始化一个内部指针/状态，告诉迭代器从数字 1 开始
        return self # 返回对象本身，因为这个对象自己就包含了接下来需要的 __next__ 方法

    def __next__(self):
        if self.a <= 5: # 边界条件：只要当前的数字小于等于 5，就继续生成
            x = self.a  # 先把当前的值保存到变量 x 中准备返回
            self.a += 1 # 内部状态更新（指针往后走一步），为了下一次调用做准备
            return x    # 把刚刚保存的值弹出去，交给调用者
        else:            # 如果超过了 5
            raise StopIteration  # 抛出 StopIteration 异常。在 Python 中，这是迭代结束的标准化信号
         # for 循环如果在底层捕获到了这个异常，就会懂事地自动结束循环，而不会报错导致程序崩溃。

myclass = MyNumbers()
myiter = iter(myclass)

print("\n\n--- 自定义迭代器 ---")
print(next(myiter))
print(next(myiter))
# 剩下的用 for 遍历打印
for x in myiter:
    print(x, end=" ")
print()


# ----------------------------------------------------------生成器函数
# 生成器函数（Generator Function） 就是Python里一种拥有“记忆”和“暂停”能力的特殊函数。
print("-------------生成器-------------")
# 生成器是一种特殊的迭代器，它可以用更简单的方式创建。
# 生成器可以用 yield 语句创建。
# 生成器可以用生成器表达式创建。

# 虽然这个结构看着像老式的 def 函数，但因为里面带有 yield 关键字，Python 就不把它当普通函数看了，
# 而是把它编译成一个生成器函数。 普通函数的 return 代表“结束并强制退出函数”，而 yield 就像是“按下了暂停键并交出一个值”。
def countdown(n):
    while n > 0:
        yield n  # 关键点：产生一个值并暂停
        n -= 1   # 当 n 变成 0 的时候跳出 while 循环且没有遇到任何 yield 和 return，则默认抛出 StopIteration

# 一旦这个函数体正常跑完，或者遇到了真正的 return 关键字，没有任何多余的代码可以执行的时候，我就自动替你抛出 StopIteration 异常。
# 创建生成器对象
# 当你调用 countdown(5) 时，函数里面的代码（例如 while 和 yield）一行都没有执行！ 
# 它仅仅在后台创建并返回了一个生成器（一种特殊的迭代器）交给你。此时，里面的内部变量 n 被装载为了 5。
generator = countdown(5)
 
# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
 
# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1


# 自定义类迭代器：你自己当老板，员工什么时候下班，你得亲自喊（raise StopIteration）。
# 拥有 yield 的生成器：Python 会派一个监工帮盯着。监工一旦看到活干完了（代码跑到底了，或者遇到了 return），
# 监工会自动开除员工并上报完成（它替你抛出 StopIteration），完全不需要你操心。
