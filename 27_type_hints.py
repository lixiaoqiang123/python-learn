from __future__ import annotations
# 类型注解
# ----------Python 的类型注解在运行时完全不起作用！注解只是一个"标签"，写给人看、给工具看的，运行时直接忽略。-------------------------
# -------------------------------------------------------------简单类型注解
def add(a:int,b:int=1)->int:
    return a+b

print(add(1))

# -------------------------------------------------------------复杂类型注解
# 在 Python 3.9 之前，list[str] 这种语法会直接报 TypeError，因为内置类型不支持 [] 下标操作。
# typing.List 是专门为类型注解设计的"包装版"，支持 [str] 这种泛型写法。
# 3.9之后可以直接使用 def func(names: list[str]) -> dict[str, int]:
from typing import List, Dict, Tuple, Set

# List[int] 表示这是一个只包含整数的列表
numbers: List[int] = [1, 2, 3, 4, 5]

# Dict[str, int] 表示这是一个键为字符串、值为整数的字典
student_scores: Dict[str, int] = {"Alice": 95, "Bob": 88}

# Tuple[int, str, bool] 表示这是一个包含整数、字符串、布尔值的元组
person_info: Tuple[int, str, bool] = (25, "Alice", True)

# Set[str] 表示这是一个只包含字符串的集合
unique_names: Set[str] = {"Alice", "Bob", "Charlie"}

# -------------------------------------------------------------from __future__ import annotations

# Python 3.8，没有 from __future__ import annotations
def func(names: list[str]):  # ← Python 立刻尝试执行 list[str]
    pass                     # 💥 TypeError: 'type' object is not subscriptable
# from __future__ import annotations 的目的就是让 Python 解析文件时不报错。
# 至于运行时 —— 根本不存在"注解被执行"这件事，所以也就谈不上报错。
# Python 3.8，有 from __future__ import annotations
def func(names: list[str]):  # ← Python 延迟执行 list[str]，保存为字符串func.__annotations__ == {'names': 'list[str]'}
    pass                     # ✅ 正常工作

# -------------------------------------------------------------可选类型（Optional）
# 1. 函数参数可以不传（默认为 None）
# 2. 函数返回值可能是 None（找不到结果时）
from typing import Optional

def find_student(name: str) -> Optional[str]:
    """根据名字查找学生，可能找到也可能返回None"""
    students = {"Alice": "A001", "Bob": "B002"}
    return students.get(name)  # 可能返回字符串或None

# 等价于 Union[str, None]

# --------------------------------------------------------------联合类型（Union）
from typing import Union

def process_input(data: Union[str, int, List[int]]) -> None:
    """处理可能是字符串、整数或整数列表的输入"""
    if isinstance(data, str):
        print(f"字符串: {data}")
    elif isinstance(data, int):
        print(f"整数: {data}")
    elif isinstance(data, list):
        print(f"列表: {data}")

process_input("hello")    # 输出：字符串: hello
process_input(42)         # 输出：整数: 42  
process_input([1, 2, 3])  # 输出：列表: [1, 2, 3]



# ----------------------------------------------------------类型检查实战
# mypy 可以检查是否有类型不符合，但是如果不检查，运行也不会报错，python运行不会校验类型注解
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers("5", "3")  # 这里有问题！传入了字符串

# -----------------------------------------------------------
from typing import List, Dict, Optional, Union

def process_students(students: List[Dict[str, Union[str, int]]]) -> Optional[float]:
    """
    处理学生数据，计算平均分数
    
    参数:
        students: 学生列表，每个学生是包含'name'和'score'的字典
        
    返回:
        平均分数（浮点数），如果没有学生则返回None
    """
    if not students:
        return None
    
    total = 0
    for student in students:
        total += student['score']
    
    return total / len(students)

# 测试数据
students_data = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie", "score": 92}
]

average = process_students(students_data)
print(f"平均分: {average}")