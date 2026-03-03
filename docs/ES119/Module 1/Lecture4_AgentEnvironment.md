---
title: "Agent and Environment Representation for Pathfinding"
lecture_number: 4
lecture_name: "Agent and Environment Representation for Pathfinding"
category: 'Module 1: Search and Planning'
sidebar_label: 'Lecture 4'
sidebar_position: 4
course: "ES119: Principles of AI"
topic:
  - Agent Characteristics
  - Environment Types
  - Search Problem Formulation
  - State Space Representation
  - Search Trees
tags:
  - AI
  - Search
  - Pathfinding
  - Agents
  - Environment
  - State Space
  - Problem Formulation
  - Tree Traversal
summary: "This lecture introduces the foundational concepts of agent-environment interaction in the context of pathfinding problems. It details how real-world applications are modeled by defining environment characteristics, agent objectives, states, actions, transition models, goal tests, and path costs. The lecture further explains how these problem formulations lead to the concept of a search tree, defining its components and introducing basic tree traversal strategies like Breadth-First Search (BFS) and Depth-First Search (DFS)."
math: true
---

## Introduction to Pathfinding Applications

Pathfinding is a fundamental problem in Artificial Intelligence, with widespread applications across various domains. It involves finding an optimal sequence of actions or states to navigate from a starting point to a destination. Consider the following real-world examples:

*   **Warehouse Robots:** Autonomous robots in large warehouses require efficient, collision-free paths to transport items, optimizing travel time and avoiding congestion.
*   **Hospitality Robots:** Service robots in hotels or hospitals need to navigate safely among humans, delivering services with comfort, safety, and social awareness.
*   **Drones:** Rescue or delivery drones must plan energy-efficient and safe 3D trajectories to reach targets, often operating under uncertainty and environmental constraints.
*   **Google Maps/Navigation Systems:** These systems compute the fastest routes by minimizing travel time under dynamic conditions like changing traffic.

Each of these applications presents unique challenges and requires a specific understanding of the agent and its environment to formulate an effective pathfinding solution.

## Agent-Environment Interactions and Problem Characteristics

To approach any pathfinding problem, it's crucial to characterize the environment and the agent's objectives. Different environments necessitate different problem-solving strategies. We can classify environments based on several key characteristics:

*   **Observability:**
    *   **Fully Observable:** The agent has complete and accurate access to the entire state of the environment. Example: A robot in a known, static grid map.
    *   **Partially Observable:** The agent can only perceive a part of the environment, or its perceptions are noisy/incomplete. Example: A robot with limited sensors or a navigation system dealing with unseen traffic.
*   **Agent Count:**
    *   **Single-Agent:** Only one agent operates in the environment. Example: A single drone delivering a package.
    *   **Multi-Agent:** Multiple agents operate, potentially interacting or competing. Example: Multiple warehouse robots sharing a space.
*   **Determinism:**
    *   **Deterministic:** The outcome of any action is precisely predictable. Example: A robot moving on a grid with perfect control.
    *   **Stochastic:** The outcome of an action involves an element of chance or randomness. Example: A robot on a slippery surface where an "Up" action might sometimes result in a "Left" move.
*   **Temporality:**
    *   **Static:** The environment does not change while the agent is deliberating.
    *   **Dynamic:** The environment can change while the agent is deliberating or executing actions. Example: Traffic conditions changing in Google Maps.
*   **Nature:**
    *   **Discrete:** The number of states and actions is finite or countably infinite. Example: A grid world.
    *   **Continuous:** States and actions are defined over continuous ranges. Example: A drone's 3D trajectory.

The objective of the agent directly relates to these characteristics. For instance, warehouse robots in a fully observable, multi-agent, deterministic, sequential, dynamic, and discrete environment aim to compute collision-free paths efficiently. Hospitality robots operate in a partially observable, multi-agent, stochastic, sequential, dynamic, and continuous environment, prioritizing safety and social awareness.

## Formalizing a Search Problem

A search problem is formally defined by the following components, using a "toy example" grid world for illustration:

Imagine a $5 \times 5$ grid where some cells are blocked (grey). An agent starts at a source and needs to reach a destination.

1.  **States ($S$):**
    These represent the possible configurations of the agent in the environment. In our grid world, the states are the agent's locations, represented as $(x,y)$ coordinates, excluding the blocked cells.
    $$ S = \{ (x,y) \mid 1 \le x, y \le 5, \text{ (x,y) is not a blocked cell} \} $$

2.  **Initial State ($s_0$):**
    The state where the agent begins its search. In our toy example, $s_0 = (1,1)$.

3.  **Actions ($A$):**
    A set of legal moves available to the agent from any given state. For the grid world, actions could be:
    $$ A = \{ \text{Up, Down, Left, Right} \} $$
    It's important that actions are only "legal" if they don't move the agent into a blocked cell or off the grid boundaries.

