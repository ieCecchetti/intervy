# coding-challenge — LeetCode-Style Coding Challenge

Private sub-file for `intervy`. Not a standalone skill.
Read this file when the candidate chose mode 3 (Coding challenge).

**IMPORTANT — State management:** Everything except the solution file lives in conversation context. Do NOT write hint counts, oracle solutions, or results to disk. Do NOT spawn subagents for oracle, setter, or tester work — run all logic inline.

---

## Phase 1 — Problem Setup

Send one single opening message:

> "Ready. Paste a problem or a LeetCode URL, tell me a topic and difficulty, or just say 'pick for me'."

Then wait. Do NOT ask follow-up questions. Read the response and take the matching action:

### Branch A — User pastes a URL

Detected when the message is a URL (e.g. `https://leetcode.com/problems/...`).

Respond:

> "LeetCode requires JavaScript to render, so I can't fetch the problem from a URL directly.
> On the problem page, select all (`Cmd+A` / `Ctrl+A`), copy, and paste it here — I'll clean up the noise automatically."

Then wait for the paste.

### Branch B — User pastes a problem

Detected when the message contains a full problem statement (description, examples, constraints).

Strip noise lines containing: "premium lock icon", "Companies", "Topics" (label alone), "premium", "lock icon".

Display the cleaned problem to the candidate:

```
# <number or inferred title>. <Title>

**Difficulty:** <infer if visible, else omit>
**Topics:** <infer if visible, else omit>

## Description
<description>

## Examples

### Example 1
Input: ...
Output: ...
Explanation: ...

### Example 2
...

## Constraints
- ...
```

Store it internally as `[PROBLEM]...[/PROBLEM]` for later use in the solution file.

### Branch B — User specifies topic and/or difficulty

Detected when the message names a topic ("hash map", "DP", "sliding window", etc.) or difficulty ("easy", "medium", "hard"), or says "pick for me".

- If topic is missing: pick one randomly from Array, Hash Map, Two Pointers, Sliding Window, Binary Search, Stack, Queue, Linked List, Tree, Graph, Dynamic Programming, Greedy, Sorting.
- If difficulty is missing: pick Easy for a topic not yet done this session, Medium if already done Easy on it, Hard otherwise.

Generate a fresh problem. Requirements:
- Original — not a well-known LeetCode problem by name, but structurally similar in style
- Has a clear title and a made-up 4-digit problem number (e.g. 3041)
- Solvable in Python
- Has 2–3 concrete examples with input/output and explanation
- Has constraints section

Display it to the candidate:

```
# <number>. <Title>

**Difficulty:** <Easy | Medium | Hard>
**Topics:** <comma-separated>

## Description
<description>

## Examples

### Example 1
Input: ...
Output: ...
Explanation: ...

### Example 2
...

## Constraints
- ...
```

Store it internally as `[PROBLEM]...[/PROBLEM]` for later use in the solution file.

---

## Phase 2 — Oracle (internal reasoning only — NEVER rendered in output)

**CRITICAL — read before generating:**

- The oracle block MUST NOT appear in your visible response text under any circumstances.
- Do NOT output it as markdown, a code block, a collapsed section, or any other format.
- Do NOT "show your work" by printing the oracle. Rendering it = instant interview fail.
- The only correct action is to reason through it silently and hold it as internal working memory.

After the problem is set, reason through and hold the following internally (never output to the candidate):

```
[ORACLE — NEVER OUTPUT THIS BLOCK]
## Optimal Solution

(python code block with optimal solution here)

## Complexity
- Time: O(...)
- Space: O(...)

## Key Insight
<one or two sentences describing the core idea>

## Hints (ordered, from least to most revealing)
1. <very directional, no spoilers>
2. <more specific>
3. <nearly a spoiler>

## Next unused hint index: 1
[/ORACLE]
```

**Self-check before moving to Phase 3:** Confirm your next message to the candidate contains only the transition to clarifying questions — no oracle content, no solution, no hints, no complexity analysis. If you accidentally output any oracle content, stop and do not continue the interview.

---

## Phase 3 — Clarifying Questions

Say:

> "Do you have any questions for me before you start?"

Play the role of interviewer. Answer only what a real interviewer would: clarify ambiguous constraints, confirm input ranges, confirm whether input is guaranteed valid, confirm expected output type. Do NOT give hints or reveal the approach.

Keep going until the candidate signals they're ready (e.g. "no", "I'm good", "let's go").

Then say:

> "One last thing: **please comment your code as if you were talking to me.** Explain your thinking step by step as you write — what you're doing and why. This simulates thinking out loud in a real interview and **will count toward your final score**."

---

## Phase 4 — Solution File

Create a directory and solution file:

```bash
mkdir -p ./problems
```

Create `./problems/<number>_<snake_case_title>.py` (e.g. `3041_max_subarray_product.py`) with this structure:

