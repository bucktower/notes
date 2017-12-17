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

## Special Continuous Distributions
