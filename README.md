# Intervy — AI Interview Coach

A Claude Code skill set that prepares you for technical interviews across three modes.

## Modes

### 1. Assignment Review
Paste a project or give a git clone URL. Conducts a seniority-calibrated technical interview on your code — architecture, failure modes, security, testing, production readiness. Scored 0–100.

### 2. From Scratch
Build a backend API from scratch under time pressure, FAANG-style. Supports Python (FastAPI/Flask) and Java Spring Boot. Generates a randomised business scenario, runs you through theory and coding rounds, scores each phase.

### 3. Coding Challenge
LeetCode-style algorithm practice. Generate a fresh problem or paste one. Hints available on demand, edge case testing, scored 1–10 with complexity and comment analysis.

## Usage

Just start a session and type anything like "interview", "practice", or "intervy". The `intervy` skill picks it up and walks you through mode selection.

```
> interview
```

## Documentation

- [Assignment Review](docs/assignment-review.md) — seniority-calibrated code walkthrough, scored 0–100
- [From Scratch](docs/from-scratch.md) — FAANG-style live coding rounds, Bootstrap through Expert
- [Coding Challenge](docs/coding-challenge.md) — LeetCode-style problem session with hints and edge case testing

## Skills

| Skill | Role |
| --- | --- |
| `intervy` | Main entry point — dispatcher for all 3 modes |
| `intervy-problem` | Generates randomised project scenarios for from-scratch mode |
| `intervy-score` | Evaluates and scores from-scratch interview rounds |
| `intervy-questioner` | Fires language-specific deep-dive questions between rounds |

## Installation

Clone this repo into any project's `.claude/skills/` folder (or your global `~/.claude/skills/`):

```bash
git clone https://github.com/ieCecchetti/intervy .claude/skills/intervy-suite
```

Or clone individual skills as needed.

## Structure

```
.claude/skills/
  intervy/              ← dispatcher + sub-files for all 3 modes
  intervy-problem/      ← story/scenario generator (standalone)
  intervy-score/        ← round evaluator (standalone)
  intervy-questioner/   ← theory question bank (standalone)
docs/
  assignment-review.md  ← assignment review mode guide
  from-scratch.md       ← from scratch interview guide
  coding-challenge.md   ← coding challenge mode guide
```
