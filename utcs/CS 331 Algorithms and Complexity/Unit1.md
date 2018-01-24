# Unit 1
Everything up until Exam 1

## Table of Contents
[TOC]

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

## 3.1: Graphs Basic Definitions and Applications
- Graphs are a collection of nodes and edges
- Edges are described as a two-element subset `e = {u, v}` where `u` and `v` are *ends* of `e`
- Graphs can have directed edges: `e = (u, v)`
    - If this is the case, `u` and `v` are not interchangeable
    - "`e` leaves node `u` and enters node `v`"
- Not directed = *undirected*
- `()` indicates directed or (casually) undirected (ordered pair), `{}` (formally, correctly) indicates undirected
- "node" = "vertex"

### Paths
- Undirected graph is *connected* if for every pair of nodes `u` and `v`, there is a path from `u` to `v`
- Directed graph is *strongly connected* if for every path `u` to `v` there is also a path `v` to `u`
- *distance* between two nodes is the min # of edges between them

### Trees
- Undirected graph is a tree if it is connected and does not contain a cycle
- Grab a particular node to serve as the "root"
- Parent of a node is the node that precedes it coming from the root (the node would be the child of the parent)
- Descendants can lie anywhere on the lineage from the root

#### Truths
Every `n`-node tree has exactly `n - 1` edges

Let `G` be an undirected graph on `n` nodes. Any two of the following implies the third:

1. G is connected
2. G does not contain a cycle
3. G has `n - 1` edges

## 3.2: Graph Connectivity and Graph Traversal
Trying to determine whether there's a path from `s` to `t` nodes in a graph:

### Breadth-First-Search (BFS)
"Flood": move to all connected nodes every level until no new nodes have been reached

The tree produced from BFS starting at some root is called a *breadth-first search tree*

> **Truth**: In running a BFS on a graph, all nontree edges are either connected nodes in the same layer or connected nodes in adjacent layers

#### Connected Components
**Connected component**: set of nodes discovered by the BFS algorithm

To check if `t` is connected to root, we just check if it belongs to the connected component

### Depth-First-Search (DFS)
"Maze": explore as deeply as possible to new nodes until you reach a dead-end, then backtrack until there's another new node and continue

> **Truth**: For a given recursive call of DFS(u), all nodes that are marked "explored" between the invocation and end of this recursive call are descendants of u

#### Set of All Connected Components
> **Truth**: For any two nodes `s` and `t` in a graph, their connected components are either identical or disjoint

## 3.3: Implementing Graph Traversal Using Queues and Stacks
2 basic ways for representing a graph:

1. Adjacency matrix
    - `n` x `n` matrix `A` where `A[u, v]` = 1 if the graph contains the edge `(u, v)` and 0 otherwise
    - Advantage: check in O(1) time if a given edge (u, v) is present
    - Disadvantage: space-efficiency is O(n^2)
2. Adjacency list
    - A 2D list, where `Adj[v]` gives back a list containing all nodes adjacent to node `v`
    - Advantage: requires O(`m` + `n`) space (`n` nodes, `m` connections per node, each edge appears in exactly two of the lists). Total length of all lists is 2`m` = O(`m`)

- *Degree* of a node is # of incident edges it has
    - Total length over all nodes = 2`m`

Graphs are often stored as doubly linked list -- question is whether it's a queue (FIFO) (BFS) or stack (LIFO) (DFS)

## 3.4: Testing Bipartiteness: An Application of Breadth-First Search
**Bipartite graph**: one where node set V can be partitioned into sets `X` and `Y` s.t. every edge has one end in `X` and the other end in `Y`

> **Truth**: If a graph is bipartite, then it cannot contain an odd cycle

> **Truth**: If `G` is a connected graph, then one of the two must be true:
> 
> 1. There is no edge of `G` joining two nodes of the same layer. `G` is a bipartite graph in which the nodes in even-numbered layers can be red, and odd-numbered can be blue
> 2. There IS an edge of `G` joining two nodes of the same layer. `G` contains an odd-length cycle and is therefore not bipartite