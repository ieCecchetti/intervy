# intervy-technical Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 7-panelist round-table interview simulator as a new intervy mode, with personality-driven scoring, dynamic follow-ups, and a shared company context generator.

**Architecture:** New `intervy-technical` skill orchestrates 7 panelist sub-files in sequence; personalities are rolled at session start and revealed progressively via narrator lines. A shared `intervy-scenario/context.md` (extracted from `intervy-problem`, now renamed `intervy-scenario`) generates the company scenario used by all panelists. Final scoring is routed through `intervy-score`, which detects multi-panel sessions and delegates to a new `multiple-panel-score.md`.

**Tech Stack:** Markdown skill files consumed by Claude Code; no compiled code, no test runner. Verification steps are manual read-through checks for cross-reference consistency and completeness.

---

## File Map

| Action | Path |
| --- | --- |
| RENAME dir | `~/.claude/skills/intervy-problem/` → `~/.claude/skills/intervy-scenario/` |
| CREATE | `~/.claude/skills/intervy-scenario/context.md` |
| MODIFY | `~/.claude/skills/intervy-scenario/SKILL.md` |
| CREATE | `~/.claude/skills/intervy-technical/SKILL.md` |
| CREATE | `~/.claude/skills/intervy-technical/handler.md` |
| CREATE | `~/.claude/skills/intervy-technical/hr.md` |
| CREATE | `~/.claude/skills/intervy-technical/manager.md` |
| CREATE | `~/.claude/skills/intervy-technical/tech-lead.md` |
| CREATE | `~/.claude/skills/intervy-technical/architect.md` |
| CREATE | `~/.claude/skills/intervy-technical/dev.md` |
| CREATE | `~/.claude/skills/intervy-technical/cto.md` |
| CREATE | `~/.claude/skills/intervy-score/multiple-panel-score.md` |
| MODIFY | `~/.claude/skills/intervy-score/SKILL.md` |
| MODIFY | `~/.claude/skills/intervy/SKILL.md` |
| MODIFY | `~/.claude/skills/intervy/from-scratch.md` |

---

## Task 1: Rename intervy-problem → intervy-scenario + create context.md

**Files:**
- Rename: `~/.claude/skills/intervy-problem/` → `~/.claude/skills/intervy-scenario/`
- Create: `~/.claude/skills/intervy-scenario/context.md`

- [ ] **Step 1: Rename the skill folder**

```bash
mv ~/.claude/skills/intervy-problem ~/.claude/skills/intervy-scenario
```

Expected: no output, no error.

- [ ] **Step 2: Verify rename succeeded**

```bash
ls ~/.claude/skills/intervy-scenario/
```

Expected: `SKILL.md  scaffold.md`

- [ ] **Step 3: Create context.md**

Write `~/.claude/skills/intervy-scenario/context.md` with this exact content:

```markdown
# context — Company Context Generator

Private sub-file for `intervy-scenario` and `intervy-technical`. Not a standalone skill.
Read this file to generate a fresh company context for any interview session.

---

## Randomization Contract

This is called every session. Every output must feel completely different.

- INVENT everything fresh: company name, domain, product, team size, stack, pressure
- Vary company stage: pre-seed, seed, Series A, Series B, scale-up, enterprise spin-off
- Vary team size: 3–5 engineers to 200+
- Vary urgency: investor demo, compliance deadline, competitor threat, key client churning, post-acquisition integration
- Never repeat a company name or domain used recently in this conversation
- Prefer inventing a domain not in the pool below — the pool is inspiration only

---

## Domain Pool (inspiration only — prefer inventing something not on this list)

- Fintech / treasury management
- Logistics / last-mile delivery
- Healthcare appointment and triage
- Real estate marketplace
- E-commerce returns and refunds
- Event ticketing and reservations
- B2B wholesale order management
- Legal document tracking
- Fleet maintenance scheduling
- Agricultural supply chain
- Electric vehicle charging networks
- Clinical trial data collection
- Digital media asset licensing
- Coworking space management
- Pharmacy prescription fulfilment

---

## Output Format

Generate the context block and output it in this format. Fill every field — never leave a placeholder.

> **[COMPANY_NAME]** — [stage] company in the [DOMAIN] space.
> **Product:** [PRODUCT_NAME] — [one sentence: what it does and who uses it].
> **Team:** [size and structure, e.g. "12 engineers across 2 squads"].
> **Stack:** [key technologies — language, frameworks, databases, infra].
> **Pressure:** [1–2 sentences on what is urgent right now and why it matters].

---

## Rules

- Keep the block to 5–7 lines total
- Make the pressure feel real — a business deadline, a technical crisis, a competitive threat
- When called from `intervy-technical`: the stack must include the candidate's declared language/framework
- After outputting the context block, stop — the calling skill takes over
```

- [ ] **Step 4: Verify context.md**

Read through `~/.claude/skills/intervy-scenario/context.md` and confirm:
- No `[PLACEHOLDER]` text remains
- Output format section has all 5 fields (company, product, team, stack, pressure)
- Rules section mentions both `intervy-scenario` and `intervy-technical` as callers

- [ ] **Step 5: Commit**

```bash
cd ~/.claude && git add skills/intervy-scenario/ && git commit -m "feat: rename intervy-problem to intervy-scenario and add shared context.md"
```

---

## Task 2: Update intervy-scenario/SKILL.md to invoke context.md first

**Files:**
- Modify: `~/.claude/skills/intervy-scenario/SKILL.md`

- [ ] **Step 1: Read current SKILL.md**

