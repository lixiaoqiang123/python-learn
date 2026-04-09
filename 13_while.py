# 循环语句
# for 迭代循环，用于遍历序列或可迭代对象
# range() 生成整数序列，常与 for 循环配合使用
# for适合列表，set，tuple，字符串，字典的循环
#while适合不知道要循环多少次，知道条件成立
for x in range(10):
    print(x,end=" ")
else:
    print("\nrange循环正常结束")
print("\n")
# while 循环，用于当条件为真时重复执行代码块
# break 语句用于跳出循环
while True:
    print("Hello World")
    break
else:
    pass
    print("\n循环正常结束")  # 有break，当前else不执行
# continue 语句用于跳过当前循环，进入下一次循环
#  else（循环） 循环正常结束（未被 break）时执行
num = 0
while num < 10:
    print(num,end=" ")
    num += 1
    continue  # 这一行后面的代码不会被执行,直接进入下一次循环
    num += 1
else:
    pass # pass 语句用于占位
    print("\nwhile循环正常结束")
print("\n")

# enumerate() 同时获取索引和值
fruits = ["Apple", "Banana", "Cherry"]
for index, value in enumerate(fruits):
    print(f"索引: {index}, 值: {value}")
print("\n")

# 循环 list  range(len(a)):  list(range(5))
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for x in a:
    print(x,end=" ")
else:
    print("\nlist循环正常结束")
print("\n")


for char in 'PYTHON STRING': # 会把字符串当成一个序列，一个一个的打印
    if char == ' ':
        break

    print(char, end=' ')
    
    if char == 'O':
        continue