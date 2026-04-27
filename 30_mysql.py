# mysql 数据库连接
from importlib.metadata import PackageNotFoundError, version
import os

import mysql.connector
import dotenv

dotenv.load_dotenv()

def ensure_supported_connector():
    try:
        connector_version = version("mysql-connector-python")
    except PackageNotFoundError as exc:
        raise RuntimeError(
            "未检测到 mysql-connector-python。请先执行 `uv sync` 安装正确的 MySQL 驱动。"
        ) from exc

    major = int(connector_version.split(".", 1)[0])
    if major < 8:
        raise RuntimeError(
            f"当前 mysql-connector-python 版本过旧: {connector_version}。"
            "请升级到 8.x 或更高版本以支持 MySQL 8 的 caching_sha2_password 认证。"
        )


def show_tables():
    mydb = open_db()
    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for row in mycursor:
        print(row)

    mycursor.close()
    mydb.close()

def open_db():
    ensure_supported_connector()
    mydb = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),  # 数据库主机地址
        user=os.getenv("MYSQL_USER"),       # 数据库用户名
        password=os.getenv("MYSQL_PASSWORD"),       # 数据库密码
        database=os.getenv("MYSQL_DATABASE"),       # 数据库名，可选
    )
    return mydb

def execute_sql(sql):
    mydb = open_db()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    mydb.commit()
    mycursor.close()
    mydb.close()


if __name__ == "__main__":
    execute_sql("SELECT * FROM sys_user limit 1")