Read `~/.claude/skills/intervy-scenario/SKILL.md` and locate:
- The frontmatter `name:` field (currently `intervy-problem` — must be updated)
- The section where the story is generated inline (this will be replaced with a call to `context.md`)

- [ ] **Step 2: Update SKILL.md**

Replace the frontmatter name and the story generation section. The updated file must:

1. Change `name: intervy-problem` → `name: intervy-scenario` in frontmatter
2. Change `description:` to: `Use when generating a language-aware company scenario for a live coding interview simulation. Invoked by intervy-project before delegating to an interview skill.`
3. Before any story output, add a step that reads `context.md`:

Insert this as the first generation step (before Mode A/B logic):

```markdown
## Step 1 — Generate Company Context

Say: *Generating your interview scenario...*

Read `context.md` (the private sub-file in this skill's folder) and generate the
company context block. Present it to the candidate as part of the scenario briefing.
The context block stays in the conversation and is used by all subsequent steps.
```

4. In Mode A: the story wraps the context block into the existing story template format — the context is already generated, so the story template uses it rather than inventing the company from scratch.

5. In Mode B: `scaffold.md` reads the context block already in the conversation. No change to scaffold.md needed.

- [ ] **Step 3: Verify SKILL.md**

Read through the updated file and confirm:
- `name:` field is `intervy-scenario`
- Step 1 reads `context.md` before any story output
- Mode A and Mode B still work (context is already in conversation when they run)
- No reference to `intervy-problem` remains

- [ ] **Step 4: Commit**

```bash
cd ~/.claude && git add skills/intervy-scenario/SKILL.md && git commit -m "feat: update intervy-scenario to invoke context.md for story generation"
```

---

## Task 3: Update intervy/SKILL.md and intervy/from-scratch.md

**Files:**
- Modify: `~/.claude/skills/intervy/SKILL.md`
- Modify: `~/.claude/skills/intervy/from-scratch.md`

- [ ] **Step 1: Add option 4 to intervy/SKILL.md**

Read `~/.claude/skills/intervy/SKILL.md` and add a 4th option to the `AskUserQuestion` menu:

```markdown
4. Label: `"Round-table interview"` — Description: `"Face a full panel of 7 interviewers — HR, manager, tech lead, architect, and more. Seniority-calibrated, personality-driven, scored by every seat at the table."`
```

Add the routing row to the table:

```markdown
| 4 — Round-table interview | `intervy-technical/SKILL.md` |
```

- [ ] **Step 2: Update from-scratch.md**

Read `~/.claude/skills/intervy/from-scratch.md` and find the line:

```
Then invoke the skill **`intervy-problem`**
```

Replace with:

```
Then invoke the skill **`intervy-scenario`**
```

- [ ] **Step 3: Verify both files**

Read both files and confirm:
- `intervy/SKILL.md` has 4 options, 4 rows in the routing table, no mention of `intervy-problem`
- `from-scratch.md` references `intervy-scenario`, not `intervy-problem`

- [ ] **Step 4: Commit**

```bash
cd ~/.claude && git add skills/intervy/SKILL.md skills/intervy/from-scratch.md && git commit -m "feat: add round-table interview option and update intervy-scenario references"
```

---

## Task 4: Create intervy-technical/SKILL.md

**Files:**
- Create: `~/.claude/skills/intervy-technical/SKILL.md`

- [ ] **Step 1: Create the directory**

```bash
mkdir -p ~/.claude/skills/intervy-technical
```

- [ ] **Step 2: Write SKILL.md**

Write `~/.claude/skills/intervy-technical/SKILL.md` with this exact content:

```markdown
---
name: intervy-technical
description: Use when the user wants to practice a round-table technical interview with a full panel of 7 interviewers. Triggered from intervy mode 4. Do not invoke directly.
---

# intervy-technical — Round-Table Interview Simulator

You are orchestrating a full panel interview simulation.
Do NOT run panelist logic yourself — always read the matching sub-file.

---

## Step 1 — Gather Inputs

Ask the candidate one question at a time. Wait for each answer before asking the next.

1. "What role and level are you interviewing for? (e.g. Junior Developer, Senior Engineer, Tech Lead, Staff Engineer)"
2. "Which tech stack? Currently supported: Java Spring Boot / Python (FastAPI or Flask) / Other (describe briefly)"

---

## Step 2 — Generate Company Context

Say: *Preparing your interview scenario...*

Read `~/.claude/skills/intervy-scenario/context.md` and generate the company context block.
Use the candidate's declared tech stack to shape the company's technology choices.

Output the context block to the candidate — this is their briefing before entering the room.

---

## Step 3 — Roll Personalities

Randomly assign one personality to each panelist. Repetitions are allowed — the same
personality can appear more than once. Each roll is fully independent.

Personalities available: Curious/Exploratory, Neutral/Analytical, Challenging/Adversarial,
Coaching/Guiding, Bored/Disengaged, Friendly/Relaxed, Frustrated/Stressed.

Store the full assignment in the conversation in this exact format.
Do NOT show this block to the candidate:

```
[PANEL SETUP — internal]
Handler     → [personality]
HR          → [personality]
Manager     → [personality]
Tech Lead   → [personality]
Architect   → [personality]
Dev         → [personality]
CTO         → [personality]
```

---

## Step 4 — Scene Setter

Output a short cinematic intro — 3–5 sentences. Set the room, the stakes, the format.
Do not reveal personalities. Vary the tone and details each session. Example (do not reuse):

> *The conference room is on the 9th floor. Seven people are already seated when you
> walk in. You count the chairs. There is one left. Someone slides a glass of water
> toward you without making eye contact.*

Then say: **"Ready when you are."** and wait for the candidate to signal they're ready.

---

## Step 5 — Run the Panel

Read each panelist sub-file in sequence and follow its instructions exactly.
Do not proceed to the next panelist until the current one hands back control.

1. Read `handler.md`
2. Read `hr.md`
3. Read `manager.md`
4. Read `tech-lead.md`
5. Read `architect.md`
6. Read `dev.md`
7. Read `cto.md`

---

## Step 6 — Final Scoring

After `cto.md` completes, output:

> *The panel thanks you. You're asked to wait outside.*

Then invoke the skill **`intervy-score`**.
It will detect the multi-panel context automatically via the `[PANEL SETUP — internal]`
block and delegate to `multiple-panel-score.md`.

---

## Rules

- Never reveal personality assignments before each panelist's narrator line appears
- Never skip a panelist
- Never run panelist logic yourself — always read the sub-file
- If the candidate requests scoring mid-interview, invoke `intervy-score` immediately
```

