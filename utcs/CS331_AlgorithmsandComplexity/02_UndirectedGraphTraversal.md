# Undirected Graph Traversal

## Table of Contents
[TOC]

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

n^0.999 * log(n) vs. n
= n^0.999 * log(n) vs. n^0.999 * n^0.001

### Graphs
**dense**: # of edges close to max # of edges
**sparse**: # of edges NOT close to max # of edges

| Dense | *middle ground* | Sparse |
| --- | --- | --- |
| $ m = \frac{n(n-1)}{2} $ | | $ m = 0 $ |

Using lists to store graphs:

- `n` = # vertices, `m` = # edges
- Space: `n` + 2`m` >> O(`n` + `m`)
- Time-to-read: O(`n` + `m`)

## Campsite
Imagine trying to travel from Point A to Point B. You have to use several campsites along the way, and you can only hike a max set distance each day.

Prove that the greedy algorithm is optional.

$(p_1, p_2, ..., p_k)$ representing the campsites that you stop @ $(ex:\ p_1 = x_2, p_2 = x_7, p_k = x_n)$

Number of stops = $k$

### Black Box
(proof by contradiction, assume $q$s are better than $p$s)

If $l < k$, then you would have to travel further each day then k (skipping some of the campsites)

### Assume $q$ Strategy is Better

#### Base Case
On Day 1

$x_{p_1} \geq x_{q_1}$

Prove $x_{p_k} > x_{q_k}$

On the last day, you should be able to get from final campsite $(B - p_x)$