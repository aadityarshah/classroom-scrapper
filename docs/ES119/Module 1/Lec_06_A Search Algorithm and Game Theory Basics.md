---
title: A* Search Algorithm and Game Theory Basics
lecture_number: 6
lecture_name: A* Search Algorithm and Game Theory Basics
category: 'Module 1: Search and Planning'
sidebar_label: Lecture 6
sidebar_position: 6
course: 'ES119: Principles of AI'
topic:
- A* Search
- Heuristics
- Admissibility
- Consistency
- Multi-Agent Systems
- Adversarial Search
- Game Trees
- Min-max Algorithm
tags:
- AI
- Search
- Pathfinding
- Heuristic Search
- Game Theory
- Adversarial Games
- Minimax
summary: This lecture introduces the A* search algorithm, detailing its components
  $g(n)$ and $h(n)$, and the conditions for its optimality (admissibility and consistency
  of heuristics). It then transitions into multi-agent systems, focusing on two-agent
  adversarial settings and the Min-max search algorithm for decision-making in such
  environments.
math: true
---


# A* Search Algorithm

The A\* search algorithm is a cornerstone of pathfinding and graph traversal, widely used in artificial intelligence and computer science for its efficiency and optimality under certain conditions. It builds upon ideas from Breadth-First Search (BFS) and Dijkstra's algorithm by incorporating a heuristic function to guide its search more effectively.

## How A\* Modifies BFS

BFS is an uninformed search algorithm that expands nodes uniformly, typically by depth. A\* fundamentally improves upon BFS by expanding nodes based on an estimated total cost.

The key differences are:
*   **Expansion Criterion:** BFS expands nodes purely by depth (or uniform cost for unweighted graphs); A\* expands nodes based on an estimated total cost, $f(n)$.
*   **Cost Function:** For any node $n$, A\* uses a cost function $f(n)$ defined as:
    $$f(n) = g(n) + h(n)$$
    where:
    *   $g(n)$: The actual cost from the start node to the current node $n$. This is the "cost so far".
    *   $h(n)$: The estimated cost (heuristic) from the current node $n$ to the goal node. This represents the "promising future" cost.
*   **Data Structure:** BFS uses a First-In, First-Out (FIFO) queue, expanding the oldest unvisited node. A\* replaces this with a **priority queue**, ordered by the $f(n)$ value. Nodes with lower $f(n)$ values are prioritized for expansion.
*   **Exploration Bias:** BFS explores uniformly in all directions from the start. A\* biases its exploration toward the goal using the heuristic, making it a *best-first search* algorithm.
*   **Efficiency:** While both store parent pointers and visited states (bookkeeping), A\* typically reaches the goal with far fewer node expansions than BFS (especially for large search spaces), due to its informed guidance.

## Components of A\* Search

A "good path" in A\* search is one with a low cost so far ($g(n)$) and a promising future ($h(n)$). The algorithm continuously explores or dequeues nodes that have the minimum $f(n)$ value.

### Cost from Start: $g(n)$
$g(n)$ represents the actual cost incurred to reach node $n$ from the start node. This is a sum of edge weights along the path found so far. If multiple paths exist to $n$, $g(n)$ stores the minimum cost found.

### Heuristic Estimate: $h(n)$
$h(n)$ is an estimate of the cost from node $n$ to the goal. It must be an optimistic estimate, meaning $h(n)$ must always be less than or equal to the true minimum cost from $n$ to the goal.
A common example of $h(n)$ is the **straight-line distance (Euclidean distance)**, often referred to as "as the crow flies" distance, used in navigation systems like Google Maps. For a grid-based search, Manhattan distance can also be an admissible heuristic.

## Optimality of A\*

A\* is guaranteed to find the optimal path (the path with the lowest total cost) if two conditions are met concerning its heuristic function:

### Admissible Heuristic
An heuristic $h(n)$ is **admissible** if, for every node $n$, the estimated cost $h(n)$ is less than or equal to the true minimum cost $h^*(n)$ from $n$ to the goal node.
$$h(n) \le h^*(n) \quad \forall n$$
If an A\* search uses an admissible heuristic, it is guaranteed to find an optimal path to the goal. This is because it never overestimates the cost to the goal, ensuring that an optimal path will eventually be considered before any suboptimal path that might appear cheaper due to an inflated heuristic.