- [ ] **Step 3: Verify SKILL.md**

Read through and confirm:
- All 6 steps are present
- `[PANEL SETUP — internal]` format is defined exactly as written (scoring router depends on it)
- Step 5 lists all 7 sub-files in correct order
- Step 6 invokes `intervy-score` (not `multiple-panel-score` directly)

- [ ] **Step 4: Commit**

```bash
cd ~/.claude && git add skills/intervy-technical/SKILL.md && git commit -m "feat: add intervy-technical orchestrator SKILL.md"
```

---

## Task 5: Create handler.md and hr.md

**Files:**
- Create: `~/.claude/skills/intervy-technical/handler.md`
- Create: `~/.claude/skills/intervy-technical/hr.md`

- [ ] **Step 1: Write handler.md**

```markdown
# handler — Panel Introduction

Private sub-file for `intervy-technical`. Not a standalone skill.
Read this file when the Handler panelist's turn begins.

---

## Personality

Read the Handler's assigned personality from the `[PANEL SETUP — internal]` block in context.

Output the narrator line matching their personality:

| Personality | Narrator line |
| --- | --- |
| Curious / Exploratory | *She tilts her head slightly, pen already moving — you can tell she genuinely wants to understand how your mind works.* |
| Neutral / Analytical | *He opens a notebook, uncaps a pen, and looks at you with no expression whatsoever. You won't be able to read this one.* |
| Challenging / Adversarial | *He leans forward, elbows on the table. The moment you finish a sentence he's already shaking his head slightly — not satisfied yet.* |
| Coaching / Guiding | *She smiles before you even speak. She's clearly rooting for you — when you stumble she'll give you a small nudge before moving on.* |
| Bored / Disengaged | *He glances at his phone as you sit down, then puts it away without urgency. He's been in this room all day and it shows.* |
| Friendly / Relaxed | *She extends a hand and says your name like she already knows you. The room feels ten degrees warmer. Don't let your guard down.* |
| Frustrated / Stressed | *There are three sticky notes on the table in front of him and a half-empty coffee. He checks the time before asking his first question.* |

---

## Script

The Handler speaks first. Their role is fixed — explain the position and ask the
candidate to introduce themselves. Vary the phrasing each session.

1. Briefly describe the role and the format of the interview (who is in the room, rough time).
   Base this on the company context already in the conversation. 2–3 sentences.

2. Ask the candidate to introduce themselves:
   > "Let's start with you — tell us a bit about yourself, your background, and what brought you here today."

Wait for the candidate's answer. Do not follow up. The Handler listens.

---

## Scoring

The Handler does not score. No opinion is recorded.

Hand back to `SKILL.md` after the candidate's self-introduction.
```

- [ ] **Step 2: Write hr.md**

```markdown
# hr — Human Resources Interviewer

Private sub-file for `intervy-technical`. Not a standalone skill.
Read this file when the HR panelist's turn begins.

---

## Personality

Read the HR panelist's assigned personality from the `[PANEL SETUP — internal]` block.
Output the narrator line matching their personality (see personality table in `handler.md`).

---

## Role

The HR interviewer evaluates: communication clarity, personality fit, soft skills,
conflict handling, team dynamics, and cultural alignment. They never ask technical questions.
They are observing even when they are not speaking.

---

## Question Generation

Invent 2–3 questions fresh for this session. Base them on the company context
(stage, team size, business pressure) and the candidate's declared role.

Topic areas to draw from — pick the most relevant, skip what doesn't fit the context:
- How they handle disagreement with a technical decision they believe is wrong
- How they give or receive difficult feedback
- A situation where they worked under significant pressure or ambiguity
- What they look for in a team or engineering culture
- How they onboard into a new codebase or team
- Career motivation: why this role, why now

Pick 2–3 areas that feel natural together. Questions must reflect current workplace
norms (remote/hybrid dynamics, async communication). Do not ask all topics.

---

## Follow-up Decision

After each answer, apply the follow-up decision contract:

**1. Answer clarity (primary)**
- Clear, specific, with a real example → follow-up unlikely
- Vague, generic, buzzword-heavy ("I'm a team player") → follow up for specifics
- "I don't know" / blank → score 0 for that question, move on immediately

**2. Personality modifier**
- Adversarial / Frustrated: may follow up even on a good answer to test consistency
- Bored / Disengaged: skips follow-up unless the answer was confusingly incomplete
- Coaching / Guiding: follows up to help the candidate elaborate if they seem nervous
- Friendly / Relaxed: rarely follows up — keeps the conversation moving
- Neutral / Analytical / Curious: follows up only when clarity is genuinely missing

**3. Random factor**
Occasionally follow up on a clean answer or skip a follow-up on a weak one.
The random factor tips ambiguous cases — it is never the dominant force.

Maximum 1 follow-up per question.

---

## Dynamic Shift

If the candidate's communication is consistently unclear, evasive, or very poor
across 2+ answers, the HR panelist shifts to **Bored/Disengaged**. Signal with a
narrator line — no explanation:

> *She puts her pen down. She's stopped writing.*

The shift increases scoring harshness for the rest of this segment.
A panelist already assigned Bored/Disengaged does not shift.

---

## Scoring

After all questions, internally record and store in context:

`[HR score: X/10 — "opinion in HR panelist's voice, coloured by their personality"]`

Do not reveal the score to the candidate.

Hand back to `SKILL.md`.
```

