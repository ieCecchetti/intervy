# Coding Challenge

A LeetCode-style timed coding session. You get a problem, work in your IDE, and are scored 0–10 on optimality, hints used, and code quality.

---

## How to start

Invoke the `intervy` skill and choose **option 3**.

---

## Flow

### Phase 1 — Problem Setup

Choose how you want your problem:

**Fresh problem** — the interviewer generates an original problem for you.
- You pick a topic (Array, Hash Map, Two Pointers, Sliding Window, Binary Search, Stack, Queue, Linked List, Tree, Graph, Dynamic Programming, Greedy, Sorting) or let the interviewer choose.
- You pick a difficulty (Easy / Medium / Hard) or let the interviewer choose based on your history in this session.
- The problem is structurally similar to LeetCode but original — not a well-known problem by name.

**Pasted problem** — you paste an existing problem from any source.
- The interviewer strips noise lines (lock icons, "Companies", "Topics" labels, premium markers) and formats the problem consistently.

In both cases, the problem is formatted as:

```
# <number>. <Title>
Difficulty: <Easy | Medium | Hard>
Topics: <comma-separated>

## Description
...

## Examples
...

## Constraints
...
```

---

### Phase 2 — Oracle (never shown to you)

Immediately after the problem is set, the interviewer silently generates and holds in context:
- The optimal solution
- Time and space complexity analysis
- The core insight
- 3 ordered hints (from least to most revealing)

None of this is shown to you during the session.

---

### Phase 3 — Clarifying Questions

You can ask questions before starting. The interviewer answers as a real interviewer would:
- Clarify ambiguous constraints
- Confirm input ranges
- Confirm whether input is guaranteed valid
- Confirm expected output type

What they will **not** do: give hints, suggest approaches, or reveal the algorithm.

When you are ready, say so. The interviewer will remind you to **comment your code as you write** — explaining your thinking step by step. This simulates thinking out loud and counts toward your score.

---

### Phase 4 — Solution File

The interviewer creates `./coding_challenges/<number>_<title>.py` (e.g. `3041_max_subarray_product.py`) with:
- The full problem statement in the docstring
- An empty `Solution` class with the correct method signature inferred from the problem
- A `__main__` block pre-wired with the given examples

Open the file in your IDE and start coding.

Available commands during the session:
- **"hint"** — get the next hint (hints are ordered; you always get the least revealing one that hasn't been given yet)
- **"done"** — signal that you're finished and want to be scored

---

### Phase 5 — Reactive Session

While you work, the interviewer stays quiet except to:
- Give the next unused hint when you ask
- Ask one short probing question when you describe your approach ("Why that data structure?", "What's the time complexity there?", "What happens at the boundary?")

They will not volunteer information, write code, or reveal the oracle solution.

---

### Phase 6 — Edge Case Testing

When you say "done", the interviewer reads your solution file and runs inline edge case testing (no subagents, no external tools).

They derive correct expected outputs mathematically from the problem statement — not from your code. They then trace your code against 6–10 edge cases beyond the given examples:
- Boundary values (min/max of each constraint)
- Empty input, single element, two elements
- All same values, all duplicates
- Already sorted, reverse sorted
- Partial-match cases

**If all pass:** you go straight to scoring.

**If a case fails:** the interviewer shows you one failing case with a tip (no spoiler):

> "I found a failing edge case:
> - Input: `...`
> - Expected: `...`
> - Tip: `<what kind of case this is>`
>
> Are you willing to terminate the test?
> - **Yes** → scored now (incomplete solution penalty applies)
> - **No** → fix it, then say "done" again"

If you choose No, edge case testing runs again from scratch after your fix.

---

### Phase 7 — Scoring

**Step 1** — you state your time and space complexity.

**Step 2** — the interviewer evaluates:
- Correctness against examples and edge cases
- Whether your stated complexity is accurate
- Whether your solution is optimal, one step worse, or two steps worse than the oracle
- Code quality (naming, readability, structure)
- Comment quality (do they explain *why*, or just restate what the code does)

**Step 3** — scoring formula:

| Optimality | Base score |
|---|---|
| Optimal | 10 |
| One step worse (e.g. O(N log N) vs O(N)) | 7 |
| Two steps worse | 4 |

**Hint deductions** (applied after base):

| Difficulty | Free hints | Deduction per extra hint | Maximum deduction |
|---|---|---|---|
| Easy | 0 | −1 per hint | −3 |
| Medium | 1 | −1 per extra | −3 |
| Hard | 2 | −1 per extra | −3 |

**Comment bonus/penalty** (±1, applied after hints):
- +1 — comments clearly explain reasoning at key steps (data structure choice, edge case awareness, complexity trade-offs)
- 0 — comments present but superficial
- −1 — no comments, or comments only restate what the code does

**Incomplete penalty:** −2 if you terminated the test with a failing edge case (floor: 1).

**Step 4** — the interviewer shows the full breakdown. Example:

> "Optimal O(N) solution → 10
> Medium difficulty, 2 hints used (1 free) → −1
> Good comments → +1
> **Final score: 10/10**"

---

## Tips

- Comment as you code — it directly affects your score, and it's the closest thing to thinking out loud in a real interview.
- Clarify before you start. A well-scoped question saves you from building the wrong thing.
- "hint" costs you points on Easy (0 free) and less on Hard (2 free) — use them strategically.
- If you fail an edge case, fixing it and re-running avoids the incomplete penalty.
- You don't need to be optimal to score well — a clean, well-commented O(N log N) solution with no hints can outscore a sloppy optimal solution.
