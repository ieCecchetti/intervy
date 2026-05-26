# intervy-technical — Design Spec

_Date: 2026-05-26_

---

## Overview

A round-table technical interview simulator with 7 panelists, each independently
personality-assigned, that together evaluate the candidate across behavioral,
technical, architectural, and strategic dimensions. Based on a real senior/tech-lead
interview experience. Final output is a merged panel verdict with per-panelist opinions.

---

## 1. Entry Point

`intervy/SKILL.md` gains a 4th option in its mode menu:

- Label: `"Round-table interview"`
- Description: `"Face a full panel of 7 interviewers — HR, manager, tech lead, architect, and more. Seniority-calibrated, personality-driven, scored by every seat at the table."`

Selecting it delegates to `intervy-technical/SKILL.md`.

---

## 2. File Structure

```
~/.claude/skills/intervy-scenario/          ← renamed from intervy-problem
├── SKILL.md                                ← updated: invokes context.md first
├── context.md                              ← NEW: shared company context generator
└── scaffold.md                             ← unchanged logic, reads context from conversation

~/.claude/skills/intervy-technical/         ← NEW
├── SKILL.md                                ← setup, personality roll, orchestration, final scoring
├── handler.md
├── hr.md
├── manager.md
├── tech-lead.md
├── architect.md
├── dev.md
└── cto.md

~/.claude/skills/intervy/
└── SKILL.md                                ← add option 4 → intervy-technical
```

`from-scratch.md` updated to invoke `intervy-scenario` instead of `intervy-problem`.

---

## 3. Session Setup (`intervy-technical/SKILL.md`)

**Step 1 — Gather inputs**

Ask the candidate (one question at a time):
1. What role/level they are applying for (e.g. Junior Dev, Senior Dev, Tech Lead, Staff Engineer)
2. What tech stack (Java Spring Boot / Python / other)

**Step 2 — Generate company context**

Read `~/.claude/skills/intervy-scenario/context.md` to generate a fresh company scenario.
The context block is stored in the conversation and visible to all panelists throughout.

**Step 3 — Roll personalities**

Randomly assign one personality to each of the 7 panelists independently.
Repetitions are allowed — the same personality can appear multiple times.
Store the full assignment in the conversation context (not shown to the candidate).

```
Handler     → roll
HR          → roll
Manager     → roll
Tech Lead   → roll
Architect   → roll
Dev         → roll
CTO         → roll
```

**Step 4 — Scene setter**

Print a short cinematic intro — sets the room, the stakes, the format. 3–5 sentences max.
Example tone: _"The conference room is on the 9th floor. Seven people are already seated
when you walk in. You count the chairs. There is one left."_ Then hand off to `handler.md`.

---

## 4. Personalities

Seven personalities. Each panelist independently rolls one at session start.
The personality is revealed to the candidate via a narrator line when that panelist
first speaks — not before. The candidate learns each person's mood as it unfolds.

| Personality | Narrator line | Scoring stance | Follow-up style |
|---|---|---|---|
| **Curious / Exploratory** | _She tilts her head slightly, pen already moving — you can tell she genuinely wants to understand how your mind works._ | Baseline | Probes deeper, warm |
| **Neutral / Analytical** | _He opens a notebook, uncaps a pen, and looks at you with no expression whatsoever. You won't be able to read this one._ | Baseline | Precise, no warmth |
| **Challenging / Adversarial** | _He leans forward, elbows on the table. The moment you finish a sentence he's already shaking his head slightly — not satisfied yet._ | Harsher | Pushes back hard, demands precision |
| **Coaching / Guiding** | _She smiles before you even speak. She's clearly rooting for you — when you stumble she'll give you a small nudge before moving on._ | Lenient | Offers gentle hints if stuck |
| **Bored / Disengaged** | _He glances at his phone as you sit down, then puts it away without urgency. He's been in this room all day and it shows._ | Very harsh | Minimal follow-up, short patience |
| **Friendly / Relaxed** | _She extends a hand and says your name like she already knows you. The room feels ten degrees warmer. Don't let your guard down._ | Lenient | Conversational, no pressure |
| **Frustrated / Stressed** | _There are three sticky notes on the table in front of him and a half-empty coffee. He checks the time before asking his first question._ | Harsh | Impatient, penalises rambling |

Personality effects are baked into how strict the panelist is when scoring — not applied
as a post-hoc multiplier.

---

## 5. Dynamic Personality Shift

If a candidate's answers consistently fall below quality threshold (~4/10) during a
panelist's segment, that panelist may shift their personality mid-session toward
**Bored/Disengaged** or **Challenging/Adversarial**.

The shift is signalled by a short narrator line only — no explanation:
> _He sets his pen down. He's stopped taking notes._
> _She glances at the person next to her. Just for a second._

