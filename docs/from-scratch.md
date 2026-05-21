# From-Scratch Interview

You are given a project domain (generated fresh each session) and must build a production-grade API from zero. The interviewer reviews your code between rounds and scores you 0–100.

---

## How to start

Invoke the `intervy` skill and choose **option 2**.

---

## Flow

### Step 1 — Language selection

Choose your language and framework:

- **Python** (FastAPI / Flask)
- **Java Spring Boot**

The session is fully tailored to your choice.

### Step 2 — Project scenario

The `intervy-problem` skill generates a unique project story for this session: a product name, a domain, a brief, and a specific feature set to build. Every session produces a different scenario — the same product will never appear twice in a row.

The story determines:
- All endpoint names and paths (no generic `/items`)
- Model names and field names
- The feature theme for each coding round

### Step 3 — Briefing

Before any coding begins, the interviewer explains the structure, rules, and scoring. You type **"start"** to begin.

---

## Interview Structure

### Phase 0 — Project Bootstrap

**Normal mode (build from scratch)**

Build a minimal but launchable API. Requirements:
- Clean project structure with separate modules (routes, models, config, tests)
- A working HTTP server
- A `GET /health` endpoint returning `{"status": "ok"}`
- A domain-specific stub endpoint (e.g. `GET /bookings` returning an empty list)
- A test file covering at least the health endpoint
- The app must start with a single command

**Restructure mode** *(assigned randomly)*

A working single-file prototype is handed to you. Your task:
- Split it into a proper layered structure
- Keep the app runnable after restructuring
- Find and fix a bug or code smell
- Add one extension (query filter, validation constraint, or new endpoint)
- Write at least one test for the extension

**Review:** The interviewer checks structure, correctness, testability, and naming conventions. Every failure is called out with the file and line.

---

### Round 1 — Easy

**Theory question** — a fresh Python fundamentals question every session. Examples of topics:
- `__str__` vs `__repr__`
- The GIL and async workloads
- Context managers
- Generator vs list
- MRO and multiple inheritance

Scored 0–10. Shallow answers trigger 1–2 follow-up probes before scoring.

**Coding challenge** — Add a `POST` endpoint for the domain resource:
- Accepts a JSON body (name + at least one numeric field)
- Returns the created record with an auto-generated `id`
- At least one test (bonus: invalid input case)

Review checklist: Pydantic model, response model, HTTP 201, no business logic in route, no mutable global state.

---

### Round 1.a — Database Migrations (theory only)

A deep-dive question on Alembic and migration safety. Examples of topics:
- Risks of `Base.metadata.create_all()` in production
- How Alembic's version chain works
- Safe multi-step `NOT NULL` migration on a large table
- Handling multi-head migration conflicts
- Running migrations on startup in a multi-replica deployment

Scored 0–10. Probe topics include the safe `add nullable → backfill → add constraint` pattern.

---

### Round 1.b — Configuration and Secrets (theory only)

A deep-dive question on externalized config and secrets management. Examples of topics:
- Pydantic `BaseSettings` mechanics and precedence order
- `os.getenv` vs `BaseSettings`
- `@lru_cache` on `get_settings()` and its testing implications
- 12-factor app config principle
- Nested config with `env_nested_delimiter`

Scored 0–10.

---

### Round 2 — Medium

**Theory question** — a harder systems/patterns question. Examples of topics:
- ACID properties and distributed guarantees
- N+1 query problem and `selectinload` / `joinedload`
- Repository Pattern trade-offs
- Dependency injection in FastAPI
- Optimistic vs pessimistic locking

Scored 0–10. Probing is more aggressive than Round 1.

**Coding challenge** — Integrate a real database:
- Add SQLAlchemy ORM (async for FastAPI)
- Create a domain entity model: `id`, `name`, numeric field, `created_at` (server-side)
- Update `POST` to persist to DB
- Add `GET /resource` (all records) and `GET /resource/{id}` (404 if not found)
- Integration test hitting a real (test) DB — no mocks

Review checklist: session lifecycle, 404 via `HTTPException`, `created_at` not client-controlled, no raw SQL mixed with ORM, async correctness.

---

### Round 3 — Difficult

**Theory question** — distributed systems depth. Examples of topics:
- CAP theorem and partition tolerance
- Idempotency patterns for `POST`
- Saga pattern: choreography vs orchestration
- Backpressure in async Python services
- Rate limiting: token bucket vs leaky bucket

Scored 0–10.

**Coding challenge** — Production hardening:
- Pagination on list endpoint (`?page=1&page_size=20`, capped at 100)
- Soft delete: `DELETE /{id}` sets `deleted_at`, all reads exclude soft-deleted records
- Background task: log on record creation asynchronously (non-blocking)
- Feature test: create → soft-delete → verify gone from list, all against a real test DB
- Input sanitisation: reject empty/whitespace names with 422

Review checklist: `LIMIT`/`OFFSET` at DB level, `deleted_at` filter in ALL read queries, background task non-blocking, Pydantic validator for whitespace, no f-string SQL.

---

### Round 5 — Expert (optional)

Offered after Round 3. Declining is valid — it does not lower your score.

**Theory question** — advanced library and resilience topics. Examples of topics:
- `testcontainers-python` vs SQLite in-memory for integration tests
- `tenacity` retry logic and the idempotency risk on `POST`
- `fastapi-cache2` / `aiocache` and cache stampede
- Circuit breaker pattern: `pybreaker` vs custom implementation
- Session-scoped vs function-scoped containers in pytest

Scored 0–10.

**Coding challenge** — one of three assigned randomly (not your choice):
- **Option A:** Replace SQLite tests with `testcontainers-python` using a real PostgreSQL container (session-scoped fixture, 3 test cases)
- **Option B:** Add response caching with `fastapi-cache2`, TTL 60 s, cache invalidation on write, spy test asserting DB is not called on cache hit
- **Option C:** Add retry logic around an external call using `tenacity` (exponential backoff, 3 attempts, graceful fallback — no raw 500)

---

## Between-Round Probes

After each coding round (and after each theory sub-round), `intervy-questioner` fires 1–2 short probes:

1. A code-specific question about the last snippet (skipped after theory-only rounds)
2. A language/ecosystem deep-dive question targeting a gap or pattern seen in your code

These probe scores are averaged into a single **Between-Round Probes** component (10 points).

---

## Scoring

Say **"score me"** at any point to stop and get your results. You do not need to complete all rounds — scores are normalised over completed rounds only.

| Component | Max |
|---|---|
| Project Bootstrap | 10 |
| Round 1 Theory | 10 |
| Round 1 Code | 10 |
| Round 1.a — DB Migrations | 10 |
| Round 1.b — Config & Secrets | 10 |
| Round 2 Theory | 10 |
| Round 2 Code | 10 |
| Round 3 Theory | 10 |
| Round 3 Code | 10 |
| Between-Round Probes (avg) | 10 |
| Round 5 Theory *(optional)* | 10 |
| Round 5 Code *(optional)* | 10 |

Each component is 10 points. The final score is the average across all completed components (including optional ones if attempted).

**Verdict** — one of: Junior / Junior-Mid / Mid / Mid-Senior / Senior / Strong Senior / Staff. Comes with a note on which specific rounds you excelled or struggled in.

---

## Tips

- Name everything after the story domain — generic `Item` / `items` naming is penalised.
- The interviewer will NOT implement anything. They only review, question, and probe.
- Probes fire before you advance — a strong probe answer can lift a borderline round score.
- Say "score me" whenever you want to stop; partial sessions are scored fairly.
