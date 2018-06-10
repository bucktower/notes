# Directed Graph Traversal

## Table of Contents
[TOC]

## 3.5: Connectivity in Directed Graphs
**Strong connectivity** - two directed edges going opposite ways between two nodes (the nodes are *mutually reachable*)

- Points can be mutually reachable if they run along a path through others that are also all mutually reachable

## 3.6: Directed Acyclic Graphs and Topological Ordering
**DAG** - *directed acyclical graph*; a directed graph with no cycles

**Topological ordering** - an ordering through all nodes of the tree where every node points forward

Topological ordering <=> DAG

### How to Create a Topological Ordering
Delete nodes from a DAG one-by-one until there are none left (where the node that you're currently deleting has no edges towards it)