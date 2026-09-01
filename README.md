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

---

### Roadmap & Implementation Progress

<details>
<summary><b>Phase 1: Architecture & Local Dev Environment Setup</b></summary>

- [x] Initialize monorepo project structure
- [x] Setup Python 3.12 backend workspace with `uv` package manager and `ruff` linter
- [x] Setup React 19 frontend workspace with `bun` and `biome` linter
- [x] Create `docker-compose.yml` for local infrastructure:
  - [x] PostgreSQL 16 (Relational metadata)
  - [x] ClickHouse (OLAP analytical engine)
  - [x] Neo4j 5 (Graph database)
  - [x] NATS JetStream (Event broker)
  - [x] Redis (Cache & Session state)
  - [x] MinIO (S3 object storage for report exports)
- [ ] Verify connectivity and health checks across all containerized services

</details>

<details>
<summary><b>Phase 2: Database Schemas & Domain Modeling (DDD)</b></summary>

- [ ] **PostgreSQL Setup:**
  - [ ] Configure `SQLAlchemy 2.0` async models and `Alembic` migrations
  - [ ] Design domain entities: `User`, `InvestigationCase`, `RiskRule`, `AuditLog`
- [ ] **ClickHouse Setup:**
  - [ ] Design high-throughput `transactions` table using `MergeTree` engine
  - [ ] Configure partitioning strategy (by month) and primary sorting keys (`timestamp`, `from_bin`, `to_bin`)
- [ ] **Neo4j Setup:**
  - [ ] Define graph node types: `Company`, `Person`, `BankAccount`
  - [ ] Define relationship edges: `OWNER_OF`, `DIRECTOR_OF`, `TRANSFERRED_FUNDS`
  - [ ] Write Cypher indexes for rapid multi-hop pattern queries

</details>

<details>
<summary><b>Phase 3: High-Volume Synthetic Data Engine (Anti-Mocking Strategy)</b></summary>

- [ ] Create standalone Python generator using `Faker` and `mimesis`
- [ ] Implement synthetic entity generation (5,000+ companies with BIN/IIN numbers)
- [ ] Seed Neo4j graph with complex ownership trees and hidden UBO connections
- [ ] Seed ClickHouse with 1,000,000+ historical transactions
- [ ] Inject pre-seeded financial crime patterns:
  - [ ] *Circular money flows (Ring schemes)*
  - [ ] *Pass-through shell company transactions*
  - [ ] *Smurfing / Structuring split payments*
- [ ] Build background worker publishing live stream transactions to **NATS** (50 events/sec)

</details>

<details>
<summary><b>Phase 4: Backend Core Development (Python 3.12 / Litestar)</b></summary>

- [ ] Configure **Dishka** Dependency Injection container (`APP` & `REQUEST` scopes)
- [ ] Implement Domain-Driven Design (DDD) layers:
  - [ ] `domain/` (Entities, value objects, repository interfaces)
  - [ ] `infrastructure/` (ClickHouse, Neo4j, Postgres, NATS adapters)
  - [ ] `application/` (Use cases: pattern detection, scoring algorithms)
  - [ ] `presentation/` (Litestar REST API controllers)
- [ ] Build key backend modules:
  - [ ] `GET /api/v1/analytics/summary` (ClickHouse OLAP aggregated metrics)
  - [ ] `GET /api/v1/graph/trace/{bin}` (Neo4j Cypher multi-hop graph execution)
  - [ ] `GET /api/v1/stream/incidents` (SSE stream for live NATS transactions)
- [ ] Integrate `pydantic-ai` with LLM endpoint for auto-generating case reports
- [ ] Add unit and integration tests using `pytest-asyncio`

</details>

<details>
<summary><b>Phase 5: Frontend Core Development (React 19 / FSD Architecture)</b></summary>

- [ ] Setup Feature-Sliced Design folder structure (`app`, `pages`, `widgets`, `features`, `entities`, `shared`)
- [ ] Generate type-safe API client using `@hey-api/openapi-ts` from backend OpenAPI spec
- [ ] Setup global state management (`Zustand`) and server cache (`TanStack Query`)
- [ ] **Module 1: Interactive Graph Canvas (`@xyflow/react`)**
  - [ ] Create custom company & individual graph nodes
  - [ ] Implement custom animated edges for transaction volume representation
  - [ ] Add interactive node controls (expand sub-graphs, highlight high-risk paths)
- [ ] **Module 2: High-Performance OLAP Dashboard**
  - [ ] Build analytical charts using `ECharts` (volume spikes, risk distributions)
  - [ ] Build high-density transaction tables using `TanStack Table`
- [ ] **Module 3: Real-Time Incident Monitor**
  - [ ] Connect SSE/WebSocket consumer to live transaction stream
  - [ ] Add push notifications for high-risk alerts

</details>

<details>
<summary><b>Phase 6: CI/CD, DevOps & Final Portfolio Presentation</b></summary>

- [ ] Setup `.github/workflows/ci.yml` (automated `ruff`, `pytest`, `biome`, and build checks)
- [ ] Write production-ready multi-stage `Dockerfile` for frontend and backend
- [ ] Create Ansible playbooks / Terraform scripts for single-command VPS deployment
- [ ] **Documentation & Polish:**
  - [ ] Write detailed repository `README.md` with system architecture diagrams
  - [ ] Add ClickHouse query benchmarks (e.g., *"SQL query execution over 1M records in 12ms"*)
  - [ ] Record demo GIF / video showcasing real-time graph rendering and stream alerting

</details>

---

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
