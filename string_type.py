# 字符串
#-----------------------------------------------------------------访问字符串中的值
string_one = "Hello World"
print(string_one[0])
print(string_one[0:7])

#------------------------------------------------------------------字符串更新；字符串是不可变的
print(f"更新字符串：{string_one[0:6] + 'Python'}")
print("更新字符串：",{string_one[0:6] + 'Python'},"World")
# 转义字符
print(r"\n")
# 续行符
print("Hello World \
            Python")
# 反斜杠符号
print("\\")
# 单引号
print("\'")
# 双引号
print("\"")
# 退格(Backspace)
print("Hello  \bWorld")
# 空
print("\000")
# 换行
print("\n")
# 纵向制表符
print("Hello  \v World")
# 横向制表符  对齐文本  \t 会跳到下一个 8 的倍数位
print("姓名\t年龄\t城市")
print("张三\t25\t北京")
print("李四\t30\t上海")
print("王五二\t22\t广州")

# 回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print("Hello\rWorld")
# 换页
print("Hello\fWorld")
# 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\110\145\154\154\157\40\127\157\162\154\144\41")
# 十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")
# 其它的字符以普通格式输出
print("\other")


#-----------------------------------------------字符串运算符
# + 拼接
# * 重复打印
print("HelloWorld"*2)
# in 在字符串中  not in 不在字符串中
print("a" in "abc")
print("a" not in "abc")

# /r 实现进度条
# end=''	不自动换行	让 \r 能覆盖同一行
# flush=True  立即刷新输出缓冲区	进度条实时更新，不卡顿
#import time
for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
    #time.sleep(0.05)
print()
# {i:3}  i 占 3 位，不足补空格  防止打印的时候抖动
# # 必须有 f 前缀！
# ' 10'  ← 宽度3，右对齐
print(f"{10:3}")

#------------------------------------------------------------------字符串格式化
# %s	字符串
# %d	整数
# %f	浮点数
# %.2f	保留2位小数
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# str.format() 较常用
print("我叫{}今年{}岁!".format("小明",10))

# f-string python3.6+ 推荐使用
name = "小明"
age = 10
price = 3.14159

print(f"我叫 {name} 今年 {age} 岁!")        # 基本用法
print(f"价格: {price:.2f}")                  # 保留2位小数 → 3.14
print(f"年龄: {age:3d}")                     # 宽度3位     →  10
print(f"计算: {age * 2}")                    # 支持表达式  → 20
print(f"大写: {name.upper()}")               # 支持方法    → 小明（无效，upper对中文无效）

# 在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：
x = 1
print(f'{x+1}')   # Python 3.6   2
x = 1
print(f'{x+1=}')   # Python 3.8   x+1=2

# Unicode 字符串
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
# 在Python3中，所有的字符串都是Unicode字符串。



#----------------------------------------------------------------------字符串内建函数
# capitalize() 
# 将字符串的第一个字符转换为大写


# center(width, fillchar) 
# 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

# count(str, beg= 0,end=len(string)) 
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

# bytes.decode(encoding="utf-8", errors="strict") 
# Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。

# encode(encoding='UTF-8',errors='strict')
# 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

# endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 suffix 结束，如果 beg 或者 end 指定则检查指定的范围内是否以 suffix 结束，如果是，返回 True,否则返回 False。

# expandtabs(tabsize=8)
# 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

# find(str, beg=0, end=len(string))
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1

# index(str, beg=0, end=len(string))
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常。

# isalnum()
# 检查字符串是否由字母和数字组成，即字符串中的所有字符都是字母或数字。如果字符串至少有一个字符，并且所有字符都是字母或数字，则返回 True；否则返回 False。

# isalpha()
# 检查字符串是否只由字母组成，即字符串中的所有字符都是字母。如果字符串至少有一个字符，并且所有字符都是字母，则返回 True；否则返回 False。

# isdecimal()
# 检查字符串是否只由十进制数字组成，即字符串中的所有字符都是十进制数字。如果字符串至少有一个字符，并且所有字符都是十进制数字，则返回 True；否则返回 False。

# isdigit()
# 检查字符串是否只由数字组成，即字符串中的所有字符都是数字。如果字符串至少有一个字符，并且所有字符都是数字，则返回 True；否则返回 False。

