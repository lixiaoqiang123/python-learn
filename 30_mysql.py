# mysql 数据库连接
from importlib.metadata import PackageNotFoundError, version
from typing import Any
import os
import logging as log

import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
import dotenv

dotenv.load_dotenv()

log.basicConfig(
    level=log.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

QueryParams = tuple[Any, ...] | list[Any] | None
RowType = tuple[Any, ...]
QueryResult = list[RowType]


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


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"缺少环境变量 `{name}`，请检查 .env 配置。")
    return value


def close_db_resources(
    connection: MySQLConnection | None, cursor: MySQLCursor | None
) -> None:
    if cursor is not None:
        cursor.close()
    if connection is not None and connection.is_connected():
        connection.close()


def show_tables():
    rows = query_sql("SHOW TABLES")
    for row in rows:
        print(row)


def open_db() -> MySQLConnection:
    ensure_supported_connector()
    return mysql.connector.connect(
        host=get_required_env("MYSQL_HOST"),  # 数据库主机地址
        user=get_required_env("MYSQL_USER"),  # 数据库用户名
        password=get_required_env("MYSQL_PASSWORD"),  # 数据库密码
        database=os.getenv("MYSQL_DATABASE"),  # 数据库名，可选
    )

def query_sql(sql: str, params: QueryParams = None) -> QueryResult:
    mydb: MySQLConnection | None = None
    mycursor: MySQLCursor | None = None
    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        mycursor.execute(sql, params or ())
        return mycursor.fetchall()
    except mysql.connector.Error:
        log.exception("mysql query failed, sql=%s, params=%s", sql, params)
        raise
    finally:
        close_db_resources(mydb, mycursor)


def execute_sql(sql: str, params: QueryParams = None) -> int:
    mydb: MySQLConnection | None = None
    mycursor: MySQLCursor | None = None
    try:
        mydb = open_db()
        mycursor = mydb.cursor()
        mycursor.execute(sql, params or ())
        mydb.commit()
        return mycursor.rowcount
    except mysql.connector.Error:
        if mydb is not None and mydb.is_connected():
            mydb.rollback()
        log.exception("mysql execute failed, sql=%s, params=%s", sql, params)
        raise
    finally:
        close_db_resources(mydb, mycursor)



if __name__ == "__main__":
    result = query_sql("SELECT * FROM sys_user WHERE user_id = %s", (1,))
    log.info("sys_user query result: %s", result)