### Consistent Heuristic (Monotonicity)
An heuristic $h(n)$ is **consistent** (or monotonic) if, for every node $n$ and every successor node $n'$ of $n$, the estimated cost $h(n)$ is less than or equal to the cost of moving from $n$ to $n'$ plus the estimated cost from $n'$ to the goal.
$$h(n) \le c(n,n') + h(n') \quad \forall n \to n'$$
where $c(n,n')$ is the actual cost of the edge from $n$ to $n'$.
A consistent heuristic is always admissible. Furthermore, if the heuristic is consistent, A\* performs even better by never having to reopen nodes (i.e., finding a cheaper path to an already expanded node), which simplifies implementation and improves efficiency in certain scenarios.

---

# Multi-Agent Systems

Moving beyond single-agent pathfinding, many real-world AI problems involve **Multi-Agent Systems (MAS)**. These systems consist of more than one intelligent agent interacting within an environment.

Key characteristics and considerations in Multi-Agent Systems include:
*   **Multiple Agents:** The presence of several autonomous entities.
*   **Environment:** The shared space or context in which agents operate and interact.
*   **Cooperation vs. Competition:** Agents might work together towards a common goal (cooperation) or against each other with conflicting objectives (competition).
*   **Perfect vs. Imperfect Information:** Agents may have full knowledge of the environment and other agents' states (perfect information) or only partial and uncertain knowledge (imperfect information).
*   **Examples:** Multi-agent systems are found in various applications, from robot teams and traffic control to complex game environments like Atari games, where multiple characters (controlled by AI or players) interact.

## Two-Agent Systems: Adversarial Search

A specific and important type of multi-agent system is the **two-agent system** operating in an **adversarial setting**. These are often modeled as **two-player zero-sum games**, where one agent's gain is exactly another agent's loss (e.g., chess, checkers).

The formal definition of an adversarial game typically includes:
*   **Initial State ($S_0$):** The starting configuration of the game.
*   **Player(s):** A function that defines which player has the move in a given state $s$.
*   **Action(s):** A function that returns the set of legal moves available in state $s$.
*   **Transition Model ($T(s,a)$ or $Result(s,a)$):** A function that describes the state resulting from performing action $a$ in state $s$.
*   **Terminal Test ($Terminal\_Test(s)$ or $G(s)$):** A function that determines if a state $s$ is a terminal (game-over) state.
*   **Utility ($Utility(s,p)$):** A function that assigns a numerical value to a terminal state $s$ from the perspective of player $p$. In zero-sum games, if player 1's utility is $X$, player 2's utility is $-X$.

## Game Trees and Min-max Search

Adversarial games are often represented using **game trees**, where nodes represent game states and edges represent moves. The root is the initial state, and branches extend for all possible moves, creating subsequent states. Leaf nodes represent terminal states with associated utility values.

The **Min-max Search** algorithm is a decision-making strategy for two-player zero-sum games with perfect information. It aims to choose the best move for the current player, assuming the opponent will also play optimally.

*   **Maximizer (MAX) Player:** The current player (e.g., Player A in the slides) seeks to maximize their utility.
*   **Minimizer (MIN) Player:** The opponent (e.g., Player B in the slides) seeks to minimize the MAX player's utility (which is equivalent to maximizing their own utility in a zero-sum game).

The Min-max algorithm recursively explores the game tree:
1.  **Terminal States:** For leaf nodes (terminal states), the utility values are assigned.
2.  **Minimizer Levels:** For nodes where it's the MIN player's turn, the value of the node is the minimum of the values of its children.
3.  **Maximizer Levels:** For nodes where it's the MAX player's turn, the value of the node is the maximum of the values of its children.
4.  **Root Value:** The process propagates values up the tree until the root, where the MAX player chooses the action leading to the child with the highest value.

### Min-max Algorithm Complexity
Implementing a full Min-max search typically uses a Depth-First Search (DFS) approach to explore the tree.
*   **Time Complexity:** $O(b^m)$, where $b$ is the branching factor (average number of legal moves from a state) and $m$ is the maximum depth of the game tree. This exponential complexity makes Min-max intractable for games with large $b$ or $m$ (e.g., chess).
*   **Space Complexity:** $O(bm)$ for storing the game tree and states during DFS traversal.

Due to its high computational cost, pure Min-max search is often enhanced with techniques like Alpha-Beta Pruning, which drastically reduces the number of nodes evaluated without affecting the final decision.

## Quick Summary

This lecture covered the A\* search algorithm, highlighting its improvements over BFS by using an estimated total cost $f(n) = g(n) + h(n)$. We defined $g(n)$ as the cost from the start and $h(n)$ as an admissible (optimistic) heuristic estimate to the goal. The optimality of A\* relies on the admissibility and consistency of its heuristic. We then transitioned to multi-agent systems, specifically two-player zero-sum adversarial games. The components of such games were outlined, leading to an introduction to game trees and the Min-max search algorithm, which allows an agent to make optimal decisions against an optimal opponent by evaluating future game states. The exponential time complexity of Min-max was also noted.
