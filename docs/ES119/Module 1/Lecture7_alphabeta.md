---
title: Alpha-Beta Pruning
lecture_number: 7
lecture_name: Alpha-Beta Pruning
category: 'Module 1: Search and Planning'
sidebar_label: 'Lecture 7'
sidebar_position: 7
course: 'ES119: Principles of AI'
topic:
  - Adversarial Search
  - Minimax Algorithm
  - Alpha-Beta Pruning
  - Game AI
  - Computational Complexity
tags:
  - AI
  - Search
  - Games
  - Minimax
  - Alpha-Beta
  - Pruning
  - Optimal Decisions
  - Computational Efficiency
summary: This lecture introduces Alpha-Beta Pruning, an optimization technique for the Minimax algorithm in adversarial search. We explore its theoretical foundations, implementation details, and practical effectiveness in game AI, including historical context with Samuel's Checker Player and IBM Deep Blue, and its limitations for games with high branching factors leading to Monte Carlo Tree Search.
math: true
---

# Alpha-Beta Pruning

In adversarial search, the Minimax algorithm provides a theoretical framework for optimal decision-making in zero-sum games. However, its computational complexity renders it impractical for games with large search spaces. Alpha-Beta Pruning is an optimization that drastically reduces the number of nodes evaluated by the Minimax algorithm without affecting the final decision.

## 1. Revisiting Minimax Search

Recall that Minimax search explores a game tree to find the optimal move for the maximizing player (MAX), assuming the minimizing player (MIN) plays optimally to minimize MAX's score.

The time complexity of Minimax search is $O(b^m)$, where $b$ is the branching factor (average number of legal moves from a state) and $m$ is the maximum depth of the search tree. The space complexity is $O(bm)$ for Depth-First Search (DFS) implementation. This exponential complexity quickly becomes unmanageable for realistic game depths.

## 2. Introduction to Alpha-Beta Pruning

Alpha-Beta Pruning is a technique that prunes branches of the search tree that cannot possibly influence the final Minimax decision. It maintains two values, $\alpha$ and $\beta$, which represent the best guaranteed outcomes for MAX and MIN, respectively, along the current path of exploration.

*   $\alpha$: The best (highest) score that MAX can guarantee so far at any point in the search. This value is initialized to $-\infty$.
*   $\beta$: The best (lowest) score that MIN can guarantee so far at any point in the search. This value is initialized to $+\infty$.

These values are passed down the tree and updated as the search progresses. Pruning occurs when the current $\alpha$ value becomes greater than or equal to the current $\beta$ value. This condition indicates that the current branch cannot yield a better outcome for the current player than an already explored alternative, hence further exploration of this branch is unnecessary.

### 2.1 The Pruning Logic