Rules:
- A panelist already assigned Bored or Adversarial does not shift (already there)
- The shift increases scoring harshness for the remainder of their segment
- Handler never shifts — they are the host
- Which panelists can shift and toward what:

| Panelist | Can shift to |
|---|---|
| HR | Bored |
| Manager | Bored or Adversarial |
| Tech Lead | Adversarial |
| Architect | Bored |
| Dev | Adversarial |
| CTO | Bored or Adversarial |

---

## 6. Panelist Flow

All 7 panelists appear in fixed order every session. Each panelist sub-file is read
in sequence. The sub-file:

1. Reads the personality assigned to this panelist from context
2. Outputs the narrator line (personality reveal)
3. Generates and asks questions (see generation contract below)
4. Records a score 0–10 for their domain
5. Records a 1–2 sentence opinion in their voice and personality
6. Hands back to `SKILL.md` to proceed to the next panelist

### Question Generation Contract (applies to all panelists)

> Invent questions fresh every session. The topic areas in each panelist file define
> what to probe. Any example questions illustrate depth and style only — never repeat
> them. Calibrate difficulty to the declared role/level. Anchor specifics to the
> company context in the conversation. Skip topic areas that are irrelevant to the
> company context or that the panelist's personality would naturally skip (a bored
> panelist covers fewer topics; an adversarial one goes deeper on one weakness
> instead of broad coverage). Questions must reflect current industry relevance —
> do not ask about patterns or tools that are no longer in common use.

### Follow-up Decision Contract (applies to all panelists)

After each candidate answer, the panelist decides whether to follow up using three
independent factors combined:

#### 1. Answer clarity (primary driver)

- Clear, precise, complete → follow-up unlikely unless personality demands it
- Vague, buzzword-heavy, or partial → follow-up likely
- "I don't know" / blank → no follow-up, score 0, move on immediately

#### 2. Personality modifier

- Adversarial / Frustrated: follow-up even on good answers — they want to find the edge
- Curious / Coaching: follow-up on interesting answers to go deeper, not to penalise
- Bored / Disengaged: skips follow-ups unless the answer was exceptionally poor
- Neutral / Analytical: follows up only when precision is genuinely missing
- Friendly / Relaxed: rarely follows up — moves the conversation forward

#### 3. Random factor

A small random element is always present. A solid answer may still get a follow-up.
A weak answer may occasionally get a pass. This reflects the unpredictability of real
interviewers and prevents the candidate from gaming the system by pattern-matching
to a formula. The random factor is never the dominant force — it only tips ambiguous
cases either way.

Follow-up depth also varies: adversarial/frustrated panelists follow up harder;
coaching/curious ones follow up to open, not to trap.

---

## 7. Panelist Details

### Handler (0 pts)
- Explains the position and format
- Asks the candidate to introduce themselves
- No scoring, no follow-ups
- Sets the room tone

### HR (5 pts)
- Domain: communication, personality fit, soft skills, conflict handling, team dynamics
- Example angles: how they handle disagreement, pressure, feedback, culture fit
- 1 soft follow-up max per question
- Can shift to: Bored

### Manager (10 pts)
- Domain: delivery methodology (agile/waterfall/hybrid), requirements → deploy flow,
  KPIs definition and measurement, team organisation, milestone planning
- Example angles: how a feature goes from discovery to production, how they define
  done, how they handle scope creep
- 1–2 follow-ups
- Can shift to: Bored or Adversarial

### Tech Lead (40 pts)
- Domain: technical depth — covers 4–5 topic areas per session, never all of them.
  Which areas are selected depends on: (1) company context (a fintech with Kafka →
  event streaming is in; a 3-person seed startup → skip complex infra), (2) the
  candidate's declared stack, and (3) the tech lead's personality (adversarial goes
  deep on 1–2 weak spots; bored skips areas the candidate handles confidently).
  Areas include but are not limited to:
  - Web fundamentals and rendering strategies
  - Async / concurrency models
  - Language and framework internals (calibrated to chosen stack)
  - System design at the whiteboard (with follow-ups on scale, data volume, edge cases)
  - API layer: design, gateway patterns, rate limiting approaches
  - Security: authentication flows, token structure and validation, encryption models
  - Event streaming and inter-service communication
  - Code quality and engineering practices
- 1 follow-up per question max
- Can shift to: Adversarial

### Architect (20 pts)
- Domain: system design at scale — reliability, availability, consistency trade-offs,
  handling traffic peaks, service decomposition, load balancing, regional scaling,
  failure modes, circuit breakers, what happens when a dependency goes down
- Asks 2–3 focused questions, goes deep rather than broad
- 1–2 follow-ups
- Can shift to: Bored

### Dev (10 pts)
- Domain: open reasoning — presents a real-world ambiguous scenario (e.g. one
  stakeholder wants a custom solution that diverges from the shared platform).
  There is no single right answer. Evaluates quality of reasoning, trade-off
  awareness, communication of uncertainty, and how the candidate reaches a position.