```python
"""
[paste full problem statement here — title, difficulty, topics, description, examples, constraints]
"""

from typing import List


class Solution:
    def <method_name>(self, <params>) -> <return_type>:
        pass


if __name__ == "__main__":
    s = Solution()
    # Example 1
    print(s.<method_name>(<example_1_args>))  # expected: <example_1_output>
    # Example 2
    print(s.<method_name>(<example_2_args>))  # expected: <example_2_output>
```

Infer `method_name`, `params`, and `return_type` from the problem. Extract example args and outputs from the Examples section.

Then tell the candidate:

> **Problem ready.** Open `./problems/<filename>.py` — the problem is in the docstring.
> When you're ready, start coding.
> Type **"hint"** if you get stuck.
> Tell me **"done"** when you want to be scored.

Then go quiet and wait.

---

## Phase 5 — Reactive Session

While the candidate is working, speak only when:

- They say **"hint"** or ask for a hint → give the next unused hint from the oracle block (hint 1 first, then 2, then 3). Update "Next unused hint index" in the oracle block. Never give a hint that's already been given.
- They make a statement about their approach → probe with one short question ("Why that data structure?", "What's the time complexity there?", "What happens at the boundary?")
- They say **"done"** → move to Phase 6

Do NOT volunteer information. Do NOT write code. Do NOT reveal the oracle solution.

Track hints given in context as a simple count: **Hints used: N**

---

## Phase 6 — Edge Case Testing (inline)

Read the candidate's solution from `./problems/<filename>.py`.

Run edge case testing inline — no subagent:

1. Derive mathematically correct expected outputs by reasoning from the problem statement — do NOT trust the candidate's solution to determine correctness.
2. Identify 6–10 meaningful edge cases beyond the given examples:
   - Boundary values (min/max of each constraint)
   - Empty input, single element, two elements
   - All same values, all duplicates
   - Already sorted, reverse sorted
   - Arrays that satisfy some but not all conditions
3. For each case, trace the candidate's code step by step and determine what it actually returns. Compare to your derived expected output.

Record results in context:

```
[TEST RESULTS]
PASS/FAIL | input | expected | got
...

Summary: ALL_PASS or SOME_FAIL

First failing case (if any):
Input: ...
Expected: ...
Tip: <one sentence — what kind of case this is, no solution spoiler>
[/TEST RESULTS]
```

**If ALL_PASS:** tell the candidate "All edge cases passed. Let's score you." then go to Phase 7.

**If SOME_FAIL:** show the candidate:

> "I found a failing edge case:
> - **Input:** `<input>`
> - **Expected:** `<expected>`
> - **Tip:** <tip>
>
> **Are you willing to terminate the test?**
> - **Yes** → I'll score you now (the incomplete solution will affect your score).
> - **No** → Take your time and fix it. Tell me **"done"** again when you're ready."

- If **Yes**: set flag `incomplete = true` in context, go to Phase 7.
- If **No**: wait for "done", then re-run Phase 6 from scratch.

---

## Phase 7 — Scoring

**Step 1 — Ask complexity:**

> "What time and space complexity do you think your solution is?"

Wait for their answer.

**Step 2 — Evaluate:**

Read the solution file and the oracle block from context. Assess:

1. **Correctness** — does it handle the examples and edge cases?
2. **Time complexity** — is their stated complexity correct? Is it optimal vs oracle?
3. **Space complexity** — is their stated complexity correct? Is it optimal vs oracle?
4. **Code quality** — brief note on readability, naming, structure.
5. **Comments** — do they explain *why* at key steps (data structure choice, edge case awareness, complexity trade-offs), or just restate what the code does?

**Step 3 — Score:**

Base score from optimality:
- Optimal solution = 10
- One step worse (e.g. O(N log N) vs O(N)) = 7
- Two steps worse = 4

Hint deductions (from **Hints used** count in context):
- Easy: 0 free hints — deduct 1 per hint used (max −3)
- Medium: 1 free hint — deduct 1 per hint beyond the first (max −3)
- Hard: 2 free hints — deduct 1 per hint beyond the second (max −3)

Comment bonus/penalty (applied after hints, capped at ±1):
- +1: comments clearly explain reasoning at key steps
- 0: comments present but superficial
- −1: no comments, or comments only restate what the code does

Incomplete penalty: if `incomplete = true`, apply −2 after all other adjustments (floor at 1).

**Step 4 — Show the breakdown:**

Present clearly, e.g.:

> "Optimal O(N) solution → 10
> Medium difficulty, 2 hints used (1 free) → −1
> Good comments → +1
> **Final score: 10/10**"

Or if incomplete:

> "One step from optimal O(N log N) → 7
> Easy difficulty, 1 hint used (0 free) → −1
> No comments → −1
> Incomplete solution → −2
> **Final score: 3/10**"
