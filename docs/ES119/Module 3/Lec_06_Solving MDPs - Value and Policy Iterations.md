---
title: 'Solving MDPs: Value and Policy Iteration'
lecture_number: 6
lecture_name: Solving MDPs - Value and Policy Iterations
category: Module 3
sidebar_label: Lecture 6
sidebar_position: 6
course: ES119 Principles of AI
topic:
- Sequential Decision Making
- Markov Decision Processes (MDPs)
- Value Iteration
- Policy Iteration
- Q-Values
- Curse of Dimensionality
tags:
- AI
- Reinforcement Learning
- MDP
- Value Iteration
- Policy Iteration
- Bellman Equation
- Q-Learning
- Dynamic Programming
summary: 'This lecture delves into the core algorithms for solving Markov Decision
  Processes (MDPs): Value Iteration and Policy Iteration. We introduce Q-values, examine
  the iterative Bellman update rule, and discuss how utilities propagate. We then
  contrast Value Iteration''s slow convergence with Policy Iteration''s ''leapfrog''
  approach, exploring their respective advantages and limitations. The lecture concludes
  by addressing the ''Curse of Dimensionality'' and the transition to function approximation
  for large state spaces.'
math: true
last_updated: 14 April 2026
---

---

# Solving MDPs: Value and Policy Iteration

In the previous lectures, we introduced Markov Decision Processes (MDPs) and the Bellman equation. This lecture focuses on the foundational algorithms for finding optimal policies in MDPs: Value Iteration and Policy Iteration.

## Q-Values: Expected Utility of an Action

While $U(s)$ represents the optimal utility of a state, we often need to evaluate the worth of a specific action taken from that state. This is captured by the **Q-Value** or **Action-Utility**, $Q(s, a)$.

*   $Q(s, a)$ is the expected utility of taking action $a$ in state $s$, and then acting optimally forever after.
*   In a Gridworld, a state $s$ has distinct $Q$-values for each available action (e.g., North, South, East, West).

### The Math of $Q(s, a)$

The term inside the `max` operator of the Bellman equation is precisely $Q(s, a)$:

$$Q(s, a) = \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma U(s')]$$

This equation calculates the expectation over "nature's dice roll" for a specific action $a$. It considers the immediate transition reward $R(s, a, s')$ plus the discounted future utility $U(s')$.

### Relationship between $U$ and $Q$

The optimal utility of a state $U(s)$ is simply the maximum $Q$-value across all possible actions from that state:

$$U(s) = \max_a Q(s, a)$$

The Bellman equation can be seen as a combination of these two concepts.

### Why Q-Values Matter: Policy Extraction

$Q$-values are crucial because they directly provide the optimal policy $\pi^*(s)$. If an agent knows the $Q$-value for every possible action in a state, choosing the optimal action is trivial:

$$\pi^*(s) = \arg\max_a Q(s, a)$$

The agent simply picks the action $a$ that yields the largest $Q$-value. This concept forms the foundation of **Reinforcement Learning** (Q-Learning).

## Value Iteration

The Bellman equation cannot be solved instantly due to its recursive nature. Value Iteration is an iterative approach that transforms the Bellman equation into an **update rule**:

$$U_{k+1}(s) \leftarrow \max_a \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma U_k(s')]$$

*   $U_k(s)$ is the utility estimate at iteration $k$.
*   $U_{k+1}(s)$ is the new utility estimate for the next step, calculated using the previous estimates $U_k(s')$.

### Iterative Process

1.  **Iteration $k=0$: Initial State**
    *   Initialize all state utilities to zero: $U_0(s) = 0$. The agent is "blind" to future rewards.

2.  **Iteration $k=1$: Discovering Local Rewards**
    *   Apply the update rule once. Since $U_0(s')$ are all zero, the future utility term vanishes:
        $$U_1(s) \leftarrow \max_a \sum_{s'} P(s'|s, a) [R(s, a, s') + 0]$$
    *   $U_1(s)$ now reflects purely the expected immediate living cost or terminal rewards. States adjacent to goals/pits will show high/low utilities. This represents a "planning horizon" of one step.

3.  **Iteration $k=2$: Horizon of Two**
    *   The update rule now uses $U_1(s')$. States two steps away from the Goal can "see" it. They incorporate their neighbors' $U_1(s')$ values, updating their own utility (slightly lower due to discount factor $\gamma$ and living rewards).

4.  **Iteration $k=3$ and Beyond: Utility Propagation**
    *   The loop continues, with $U_3$ using $U_2$, $U_4$ using $U_3$, and so on.
    *   Utility information propagates backward from terminal states across the entire state space.
    *   Utilities form a smooth landscape, increasing closer to positive goals. The optimal policy is to "climb" towards higher utilities.

### Propagation Complete and Convergence

*   Eventually, the changes between $U_k(s)$ and $U_{k+1}(s)$ become microscopic.
*   The utilities stabilize into their true optimal values, $U^*(s)$.
*   **Stopping Criterion:** Value Iteration stops when the maximum change across all states between iterations falls below a small tolerance threshold $\epsilon$:
    $$\max_s |U_{k+1}(s) - U_k(s)| < \epsilon$$

### Why Updates Get Smaller

The convergence of Value Iteration is mathematically guaranteed by the **discount factor $\gamma < 1$**.
*   Each time the update rule is applied, future utilities are multiplied by $\gamma$.
*   This means any initial "errors" or arbitrary guesses from $U_0(s) = 0$ are shrunk by a fraction in every iteration, forcing the utility values to converge to a stable solution.

### Policy Extraction After Convergence

Once Value Iteration converges to $U^*(s)$, we extract the optimal policy $\pi^*(s)$ by performing a **one-step lookahead**:

$$\pi^*(s) = \arg\max_a \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma U^*(s')]$$

Recognizing the $Q$-value definition, this simplifies to:

$$\pi^*(s) = \arg\max_a Q^*(s, a)$$

## The Flaw in Value Iteration

Despite its effectiveness, Value Iteration has a significant drawback:
*   **Asymptotic Slowness:** It crawls toward the exact utility numbers $U^*(s)$ one step at a time.
*   **The Catch:** The optimal action for a state often becomes obvious long *before* its utility number stops changing significantly. Value Iteration wastes computational time refining utilities to microscopic precision when the policy remains stable.

## Policy Iteration

Policy Iteration offers a "mathematical shortcut" to address Value Iteration's inefficiency. It avoids the `max_a` operator, which is the hardest part of the Bellman equation, by **fixing a policy**.

If a policy $\pi$ is fixed, there is no choice to make. The `max_a` vanishes, and the Bellman equation for a fixed policy $\pi$, $U^\pi(s)$, becomes a standard system of linear equations:

$$U^\pi(s) = \sum_{s'} P(s'|s, \pi(s)) [R(s, \pi(s), s') + \gamma U^\pi(s')]$$

For an $N$-state environment, this is a system of $N$ linear equations with $N$ unknowns, which can be solved exactly and quickly using linear algebra.

### The "Leapfrog" Effect

Policy Iteration takes giant leaps compared to Value Iteration's tiny steps:

1.  **Guess a Policy (Initialization):** Start with an arbitrary random policy $\pi_0$.
2.  **Instantly Evaluate (Policy Evaluation):** Solve the system of linear equations to find $U^{\pi_i}(s)$ for the current policy $\pi_i$. This determines the exact utility of following $\pi_i$ over an infinite horizon.
3.  **Greedily Improve (Policy Improvement):** For each state $s$, perform a one-step lookahead to find a better action. Calculate the $Q$-value for all actions $a$ using the current policy's utilities $U^{\pi_i}(s')$:
    $$\pi_{i+1}(s) = \arg\max_a \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma U^{\pi_i}(s')]$$
    This update creates a new, improved policy $\pi_{i+1}$. We are guaranteed that $\pi_{i+1}$ is strictly better than (or equal to) $\pi_i$.

### The Full Cycle and Convergence

Policy Iteration repeats the Policy Evaluation and Policy Improvement steps. It stops when the Policy Improvement step yields the exact same policy it started with ($\pi_{i+1} = \pi_i$). Because there is a finite number of possible policies in a discrete MDP, this algorithm is guaranteed to converge to the optimal policy $\pi^*$ in a finite number of steps, often significantly fewer than Value Iteration.

## Reward Engineering Revisited

The **transition reward $R(s, a, s')$** defines the agent's motivation and profoundly influences the optimal policy.

*   **"Suicidal" Sequence (e.g., $R(s, a, s') = -2.0$ for all transitions):** A large negative living reward makes the penalty for each step overwhelming. The optimal policy becomes to terminate as rapidly as possible, even if it means plunging into a negative-reward pit intentionally. The global utility $U(s)$ becomes highly negative everywhere.
*   **"Conservative" Sequence (e.g., $R(s, a, s') = -0.01$ for all transitions):** A negligible transition cost allows the agent to prefer long histories, prioritizing avoidance of negative pits (even with slip probabilities) over reaching the positive goal quickly. The utility surface $U(s)$ appears very flat, gently sloping towards the positive goal.

The Bellman mathematics perfectly maps the supplied $R(s, a, s')$ to the agent's optimal behavior. Failures in AI behavior are rarely algorithm flaws, but rather misdesigns of the reward function.

## The Curse of Dimensionality

While Value and Policy Iteration work perfectly for small Gridworlds, they fail in high-dimensional environments:

*   **Chess:** $\approx 10^{43}$ states.
*   **Go:** $\approx 10^{170}$ states.

Both algorithms require calculating and storing $U(s)$ (or $Q(s,a)$) for **every single state** on every iteration. In high-dimensional spaces, this is:
*   **Memory Impractical:** Physically impossible to store such large tables.
*   **Computationally Impossible:** Inverting matrices of size $10^{43} \times 10^{43}$ (for Policy Evaluation) or iterating over all $10^{43}$ states (for Policy Improvement) is not feasible.

This exponential explosion in state space is known as the **Curse of Dimensionality**.

### Beyond Exact MDPs: Function Approximation

Exact tabular methods like Value and Policy Iteration are not practical for complex, real-world tasks. Modern AI employs **Function Approximation** to overcome this limitation.

*   Instead of lookup tables, we use parameterized mathematical functions (e.g., **Neural Networks**) to estimate $U(s)$ or $Q(s, a)$ directly.
*   The network takes state features as input and outputs the estimated utility or Q-value, without needing to explicitly map out or store the entire state space. This is a cornerstone of modern Deep Reinforcement Learning.

## Quick Summary

*   **Q-Values ($Q(s,a)$):** Represent the expected utility of taking action $a$ in state $s$ and acting optimally thereafter. $U(s) = \max_a Q(s,a)$ and $\pi^*(s) = \arg\max_a Q(s,a)$.
*   **Value Iteration:** Iteratively updates state utilities $U_k(s)$ using the Bellman update rule until convergence. Information propagates backward from terminal states. It is asymptotically slow as it refines utilities to a high precision, even after the optimal policy has stabilized.
*   **Policy Iteration:** An alternating two-step process:
    1.  **Policy Evaluation:** Solves a system of linear equations to exactly calculate $U^\pi(s)$ for a fixed policy $\pi$.
    2.  **Policy Improvement:** Greedily updates the policy by selecting the action that maximizes $Q(s,a)$ using the current $U^\pi(s')$ values.
    It converges to $\pi^*$ in fewer iterations than Value Iteration but each iteration is computationally more intensive.
*   **Reward Engineering:** The design of the reward function $R(s,a,s')$ is critical, directly shaping the agent's optimal behavior and policy.
*   **Curse of Dimensionality:** Both Value and Policy Iteration are tabular methods that require storing and computing values for every state. This becomes intractable for large or continuous state spaces, necessitating techniques like **Function Approximation** (e.g., using neural networks) in modern Reinforcement Learning.
*   The ultimate goal is to find the optimal policy $\pi^*$ that maximizes the expected utility of the agent's history.