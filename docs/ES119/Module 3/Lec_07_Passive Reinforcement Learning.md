---
course: ES119 Principles of AI
title: Passive Reinforcement Learning
lecture_number: 7
lecture_name: Passive Reinforcement Learning
category: Module 3
sidebar_label: Lecture 7
sidebar_position: 7
topic:
- Policy Evaluation
- Direct Utility Estimation
- Adaptive Dynamic Programming
- Temporal Difference Learning
tags:
- Reinforcement Learning
- Passive RL
- Bellman Equation
- Bootstrapping
summary: This lecture explores techniques for policy evaluation in unknown environments,
  contrasting model-free Direct Utility Estimation and Temporal Difference learning
  with model-based Adaptive Dynamic Programming.
math: true
last_updated: 23 April 2026
---


## From MDPs to Reinforcement Learning

In standard Markov Decision Processes (MDPs), we assume the agent possesses the complete tuple $(S, A, P, R)$. With the "physics" ($P$) and "motivation" ($R$) known, the optimal policy $\pi^*$ is calculated offline using Bellman equations. 

**The RL Reality:** The agent is dropped into an unknown world.
- $P(s'|s, a)$ is **hidden**: The agent doesn't know transition probabilities (e.g., slip chances).
- $R(s, a, s')$ is **hidden**: The agent only discovers rewards by experiencing them.
- **Consequence**: Utilities cannot be calculated on a "whiteboard"; the agent must learn from a sequence of interactions or **Experience Tuples**: $(s, a, s', r)$.

---

## Passive RL Paradigm

In **Passive Reinforcement Learning**, the agent's policy $\pi$ is **fixed**. The agent follows the rulebook $\pi(s)$ without deviation. 

- **Objective**: Policy Evaluation. Estimate the expected utility $U^\pi(s)$ for every state $s$ under the fixed policy.
- **Stochasticity**: Even with a fixed policy, trajectories are noisy. The agent might intend to go North but slip East, creating different episodes each run.
- **Episode (Trial)**: A sequence of transitions from an initial state to a terminal state.

---

## Method 1: Direct Utility Estimation (DUE)

DUE treats policy evaluation as a **supervised learning** problem. If we want the expected value of a state, we observe it many times and average the results.

### The Algorithm
1.  **Input Data ($X$)**: The state $s$ visited.
2.  **Target Label ($Y$)**: The observed **Reward-to-Go** ($g_t$) from that state until the end of the episode.
3.  **Calculation**: For each visit to state $s$, calculate:
    $$g_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \dots$$
4.  **Estimation**: After $N$ visits, the utility is the empirical average:
    $$U^\pi(s) \approx \frac{1}{N} \sum_{i=1}^N g_i$$

### Evaluation
- **Pros**: Simple to implement, model-free (no need for $P$), and unbiased. 
- **Cons (The Fatal Flaw)**: It treats states as independent "buckets." It ignores the **Bellman Equation** constraint: $U^\pi(s) = R(s) + \gamma \sum_{s'} P(s'|s, \pi(s))U^\pi(s')$. Because it misses state connectivity, it is highly data-inefficient.

---

## Method 2: Adaptive Dynamic Programming (ADP)

ADP is a **model-based** approach. Instead of ignoring the hidden $P$ and $R$, the agent builds an internal model of them.

### The Three-Step Process
1.  **Act**: Observe transitions and rewards while following $\pi$.
2.  **Model**: Estimate the transition model $\hat{P}$ and reward function $\hat{R}$ via counting:
    $$\hat{P}(s'|s, a) = \frac{N(s, a, s')}{N(s, a)}$$
3.  **Solve**: Plug $\hat{P}$ and $\hat{R}$ into the simplified Bellman Equation for a fixed policy:
    $$U^\pi(s) = \sum_{s'} \hat{P}(s'|s, \pi(s)) \left[ \hat{R}(s, \pi(s), s') + \gamma U^\pi(s') \right]$$

### Evaluation
- **Pros**: Maximum data efficiency. Discovered information (like a penalty) propagates backward instantly to all related states.
- **Cons**: Computationally expensive. Solving $N$ linear equations after every step is intractable for large state spaces (e.g., $10^{20}$ states in Backgammon).

---

## Method 3: Temporal Difference (TD) Learning

TD learning is the "Missing Link": it is model-free (like DUE) but respects state connectivity (like ADP).

### The Concept of Bootstrapping
Instead of waiting for an episode to end to calculate total rewards, TD updates the estimate of a state the moment it transitions to the next state. It updates a **guess based on another guess**.

### The TD Update Rule
Every time the agent takes a step $(s, a, s', r)$, it applies:
$$U^\pi(s) \leftarrow U^\pi(s) + \alpha \underbrace{\left[ r + \gamma U^\pi(s') - U^\pi(s) \right]}_{\text{TD Error}}$$

- **TD Target**: $r + \gamma U^\pi(s')$. This is treated as the "local truth."
- **Learning Rate ($\alpha$)**: Determines the step size toward the new error.
- **Model-Free Nature**: Notice $P(s'|s, a)$ is missing. TD accounts for probabilities by **experiencing** transitions at their natural frequency.

### Convergence and Conditions
To guarantee convergence to the true utility despite noise, the learning rate $\alpha$ must decrease over time according to the **Robbins-Monro Conditions**:
1.  $\sum_{t=1}^{\infty} \alpha(t) = \infty$: Ensures the agent can reach any target value.
2.  $\sum_{t=1}^{\infty} \alpha^2(t) < \infty$: Ensures the updates eventually settle and stop "bouncing."
*Example: $\alpha(t) = 1/t$ satisfies these conditions.*

---

## Comparison Summary

| Feature | Direct Utility (DUE) | Adaptive DP (ADP) | TD Learning |
| :--- | :--- | :--- | :--- |
| **Model** | Model-Free | Model-Based | Model-Free |
| **Bellman Eq** | Ignores | Explicitly Solves | Implicitly Solves |
| **Efficiency** | Low (Data) | High (Data) | Medium |
| **Computation** | Very Cheap | Highly Expensive | Cheap |
| **Update Time** | End of Episode | Every Step | Every Step |

---

## Quick Summary
- **Passive RL** focuses on **policy evaluation** ($U^\pi$) rather than optimization.
- **DUE** averages observed rewards-to-go but ignores state connections, making it data-inefficient.
- **ADP** builds a model ($\hat{P}, \hat{R}$) and solves linear equations; it is data-efficient but computationally "explosive."
- **TD Learning** uses **bootstrapping** to update estimates mid-episode. It serves as a lightweight approximation of ADP, respecting the Bellman constraint without requiring an explicit model.
- **Robbins-Monro conditions** are necessary for TD convergence in stochastic environments.