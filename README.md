# AMLIP - AML Intelligence Platform (Graph & OLAP Financial Tracing)

An enterprise-grade analytical platform designed to detect money laundering schemes, identify hidden ultimate beneficial owners (UBOs), and track suspicious financial transactions in real time.

Built specifically to handle high-throughput analytical workloads, complex graph relationships, and real-time event processing.

---

## Key Features

* **Interactive Graph Canvas:** Renders multi-hop ownership structures, corporate networks, and financial flows using `@xyflow/react` with custom node/edge components.
* **High-Speed OLAP Engine:** Sub-50ms analytical aggregation querying across 1,000,000+ transaction records powered by **ClickHouse**.
* **Real-Time Stream Processing:** Ingests live financial transaction streams via **NATS** at 50+ events per second and pushes live alerts to the frontend via Server-Sent Events (SSE).
* **Pattern Detection Algorithms:** Automatically identifies circular money routing (ring schemes), rapid pass-through accounts, and smurfing operations.
* **AI Case Summarization:** Uses `pydantic-ai` integrated with LLM endpoints to generate structured investigation summaries for compliance officers.

---

## Tech Stack

### Backend
* **Language & Framework:** Python 3.12+, Litestar
* **Dependency Injection:** Dishka (App & Request scopes)
* **Data Validation & ORM:** Pydantic v2, SQLAlchemy 2.0 (async), Alembic
* **Databases:** 
  * **ClickHouse** (OLAP transaction logs & aggregations)
  * **Neo4j** (Graph data for company links and UBOs)
  * **PostgreSQL** (Relational metadata, rules, user cases)
* **Messaging & Tasks:** NATS JetStream, Taskiq
* **Tooling & Quality:** `uv`, `ruff`, `pytest-asyncio`

### Frontend
* **Core:** React 19, TypeScript, Vite, Bun
* **Architecture:** Feature-Sliced Design (FSD)
* **Graph & Data Viz:** `@xyflow/react`, ECharts
* **State & Data Fetching:** TanStack Query, Zustand
* **UI Components:** Tailwind CSS 4, Radix UI / shadcn
* **API Integration:** Code-generated client via `@hey-api/openapi-ts`

---

## Architecture Overview


```

```
                    +----------------------------------+
                    | Continuous Synthetic Data Engine |
                    |     (NATS Stream @ 50 req/sec)   |
                    +----------------+-----------------+
                                     |
                                     v

```

+-----------------------+     +--------------------+     +-------------------+
|  ClickHouse (OLAP)    |     |  Litestar Backend  |     |  Neo4j (Graph DB) |
| Transaction Logs &    | <-> |  (Dishka DI, DDD)  | <-> | Company Links &   |
| Fast Aggregations     |     |                    |     | Ownership Nodes   |
+-----------------------+     +---------+----------+     +-------------------+
|
| SSE / HTTP REST
v
+----------------------------------+
|  React 19 Frontend (FSD)         |
|  - Interactive Graph Canvas      |
|  - ECharts Analytical Dashboard  |
+----------------------------------+

```

---

## Synthetic Data Generator

This project includes a dedicated **Data Engine** that populates the platform with realistic, high-volume synthetic datasets upon deployment:
* **5,000+ Legal Entities & Individuals** with realistic tax IDs, registration details, and cross-company links.
* **1,000,000+ Historical Transactions** partitioned in ClickHouse for OLAP benchmarking.
* **Embedded Laundering Patterns:** Pre-seeded financial anomalies (circular routing, shell company networks) for testing detection algorithms.

---

## Quick Start (Docker)

```bash
# 1. Clone repository
git clone [https://github.com/itsventie/AMLIP.git](https://github.com/itsventie/AMLIP.git)
cd AMLIP

# 2. Environment Setup
cp .env.example .env

# 3. Spin up all services
docker compose up -d --build

```

### Endpoints

* **Web UI:** `http://localhost:3000`
* **API Documentation:** `http://localhost:8000/schema/swagger`
* **Neo4j Browser:** `http://localhost:7474`

---

## Testing

```bash
# Backend tests
uv run pytest

# Frontend tests & linting
bun run biome check .
bun run vitest

```
