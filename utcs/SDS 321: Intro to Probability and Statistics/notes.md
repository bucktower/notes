# Final Exam Review
SDS 321: Intro to Probability and Statistics

## Basics
**Sample space**: set of all possible outcomes of an experiment
**Event**: subset of sample space

### Sets
**Union**: $ \{1,2\} \cup \{2,3\} = \{1,2,3\} $

**Intersection**: $ \{1,2\} \cap \{2,3\} = \{2\} $

$ \{\{1,2\}, \{3\}, \{4,5\}\} $ is a **partition** of $ \{1,2,3,4,5\} $ and is **mutually exclusive**.

### Komolgrov's Axioms
1. $ 0 \leq P(E) \leq 1 $
2. $ P(S) = 1 $
3. $ P(\cup E_i) = \sum P(E_i) $ for events that are mutually exclusive

As a result:

- $ P(E^c) = 1 - P(E) $ where $ E^c $ is the complement of $ E $
- $ P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2) $
- $ P(E) = \frac{\#E}{\#S} $

### Important Sums
- $ \sum_{i = 1}^{n} i = \frac{n(n + 1)}{2} $
- $ \sum_{i = 1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} $
- $ \sum_{i = 0}^{n} a^i = \frac{1 - a^{n+1}}{1 - a} $
- $ \sum_{i = 0}^{\infty} a^i = \frac{1}{1 - a} $ if $ |a| < 1 $

#### Binomial Theorem
$ \sum_{i = 0}^{n} {n \choose i} a^{n-i}b^i = (a + b)^n $

Tip: $ {n \choose i} $ is the same as C(n,i)

## Basic Counting Principles
**Product rule**: if there are two tasks, with n<sub>1</sub> ways to do the first **and** n<sub>2</sub> ways to do the second, then there are n<sub>1</sub>n<sub>2</sub> ways to do the procedure.

**Sum rule**: if a task can be done either in n<sub>1</sub> ways **or** n<sub>2</sub> ways, then there are n<sub>1</sub>n<sub>2</sub> ways to do the task.

## Conditional and Total Probability
**Conditional Probability**:
$$
P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)P(B|A)}{P(B)}
$$
Rearrange the terms to get other equations, such as $P(A \cap B)$.

**Total Probability** (just apply Conditional Probability with the A<sup>C</sup>):
$$
P(B) = P(A \cap B) + P(A^C \cap B) = P(A)P(B|A) + P(A^C)P(B|A^C)
$$

## Independence
**Independent**: A and B are independent if $ P(B|A) = P(B) $; occurence of A provides no information about B's occurence

- $ P(A \cap B) = P(A) * P(B) $
- Applies even if $ P(A) = 0 $

Conditioning can effect independence:

![Independence Conditioning Example]()

If A and B are independent by themselves, yet we are told that C occurred, then A and B are *no longer independent*.

**Pairwise independence**: a set of random variables from which any two are independent -- *does not imply independence*

**Conditional independence**: $ P(A \cap B|C) = P(A|C) * P(B|C) $

## Permutations and Combinations
|                | Ordered      | Not Ordered |
|----------------|--------------|-------------|
| Replacement    | Product Rule |             |
| No Replacement | Permutation  | Combination |

### Permutation
Order matters, no replacement

$$
P(n,k) = \frac{n!}{(n-k)!}
$$

"How many ways are there of arranging...?"

### Combination
Order *doesn't* matter, no replacement

$$
C(n,k) = \frac{n!}{k!(n-k)!}
$$

"How many ways are there of selecting at once...?"

#### Stars and Bars/Bagels
Explains the Combination equation. Say you're buying 6 bagels of 4 types.

Stars = bagels, Bars = separator between types

Example assortment: * * | * | * | * *

6 stars (**n**) + 3 bars (**k**) = 9 symbols

How many possible assortments? C(n,k) = C(6,3) = 20 possible assortments

## Special Continuous Distributions
