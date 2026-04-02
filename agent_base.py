# ✅ 必须会的（Agent / LangChain 基础）

# ─────────────────────────────────────────────
# 1. 基本语法（变量、if/for、函数、类）
# ─────────────────────────────────────────────

# 变量
name = "Alice"
age = 30
is_active = True

# if 判断
if age >= 18:
    print(f"{name} 是成年人")
elif age >= 12:
    print(f"{name} 是青少年")
else:
    print(f"{name} 是儿童")

# for 循环
tools = ["search", "calculator", "browser"]
for i, tool in enumerate(tools):
    print(f"  [{i}] {tool}")

# 函数
def greet(name: str, greeting: str = "你好") -> str:
    return f"{greeting}, {name}!"

print(greet("Bob"))
print(greet("Carol", "Hi"))

# 类
class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def describe(self) -> str:
        return f"Agent: {self.name}, 角色: {self.role}"

    def __repr__(self):
        return f"Agent(name={self.name!r}, role={self.role!r})"

agent = Agent("Jarvis", "助手")
print(agent.describe())


# ─────────────────────────────────────────────
# 2. pip / venv 环境管理（命令行操作，注释说明）
# ─────────────────────────────────────────────

# 创建虚拟环境：
#   python -m venv .venv
#
# 激活（Windows）：
#   .venv\Scripts\activate
#
# 激活（macOS/Linux）：
#   source .venv/bin/activate
#
# 安装依赖：
#   pip install langchain openai
#
# 导出依赖：
#   pip freeze > requirements.txt
#
# 从文件安装：
#   pip install -r requirements.txt


# ─────────────────────────────────────────────
# 3. 异步基础（async / await）— LangChain 大量用异步
# ─────────────────────────────────────────────
import asyncio

async def fetch_data(source: str) -> dict:
    """模拟异步获取数据（如调用 LLM API）"""
    await asyncio.sleep(0.1)  # 模拟网络延迟
    return {"source": source, "data": "some result"}

async def run_agent_async():
    # 并发执行多个异步任务
    results = await asyncio.gather(
        fetch_data("web"),
        fetch_data("database"),
    )
    for r in results:
        print(r)

# asyncio.run(run_agent_async())  # 取消注释即可运行


# ─────────────────────────────────────────────
# 4. 字典、列表操作（Agent 数据传递主要靠 dict）
# ─────────────────────────────────────────────

# --- 列表常用操作 ---
messages = []
messages.append({"role": "user", "content": "你好"})
messages.append({"role": "assistant", "content": "你好！有什么可以帮你的？"})

last_msg = messages[-1]          # 最后一条
user_msgs = [m for m in messages if m["role"] == "user"]  # 列表推导式

# --- 字典常用操作 ---
state = {"input": "帮我搜索天气", "steps": [], "output": None}

state["steps"].append("call_search_tool")  # 更新
output = state.get("output", "暂无结果")   # 安全取值

# 字典合并（Python 3.9+）
extra = {"model": "gpt-4", "temperature": 0.7}
config = {**state, **extra}       # 解包合并
# config = state | extra          # 等价写法（3.9+）

# 字典推导式
tool_map = {tool: idx for idx, tool in enumerate(tools)}
print(tool_map)  # {'search': 0, 'calculator': 1, 'browser': 2}


# ─────────────────────────────────────────────
# 5. 装饰器（@tool、@chain 等常见）
# ─────────────────────────────────────────────
import functools
import time

# 5-1 基础装饰器：计时器
def timer(func):
    @functools.wraps(func)  # 保留原函数元信息
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时 {elapsed:.3f}s")
        return result
    return wrapper

@timer
def slow_search(query: str) -> str:
    time.sleep(0.05)  # 模拟耗时操作
    return f"搜索结果: {query}"

print(slow_search("Python 装饰器"))

