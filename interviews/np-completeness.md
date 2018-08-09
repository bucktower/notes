# NP-Completeness Time Complexity

[What is NP Complete?](https://stackoverflow.com/questions/210829/what-is-an-np-complete-in-computer-science)

![NP Completness chart](https://en.wikipedia.org/wiki/NP-completeness#/media/File:P_np_np-complete_np-hard.svg)

Most of the time, people assume P \neq NP

- `O(n!)` and `O(2^n)` are **NOT** in polynomial time
  - Polynomial time => bounded by some function `O(n^k)` (`k` = some constant)

- `P`: Set of all decision problems which can be **solved** (and therefore **verified**) in *polynomial time* by a *deterministic Turing machine*
- `NP`: Set of all decision problems which can be **verified** in *polynomial time* by a *deterministic Turing machine*
- `NP-Complete`: Problem is in NP, and every problem in NP is *reducible* to it
  - If any one of the NP Complete problems was to be solved "quickly" (in polynomial time), then all NP problems can be solved "quickly"
- `NP-Hard`: Set of all problems at least as hard as the hardest problems in NP (in other words, `NP-Complete` or harder)
  - Some of these problems aren't actually in NP

## Traveling Salesman Problem (`NP-Hard`)

*Given a list of cities and distances between each pair, what is the shortest possible route that visits each city once and returns to the origin city?*

(We already know that it's possible to do so/Hamiltonian cycle does in fact exist)

No known polynomial time solution

### Naive Solution

1. **City 1** is starting (and ending) point
2. Generate all `(n-1)!` permutations of cities
3. Calculate costs of every permutation and keep track of minimum cost permutation
4. Return the minimum cost permutation

Time Complexity: `O(n!)`

### Dynamic Programming

1. Compute optimal path from each n = 2 nodes in path from starting node
2. Continue counting path to new nodes, storing 

Time Complexity: `O(n^2 2^n)`

## Knapsack Problem
