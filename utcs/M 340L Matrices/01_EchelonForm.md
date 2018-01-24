# Unit 1
Everything up until Exam 1

## 1.1: Systems of Linear Equations
General form for linear equations: $a_1x_1 + a_2x_2 + ... + a_nx_n = b$

> **Solution set:** set of all possible solutions
> 
> Two linear systems are **equivalent** if they have the same solution set

A system of linear equations has:
1. No solution
2. Exactly one solution
3. Infinitely many solutions

> **Coefficient matrix** contains coefficients
> 
> **Augmented matrix** adds in another column for the right side of the equation
> 
> A matrix's **size** = # rows x # columns = m x n (*matrix notation*)

### Solving a Linear System
One way: Eliminate a variable by subtracting it from the first equation

### Elementary Row Operations
1. (Replacement) Replace one row by the sum of itself and a multiple of another row2. (Interchange) Interchange two rows3. (Scaling) Multiply all entries in a row by a nonzero constant

> **Row equivalent**: there's a sequence of elementary row operations that transform one matrix into the other

Row operations are *reversible*

Augmented matrices of two linear systems are row equivalent >> two systems have the same solution set

### Existence and Uniqueness
1. Is the system *consistent* -- does at least one solution exist (can you put it into triangular form)?
2. If it does exist, is it the only one -- is the solution *unique*?

### Possible Solutions
1. **No solution** (inconsistent)
2. **Exactly one solution** (consistent)
3. **Infinitely many solutions** (consistent)

## Solving Linear Equations/Matrices

**Back subsitution**: working your way from the bottom back up to get an answer with matrices

### Echelon Form
1. The leading entry (1st nonzero element) in any given row is to the right of leading entries above it (reverse staircase)
2. Every # in a column below a leading entry is zero
3. Any rows of just 0s are below all other rows

### Reduced Row Echelon Form (RREF)
4. Every leading entry is one
5. Everything in a column above a leading entry is zero

- Leading 1s = "pivot" (column has "basic variable")
- No pivot >> column has "free variable")

- The row being changed gets written first
- Multiple row operations in the same step must be independent (don't effect each other)
- You can also multiply/divide a row by a constant, but try to *avoid introducing fractions* or you're in for a world of hurt! (still correct, but complicated)

"Forward phase of Gaussian elimination" >> putting into Echelon Form
"Backward phase of Gaussian elimination" >> putting into RREF

To double check: plug back into original, untouched problem

- For free variables in your equation, define the basic variables in relation to free variables and something like "z is free" or "z = s, $s \in \mathbb{R}$"
- Presence of free variables <<>> infinitely many solutions