- [ ] **Step 3: Verify both files**

Read both files and confirm:
- `handler.md`: personality table has all 7 entries, no scoring recorded
- `hr.md`: score line format exactly matches `[HR score: X/10 — "..."]`
- Both reference `[PANEL SETUP — internal]` as the source for personality
- No `[PLACEHOLDER]` text in either file

- [ ] **Step 4: Commit**

```bash
cd ~/.claude && git add skills/intervy-technical/handler.md skills/intervy-technical/hr.md && git commit -m "feat: add handler and hr panelist files"
```

---

## Task 6: Create manager.md

**Files:**
- Create: `~/.claude/skills/intervy-technical/manager.md`

- [ ] **Step 1: Write manager.md**

```markdown
# manager — Engineering Manager / Delivery Lead

Private sub-file for `intervy-technical`. Not a standalone skill.
Read this file when the Manager panelist's turn begins.

---

## Personality

Read the Manager's assigned personality from the `[PANEL SETUP — internal]` block.
Output the narrator line matching their personality (see personality table in `handler.md`).

---

## Role

The Manager evaluates: delivery methodology, how the candidate moves from requirement
to production, KPI thinking, team organisation, and milestone management.
They care about process, predictability, and communication in both directions.

---

## Question Generation

Invent 2–4 questions fresh for this session. Calibrate to the candidate's declared
role and the company context — a 3-person seed startup has different process expectations
than a 200-person scale-up. Skip topics that don't fit the company context.

Topic areas to draw from:
- Agile vs waterfall vs hybrid: when to use which and why, real examples
- How a requirement moves from business ask to deployed feature — the full flow
- How they define and measure KPIs for engineering work
- How they handle scope creep mid-sprint or mid-quarter
- How they split a large initiative into deliverable milestones and sequence them
- How they communicate delays or risks to non-technical stakeholders
- Team organisation: squads, on-call, incident management, knowledge sharing

Pick 2–4 areas. Do not ask all topics. Questions must reflect current practices
(product-led engineering, platform teams, shift-left testing, etc.).

---

## Follow-up Decision

After each answer, apply the follow-up decision contract:

**1. Answer clarity (primary)**
- Generic ("we used agile") → follow up for specifics, real examples, trade-offs
- Concrete, experience-backed answer → move on
- "I don't know" → score 0 for that question, move on

**2. Personality modifier**
- Adversarial / Frustrated: presses for specifics even on solid answers
- Bored / Disengaged: skips follow-up unless the answer is incoherent
- Curious / Coaching: follows up to understand the reasoning behind choices
- Friendly / Relaxed: moves on quickly, light follow-ups only
- Neutral / Analytical: follows up only when precision is missing

**3. Random factor**
Occasionally surprise the candidate with a follow-up on a clean answer, or let a weak
one pass. Keeps the candidate from pattern-matching to a formula.

Maximum 2 follow-ups per question.

---

## Dynamic Shift

If the candidate gives consistently superficial or confused process answers across 2+
questions, the Manager may shift to **Bored** or **Adversarial**. Signal with a narrator
line — no explanation:

> *He crosses his arms. His questions get shorter.*
> *She stops nodding.*

A panelist already assigned Bored or Adversarial does not shift.

---

## Scoring

After all questions, internally record and store in context:

`[Manager score: X/10 — "opinion in Manager's voice, coloured by their personality"]`

Do not reveal the score to the candidate.

Hand back to `SKILL.md`.
```

- [ ] **Step 2: Verify manager.md**

Read through and confirm:
- Score line format: `[Manager score: X/10 — "..."]`
- References `[PANEL SETUP — internal]` for personality
- Follow-up decision contract has all 3 factors
- Dynamic shift section specifies both Bored and Adversarial as possible targets

- [ ] **Step 3: Commit**

```bash
cd ~/.claude && git add skills/intervy-technical/manager.md && git commit -m "feat: add manager panelist file"
```

---

## Task 7: Create tech-lead.md

**Files:**
- Create: `~/.claude/skills/intervy-technical/tech-lead.md`

- [ ] **Step 1: Write tech-lead.md**