# isidentifier()
# 检查字符串是否是有效的 Python 标识符。如果字符串至少有一个字符，并且所有字符都是字母、数字或下划线，并且第一个字符不是数字，则返回 True；否则返回 False。

# islower()
# 检查字符串是否只由小写字母组成，即字符串中的所有字符都是小写字母。如果字符串至少有一个字符，并且所有字符都是小写字母，则返回 True；否则返回 False。

# isnumeric()
# 检查字符串是否只由数字组成，即字符串中的所有字符都是数字。如果字符串至少有一个字符，并且所有字符都是数字，则返回 True；否则返回 False。

# isprintable()
# 检查字符串是否只由可打印字符组成，即字符串中的所有字符都是可打印字符。如果字符串至少有一个字符，并且所有字符都是可打印字符，则返回 True；否则返回 False。

# isspace()
# 检查字符串是否只由空白字符组成，即字符串中的所有字符都是空白字符。如果字符串至少有一个字符，并且所有字符都是空白字符，则返回 True；否则返回 False。

# istitle()
# 检查字符串是否是标题化的，即字符串中的每个单词的首字母都是大写，其余字母都是小写。如果字符串至少有一个字符，并且是标题化的，则返回 True；否则返回 False。

# isupper()
# 检查字符串是否只由大写字母组成，即字符串中的所有字符都是大写字母。如果字符串至少有一个字符，并且所有字符都是大写字母，则返回 True；否则返回 False。

# join(iterable)
# 将可迭代对象中的所有元素连接成一个字符串，元素之间用字符串分隔。如果可迭代对象中的元素不是字符串，则会报一个 TypeError 异常。

# ljust(width, fillchar)
# 返回一个指定的宽度 width 居左的字符串，fillchar 为填充的字符，默认为空格。

# lower()
# 将字符串中的所有字符转换为小写。

# lstrip(chars)
# 返回一个字符串的副本，其中开头的指定字符被删除。如果 chars 未指定，则删除开头的空白字符。

# partition(sep)
# 将字符串分割成三部分：分隔符之前的部分、分隔符本身和分隔符之后的部分。如果分隔符不存在，则返回字符串本身和两个空字符串。

# replace(old, new, count)
# 返回一个字符串的副本，其中所有出现的 old 都被 new 替换。如果 count 未指定，则替换所有出现的 old。

# rfind(str, beg=0, end=len(string))
# 跟 find() 方法一样，只不过是从字符串的末尾开始查找。

# rindex(str, beg=0, end=len(string))
# 跟 index() 方法一样，只不过是从字符串的末尾开始查找。

# rpartition(sep)
# 将字符串分割成三部分：分隔符之前的部分、分隔符本身和分隔符之后的部分。如果分隔符不存在，则返回两个空字符串和字符串本身。

# rjust(width, fillchar)
# 返回一个原字符串右对齐，并使用 fillchar（默认空格）填充至长度 width 的新字符串。

# rstrip(chars)
# 返回一个字符串的副本，其中结尾的指定字符被删除。如果 chars 未指定，则删除结尾的空白字符。

# split(sep=None, maxsplit=-1)
# 将字符串分割成一个列表，元素之间用分隔符分隔。如果分隔符未指定，则按空白字符分割。如果 maxsplit 未指定，则分割所有出现的分隔符。

# splitlines(keepends=False)
# 将字符串分割成一个列表，元素之间用换行符分隔。如果 keepends 为 True，则保留换行符。

# startswith(prefix, beg=0, end=len(string))
# 检查字符串是否以 prefix 开始，如果 beg 或者 end 指定则检查指定的范围内是否以 prefix 开始，如果是，返回 True,否则返回 False。

# strip(chars)
# 返回一个字符串的副本，其中开头的和结尾的指定字符被删除。如果 chars 未指定，则删除开头的和结尾的空白字符。

# swapcase()
# 将字符串中的所有大写字母转换为小写，所有小写字母转换为大写。

# title()
# 将字符串中的每个单词的首字母转换为大写，其余字母转换为小写。

# translate(table, deletechars="")
# 返回一个字符串的副本，其中所有出现的指定字符都被替换。如果 deletechars 未指定，则不删除任何字符。

# upper()
# 将字符串中的所有字符转换为大写。

# zfill(width)
# 返回一个指定的宽度 width 的字符串，左侧用零填充。

# maketrans()
# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

# max(str)
# 返回字符串中最大的字符。

# min(str)
# 返回字符串中最小的字符。
