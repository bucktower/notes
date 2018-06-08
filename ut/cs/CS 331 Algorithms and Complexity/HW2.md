# Homework #2
From discussion section (2/2/18)

## Problem 1
T is a tree where every non-leaf node has 2 children and every leaf node has the same depth ($d$)

* Basically a full binary tree
* Want $2^{d+1} - 1$ total nodes in $T$
* In the tree, there are $d + 1$ layers

### Base Case
$$d = 1$$

### Inductive Hypothesis
When $d = k$ in $T$, there are $2^{k+1} - 1$ nodes

### Inductive Step
$d = k + 1$: some node $l$ that was leaf in $T_k$ now has a child

* $l$ actually has 2 children
* all leaf nodes must have 2 children

**Theorem**: a tree with structure $T$ and depth $k$ has $2^k$ leaf nodes

**Lemma**: in any tree with structure $T$, layer $L$ has $2^l$ nodes -- this is much easier to prove than the theorem:

#### Proof by Induction
**Base Case**: $l = 0$ (the root node)

**Inductive Hypothesis**: layer $k$ has $2^k$ nodes

**Inductive C**: Assume at least one of these layer $k$ nodes has a child layer $k$ has $2^{k + 1}$ nodes

Take arbitrary $d$

Consider $T$ with depth $d$

Every node in $T$ belongs to exactly 1 layer

No node in a layer is not $T$

Then nodes in $T = \displaystyle\sum_{l = 0}^{d} n_l = \displaystyle\sum_{l = 0}^{d} 2^l = 2^{d + 1} - 1$

$n_l$ = number of nodes in layer $l$

Question: How many different shortest paths from $s$ to $d$ in $O(V + E)$