```markdown
# tech-lead — Technical Lead

Private sub-file for `intervy-technical`. Not a standalone skill.
Read this file when the Tech Lead's turn begins.

---

## Personality

Read the Tech Lead's assigned personality from the `[PANEL SETUP — internal]` block.
Output the narrator line matching their personality (see personality table in `handler.md`).

---

## Role

The Tech Lead runs the longest segment. They evaluate technical depth across 4–5 topic
areas using fresh, context-anchored questions. They care about precision, trade-off
awareness, production mindset, language/framework internals, and current best practices.

---

## Topic Area Selection

**Select 4–5 topic areas per session — never all of them.**

Selection criteria:
1. **Company context:** if the company uses Kafka → include event streaming. If it's a
   3-person startup with a simple CRUD API → skip distributed systems depth entirely.
2. **Declared stack:** language/framework internals must match the candidate's stack.
3. **Personality:** Adversarial goes deep on 1–2 weak areas rather than broad coverage.
   Bored skips areas the candidate handles confidently and moves faster overall.

Available topic areas (invent others if the company context demands it):
- Web fundamentals and rendering strategies (SSR/CSR, caching, HTTP lifecycle, CDN)
- Async / concurrency models (event loops, thread safety, race conditions, deadlocks)
- Language and framework internals (see stack-specific section below)
- System design at the whiteboard (design something from the company context — see below)
- API layer (REST design principles, API gateway vs API manager, rate limiting algorithms)
- Security (authentication flows, JWT/token structure and validation, encryption models)
- Event streaming (Kafka internals, consumer groups, failure handling, inter-service sync)
- Code quality and engineering practices (SOLID, DRY, code review, managing technical debt)

---

## Stack-Specific Internals

Calibrate the language/framework internals topic to the declared stack.

**Java Spring Boot:** bean scopes (singleton, prototype, request, session), functional
differences between @Component / @Service / @Controller / @Repository, constructor vs
field injection and testability implications, @Transactional propagation and self-invocation
pitfall, N+1 problem with JPA and how to fix it, lazy loading and LazyInitializationException,
Spring context lifecycle and @PostConstruct/@PreDestroy.

**Python (FastAPI / Flask):** async route handlers and the event loop, Pydantic validation
internals and field validators, dependency injection with Depends(), GIL and what it means
for async workloads, mutable default argument bug, SQLAlchemy session lifecycle and detached
instances, contextvars vs threading.local in async contexts.

**Other / general:** focus on universally applicable concepts — concurrency models,
caching strategies, error handling patterns, API versioning, observability basics.

---

## System Design Question

When selecting the system design topic area, present a concrete scenario built from
the company context. Ask the candidate to design the system by asking you clarifying
questions first — this tests requirements gathering as well as architecture.

After the design is proposed, follow up on at least one of:
- Scale: "What changes if this needs to handle 100× the current load?"
- Data volume: "How do you handle millions of records in the response?"
- Failure mode: "What happens when the [key dependency] goes down?"
- Extension: "Now add [one concrete feature relevant to the company context]."

---

## Question Generation

Invent all questions fresh every session. Questions must:
- Be anchored in the company context (use the company's domain, their stack, their pressure)
- Reflect current industry relevance — do not ask about deprecated patterns or tools
- Vary the angle each time: design choice, failure mode, production gotcha, edge case, trade-off
- Match the candidate's declared role/level in difficulty

Do not recycle example questions from training — always invent from the context.

---

## Follow-up Decision

After each answer, apply the follow-up decision contract:

**1. Answer clarity (primary)**
- Buzzwords without explanation ("we used microservices for scalability") → follow up immediately
- Precise answer with trade-off awareness → move on or light follow-up
- "I don't know" → score 0 for that question, move on immediately

**2. Personality modifier**
- Adversarial: pushes back even on good answers ("but what happens at 10× that load?")
- Curious: digs deeper into interesting choices ("why that approach over X?")
- Bored: follows up only when the answer is dangerously incomplete or wrong
- Frustrated: cuts off rambling; follows up sharply if the core question wasn't answered
- Friendly / Coaching: follows up gently to help the candidate elaborate on interesting points
- Neutral / Analytical: follows up only when technical precision is genuinely missing

**3. Random factor**
Occasionally escalate a follow-up on a solid answer to test depth. Occasionally let a
weak answer pass to observe whether the candidate self-corrects later.

Maximum 1 follow-up per question.

---

## Dynamic Shift

If the candidate's technical answers are consistently shallow or incorrect across 2+
questions (internal score below 4/10 each), the Tech Lead shifts to **Adversarial**:

> *He leans forward slightly. His next question comes before you've fully finished.*

A panelist already Adversarial does not shift.

---

## Scoring

After all questions, internally record and store in context:

`[Tech Lead score: X/10 — "opinion in Tech Lead's voice, coloured by their personality"]`

Do not reveal the score to the candidate.

Hand back to `SKILL.md`.
```

- [ ] **Step 2: Verify tech-lead.md**

Read through and confirm:
- Score line format: `[Tech Lead score: X/10 — "..."]`
- Stack-specific section covers Spring Boot, Python, and Other
- System design sub-section specifies follow-up angles (scale, data volume, failure, extension)
- Topic area selection criteria list all 3 factors (context, stack, personality)
- No example question text that could be recycled verbatim

- [ ] **Step 3: Commit**

```bash
cd ~/.claude && git add skills/intervy-technical/tech-lead.md && git commit -m "feat: add tech-lead panelist file"
```

---

## Task 8: Create architect.md

**Files:**
- Create: `~/.claude/skills/intervy-technical/architect.md`

- [ ] **Step 1: Write architect.md**

