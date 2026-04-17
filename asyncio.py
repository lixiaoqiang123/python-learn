import asyncio
import time

"""
asyncio 是 Python 用于编写并发代码的库。

底层原理：
1. 事件循环 (Event Loop): 管理和调度所有任务。
2. 协程 (Coroutines): 特殊的函数，可以在 await 处挂起，让出 CPU 给其他任务。
3. 非阻塞 I/O: 利用操作系统的 select/poll/epoll 机制，在等待网络/磁盘时不需要阻塞线程。
"""

async def fetch_data(id, delay):
    print(f"任务 {id}: 准备获取数据... (预计耗时 {delay}秒)")
    # await 会挂起当前协程，事件循环会去执行其他协程
    await asyncio.sleep(delay) 
    print(f"任务 {id}: 数据获取成功！")
    return f"Data_{id}"

async def main():
    start_time = time.time()
    print("主程序开始执行...")

    # 创建任务（立即提交到事件循环，但不会阻塞）
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 1))

    print("主程序继续执行其他业务...")

    # 获取结果（如果结果还没出来，main 会在此挂起等待）
    result1 = await task1
    result2 = await task2

    end_time = time.time()
    print(f"所有任务完成！结果: {result1}, {result2}")
    print(f"总计用时: {end_time - start_time:.2f} 秒 (如果串行需要 3 秒)")

if __name__ == "__main__":
    # 启动事件循环
    asyncio.run(main())