# 5-2 带参数的装饰器
def retry(max_times: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第 {attempt} 次失败: {e}")
            raise RuntimeError("超过最大重试次数")
        return wrapper
    return decorator

@retry(max_times=3)
def call_llm(prompt: str) -> str:
    # 模拟可能失败的 API 调用
    return f"LLM 回复: {prompt}"

# 5-3 模拟 LangChain @tool 装饰器
def tool(func):
    """简化版 @tool 装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Tool] 调用: {func.__name__}")
        return func(*args, **kwargs)
    wrapper.is_tool = True
    wrapper.tool_name = func.__name__
    return wrapper

@tool
def search(query: str) -> str:
    """在网络上搜索信息"""
    return f"搜索 '{query}' 的结果..."

print(search("LangChain 教程"))


# ─────────────────────────────────────────────
# 6. Type Hints（类型注解）
# ─────────────────────────────────────────────
from typing import Any, Optional, Union

# 基本注解
def process(text: str) -> dict:
    return {"input": text, "length": len(text)}

# Optional = 可以为 None
def get_memory(key: str) -> Optional[str]:
    store = {"session_id": "abc123"}
    return store.get(key)

# Union = 多种类型
def parse_input(data: Union[str, dict]) -> dict:
    if isinstance(data, str):
        return {"raw": data}
    return data

# list / dict 中的泛型
def run_chain(steps: list[str], config: dict[str, Any]) -> dict[str, Any]:
    return {"steps": steps, "config": config, "status": "done"}

# 使用示例
print(process("Hello Agent"))
print(get_memory("session_id"))
print(parse_input("some text"))


# ─────────────────────────────────────────────
# 👌 了解就行
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
# 7. 上下文管理器（with 语句）
# ─────────────────────────────────────────────
from contextlib import contextmanager

# 7-1 自定义上下文管理器（类写法）
class DBConnection:
    def __enter__(self):
        print("打开数据库连接")
        return self  # 赋值给 as 后的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        return False  # 不抑制异常

with DBConnection() as db:
    print("执行查询...")

# 7-2 用 @contextmanager 更简洁地定义
@contextmanager
def managed_session(session_id: str):
    print(f"开启 session: {session_id}")
    try:
        yield {"id": session_id}  # yield 前 = __enter__
    finally:
        print(f"关闭 session: {session_id}")  # yield 后 = __exit__

with managed_session("s-001") as session:
    print(f"当前会话: {session}")


# ─────────────────────────────────────────────
# 8. 生成器（yield）
# ─────────────────────────────────────────────

# 8-1 基本生成器：逐步生成 token（模拟 LLM 流式输出）
def stream_tokens(text: str):
    for word in text.split():
        yield word  # 一次返回一个词，不占用大量内存

for token in stream_tokens("Hello from streaming LLM"):
    print(token, end=" ")
print()

# 8-2 生成器表达式（类似列表推导式，但惰性求值）
squares = (x ** 2 for x in range(10))  # 不立即计算
print(list(squares))

# 8-3 带状态的流式生成（Agent 中间步骤流式输出）
def agent_stream(steps: list[str]):
    for step in steps:
        yield {"step": step, "status": "running"}
    yield {"step": "done", "status": "finished"}

for event in agent_stream(["search", "summarize", "respond"]):
    print(event)


# ─────────────────────────────────────────────
# 9. 数据类（@dataclass）
# ─────────────────────────────────────────────
from dataclasses import dataclass, field

@dataclass
class Message:
    role: str
    content: str
    metadata: dict = field(default_factory=dict)  # 可变默认值必须用 field

    def is_user(self) -> bool:
        return self.role == "user"

@dataclass
class AgentState:
    input: str
    messages: list[Message] = field(default_factory=list)
    tool_calls: list[str] = field(default_factory=list)
    output: Optional[str] = None

    def add_message(self, role: str, content: str):
        self.messages.append(Message(role=role, content=content))

# 使用示例
state = AgentState(input="查询今天天气")
state.add_message("user", "查询今天天气")
state.add_message("assistant", "北京今天晴，25℃")
print(state)


# ─────────────────────────────────────────────
# 10. Pydantic（数据校验，LangChain 重度依赖）
# ─────────────────────────────────────────────
# 需要安装：pip install pydantic

from pydantic import BaseModel, Field, field_validator

class ToolInput(BaseModel):
    query: str = Field(..., min_length=1, description="搜索关键词")
    max_results: int = Field(default=5, ge=1, le=20, description="最多返回结果数")

    @field_validator("query")
    @classmethod
    def query_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("query 不能为空白字符串")
        return v.strip()

class ToolOutput(BaseModel):
    results: list[str]
    total: int
    success: bool = True

# 正常使用
inp = ToolInput(query="  Python 教程  ", max_results=3)
print(inp)  # query 自动 strip

# 数据校验失败会抛出 ValidationError
# ToolInput(query="", max_results=3)  # 取消注释查看报错

# 嵌套模型
class AgentConfig(BaseModel):
    name: str
    model: str = "gpt-4"
    tools: list[str] = Field(default_factory=list)
    settings: dict[str, Any] = Field(default_factory=dict)

    def add_tool(self, tool_name: str) -> "AgentConfig":
        """返回新实例（Pydantic model 默认不可变风格）"""
        return self.model_copy(update={"tools": self.tools + [tool_name]})

cfg = AgentConfig(name="MyAgent", tools=["search"])
cfg2 = cfg.add_tool("calculator")
print(cfg2)