Consider a MAX node $N$. As MAX explores its children, it updates its $\alpha$ value. If, for any child $C$ (which is a MIN node), the $\beta$ value returned from $C$'s subtree (i.e., the best MIN can achieve from $C$) becomes less than or equal to $N$'s current $\alpha$ value, then MAX knows that this path through $C$ will yield a score no better than $\alpha$. Since MAX can already guarantee $\alpha$ from another branch, it will not choose this path through $C$. Therefore, the remaining children of $C$ (which would be explored to determine $C$'s exact value) can be pruned. This is called a **Beta Cutoff**.

Conversely, consider a MIN node $M$. As MIN explores its children, it updates its $\beta$ value. If, for any child $C$ (which is a MAX node), the $\alpha$ value returned from $C$'s subtree (i.e., the best MAX can achieve from $C$) becomes greater than or equal to $M$'s current $\beta$ value, then MIN knows that this path through $C$ will yield a score no worse than $\beta$. Since MIN can already guarantee $\beta$ from another branch, it will not choose this path through $C$. Therefore, the remaining children of $C$ can be pruned. This is called an **Alpha Cutoff**.

## 3. Alpha-Beta Algorithm (Pseudocode)

The Alpha-Beta algorithm is typically implemented using two mutually recursive functions, one for MAX nodes and one for MIN nodes.

### 3.1 `MAX-VALUE(state, α, β)`

```
function MAX-VALUE(state, α, β):
  if IS-TERMINAL(state) then return UTILITY(state)
  v := -∞
  for each action in ACTIONS(state):
    v := max(v, MIN-VALUE(RESULT(state, action), α, β))
    if v >= β then return v  // Beta Cutoff
    α := max(α, v)
  return v
```

### 3.2 `MIN-VALUE(state, α, β)`

```
function MIN-VALUE(state, α, β):
  if IS-TERMINAL(state) then return UTILITY(state)
  v := +∞
  for each action in ACTIONS(state):
    v := min(v, MAX-VALUE(RESULT(state, action), α, β))
    if v <= α then return v  // Alpha Cutoff
    β := min(β, v)
  return v
```

The initial call to start the Alpha-Beta search from the root state $s_0$ is `MAX-VALUE(s_0, -∞, +∞)`.

### 3.3 Example Trace

Let's trace a simplified example (similar to page 8):
Suppose we have a MAX node (root) `A` with children `B` (MIN) and `C` (MIN). `B` has leaves `10, 8`. `C` has leaves `4, 50`.

1.  Call `MAX-VALUE(A, -∞, +∞)`.
2.  `A` calls `MIN-VALUE(B, -∞, +∞)`.
3.  `B` calls `MAX-VALUE` on its children:
    *   Child 1 (leaf `10`): Returns `10`. `v` for `B` becomes `10`. $\beta$ for `B` becomes `10`.
    *   Child 2 (leaf `8`): Returns `8`. `v` for `B` becomes `min(10, 8) = 8`. $\beta$ for `B` becomes `8`.
4.  `MIN-VALUE(B)` returns `8`.
5.  Back to `MAX-VALUE(A)`. `v` for `A` becomes `max(-∞, 8) = 8`. $\alpha$ for `A` becomes `8`.
6.  `A` calls `MIN-VALUE(C, 8, +∞)`. (Note: `α` passed from `A` is `8`).
7.  `C` calls `MAX-VALUE` on its children:
    *   Child 1 (leaf `4`): Returns `4`. `v` for `C` becomes `4`. $\beta$ for `C` becomes `4`.
    *   **Crucial Step**: Now, for `MIN-VALUE(C)`, current `v = 4`, current `α = 8`. The condition `v <= α` (i.e., `4 <= 8`) is true. This means the MIN node `C` has found a move (yielding `4`) that is worse for its parent (MAX node `A`) than what `A` has *already guaranteed* (`8`) from the `B` branch. Therefore, MAX node `A` will never choose the path through `C` if `C` can only guarantee `4`. The search for remaining children of `C` (e.g., the leaf `50`) can be pruned. `MIN-VALUE(C)` immediately returns `4`.
8.  Back to `MAX-VALUE(A)`. `v` for `A` remains `max(8, 4) = 8`.
9.  `MAX-VALUE(A)` returns `8`.

The path through `50` was never explored, saving computation.

## 4. Properties and Performance

*   **Optimality**: Alpha-Beta Pruning produces the *exact same* Minimax value as unpruned Minimax search. It is an optimal algorithm in terms of solution quality.
*   **Time Complexity**:
    *   **Worst-case**: When moves are ordered poorly (e.g., best moves explored last), Alpha-Beta Pruning performs no better than Minimax, remaining $O(b^m)$.
    *   **Best-case**: When moves are ordered optimally (best moves explored first), Alpha-Beta Pruning can reduce the effective branching factor to roughly $\sqrt{b}$. The time complexity becomes $O(b^{m/2})$ for an even number of ply, or $O((\sqrt{b})^m)$. This is a significant improvement, effectively allowing the search to go twice as deep for the same computational budget.

## 5. Historical Applications in Game AI

Alpha-Beta Pruning has been a cornerstone for game-playing AI for decades.

### 5.1 Samuel's Checker Player (1959-1962)

Arthur Samuel's checker-playing program, developed on IBM 704 and later IBM 7094, was one of the earliest successful AI programs. In 1962, it famously defeated a US state checkers champion.

Challenges for Samuel's player:
*   Minimax was impossible to run to full depth even for checkers (depth 6-8 was too much).

Techniques employed to make it feasible:
*   **Evaluation Function**: Instead of searching to terminal states, a heuristic `Eval(s)` function was used to estimate the utility of non-terminal states. This allowed depth-limited minimax.
*   **Alpha-Beta Pruning**: Engineered to work close to the best-case scenario. This was crucial for efficiency.
*   **Move Ordering**: The effectiveness of Alpha-Beta pruning heavily depends on exploring good moves first. Samuel's program attempted to order moves based on various heuristics (e.g., immediate captures, strategic positions).
*   **Rote Learning (Caching)**: Stored previously evaluated positions and their values (a form of transposition table), avoiding redundant computations. Pruning benefited greatly when good moves were explored first, often by looking them up in this cache.

### 5.2 IBM Deep Blue (1997)

Deep Blue famously defeated world chess champion Garry Kasparov in 1997. This demonstrated the power of highly optimized search combined with powerful hardware.

Key techniques in Deep Blue's Minimax engine:
*   **Depth-Limited Minimax**: Searched to depths of 10-14 ply (half-moves). Terminal utilities were replaced by complex heuristic `Eval(s)` functions.
*   **Alpha-Beta Pruning**: Used as the default search algorithm for its efficiency.
*   **Iterative Deepening**: Search depths $d = 1, 2, 3, \ldots$ were explored. Earlier iterations provided not only a principal variation (best move found so far) but also bounds ($\alpha, \beta$) and a better move ordering for subsequent deeper searches. This enabled near best-case $\alpha-\beta$ behavior.
*   **Transposition Tables**: A vast cache storing previously evaluated positions, their exact Minimax values, and their $\alpha/\beta$ bounds. This significantly reduced redundant computations, especially in games with many transpositions (different move sequences leading to the same board state).
*   **Massive Parallelism**: Deep Blue utilized custom chess chips and a parallel architecture to explore millions of positions per second.

## 6. Limitations and Alternatives: Monte Carlo Tree Search

Despite its efficiency, Alpha-Beta Pruning, even with optimizations like iterative deepening and transposition tables, struggles with games that have very high branching factors.

*   **Chess**: Branching factor of 30-40. Alpha-Beta is highly effective.
*   **Go**: Branching factor of 200-300. Even best-case Alpha-Beta pruning is often insufficient.
*   **Difficulty of Evaluation Function in Go**: For Go, creating an accurate heuristic `Eval(s)` function is notoriously difficult due to the global nature of the game and the complexity of territory and influence.

For such games, **Monte Carlo Tree Search (MCTS)** has emerged as a powerful alternative.

*   **Monte Carlo Tree Search (MCTS)**: MCTS builds a search tree by running many simulated games (rollouts) from the current position. It focuses its search on more promising moves by exploring them more often.
*   **Heuristic vs. Simulation**: Unlike Minimax, which relies on exact (or heuristic) backups of utility values, MCTS estimates move quality using average outcomes from simulated games. This avoids the need for a perfect evaluation function and is particularly effective in games where utility is hard to define early in the game or where the branching factor is too high for traditional tree search.
*   **AlphaGo (2016)**: Google Deepmind's AlphaGo famously defeated the world's best Go player, Lee Sedol, using a combination of MCTS with deep neural networks for move selection and state evaluation. AlphaGo utilized supervised learning from human expert games and reinforcement learning via self-play to train its neural networks. Its match-time inference leveraged both CPUs and GPUs.

You can visualize MCTS at: [https://vgarciasc.github.io/mcts-viz/](https://vgarciasc.github.io/mcts-viz/)

## Quick Summary

Alpha-Beta Pruning is a critical optimization for the Minimax algorithm, allowing efficient search in adversarial games. By maintaining $\alpha$ (MAX's guaranteed minimum score) and $\beta$ (MIN's guaranteed maximum score) bounds, it prunes subtrees that cannot influence the final optimal decision. While it guarantees optimal results, its effectiveness is highly dependent on move ordering. Historically, it underpinned the success of AI in games like Checkers (Samuel's Player) and Chess (Deep Blue), demonstrating significant computational gains over basic Minimax. However, for games with extremely high branching factors and complex evaluation functions, like Go, Alpha-Beta Pruning becomes less effective, leading to the development and success of algorithms like Monte Carlo Tree Search.