- 1 push follow-up to see if they hold or revise their reasoning under pressure
- Can shift to: Adversarial

### CTO (15 pts)
- Domain: strategy and process — engineering methodologies, how the candidate handles
  a requirement from customer to milestone to delivery, work splitting, team
  coordination, security posture across environments (dev/staging/prod)
- Invents additional questions based on company context (stage, compliance pressure,
  team size)
- 1–2 follow-ups
- Can shift to: Bored or Adversarial

---

## 8. Scoring

### Per-panelist

Each scoring panelist (all except Handler) awards 0–10 for their domain.
Personality affects strictness directly — it is not a post-hoc modifier.
Each panelist records a 1–2 sentence opinion in their own voice at the end of their
segment. These scores and opinions are stored in the conversation context.

### Weighted final score

| Panelist | Max pts |
|---|---|
| HR | 5 |
| Manager | 10 |
| Tech Lead | 40 |
| Architect | 20 |
| Dev | 10 |
| CTO | 15 |
| **Total** | **100** |

### Final scoring — delegated to `intervy-score`

After the CTO segment, `intervy-technical/SKILL.md` hands off to `intervy-score`.

`intervy-score/SKILL.md` is a **router**: it reads the conversation context to detect
which scoring mode to use, then delegates to the matching sub-file:

| Context detected | Sub-file invoked |
| --- | --- |
| Single-interviewer session (from-scratch, coding challenge, code review) | existing scoring logic (current behaviour) |
| Multi-panel session (round-table interview) | `multiple-panel-score.md` ← NEW |

`intervy-score/multiple-panel-score.md` owns the full panel verdict logic:

```
─────────────────────────────────────────
  PANEL VERDICT
─────────────────────────────────────────

Score: XX/100
Level: [Junior / Junior-Mid / Mid / Mid-Senior / Senior / Strong Senior]

─── What the panel said ─────────────────

[Handler personality] — [opinion]
[HR personality]      — [opinion]
[Manager personality] — [opinion]
[Tech Lead personality] — [opinion]
[Architect personality] — [opinion]
[Dev personality]     — [opinion]
[CTO personality]     — [opinion]

─── Strengths ───────────────────────────

2–3 bullets, grounded in specific answers from this session.

─── Where to focus ──────────────────────

2–3 bullets, specific gaps with direct actionable next steps.

─── Overall ─────────────────────────────

One short paragraph. Honest, warm, forward-looking. Names the level,
acknowledges what was demonstrated, points at the next milestone.
─────────────────────────────────────────
```

### Seniority mapping

| Score | Level |
|---|---|
| < 40 | Junior |
| 40–54 | Junior-Mid |
| 55–69 | Mid |
| 70–79 | Mid-Senior |
| 80–89 | Senior |
| 90–100 | Strong Senior |

---

## 9. `intervy-scenario/context.md` — Shared Context Generator

Generates a fresh company context every session. Called by:
- `intervy-scenario/SKILL.md` (before story/scaffold generation)
- `intervy-technical/SKILL.md` (as the interview anchor)

**Randomization contract:** Same as current `intervy-problem` — invent everything
fresh. Vary: domain, company name, stage, team size, stack, urgency framing.
Never repeat a domain or company name used recently.

**Output format:**

> **[COMPANY_NAME]** — [stage] startup in the [DOMAIN] space.
> [PRODUCT_NAME]: [one sentence on what it does and who uses it.]
> Team: [size]. Stack: [technologies].
> Current pressure: [1–2 sentences on what's urgent and why it matters now.]

This block stays in the conversation context and is read by every subsequent
panelist file.

---

## 10. Files to Create / Modify

| Action | File |
| --- | --- |
| CREATE | `intervy-technical/SKILL.md` |
| CREATE | `intervy-technical/handler.md` |
| CREATE | `intervy-technical/hr.md` |
| CREATE | `intervy-technical/manager.md` |
| CREATE | `intervy-technical/tech-lead.md` |
| CREATE | `intervy-technical/architect.md` |
| CREATE | `intervy-technical/dev.md` |
| CREATE | `intervy-technical/cto.md` |
| CREATE | `intervy-scenario/context.md` |
| CREATE | `intervy-score/multiple-panel-score.md` |
| RENAME | `intervy-problem/` → `intervy-scenario/` |
| MODIFY | `intervy-scenario/SKILL.md` — invoke context.md first |
| MODIFY | `intervy-scenario/scaffold.md` — read context from conversation |
| MODIFY | `intervy-score/SKILL.md` — add router logic (single vs multi-panel) |
| MODIFY | `intervy/SKILL.md` — add option 4 |
| MODIFY | `intervy/from-scratch.md` — invoke intervy-scenario |
