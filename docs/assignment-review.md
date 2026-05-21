# Assignment Review Interview

You paste or share a project you've built. The interviewer explores your codebase and conducts a seniority-calibrated technical interview on it, then scores you 0–100.

---

## How to start

Invoke the `intervy` skill and choose **option 1**.

---

## Flow

### Step 1 — Load the project

You'll be asked to share your code in one of two ways:

- **Paste the code** directly into the chat (works for small or single-file projects)
- **Provide a `git clone` URL** — the interviewer will clone and explore the repository

### Step 2 — Codebase exploration

Before asking any questions, the interviewer silently explores:

- Project structure and overall purpose
- Tech stack (language, frameworks, libraries)
- Architectural patterns (REST, event-driven, microservices, etc.)
- Domain concepts, DB/ORM setup, auth approach
- Test setup, config management, any README or docs

This happens before you're asked anything. The questions that follow are grounded in your actual code, not generic textbook scenarios.

### Step 3 — Seniority calibration

You're asked which seniority level you're targeting:

| Level | What's expected |
| --- | --- |
| **Junior** | Basic mechanics, syntax, simple design choices |
| **Mid** | Architecture rationale, error handling, testing approach |
| **Senior** | Failure modes, distributed systems, security depth, scalability flaws |
| **Staff / Principal** | System design at scale, cross-cutting concerns, architectural alternatives |

All subsequent questions, depth of probing, and scoring expectations are calibrated to your answer.

### Step 4 — Interview (8–12 questions)

Questions alternate between simpler and harder — you'll never get two hard ones in a row. Each question is grounded in a real file, real function name, or real decision visible in your code.

Topics covered (adapted to what your codebase contains):

1. **Architecture** — why a core design choice was made
2. **Specific mechanism** — how a particular piece of code works in detail
3. **Security** — how auth or validation works and what it provides vs alternatives
4. **Failure modes** — what breaks at each layer, what's recoverable
5. **Testing** — how tests isolate real infrastructure, why the approach is clean
6. **Scalability flaw** — a real limitation that would break under load
7. **Idempotency / correctness** — retries, duplicate writes, at-least-once guarantees
8. **Production readiness** — open-ended: top 3 things to change for real traffic

**Follow-up drill:** If an answer is vague or uses buzzwords without explanation, expect 1–3 sharp follow-up questions before moving on. Surface-level answers are not accepted.

### Step 5 — Final assessment

After the last question you receive a structured report:

**Area scores table**

| Area | Rating |
| --- | --- |
| Architecture Fundamentals | Strong / Good / Developing / Weak |
| Security | Strong / Good / Developing / Weak |
| Code Detail | Strong / Good / Developing / Weak |
| Failure Mode Analysis | Strong / Good / Developing / Weak |
| Testing | Strong / Good / Developing / Weak |
| Production Thinking | Strong / Good / Developing / Weak |

**Scored breakdown (0–100)**

| Component | Weight |
| --- | --- |
| Architecture understanding | 20% |
| Security knowledge | 15% |
| Code-level depth | 20% |
| Failure mode instinct | 20% |
| Testing awareness | 10% |
| Production thinking | 15% |

**Verdict** — one of: Junior / Junior-Mid / Mid / Mid-Senior / Senior / Strong Senior / Staff, with a note on whether it matches the level you declared.

**What played well** and **Where to sharpen** — specific, grounded in your actual answers.

---

## Tips

- The interviewer will not penalise you for reading the code to answer — but will penalise you if you still can't reason about what you read.
- Explain *why*, not just *what*. The interviewer asks for reasoning, not recall.
- Shorter interviewer turns mean you should be talking more than they are.
