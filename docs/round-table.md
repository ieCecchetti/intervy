# Round-Table Interview — How It Works

A simulation of a full senior/tech-lead panel interview. Seven people at the table, each with their own personality, their own domain, and their own opinion of you.

---

## The Panel

| Seat | Evaluates | Weight |
| --- | --- | --- |
| **Handler** | Introduces the position, hosts the session | — |
| **HR** | Communication, soft skills, personality fit, conflict handling | 5 pts |
| **Manager** | Delivery methodology, requirements→deploy flow, KPIs, team org | 10 pts |
| **Tech Lead** | Technical depth — design, internals, security, async, clean code | 40 pts |
| **Architect** | System design at scale, reliability, failure modes, circuit breakers | 20 pts |
| **Dev** | Open reasoning challenge — no right answer, evaluates your thinking | 10 pts |
| **CTO** | Strategy, process maturity, security across environments | 15 pts |

**Total: 100 points.**

---

## Personalities

Every panelist is randomly assigned a personality at session start. The same personality can appear multiple times — just like real life.

| Personality | What it feels like |
| --- | --- |
| Curious / Exploratory | Genuinely wants to understand your reasoning. Warm follow-ups. |
| Neutral / Analytical | No warmth, no harshness. Just accuracy. Hard to read. |
| Challenging / Adversarial | Not satisfied. Pushes back on everything, even solid answers. |
| Coaching / Guiding | Rooting for you. Gives hints if you stumble. Lenient scoring. |
| Bored / Disengaged | Barely engaged. Short patience. Very harsh scoring. |
| Friendly / Relaxed | Conversational, low pressure. Don't confuse it for easy. |
| Frustrated / Stressed | Impatient. Penalises rambling. Cuts you off if you drift. |

Personalities are revealed one at a time as each panelist steps in — a short narrator line sets the scene before they ask their first question.

---

## Dynamic Shifts

If your answers consistently fall short, a panelist may shift mid-segment toward **Bored** or **Adversarial**. No warning — just a narrator line:

> *He sets his pen down. He's stopped taking notes.*

The shift increases scoring harshness for the rest of their segment. A panelist already Adversarial or Bored doesn't shift further.

---

## Questions

Questions are generated fresh every session — never from a fixed list. They are anchored in the company context generated at the start, calibrated to your declared role and level, and reflect current industry relevance.

The **Tech Lead** covers 4–5 topic areas (not all of them), selected based on:
- What the company context makes relevant (e.g. Kafka if the company streams events)
- Your declared stack (Spring Boot vs Python internals)
- Their personality (Adversarial goes deep on one weakness; Bored skips ahead)

Areas include: web fundamentals, async/concurrency, framework internals, system design, API design, security, event streaming, clean code — and anything else the context calls for.

---

## Follow-ups

Each panelist decides whether to follow up after your answer based on three factors:

1. **Answer clarity** — vague or buzzword-heavy → follow-up. Precise and specific → likely move on.
2. **Personality** — Adversarial pushes even on good answers. Bored skips unless the answer is alarming. Coaching follows up to draw you out.
3. **Random factor** — a small random element means you can't game the system. A solid answer occasionally gets pushed; a weak one occasionally gets a pass.

---

## Company Context

Before the panel starts, a fresh company scenario is generated: name, domain, stage, team size, stack, and what's urgent right now. Every panelist uses this context to anchor their questions — the Tech Lead's system design question uses your company's actual domain, the Manager's milestone question reflects your team's size.

---

## Final Scoring

After the CTO's closing question, `intervy-score` produces a **Panel Verdict**:

- **Score** out of 100 with weighted panelist contributions
- **Seniority level**: Junior → Junior-Mid → Mid → Mid-Senior → Senior → Strong Senior
- **What the panel said** — each panelist's 1–2 sentence opinion, in their own voice and personality
- **Strengths** — grounded in specific moments from your session
- **Where to focus** — concrete gaps with actionable next steps
- **Overall** — one honest paragraph

---

## How to Start

```
> interview
```

Select **"Round-table interview"** from the menu. You'll be asked for your target role/level and tech stack, then briefed on the company before the panel begins.
