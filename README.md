# Intervy — AI Interview Coach

A Claude Code skill set that prepares you for technical interviews across four modes.

## Modes

### 1. Assignment Review
Paste a project or give a git clone URL. Conducts a seniority-calibrated technical interview on your code — architecture, failure modes, security, testing, production readiness. Scored 0–100.

### 2. From Scratch
Build a backend API from scratch under time pressure, FAANG-style. Supports Python (FastAPI/Flask) and Java Spring Boot. Generates a randomised business scenario, runs you through theory and coding rounds, scores each phase.

### 3. Coding Challenge
LeetCode-style algorithm practice. Generate a fresh problem or paste one. Hints available on demand, edge case testing, scored 1–10 with complexity and comment analysis.

### 4. Round-Table Interview

Face a full panel of 7 interviewers: handler, HR, manager, tech lead, architect, senior dev, and CTO. Each panelist gets a randomly assigned personality (adversarial, bored, friendly, coaching, and more) that affects how they question you and how harshly they score. Questions are generated fresh every session, anchored in a randomised company context. Scored out of 100 with a merged panel verdict at the end.

## Usage

Just start a session and type anything like "interview", "practice", or "intervy". The `intervy` skill picks it up and walks you through mode selection.

```
> interview
```

## Documentation

- [Assignment Review](docs/assignment-review.md) — seniority-calibrated code walkthrough, scored 0–100
- [From Scratch](docs/from-scratch.md) — FAANG-style live coding rounds, Bootstrap through Expert
- [Coding Challenge](docs/coding-challenge.md) — LeetCode-style problem session with hints and edge case testing
- [Round-Table Interview](docs/round-table.md) — 7-panelist panel interview with personality system and merged verdict

## Skills

| Skill | Role |
| --- | --- |
| `intervy` | Main entry point — dispatcher for all 4 modes |
| `intervy-scenario` | Generates randomised company scenarios (used by from-scratch and round-table) |
| `intervy-technical` | Round-table panel interview — 7 panelists, personality system, dynamic follow-ups |
| `intervy-score` | Evaluates and scores interviews — single-interviewer and multi-panel modes |
| `intervy-questioner` | Fires language-specific deep-dive questions between rounds |

## Requirements

- [Claude Code](https://claude.ai/code) installed and authenticated

## Installation

Skills must live directly inside a `.claude/skills/` directory — either globally (`~/.claude/skills/`) so they work in every session, or inside a specific project (`.claude/skills/`) if you want them only there.

### Global install (recommended)

```bash
git clone https://github.com/ieCecchetti/intervy /tmp/intervy-install
cp -r /tmp/intervy-install/.claude/skills/* ~/.claude/skills/
rm -rf /tmp/intervy-install
```

### Project-level install

Run this from the root of the project you want to use it in:

```bash
mkdir -p .claude/skills
git clone https://github.com/ieCecchetti/intervy /tmp/intervy-install
cp -r /tmp/intervy-install/.claude/skills/* .claude/skills/
rm -rf /tmp/intervy-install
```

### Verify

After installing, open Claude Code in any project and run:

```
/skills
```

You should see `intervy`, `intervy-scenario`, `intervy-technical`, `intervy-score`, and `intervy-questioner` listed.

### Use it

```
> interview
```

Claude will present the three modes and walk you through setup.

## Structure

```
.claude/skills/
  intervy/              ← dispatcher + sub-files for all 4 modes
  intervy-scenario/     ← company context + story generator (shared)
  intervy-technical/    ← round-table panel interview (7 panelists)
  intervy-score/        ← round evaluator — single and multi-panel
  intervy-questioner/   ← theory question bank (standalone)
docs/
  assignment-review.md  ← assignment review mode guide
  from-scratch.md       ← from scratch interview guide
  coding-challenge.md   ← coding challenge mode guide
  round-table.md        ← round-table interview guide
```
