# Data Structures Notes
These are just some notes that I make to myself, going through interview resources:

- Cracking the Coding Interview
- Leetcode
- Hackerrank
- Firecode

I'll probably rename this something other than "data structures" because interviews can go over a ton of stuff.

## Table of Contents
1. [Time Complexity](#Time Complexity)

## Time Complexity
![Time complexity graph](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Comparison_computational_complexity.svg/250px-Comparison_computational_complexity.svg.png)

Constants (like O(2N)) and non-dominant terms (like O(N<sup>2</sup> + N)) are irrelevant. Except for exponents (2<sup>n</sup> vs 8<sup>n</sup>)

"Do this *then* do that" => Add

"Do this *whenever* you do that" => Multiply

### Big O
These are the most common time complexities:

> **O(1) > O(log(N)) > O(N) > O(N log(N)) > O(N<sup>2</sup>) > O(2<sup>N</sup>)**

Big O represents the **worst case**/slowest on runtime.

**Expected case** is what we expect on any given run. For most algorithms, it's the same as the worst case.

#### Amortized Time
Sometimes, it's important to note that the worst doesn't always happen, such as inserting in an Array List (resizing only happens so often).

Because of resizing, Big O of inserting in an Array List is O(N), but the **amortized time** is O(1).

Once the worst case happens, the amortized time will be the new expected case so long as the cost is *amortized*.

#### Log(N) Runtimes
Usually suggests binary something (like binary search) where something is getting halved. N represents nodes, not depth.

Sorting a 2D list typically takes **O(N log(N))** times.

#### Multiple Inputs
Don't use N. For example if your arrays have different lengths, **a** and **b**, a nested loop with both would be **O(ab)** not O(N)

### Big Omega Ω
Big Ω represents the **best case**/fastest for runtime.

### Big Theta Θ
Only for programs that are the same for Big O and Big Ω. So if a program has O(N) and Ω(N)

## Space Complexity
Similar principles of Big O, Big Ω, and Big Θ from above

An square 2D array of size NxN requires O(N<sup>2</sup>) space. Also applicaple to stack space (mostly only relevant with recursion).