# Going in for the Interview
These are just some notes that I make to myself, going through interview resources:

- Cracking the Coding Interview
- Leetcode
- Hackerrank
- Firecode

I'll probably rename this something other than "data structures" because interviews can go over a ton of stuff.

## Index
| [Data Structures](/interviews/data-structures.md)   | [Algorithms](#)      | Concepts               |
|------------------------|----------------------|------------------------|
| Linked Lists           | Breadth-First Search | Bit Manipulation       |
| Trees, Tries, & Graphs | Depth-First Search   | Memory (Stack vs Heap) |
| Stacks & Queues        | Binary Search        | Recursion              |
| Heaps                  | Merge Sort           | Dynamic Programming    |
| Vectors/ArrayLists     | Quick Sort           | [Big O Time & Space](/interviews/time-complexity.mdg)     |
| Hash Tables            |                      |                        |

## Powers of 2
| Power of 2     | Exact Value (X)   | Approx Value | X Bytes into MB, GB, etc |
|----------------|-------------------|--------------|--------------------------|
| 2<sup>7</sup>  | 128               |              |                          |
| 2<sup>8</sup>  | 256               |              |                          |
| 2<sup>10</sup> | 1024              | 1 thousand   | 1 KB                     |
| 2<sup>16</sup> | 65,536            |              | 64 KB                    |
| 2<sup>20</sup> | 1,048,576         | 1 million    | 1 MB                     |
| 2<sup>30</sup> | 1,073,741,824     | 1 billion    | 1 GB                     |
| 2<sup>32</sup> | 4,294,967,296     |              | 4 GB                     |
| 2<sup>40</sup> | 1,099,511,627,776 | 1 trillion   | 1 TB                     |

## How to Answer a Technical Question
LABTOIW

1. **Listen** to problem, keep in mind *unique info*
2. **Draw** an example. Make sure it's sufficiently large, uses real mock data, and isn't a special case
3. **Brute Force** solution. Get something that works (kind of) ASAP. Don't worry about niceness, but know it's runtime complexity
5. **Optimize** using **BUD** Optimization Process. Forgot any info? Fresh Example? Time vs Space tradeoff? Precompute information? Hash table? Best concievable runtime?
6. **Walkthrough** Your approach in detail.
7. **Implement** using modularization (pretend methods). Todo-list for error checks.
8. **Test** conceptually, with small fresh cases, edge cases (ex: `null` and single elements).

## BUD Optimization Process
**B**ottlenecks

**U**nnecessary Work

**D**uplicated Work