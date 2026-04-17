# 输入与输出
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。

s = 'Hello World'
print(str(s))
print(repr(s))
print(str(1/7))

# rjust()、ljust()、center()
# 字符串对齐
print(s.rjust(20))
print(s.ljust(20))
print(s.center(20))

# 字符串替换
print(s.replace('World', 'Python'))

for x in range(1, 11):
    # {0:2d}: 0 代表 .format() 中的第 1 个参数（即 x）。
    # :2d: d: 表示这是一个整数（decimal）。
    # 2: 表示占据 2 个字符的宽度。如果数字只有 1 位（比如 1），左边会补一个空格。
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# zfill()
print('42'.zfill(5))

# str.format()
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

# 在括号中的数字用于指向传入对象在 format() 中的位置
print('{1} 和 {0}'.format('Google', 'Runoob'))

# 关键字参数
print('{name}网址： "{url}!"'.format(name='菜鸟教程', url='www.runoob.com'))

# 位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

# f-string
name = '菜鸟教程'
print(f'{name}网址： "{name}!"')

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 更多示例展示 !a, !s, !r 的区别
name = '菜鸟教程'
print('str:   {!s}'.format(name))    # 默认，打印字符串内容
print('repr:  {!r}'.format(name))    # 包含引号
print('ascii: {!a}'.format(name))    # 使用转义序列表示非 ASCII 字符

# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# 也可以通过在 table 变量前使用 ** 来实现相同的功能：
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

# 读写文件
with open('example.txt','r') as file:
    pass


f = open('example.txt','a+')
# f.write()
# f.write(string) 将字符串写入文件，并返回写入的字符数。
# 注意：f.write() 不会自动在末尾添加换行符，如果需要换行，需要手动添加 '\n'。
print(f.write("\nHello, World!\n"))
# f.seek(offset, whence) 用于移动文件指针到指定位置。
# offset 表示相对于 whence 参数的偏移量，from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符
f.seek(0)           # 移动指针到开头，否则 read() 会读不到内容
# f.read()
# 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
print(f.read())
# f.readline()
# f.readline() 将读取文件中的一行，包括末尾的换行符（如果存在）。
# 如果文件很大，一次性读入内存可能会导致问题。这时可以使用 f.readline() 逐行读取。
print(f.readline())
# f.readlines()
# f.readlines() 将读取文件中的所有行，并返回一个列表，列表中的每个元素都是文件中的一行（包括末尾的换行符）。
print(f.readlines())

# 第一个read()读到文件末尾，所以后面的read()读不到内容

# f.tell() 用于返回文件当前的读/写位置（即文件指针的位置）。文件指针表示从文件开头开始的字节数偏移量。
# f.tell() 返回一个整数，表示文件指针的当前位置。

print(f.tell())
# 当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
f.close()



# --------------------------------------------------------------------pickle 模块
# pickle 模块实现了二进制协议的序列化和反序列化。
# 序列化（Pickling）  ：将 Python 对象 → 字节流（bytes）
# 反序列化（Unpickling）：将字节流（bytes） → Python 对象
import pickle

# ── 1. pickle.dumps() / pickle.loads()  ──────────────────────────────
# dumps()：将对象序列化为 bytes 对象（不涉及文件）
# loads()：将 bytes 对象反序列化为 Python 对象
data = {'name': '小明', 'age': 20, 'scores': [95, 87, 76]}
serialized = pickle.dumps(data)          # 序列化 → bytes
print(type(serialized))                  # <class 'bytes'>
print(serialized[:20])                   # 显示部分字节内容

restored = pickle.loads(serialized)      # 反序列化 → dict
print(restored)                          # {'name': '小明', 'age': 20, 'scores': [95, 87, 76]}
print(type(restored))                    # <class 'dict'>

# ── 2. pickle.dump() / pickle.load()  写入/读取文件 ──────────────────
# dump()：将对象序列化后写入文件（必须以二进制模式 'wb' 打开）
# load()：从文件读取字节流并反序列化（必须以二进制模式 'rb' 打开）
with open('data.pkl', 'wb') as f:        # 'wb' 写二进制
    pickle.dump(data, f)

with open('data.pkl', 'rb') as f:        # 'rb' 读二进制
    loaded = pickle.load(f)
print(loaded)                            # {'name': '小明', 'age': 20, 'scores': [95, 87, 76]}

# ── 3. 序列化自定义类对象 ─────────────────────────────────────────────
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f'Student({self.name!r}, grade={self.grade})'

stu = Student('小红', 'A')
with open('student.pkl', 'wb') as f:
    pickle.dump(stu, f)

with open('student.pkl', 'rb') as f:
    stu_loaded = pickle.load(f)
print(stu_loaded)                        # Student('小红', grade='A')
print(stu_loaded.name)                   # 小红

# ── 4. 一次写入 / 读取多个对象 ──────────────────────────────────────
objs = [1, 'hello', [1, 2, 3], {'key': 'value'}]
with open('multi.pkl', 'wb') as f:
    for obj in objs:
        pickle.dump(obj, f)              # 逐个写入

with open('multi.pkl', 'rb') as f:
    while True:
        try:
            obj = pickle.load(f)        # 逐个读取
            print(obj)
        except EOFError:                # 文件读完时抛出 EOFError
            break

# ── 5. 注意事项 ──────────────────────────────────────────────────────
# ① pickle 文件是二进制格式，不能用普通文本编辑器打开
# ② 只能在 Python 之间传输，不适合跨语言数据交换（JSON 更合适）
# ③ 不要对来源不可信的 pickle 文件调用 load()，存在安全风险
# ④ protocol 参数可指定协议版本（默认 DEFAULT_PROTOCOL）
#    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)  # 最高版本，效率最好
