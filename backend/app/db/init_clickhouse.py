from pathlib import Path

import clickhouse_connect

from app.core.config import settings


def init_clickhouse_schema() -> None:
    client = clickhouse_connect.get_client(
        host=settings.CLICKHOUSE_HOST,
        port=settings.CLICKHOUSE_PORT,
        username=settings.CLICKHOUSE_USER,
        password=settings.CLICKHOUSE_PASSWORD,
    )

    sql_file = Path(__file__).parent / "clickhouse_ddl.sql"
    sql_script = sql_file.read_text(encoding="utf-8")

    for statement in sql_script.split(";"):
        stmt = statement.strip()
        if stmt:
            client.command(stmt)

    print("ClickHouse schema initialized successfully!")


if __name__ == "__main__":
    init_clickhouse_schema()
