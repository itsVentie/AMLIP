import asyncio
import asyncpg
import clickhouse_connect
from neo4j import AsyncGraphDatabase
import nats
from redis.asyncio import Redis

async def check_connections():
    print("Starting connectivity checks...\n")

    try:
        conn = await asyncpg.connect("postgresql://amlip_user:amlip_password@127.0.0.1:5433/amlip_db")
        val = await conn.fetchval("SELECT 1;")
        await conn.close()
        print("PostgreSQL: Connected (SELECT 1 -> OK)")
    except Exception as e:
        print(f"PostgreSQL: Failed ({e})")

    try:
        r = Redis(host="127.0.0.1", port=16379)
        await r.ping()
        await r.aclose()
        print("Redis: Connected (PING -> PONG)")
    except Exception as e:
        print(f" Redis: Failed ({e})")

    try:
        nc = await nats.connect("nats://localhost:4222")
        print("NATS: Connected")
        await nc.close()
    except Exception as e:
        print(f"NATS: Failed ({e})")

    try:
        driver = AsyncGraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "amlip_password"))
        async with driver.session() as session:
            result = await session.run("RETURN 1 AS num")
            record = await result.single()
            print("Neo4j: Connected (RETURN 1 -> OK)")
        await driver.close()
    except Exception as e:
        print(f"Neo4j: Failed ({e})")

    try:
        client = clickhouse_connect.get_client(
            host="localhost", port=8123, username="amlip_user", password="amlip_password"
        )
        res = client.command("SELECT 1")
        print("ClickHouse: Connected (SELECT 1 -> OK)")
    except Exception as e:
        print(f" ClickHouse: Failed ({e})")

    print("\nAll checks completed")

if __name__ == "__main__":
    asyncio.run(check_connections())
