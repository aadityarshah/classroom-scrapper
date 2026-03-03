---
title: 'BFS, DFS, and A* Search'
lecture_number: 5
lecture_name: 'Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search Algorithm'
category: 'Module 1: Search and Planning'
sidebar_label: 'Lecture 5'
sidebar_position: 5
course: 'ES119: Principles of AI'
topic:
  - Search Algorithms
  - Uninformed Search
  - Informed Search
  - Heuristics
tags:
  - BFS
  - DFS
  - A* Search
  - Graph Traversal
  - Tree Traversal
  - Uninformed Search
  - Informed Search
  - Heuristic Search
  - Admissible Heuristic
  - Consistent Heuristic
  - Time Complexity
  - Space Complexity
summary: 'This lecture delves into fundamental tree and graph traversal algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS). We examine their mechanics, data structures, and analyze their time and space complexities. The lecture then introduces A* Search, an informed search algorithm, explaining how it enhances BFS by incorporating heuristic knowledge to find optimal paths more efficiently. Key concepts of admissible and consistent heuristics are also discussed.'
math: true
---

# Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search

Welcome to Lecture 5 of ES119: Principles of AI. Today, we delve into foundational search algorithms crucial for navigating problem spaces: Breadth-First Search (BFS) and Depth-First Search (DFS), and then introduce A\* Search, an intelligent improvement.

## 1. Tree and Graph Traversal Fundamentals

To solve many AI problems, we represent the problem as a search space, often a tree or a graph, and then traverse this structure to find a goal state. The manner in which we "read" or explore this structure defines our search strategy.

### 1.1 Breadth-First Search (BFS)

Breadth-First Search (BFS) is an uninformed search algorithm that explores all the neighbor nodes at the present depth level before moving on to nodes at the next depth level. It systematically expands the shallowest unexpanded node first.

#### 1.1.1 Mechanism: Queue (FIFO)
BFS employs a **queue** data structure, which operates on a **First-In, First-Out (FIFO)** principle.
*   **Enqueue:** Nodes are added to the end of the queue.
*   **Dequeue:** Nodes are removed from the beginning of the queue for expansion.

The algorithm proceeds as follows:
1.  Initialize a queue with the starting node.
2.  Initialize a `visited` set to keep track of explored nodes.
3.  While the queue is not empty:
    a.  Dequeue a node $N$.
    b.  If $N$ is the goal, return the path.
    c.  Mark $N$ as visited.
    d.  For each unvisited neighbor $M$ of $N$:
        i.  Add $M$ to the queue.
        ii. Mark $M$ as visited (or add to `frontier` to avoid redundant additions).

#### 1.1.2 Characteristics of BFS
*   **Completeness:** BFS is complete. If a solution exists, BFS is guaranteed to find it, provided the branching factor is finite.
*   **Optimality:** BFS is optimal if all edge costs are uniform (e.g., unit cost). It finds the shallowest goal state, which in a uniform-cost graph, corresponds to the optimal path. For non-uniform costs, it is not necessarily optimal; uniform-cost search is a generalization for that scenario.

#### 1.1.3 Complexity Analysis of BFS
Let $b$ be the **branching factor** (maximum number of successors for any node) and $d$ be the **depth of the shallowest goal node**.

*   **Time Complexity:** In the worst case, BFS expands all nodes up to depth $d$. The number of nodes at depth $k$ is $b^k$.
    The total number of nodes expanded is $1 + b + b^2 + \dots + b^d$. This sum is $O(b^d)$.
    $$ \text{Time Complexity} = O(b^d) $$
    This exponential growth can be prohibitive for large search spaces.
*   **Space Complexity:** BFS must store all nodes in the queue at the current depth level, as well as the nodes generated for the next level. In the worst case, this means storing $O(b^d)$ nodes.
    $$ \text{Space Complexity} = O(b^d) $$
    Space is often a more significant limitation than time for BFS in practice.

### 1.2 Depth-First Search (DFS)

Depth-First Search (DFS) is an uninformed search algorithm that explores as far as possible along each branch before backtracking. It dives deep into the search tree.

#### 1.2.1 Mechanism: Stack (LIFO)
DFS employs a **stack** data structure, which operates on a **Last-In, First-Out (LIFO)** principle.
*   **Push:** Nodes are added to the top of the stack.
*   **Pop:** Nodes are removed from the top of the stack for expansion.

The algorithm proceeds as follows:
1.  Initialize a stack with the starting node.
2.  Initialize a `visited` set.
3.  While the stack is not empty:
    a.  Pop a node $N$.
    b.  If $N$ is the goal, return the path.
    c.  If $N$ has not been visited:
        i.  Mark $N$ as visited.
        ii. For each unvisited neighbor $M$ of $N$ (often in reverse order of generation to ensure a consistent exploration order):
            1.  Push $M$ onto the stack.

#### 1.2.2 Characteristics of DFS
*   **Completeness:** DFS is not complete in infinite search spaces or spaces with cycles (unless modified to keep track of visited states). If the search space is finite and acyclic, it is complete.
*   **Optimality:** DFS is not optimal. It may find a non-optimal path to the goal, even if a shorter or lower-cost path exists, because it explores one branch fully before exploring others.

#### 1.2.3 Complexity Analysis of DFS
Let $b$ be the **branching factor** and $m$ be the **maximum depth** of the search space (which could be much larger than $d$, the depth of the shallowest goal).

*   **Time Complexity:** In the worst case, DFS may explore the entire search space up to depth $m$.
    $$ \text{Time Complexity} = O(b^m) $$
    If the goal is at a very deep level and located early in the ordering of children, DFS can be very efficient. However, if the goal is shallow but located in a branch explored late, or if the search space is very deep, it can be extremely inefficient.
