# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal practice repository of Go solutions for NeetCode 150 / LeetCode algorithm problems. Solutions are organized by algorithmic category and follow LeetCode's submission format (just the function, no `package main` or `main()`).

## How Solutions Are Structured

- **No `go.mod`** — this is not a buildable Go module. Solutions are meant to be pasted directly into the LeetCode editor.
- **No package declarations** — files omit `package main` (except `49_group_anagrams.go` and `tree/test.go`). This is intentional: LeetCode provides the package wrapper.
- **No `main()` functions** — solutions are pure algorithm functions that accept inputs and return outputs, matching LeetCode's expected signature.
- **LeetCode-provided types** — `TreeNode`, `ListNode`, and similar types are defined by the LeetCode platform and referenced in comments at the top of relevant files. They are not defined in this repo.
- **Multiple implementations per file are common** — different approaches (iterative, recursive, optimized) live side-by-side as separate functions. This means files will NOT compile as-is due to duplicate function names; each variant is meant to be submitted independently.

## Directory Structure

Each subdirectory corresponds to a problem category. Files are named `<leetcode_problem_number>_<name>.go`:

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

When adding a new problem solution:

1. Place it in the appropriate category directory.
2. Name it `<problem_number>_<snake_case_name>.go`.
3. Include only the solution function(s) — no `package` declaration, no `main()`.
4. If the problem uses LeetCode-provided types (`TreeNode`, `ListNode`), add the type definition as a comment block at the top (see existing files for the format).
5. Add all necessary Go imports (e.g., `"math"`, `"fmt"`) — even if the file won't build locally, this ensures correctness when pasted into LeetCode.

## Code Style

- Follow the existing style: minimal comments, short variable names (`m` for maps, `ans` for result slices), early returns.
- Use `//` comments to label alternative implementations (e.g., `// Iterative version`, `// Recursive version`).
- Tabs for indentation (Go standard).

## Notable Files

- `tree/test.go` — scratch file for experimenting with Go slice behavior. Not a LeetCode solution. Can be ignored or deleted.
- `1_two_sum.go` — contains two `twoSum` functions (duplicate). Each is a standalone variant.