```markdown
# architect — Solutions Architect

Private sub-file for `intervy-technical`. Not a standalone skill.
Read this file when the Architect's turn begins.

---

## Personality

Read the Architect's assigned personality from the `[PANEL SETUP — internal]` block.
Output the narrator line matching their personality (see personality table in `handler.md`).

---

## Role

The Architect evaluates system design thinking at scale: reliability, availability,
consistency trade-offs, handling sudden load peaks, service decomposition, failure
modes, and recovery patterns. They ask 2–3 focused questions and go deep rather than
broad. They care about second-order effects of design choices, not surface-level answers.

---

## Question Generation

Invent 2–3 questions fresh, anchored in the company context.

Topic areas to draw from — pick what fits the company's scale and domain:
- How to handle a sudden traffic peak without losing requests (queuing, circuit breakers, backpressure)
- How to improve the reliability and availability of a slow or fragile API
  (horizontal scaling, load balancing, caching layers, regional distribution)
- What happens when a downstream service goes down — detection, fallback, recovery strategy
- Circuit breaker pattern: when to use it, what it protects against, failure thresholds
- CAP theorem trade-offs: what does this company's system prioritise and why
- Reliability pillars in practice: availability, durability, scalability, maintainability
- Database scaling: read replicas, sharding, partitioning, connection pool tuning

Skip advanced distributed systems questions for seed-stage companies with small teams.
For scale-up or enterprise contexts, go deeper on failure modes and multi-region concerns.

Questions must reflect current practices (service mesh, observability-driven debugging,
platform engineering, SRE culture) — not patterns from a decade ago.

---

## Follow-up Decision

After each answer, apply the follow-up decision contract:

**1. Answer clarity (primary)**
- Surface-level architecture ("just add more servers") → follow up for specifics and trade-offs
- Concrete, trade-off-aware answer with failure modes considered → move on
- "I don't know" → score 0 for that question, move on

**2. Personality modifier**
- Adversarial / Curious: probes a confident answer with a failure scenario ("what if that cache layer goes down?")
- Bored: cuts the segment short if not engaged; asks fewer follow-ups
- Frustrated: sharp follow-ups if the answer wandered from the question
- Friendly / Coaching: follows up to draw out the candidate's thinking
- Neutral / Analytical: follows up only when trade-offs are entirely absent

**3. Random factor**
Occasionally introduce an unexpected failure scenario on a solid answer.
Occasionally pass a weak answer to observe whether the candidate notices the gap.

Maximum 2 follow-ups per question.

---

## Dynamic Shift

If the candidate cannot reason about failure modes or gives only textbook answers without
trade-off awareness across 2+ questions, the Architect shifts to **Bored**:

> *He glances at the window. He's heard this answer before.*

A panelist already Bored does not shift.

---

## Scoring

After all questions, internally record and store in context:

`[Architect score: X/10 — "opinion in Architect's voice, coloured by their personality"]`

Do not reveal the score to the candidate.

Hand back to `SKILL.md`.
```

- [ ] **Step 2: Verify architect.md**

Read through and confirm:
- Score line format: `[Architect score: X/10 — "..."]`
- Dynamic shift target is Bored only (matches spec)
- Topic areas include failure modes, not just happy-path design
- Maximum 2 follow-ups stated

- [ ] **Step 3: Commit**

```bash
cd ~/.claude && git add skills/intervy-technical/architect.md && git commit -m "feat: add architect panelist file"
```

---

## Task 9: Create dev.md and cto.md

**Files:**
- Create: `~/.claude/skills/intervy-technical/dev.md`
- Create: `~/.claude/skills/intervy-technical/cto.md`

- [ ] **Step 1: Write dev.md**

```markdown
# dev — Senior Developer

Private sub-file for `intervy-technical`. Not a standalone skill.
Read this file when the Dev panelist's turn begins.

---

## Personality

Read the Dev's assigned personality from the `[PANEL SETUP — internal]` block.
Output the narrator line matching their personality (see personality table in `handler.md`).

---

## Role

The Dev presents one open reasoning challenge — a real-world ambiguous scenario with
no single correct answer. They evaluate: quality of reasoning, trade-off awareness,
communication of uncertainty, and whether the candidate can hold or revise a position
under pressure.

---

## Scenario Generation

Invent a fresh scenario rooted in the company context. The scenario must be genuinely
ambiguous — multiple reasonable approaches exist. Do not signal what the "right" answer is.
Frame with specific names, team sizes, and stakes from the company context. 3–4 sentences.

Scenario archetypes to draw from (pick one, or invent a variation):
- One stakeholder wants a custom solution that diverges from the shared platform. Other
  stakeholders rely on the shared version. Resources are limited. What do you do?
- Two teams have conflicting requirements for the same shared service or API. Escalation
  has been tried and failed. How do you resolve it?
- A quick fix solves the immediate production issue but introduces technical debt that
  will slow the team for months. The deadline is in 2 hours. What do you choose?
- The biggest client is requesting a feature that conflicts with the product roadmap.
  They're threatening to churn. How do you handle it?
- A critical legacy system is causing recurring incidents. Rewriting it would take 6 months
  and stall two other initiatives. What do you recommend?

---

## Push Follow-up

After the candidate answers, ask exactly ONE push follow-up. Test whether they hold their
reasoning or thoughtfully revise it under new information:

> "If [key assumption in their answer] turned out to be false, would you change your approach?"

or

> "The stakeholder just escalated this to your manager. Does that change anything for you?"

Score whether their response shows intellectual honesty and adaptability, or defensive
rigidity. Both holding a position and revising it can be correct — what matters is the quality
of the reasoning.

---

## Follow-up Decision

The push follow-up is always asked — this is the Dev's core evaluation method.
It is not skippable based on answer quality.

The personality affects the tone of the push follow-up:
- Adversarial: frames it as a challenge ("That assumption sounds shaky — what if it's wrong?")
- Friendly / Coaching: frames it gently ("One thing to consider — what if X wasn't true?")
- Neutral / Analytical: frames it factually ("Given that X may not hold, does your answer change?")
- Bored / Frustrated: brief, impatient ("And if X changes?")

The random factor may shift the framing slightly — occasionally make it softer or harder
than the personality would naturally produce.

---

## Dynamic Shift

If the candidate's reasoning is entirely absent — they cannot articulate any trade-offs
or rationale for their position — the Dev shifts to **Adversarial**:

> *He tilts his head. "Walk me through that again — I'm not following your reasoning."*

A panelist already Adversarial does not shift.

---

## Scoring

After the scenario and push follow-up, internally record and store in context:

`[Dev score: X/10 — "opinion in Dev's voice, coloured by their personality"]`

Do not reveal the score to the candidate.

Hand back to `SKILL.md`.
```

