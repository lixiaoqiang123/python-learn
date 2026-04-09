# 条件判断
# if   else  elif  pass  match
while True:
    try:
        num = int(input("请输入一个数字："))
        break  # 如果成功转换为整数，跳出循环
    except ValueError:
        print("输入无效！这不是一个正确的整数，请重新输入。")

    if num > 0:
        print("输入的数字大于0")
    elif num == 0:
        print("输入的数字是0")
    else:
        print("输入的数字小于0")

# pass 占位符
# 1. 条件判断中的占位 TODO将来补充
# 2. 未实现的函数或类
# 3. 异常捕获中忽略特定的错误  遇到除零异常什么都不做
if num > 0:
    pass
else:
    print("输入的数字小于0")

# match  匹配 
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:  # 多个匹配条件
            return "Not allowed - 无权限或未找到"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
 
print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))

# 因为 case 后面强制要求必须先给出一个用来比对的“形状/模式（Pattern）”，你不能上来就写个判断逻辑。
# 所以我们只好先塞一个什么都能配对的 _ 糊弄过去，然后依靠 if 守卫条件来完成真正的逻辑过滤
match num:
    case _ if num > 0:
        print("输入的数字大于0")
    case 0:
        print("输入的数字是0")
    case _ if num < 0:
        print("输入的数字小于0")
