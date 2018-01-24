# Unit 1
Everything up until Exam 1

## Table of Contents
toc

## 1.1: Stable Marriages
### Pseudocode
```pseudocode
Initially all m in M and w in W are freeWhile there is a man m who is free and hasn't proposed to every woman:    Choose such a man m    Let w be the highest-ranked woman in m's preference list
        to whom m has not yet proposed
    If w is free then        (m, w) become engaged    Else w is currently engaged to m'        If w prefers m' to m then
            m remains free        Else w prefers m to m'
            (m,w) become engaged
            m' becomes free        Endif
    EndifEndwhileReturn the set S of engaged pairs
```

### Proof that Marriages Algo Terminates
- Sequence of women whom a male proposes to gets worse and worse

If there are equal numbers of men (`m`) and women (`w`), then there are at most n^2 iterations of proposals

### Set `S` Returned at End is a Stable Matching
*If `m` is free, then there's a woman whom he hasn't proposed to*

**Proof:** Women remain free until they recieve their first proposal -- then they're always engaged. **This proves no man can "fall off" his preference list*

*Set `S` Returned at End is a Perfect Matching* ("perfect" => every man has a woman)

**Proof:** Then there must be a free man `m`, who must have proposed to every woman, else the while loop would have never terminated. But the previous proof contradicts that.

*Set `S` Returned at End is a Stable Matching*

**Proof**: Must involve 2 pairs. So say the pairs are: `m--w` and `m'--w'`. So `m` must favor `w'` and vice-versa. But if that's the case, then `m` would have proposed to `w'` at some earlier point before `w`

### Extensions
- Whoever proposes gets the better deal
- All executions yield the same matching
    - Every man gets the best partner he is able to obtain
    - Every woman gets the worst valid partner (lowest but still stable)

### How to Answer
*Is `{ ... }` stable matching?*

**No. Because `...` and `...` is a source of instability**

Proof by contradiction is useful

## 2.1: Computational Tractability
An algorithm is efficient if it has a polynomial running time

> Definition of $ f(n) \in O(g(n)) $:
> 
> $\exists c > 0 \ and \ n_0 > 0 \ \ s.t. \forall n > n_0 $:
> 
> We have $P(n) \leq c * g(n) $

Most important is the greatest factor, the rest can be played around with

### Growth Rates
Grows slowest to fastest

1 >> log(n) >> $ \sqrt n $ >> n >> n log(n) >> n^2 >> n^3 >> ... >> 2^n >> c^n >> n! >> n^n

### Algorithm Analysis
1. Deterministic
2. Correctness
3. Efficiency

Factors that effect efficiency:

1. Size of input (# of objs -- for now)
2. Primitive operations
    - Operations whose # dominating total # of operations
    - *Ex: # of comparison opertaions in sorting*

## 2.2: Asymptotic Order of Growth
T(n) = O(f(n)) >> f(n) is *asymptotically upper-bounded* by T(n)

T(n) = $\Omega$(f(n)) >> f(n) is *asymptotically lower-bounded* by T(n)

**Only if O(f(n)) == $\Omega$(f(n)):**

T(n) = $\Theta$(f(n)) >> f(n) is *asymptotically tight-bounded* by T(n)

### Properties

#### Transitivity
If a function `f(n)` is asymptotically upper-bounded by `g(n)` and `g(n)` is asymptotically upper-bounded by `h(n)`, then `f(n)` is also upper-bounded by `h(n)`.

Same with lower bounds.

#### Sums of Functions
An upper-bound of two functions is still the upperbound of their sum

### Asymptotic Bounds for Some Common Functions

#### Polynomials
- Polynomials' rate of growth is determined by high-order term
- *Polynomial time algorithm* >> runtime is O(n^(d)) for some constant `d` that's independent of input
    - Remember, Big Os can scale up past tightest bound (O(n log(n)) has polynomial time)

#### Logarithms
Base of the log isn't important when writing bounds.

#### Exponentials
Somewhat sloppy, but exact variables in exponents don't matter too much. For the most part: "This algorithm is exponential" will suffice.