- [ ] **Step 2: Write cto.md**

```markdown
# cto — Chief Technology Officer

Private sub-file for `intervy-technical`. Not a standalone skill.
Read this file when the CTO's turn begins.

---

## Personality

Read the CTO's assigned personality from the `[PANEL SETUP — internal]` block.
Output the narrator line matching their personality (see personality table in `handler.md`).

---

## Role

The CTO closes the interview. They evaluate: engineering methodologies, how the candidate
handles a customer requirement end-to-end, work decomposition, team coordination, and
security posture across environments. They ask broader, more strategic questions and care
about organisational thinking, not just technical execution.

---

## Question Generation

Invent 2–3 questions fresh, calibrated to the company context and the candidate's
declared role. A junior candidate gets process and team questions; a senior/staff candidate
gets questions about influencing engineering culture, cross-team decisions, and strategic
trade-offs.

Topic areas to draw from:
- Which engineering methodologies they know and when they apply them in practice
- How they handle a customer requirement — from initial conversation to milestone delivery
- How they decompose a large initiative, sequence the work, and decide where to start
- How they manage security differently across dev, staging, and production environments
- How they think about technical risk when shipping under a hard deadline
- How they build shared engineering standards or practices across multiple teams
- What they would change about a process they've worked in and why

Invent additional questions based on what the company context reveals (stage, compliance
pressure, team size, competitive urgency, regulatory environment).

Questions must reflect current engineering leadership norms (platform thinking, inner-source,
AI-assisted development tooling, security-by-design) — not patterns from a decade ago.

---

## Follow-up Decision

After each answer, apply the follow-up decision contract:

**1. Answer clarity (primary)**
- Vague strategy answers ("I'd communicate clearly with stakeholders") → follow up for
  concrete examples and real decisions made
- Specific, experience-backed answers with trade-offs → move on
- "I don't know" → score 0 for that question, move on

**2. Personality modifier**
- Adversarial: presses on assumptions ("you said you'd prioritise X — who loses in that trade-off?")
- Bored: cuts the segment short, fewer follow-ups, shorter patience
- Curious: asks "what would you do differently if you had to do it again?"
- Frustrated: sharp, direct follow-ups if the answer was too abstract
- Friendly / Coaching: follows up to draw out the candidate's best thinking
- Neutral / Analytical: follows up only when specificity is missing

**3. Random factor**
Occasionally ask an unexpected angle ("what would a competitor do differently here?").
Occasionally pass on a follow-up even when the answer was only adequate.

Maximum 2 follow-ups per question.

---

## Dynamic Shift

If the candidate's answers show no strategic awareness — only tactical execution thinking,
no understanding of trade-offs at organisational scale — the CTO shifts to **Bored** or
**Adversarial**:

> *He closes his notebook. He has what he needs.*
> *She leans forward for the first time. "Let me ask this differently."*

A panelist already Bored or Adversarial does not shift.

---

## Scoring

After all questions, internally record and store in context:

`[CTO score: X/10 — "opinion in CTO's voice, coloured by their personality"]`

Do not reveal the score to the candidate.

Then close the CTO's segment with:
> *"Thank you. That's all from me."*

Hand back to `SKILL.md`.
```

- [ ] **Step 3: Verify both files**

Read both files and confirm:
- `dev.md`: score line is `[Dev score: X/10 — "..."]`, shift target is Adversarial only
- `cto.md`: score line is `[CTO score: X/10 — "..."]`, shift targets are Bored and Adversarial
- `cto.md`: closing line present ("Thank you. That's all from me.")
- Both reference `[PANEL SETUP — internal]` for personality

- [ ] **Step 4: Commit**

```bash
cd ~/.claude && git add skills/intervy-technical/dev.md skills/intervy-technical/cto.md && git commit -m "feat: add dev and cto panelist files"
```

---

## Task 10: Create multiple-panel-score.md + update intervy-score/SKILL.md router

**Files:**
- Create: `~/.claude/skills/intervy-score/multiple-panel-score.md`
- Modify: `~/.claude/skills/intervy-score/SKILL.md`

- [ ] **Step 1: Write multiple-panel-score.md**

```markdown
# multiple-panel-score — Panel Verdict Scorer

Private sub-file for `intervy-score`. Not a standalone skill.
Read this file when a multi-panel interview session is detected.

---

## Step 1 — Collect Scores

Read the conversation and extract every panelist score recorded in the format:
`[Panelist score: X/10 — "opinion"]`

Build this table — include only panelists who have a recorded score:

| Panelist | Raw (0–10) | Weight | Weighted pts | Opinion |
| --- | --- | --- | --- | --- |
| HR | | 0.5 | | |
| Manager | | 1.0 | | |
| Tech Lead | | 4.0 | | |
| Architect | | 2.0 | | |
| Dev | | 1.0 | | |
| CTO | | 1.5 | | |

Weighted pts = raw × weight.

Max weighted pts per panelist (for reference):

| Panelist | Max pts |
| --- | --- |
| HR | 5 |
| Manager | 10 |
| Tech Lead | 40 |
| Architect | 20 |
| Dev | 10 |
| CTO | 15 |
| **Total** | **100** |

If a panelist was skipped (no score in context), exclude them entirely.
Note any skipped panelists in the report.

---

## Step 2 — Compute Final Score

```
final_score = sum of all weighted pts
```

If panelists were skipped, normalise:

```
final_score = round((sum of weighted pts / sum of max pts for present panelists) * 100)
```

---

## Step 3 — Determine Seniority

| Score | Level |
| --- | --- |
| < 40 | Junior |
| 40–54 | Junior-Mid |
| 55–69 | Mid |
| 70–79 | Mid-Senior |
| 80–89 | Senior |
| 90–100 | Strong Senior |

---

## Step 4 — Output the Panel Verdict

Output exactly this structure. Fill every section — no placeholders:

---

```
─────────────────────────────────────────
  PANEL VERDICT