4.  **Transition Model ($T(s,a)$):**
    This function describes the outcome of performing action $a$ in state $s$. For a deterministic environment, it maps a state-action pair to a new state.
    In our grid world, the transition model is:
    $$ T((x,y),a) = \begin{cases} (x-1,y) & \text{if } a = \text{Up} \\ (x+1,y) & \text{if } a = \text{Down} \\ (x,y-1) & \text{if } a = \text{Left} \\ (x,y+1) & \text{if } a = \text{Right} \end{cases} $$
    (Provided the new state is legal, i.e., within bounds and not blocked).

5.  **Goal Test ($G(s)$):**
    A function that determines if a given state $s$ is a goal state. In the toy example, $G(s)$ is true if the agent reaches $(5,5)$.

6.  **Path Cost ($c(s,a,s')$):**
    The cost associated with taking action $a$ from state $s$ to reach state $s'$. In our simple grid world, a unit cost per action is assumed, meaning the total cost is simply the number of steps taken. More complex problems might have varying costs (e.g., fuel consumption, time, risk).

### The 8-Puzzle Example
The 8-Puzzle provides another classic example of a search problem.
*   **States ($S$):** All possible permutations of the 9 tiles (8 numbered tiles + 1 blank) on a $3 \times 3$ grid.
*   **Initial State ($s_0$):** A specific starting configuration of the tiles.
*   **Actions ($A$):** Moving the blank tile Up, Down, Left, or Right (if legal).
*   **Transition Model ($T(s,a)$):** The resulting tile configuration after moving the blank tile.
*   **Goal Test ($G(s)$):** True if the tiles are arranged in the target configuration (e.g., 1-2-3, 4-5-6, 7-8-blank).
*   **Path Cost ($c(s,a,s')$):** Typically unit cost for each move.

An interesting question for such problems is solvability: "Can you start from any $s_0$ and reach any $s_{goal}$?" For the 8-puzzle, not all initial states can reach all goal states.

## The Search Tree

To solve search problems, we often visualize the problem space as a **search tree**. A tree is a hierarchical data structure that shows:
*   A starting point.
*   All possible choices from that point.
*   What those choices lead to.

Every path from the start to a node in the tree represents a possible sequence of actions (a possible future) and thus a potential solution or part of a solution.

### Components of a Tree
A generic tree structure consists of:
*   **Nodes:** The fundamental units of a tree, representing elements or states.
*   **Edges:** Connections between nodes, representing relationships or actions.
*   **Root node:** The topmost node in the tree, from which all other nodes descend.
*   **Child nodes:** Nodes directly connected to and below a parent node.
*   **Leaf nodes:** Nodes that have no children, representing terminal points in a path.
*   **Depth:** The number of edges from the root node to a given node.

### Components of a Search Tree
In the context of problem solving, these generic tree components map directly to the elements of our search problem formulation:
*   **Nodes:** Represent the **states ($S$)** in the problem space.
*   **Edges:** Represent the **actions ($A$)** that transition an agent from one state to another.
*   **Root node:** Corresponds to the **initial state ($s_0$)**.
*   **Child nodes:** Are **generated** by applying a legal action to a parent state.
*   **Leaf node:** Represents a state from which no further actions can be taken, or a state that is a terminal point for exploration (e.g., a goal state or a dead end).
*   **Depth:** The total number of actions taken from the initial state to reach the current state. This often corresponds to the path cost when using unit costs.

## Introduction to Tree Traversal

To find a path to a goal state within a search tree, we need systematic methods to explore the tree. These methods are called **tree traversal algorithms**. Two fundamental traversal strategies are:

1.  **Breadth-First Search (BFS):** Explores the tree level by level, examining all nodes at the current depth before moving on to nodes at the next depth.
2.  **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking.

### Queue for BFS
Breadth-First Search uses a **Queue** data structure to manage which nodes to visit next. A queue operates on a **First In, First Out (FIFO)** principle:
*   **Enqueue:** Elements are added to the *end* of the queue.
*   **Dequeue:** Elements are removed from the *beginning* of the queue.

This ensures that nodes are explored in the order they were discovered at each level, thus guaranteeing that the shortest path (in terms of number of steps/edges) is found first for unweighted graphs.

## Quick Summary

This lecture established the core concepts for formulating pathfinding problems in AI. We explored diverse real-world applications and learned to characterize their environments based on observability, determinism, temporality, and agent count. The formal definition of a search problem was presented, detailing states ($S$), initial state ($s_0$), actions ($A$), transition model ($T(s,a)$), goal test ($G(s)$), and path cost ($c(s,a,s')$). This framework was then mapped onto the concept of a search tree, defining its components (nodes, edges, root, child, leaf, depth) in terms of problem elements. Finally, we briefly introduced Breadth-First Search (BFS) and Depth-First Search (DFS) as fundamental tree traversal strategies, highlighting the use of a FIFO Queue for BFS. These foundational concepts are crucial for understanding and designing effective search algorithms.