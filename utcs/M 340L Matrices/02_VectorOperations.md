# Vector Operations

## Vector Addition
$\overrightarrow{v}, \overrightarrow{w} \in \mathbb{R}^n$

$\overrightarrow{v} + \overrightarrow{w} =
\begin{bmatrix}
  {v_1 + w_1} \\
  {v_2 + w_2} \\
  ... \\
  {v_n + w_n} \\
\end{bmatrix}$

## Scalar Multiplication
$\overrightarrow{v} \in \mathbb{R}^n$, $c \in \mathbb{R}$

$\overrightarrow{v} + \overrightarrow{w} =
\begin{bmatrix}
  cv_1 \\
  cv_2 \\
  ... \\
  cv_n \\
\end{bmatrix}$

If {$\overrightarrow{v_1} \overrightarrow{v_2}, ..., \overrightarrow{v_k}$} are vectors in $\mathbb{R}^n$, a linear combination of these vectors is $a_1\overrightarrow{v_1} a_2\overrightarrow{v_2}, ..., a_k\overrightarrow{v_k}$, where $a_1, a_2, ..., a_k \in \mathbb{R}$

## Linear Combination
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