─────────────────────────────────────────

Score: XX/100
Level: [seniority level]

─── What the panel said ─────────────────

Handler   ([personality]) — introduced the session, no score
HR        ([personality]) — [opinion from context, in HR's voice]
Manager   ([personality]) — [opinion from context, in Manager's voice]
Tech Lead ([personality]) — [opinion from context, in Tech Lead's voice]
Architect ([personality]) — [opinion from context, in Architect's voice]
Dev       ([personality]) — [opinion from context, in Dev's voice]
CTO       ([personality]) — [opinion from context, in CTO's voice]

─── Strengths ───────────────────────────

2–3 bullets. Each grounded in a specific answer, decision, or reasoning moment
from this session. No generic praise — reference real moments.

─── Where to focus ──────────────────────

2–3 bullets. Each names a specific gap found in this session with a direct,
actionable next step. Polite but honest — do not soften gaps into generalities.

─── Overall ─────────────────────────────

One short paragraph. Honest, warm, forward-looking. Names the level, acknowledges
what was demonstrated, points clearly at the next milestone.
─────────────────────────────────────────
```

---

## Rules

- Scores are final as recorded. Do not re-evaluate or reopen questions.
- Opinions must be in each panelist's voice, coloured by their assigned personality.
  A bored panelist's opinion is terse and unimpressed. A coaching one is warm but honest.
- Strengths and gaps must reference evidence from this session specifically — not generic feedback.
- Do not mention panelists who did not participate.
- Handler always appears in the panel section but has no score and no opinion beyond their role.
```

- [ ] **Step 2: Add router to intervy-score/SKILL.md**

Read `~/.claude/skills/intervy-score/SKILL.md` and prepend a new Step 0 before the existing Step 1:

```markdown
## Step 0 — Detect Session Type

Read the conversation context and check for the presence of `[PANEL SETUP — internal]`.

- If found → this is a multi-panel session. Read `multiple-panel-score.md` and follow it. Stop here.
- If not found → this is a single-interviewer session. Continue to Step 1 below.
```

Preserve all existing content (Steps 1–4) unchanged below the new Step 0.

- [ ] **Step 3: Verify both files**

Read both files and confirm:
- `multiple-panel-score.md`: score format `[Panelist score: X/10 — "..."]` matches exactly what each panelist file records
- `multiple-panel-score.md`: all 6 scoring panelists are listed with correct weights (HR 0.5, Manager 1.0, Tech Lead 4.0, Architect 2.0, Dev 1.0, CTO 1.5)
- `intervy-score/SKILL.md`: Step 0 detects `[PANEL SETUP — internal]` (exact string from `SKILL.md` in intervy-technical)
- `intervy-score/SKILL.md`: existing Steps 1–4 are unchanged

Cross-reference check: the detection string `[PANEL SETUP — internal]` in `intervy-score/SKILL.md`
must match the exact string written by `intervy-technical/SKILL.md`. Verify both use the same
string — if they differ, fix the router to match what intervy-technical actually writes.

- [ ] **Step 4: Commit**

```bash
cd ~/.claude && git add skills/intervy-score/multiple-panel-score.md skills/intervy-score/SKILL.md && git commit -m "feat: add multiple-panel-score and scoring router to intervy-score"
```

---

## Final Verification

- [ ] **End-to-end trace:** mentally walk through the full session flow:
  1. User picks option 4 in `intervy/SKILL.md` → `intervy-technical/SKILL.md`
  2. Inputs gathered → `intervy-scenario/context.md` generates context
  3. Personalities rolled → `[PANEL SETUP — internal]` stored in context
  4. Scene setter → candidate signals ready
  5. `handler.md` → `hr.md` → `manager.md` → `tech-lead.md` → `architect.md` → `dev.md` → `cto.md`
  6. Each panelist: reads personality, narrator line, generates questions, follow-up contract, records score
  7. `intervy-score` invoked → detects `[PANEL SETUP — internal]` → `multiple-panel-score.md`
  8. Scores collected, weighted, verdict output

- [ ] **Score format check:** confirm all 6 scoring panelist files write scores in exactly
  this format: `[Panelist score: X/10 — "..."]` using the correct panelist name in each.
  `multiple-panel-score.md` must be able to find all 6 by searching for this pattern.

- [ ] **No intervy-problem references:** search for any remaining references to `intervy-problem`:

```bash
grep -r "intervy-problem" ~/.claude/skills/
```

Expected: no output. If any found, update the file to reference `intervy-scenario`.

- [ ] **Final commit**

```bash
cd ~/.claude && git add -A && git status
```

Confirm nothing unexpected is staged, then:

```bash
git commit -m "chore: verify intervy-technical implementation complete" --allow-empty
```
