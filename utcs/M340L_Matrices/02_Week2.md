# Week 2
Sections 1.3 - 1.5 in the text

## 1.3: Vector Equations

$\mathbb{R}^2$ = "r-two" = set of all vectors with 2 entries

- Matrix with only one column is a *column vector*
- Two vectors are *equal* iff their corresponding entries are all equal

### Vector Addition
$\overrightarrow{v}, \overrightarrow{w} \in \mathbb{R}^n$

$\overrightarrow{v} + \overrightarrow{w} =
\begin{bmatrix}
  {v_1 + w_1} \\
  {v_2 + w_2} \\
  ... \\
  {v_n + w_n} \\
\end{bmatrix}$

### Scalar Multiplication
$\overrightarrow{v} \in \mathbb{R}^n$, $c \in \mathbb{R}$

$\overrightarrow{v} + \overrightarrow{w} =
\begin{bmatrix}
  cv_1 \\
  cv_2 \\
  ... \\
  cv_n \\
\end{bmatrix}$

If {$\overrightarrow{v_1} \overrightarrow{v_2}, ..., \overrightarrow{v_k}$} are vectors in $\mathbb{R}^n$, a linear combination of these vectors is $a_1\overrightarrow{v_1} a_2\overrightarrow{v_2}, ..., a_k\overrightarrow{v_k}$, where $a_1, a_2, ..., a_k \in \mathbb{R}$

### Geometric Descriptions
For $\mathbb{R}^2$, $\begin{bmatrix} {a} \\ {b} \end{bmatrix}$ = $(a, b)$

If $u$ and $v$ are both in $mathbb{R}^2$, then $u + v$ is the fourth vertex of a parallelogram made with ${0, u, v}$

### Linear Combination
If `S` = {$\overrightarrow{v_1}, \overrightarrow{v_2}, ..., \overrightarrow{v_k}$} is a set of vectors in $\mathbb{R}^n$, then the **span** of `S`, denoted span `S` = span {$\overrightarrow{v_1}, \overrightarrow{v_2}, ..., \overrightarrow{v_k}$} is the set of all possible linear combinations of the vectors in `S`

$A\overrightarrow{x} = \overrightarrow{b}$

$A = \begin{bmatrix}
  a_11, ..., a_1n \\
  ..., ..., ... \\
  a_m1, ..., a_mn \\
\end{bmatrix}$

$a_11 x_1 + a_12 x_2 + ... + a_1n x_n = b_1$

$a_21 x_1 + a_22 x_2 + ... + a_2n x_n = b_2$

...

$a_m1 x_1 + a_m2 x_2 + ... + a_mn x_n = b_m$

$A\overrightarrow{x} = \begin{bmatrix} \overrightarrow{a_1}, \overrightarrow{a_2}, ..., \overrightarrow{a_n} \end{bmatrix} \begin{bmatrix}
  x_1 \\
  x_2 \\
  ... \\
  x_n \\
\end{bmatrix}$

$x_1\overrightarrow{a_1} + x_2\overrightarrow{a_2} + ... + x_n\overrightarrow{a_n}$

Solving the system $A\overrightarrow{x} = \overrightarrow{b}$ is the same as asking: "How can you write $\overrightarrow{b}$ as a linear combination of the $\overrightarrow{a}$s?" (if possible)

Or is $\overrightarrow{b} \in span \{\overrightarrow{a_1}, \overrightarrow{a_2}, ..., \overrightarrow{a_n}\}$

Is $\overrightarrow{b}$ in the span of the columns of $A$

### Geometric Description of Span{$v$} and Span{$u, v$}
Span is simply the expanded representation if you were to pretend that you had every or infinity and negative infinity scalars of $u$ or $u$ and $v$ in every direction.

So, for example, in 3D space, the span of just one vector is a line that goes on forever in both directions. The span of two vectors $u$ and $v$ is the plane in 3D space that contains the both of them.

## TFAE (The Following Are Equivalent)
Explanation: for the following list, either all of them are true or none of them are true:

- For every $\overrightarrow{b}$ in $\mathbb{R}^m$, $A\overrightarrow{x} = \overrightarrow{b}$ has a solution
- Each $\overrightarrow{b}$ in $\mathbb{R}^m$ is a linear combination of the columns of $A$
- The column of $A$ span $\mathbb{R}^m$
- $A$ has a pivot in every row

## Homogenous Systems
$A\overrightarrow{x} = \overrightarrow{0}$

A system where $\overrrightarrow{b} = 0$

$\overrightarrow{x} = \overrightarrow{0}$ always solves this system

Free variables >> nontrivial solutions <<>> don't have pivot in every column

No free variables >> only trivial solutions <<>> pivot in every column
