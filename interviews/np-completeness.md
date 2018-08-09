# NP-Completeness Time Complexity

[What is NP Complete?](https://stackoverflow.com/questions/210829/what-is-an-np-complete-in-computer-science)

![NP Completness chart](https://en.wikipedia.org/wiki/NP-completeness#/media/File:P_np_np-complete_np-hard.svg)

Most of the time, people assume P \neq NP

- `P`: Set of all decision problems which can be **solved** (and therefore **verified**) in *polynomial time* by a *deterministic Turing machine*
- `NP`: Set of all decision problems which can be **verified** in *polynomial time* by a *deterministic Turing machine*
- `NP-Complete`: Problem is in NP, and every problem in NP is *reducible* to it
  - If any one of the NP Complete problems was to be solved "quickly" (in polynomial time), then all NP problems can be solved "quickly"
- `NP-Hard`: Set of all problems at least as hard as the hardest problems in NP (in other words, `NP-Complete` or harder)
  - Some of these problems aren't actually in NP

