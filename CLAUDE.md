# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal practice repository of Python solutions for the [NeetCode 150](https://neetcode.io/practice/practice/neetcode150) — a curated set of 150 LeetCode algorithm problems covering essential algorithms and data structures for coding interviews.

## How Solutions Are Structured

- Each `.py` file includes a **docstring** with the problem number, name, difficulty, and LeetCode URL.
- **LeetCode types** (`TreeNode`, `ListNode`, `TrieNode`) are defined as classes within the solution files — every solution is self-contained.
- All functions use **type hints** (`List[int]`, `Optional[TreeNode]`, etc.).
- Each file contains a single canonical implementation — the cleanest/most efficient approach.
- Files are named `<leetcode_problem_number>_<snake_case_name>.py`.
- There is no `requirements.txt` — only the Python standard library is used.

## Directory Structure

Each subdirectory corresponds to a NeetCode 150 category:

| Directory | Topic |
|---|---|
| `array_hashing/` | Arrays & Hashing |
| `binary_search/` | Binary Search |
| `dynamic_programming/` | Dynamic Programming (1D, 2D) |
| `greedy/` | Greedy |
| `linkedlist/` | Linked Lists |
| `sliding_window/` | Sliding Window |
| `stack/` | Stack |
| `tree/` | Trees |
| `trie/` | Tries |
| `two_pointers/` | Two Pointers |

## Adding a New Solution

1. Place it in the appropriate category directory.
2. Name it `<problem_number>_<snake_case_name>.py`.
3. Include a docstring with: problem number, name, difficulty, and LeetCode URL.
4. Define any needed LeetCode types (`TreeNode`, `ListNode`, `TrieNode`) as classes in the file.
5. Use type hints on all function signatures.
6. Update the README.md table to mark it as done.
7. Use 4-space indentation.

## Code Style

- 4-space indentation (no tabs).
- Descriptive variable names (`char_index`, `max_profit`, not `m`, `ans`).
- Type hints on all function signatures.
- Minimal inline comments; the docstring explains the problem.
- No `if __name__ == "__main__"` blocks — files are self-contained function definitions meant to be submitted to LeetCode.

## Running / Testing

There is no test suite. To verify syntax:

```bash
python3 -c "import py_compile; py_compile.compile('path/to/file.py', doraise=True)"
```

Or to check all files:

```bash
for f in $(find . -name "*.py" -type f); do
  python3 -c "import py_compile; py_compile.compile('$f', doraise=True)" && echo "OK: $f" || echo "FAIL: $f"
done
```
