import decimal
#-------------缩进
if True:
    print("True")
else:
    print("False")


#-------------换行
item_one = 1
item_two = 2
item_three = 3

item_sum = item_one + \
            item_two + \
            item_three

print(item_sum)

#---------------------数字类型：int bool float complex
print(type(1))
# 虽然布尔型看起来是独立的，但它实际上是 int 的子类。True 的值等于 1，False 的值等于 0。
print(type(True))
# float 浮点数在计算机内部是用二进制表示的，这偶尔会导致精度误差。
print(0.1+0.2)
print(decimal.Decimal('0.1')+decimal.Decimal('0.2'))
print(type(1.0))
# 复数分为实部和虚部，常用于科学计算
print(type(1+1j))


#---------------------字符串:
print('''李晓强
        学习 Python''')
str = "1234567"
print(str[0:-1])
#输出第二个字符，2不包含
print(str[1:2])
print(str[1:-2])
#步长，从0开始，到3结束，步长为2
print(str[0:3:2])
 # 使用反斜杠(\)+n转义特殊字符
print('hello\nrunoob') 
# 在字符串前面添加一个 r，表示原始字符串，不会发生转义    
print(r'hello\nrunoob')    



#---------------------用户输入
name =input("请输入：")
print(name)

#---------------------同一行显示多条语句
# print 是对 sys.stdout.write 的高级封装；print默认在末尾加 \n，而sys.stdout.write不会
# 特性	print("Hello")	sys.stdout.write("Hello")
# 自动换行	默认在末尾加 \n	不会自动加换行符
# 类型限制	可以打印数字、列表、对象等	只能接收字符串（必须手动转码）
# 返回值	返回 None	返回 写入字符的长度
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

import sys
import time

for i in range(11):
    percent = i * 10
    # \r 让光标回到行首，不换行继续写
    sys.stdout.write(f"\r进度: [{'#' * i}{'.' * (10-i)}] {percent}%")
    sys.stdout.flush() # 强制刷新缓冲区，立即显示
    time.sleep(0.2)


#---------------------多个语句构成代码组  数字 < 大写字母 < 小写字母（例如：'A' < 'a' 是 True）。
# == 比较的是 值 (Value)。  is 比较的是 内存地址 (Identity)。
#当前是比较字符串大小，空字符串小于长度小于任何字符串
num = input("请输入一个数字：")
if num =='0':
    print("等于0")
elif num>'0':
    print("大于0")
elif num<'0':
    print("小于0")

#正确的应该是比较数字大小
try:
    num = int(input("请输入一个数字："))
    if num == 0:
        print("等于0")
    elif num > 0:
        print("大于0")
    elif num < 0:
        print("小于0")
except ValueError:
    print("请输入一个有效的数字")


#---------------------print输出,实现不换行需要在变量末尾加上 end=""
print("Hello World",end=" ")

