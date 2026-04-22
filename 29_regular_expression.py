# 正则表达式
# re.match(pattern, string, flags=0)
# pattern:	匹配的正则表达式
# string:	要匹配的字符串。
# flags:	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
import re

# 它只从字符串的开头开始匹配。如果开头没对上，它就会直接放弃
# .span()：这个方法会返回一个元组，告诉你匹配到的起始位置和结束位置。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配


line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# matchObj 是 re.match() 或 re.search() 成功匹配后返回的“匹配对象”。
# 而 .group() 方法，就是从这个对象中把匹配到的字符串提取出来的“取件码”。
# .group(0) 或者 .group()  获取整个匹配的字符串
# .group(1) 获取第一个括号 () 匹配到的内容
# .group(2) 获取第二个括号 () 匹配到的内容
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


# re.search(pattern, string, flags=0)
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配


# match与search的区别
# re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，
# 而 re.search 匹配整个字符串，直到找到一个匹配。


# 检索和替换
# re.sub(pattern, repl, string, count=0, flags=0)

# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
# flags : 编译时用的匹配模式，数字形式。

phone = "2004-959-559 # 这是一个电话号码"  # 干扰信息

# 删除 # 和后面的所有内容
num = re.sub(r'#.*$', '', phone)
print ("电话号码：", num)

# repl 参数是一个函数
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))


# compile 函数 
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# re.compile(pattern[, flags])

# findall 
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。

# re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

# re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表
# re.split(pattern, string[, maxsplit=0, flags=0])


# 正则表达式对象
# re.RegexObject
# re.compile() 返回 RegexObject 对象。

# re.MatchObject
# group() 返回被 RE 匹配的字符串。

# start() 返回匹配开始的位置
# end() 返回匹配结束的位置
# span() 返回一个元组包含匹配 (开始,结束) 的位置