*   **Space Complexity:** DFS only needs to store the nodes on the current path from the root to the current node, plus the unexplored sibling nodes at each level. Thus, the space requirement is linear with respect to the maximum depth.
    $$ \text{Space Complexity} = O(b \cdot m) $$
    This is a significant advantage over BFS for problems with very deep but narrow search spaces.

## 2. Comparison of BFS and DFS

A summary of the key differences:

| Metric         | BFS                   | DFS                   |
| :------------- | :-------------------- | :-------------------- |
| **Data Structure** | Queue (FIFO)          | Stack (LIFO)          |
| **Completeness** | Yes (finite $b$)      | No (infinite paths/cycles without visited set), Yes (finite, acyclic) |
| **Optimality** | Yes (uniform costs)   | No                    |
| **Time Complexity** | $O(b^d)$              | $O(b^m)$              |
| **Space Complexity** | $O(b^d)$              | $O(bm)$               |

The choice between BFS and DFS depends heavily on the characteristics of the problem and the search space. If the depth of the solution is known to be small, BFS is preferred. If the search space is very deep and solutions are expected to be deep, DFS can be more space-efficient.

## 3. Introduction to A* Search

While BFS guarantees optimality for uniform costs and completeness, its exponential space complexity $O(b^d)$ makes it impractical for many real-world problems. This leads us to **informed search** algorithms, which leverage problem-specific knowledge to guide the search. A\* Search is one of the most widely used and efficient informed search algorithms.

### 3.1 Motivation: Improving BFS
BFS expands nodes purely based on their depth. A\* improves upon this by using an **estimated total cost** to guide its node expansion, aiming to reach the goal faster and more directly.

### 3.2 The Evaluation Function $f(n)$
A\* evaluates each node $n$ using an evaluation function $f(n)$, which is an estimate of the cheapest path from the start node through $n$ to the goal.
$$ f(n) = g(n) + h(n) $$

*   **Cost from Start: $g(n)$**
    *   $g(n)$ is the **actual cost** from the start node to node $n$. This is the sum of the edge costs along the path found so far from the start to $n$.
*   **Heuristic Estimate: $h(n)$**
    *   $h(n)$ is the **estimated cost** (or heuristic) from node $n$ to the goal. This function provides an informed guess about how "close" node $n$ is to the goal. For example, in a navigation problem, $h(n)$ could be the straight-line distance (as the crow flies) from $n$ to the goal.

### 3.3 A* Mechanism: Priority Queue
Instead of a FIFO queue (like BFS) or LIFO stack (like DFS), A\* uses a **priority queue**. Nodes are ordered in the priority queue based on their $f(n)$ values, with the node having the lowest $f(n)$ value being expanded next. This strategy ensures that A\* always explores the path that currently appears most promising.

### 3.4 Key Properties of Heuristics

The effectiveness and optimality of A\* heavily depend on the quality of its heuristic function $h(n)$.

#### 3.4.1 Admissibility
A heuristic $h(n)$ is **admissible** if, for every node $n$, the estimated cost $h(n)$ is always less than or equal to the true cost $h^*(n)$ to reach the goal from $n$.
$$ h(n) \le h^*(n) \quad \forall n $$
An admissible heuristic is **optimistic**; it never overestimates the true cost. If $h(n)$ is admissible, A\* is guaranteed to find an optimal path to the goal, provided that $g(n)$ accurately reflects the true cost from the start and edge costs are non-negative.

#### 3.4.2 Consistency (or Monotonicity)
A heuristic $h(n)$ is **consistent** if, for every node $n$ and every successor $n'$ reachable from $n$ with step cost $c(n, n')$, the estimated cost $h(n)$ is less than or equal to the sum of the step cost $c(n, n')$ and the estimated cost from $n'$ to the goal $h(n')$.
$$ h(n) \le c(n, n') + h(n') \quad \forall n \to n' $$
Consistency implies admissibility (assuming $h(\text{goal})=0$). A consistent heuristic prevents A\* from rediscovering worse paths to an already expanded node, thereby simplifying its implementation and guaranteeing optimal paths when combined with a closed list (visited set).

### 3.5 Optimality of A*
A\* search is **optimal** and **complete** under certain conditions:
*   **Completeness:** A\* is complete if the branching factor $b$ is finite and all edge costs are positive (not zero) or bounded below by some small positive constant.
*   **Optimality:** A\* is optimal if the heuristic $h(n)$ is **admissible** (for tree search) or **admissible and consistent** (for graph search where nodes might be revisited via different paths).

A\* effectively balances the need to minimize the path cost so far ($g(n)$) with the need to reach the goal quickly ($h(n)$). By prioritizing nodes with the lowest $f(n)$, it biases its exploration towards the goal, significantly reducing the number of nodes expanded compared to uninformed search.

## Quick Summary

*   **Breadth-First Search (BFS)** explores layer by layer, is complete and optimal for uniform costs, but has exponential time and space complexity ($O(b^d)$). It uses a FIFO queue.
*   **Depth-First Search (DFS)** explores deeply along one path before backtracking, is space-efficient ($O(bm)$), but not complete or optimal. It uses a LIFO stack.
*   **A\* Search** is an informed search algorithm that uses an evaluation function $f(n) = g(n) + h(n)$ to guide its exploration.
    *   $g(n)$ is the actual cost from start to $n$.
    *   $h(n)$ is the estimated cost from $n$ to goal (heuristic).
*   A\* uses a priority queue ordered by $f(n)$.
*   A\* is complete and optimal if its heuristic $h(n)$ is **admissible** ($h(n) \le h^*(n)$) and **consistent** (satisfies triangle inequality).
*   Heuristics provide powerful guidance, enabling A\* to find optimal paths much more efficiently than uninformed methods in large search spaces.