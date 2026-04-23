---
course: ES119 Principles of AI
title: Active Reinforcement Learning
lecture_number: 8
lecture_name: Active Reinforcement Learning
category: Module 3
sidebar_label: Lecture 8
sidebar_position: 8
topic:
- Exploration vs. Exploitation
- Q-Learning Algorithm
- SARSA and On-Policy vs. Off-Policy
- Exploration Functions
tags:
- RL
- Q-Learning
- SARSA
- Temporal Difference
- Exploration
summary: This lecture transitions from passive to active reinforcement learning, detailing
  the exploration-exploitation trade-off, the derivation of Q-values for model-free
  control, and the algorithmic differences between Q-Learning and SARSA.
math: true
last_updated: 22 April 2026
---


## The Paradigm Shift: From Passenger to Explorer

In **Passive Reinforcement Learning**, the agent follows a fixed policy $\pi$ and merely learns the utility $U^\pi(s)$ of the states it visits. In **Active Reinforcement Learning**, the agent is in control:
- **No Fixed Policy:** The agent must learn the environment while simultaneously choosing actions to maximize reward.
- **Goal:** Find the optimal policy $\pi^*$ through experience.
- **The Dilemma:** What the agent learns depends entirely on its choices. If it doesn't explore, it may never discover the optimal path.

## The Exploration-Exploitation Trade-off

This is the most fundamental trade-off in AI:

1.  **Exploitation:** Choosing the action currently estimated to yield the highest reward based on existing knowledge.
    - *Risk:* Getting trapped in **local optima** (e.g., finding a $+1$ reward and never searching for a hidden $+10$ reward).
2.  **Exploration:** Taking sub-optimal actions to gather new information about the environment.
    - *Risk:* Wasting time on known low-reward paths or repeatedly entering dangerous states (e.g., stepping into a fire pit just to confirm it is still hot).

### Balancing Strategies

- **$\epsilon$-Greedy Strategy:** 
  - With probability $1 - \epsilon$, the agent **exploits** (chooses the best-known action).
  - With probability $\epsilon$, the agent **explores** (chooses a random action).
  - **Guarantee:** Ensures every state-action pair is visited infinitely often as $t \to \infty$.
- **Annealing (Decaying $\epsilon$):** Start with $\epsilon = 1.0$ (pure exploration) and slowly reduce it toward $0$ as the agent learns, shifting from a "curious toddler" to a "calculating master."

## Optimism Under Uncertainty

$\epsilon$-greedy explores blindly. A more systematic approach is to artificially inflate the value of unknown states.

### The Exploration Function $f(u, n)$
We replace the standard utility in our updates with an exploration function:
$$f(u, n) = \begin{cases} R^+ & \text{if } n < N_e \\ u & \text{otherwise} \end{cases}$$
- $u$: Current estimated utility.
- $n$: Number of times the state-action pair has been visited.
- $R^+$: An optimistic reward estimate.
- $N_e$: A minimum visit threshold.

This forces the agent to systematically explore "new" territory before settling for known rewards.

## The Need for Q-Values

In Active RL, knowing the state utility $U(s)$ is insufficient because the agent lacks the **transition model** $P(s' | s, a)$. To act greedily using $U(s)$, the agent would need to solve:
$$\arg \max_a \sum_{s'} P(s' | s, a) U(s')$$
Without $P$, this is unsolvable. To achieve **Model-Free** RL, we evaluate **actions** directly.

### Q-Values Definition
$Q(s, a)$ is the expected total reward of taking action $a$ in state $s$ and acting optimally thereafter.
- **Action Selection:** $\pi^*(s) = \arg \max_a Q(s, a)$. 
- **Benefit:** No transition model $P$ is required to find the best move.

## Q-Learning: The Algorithm

Q-Learning is a model-free, **Temporal Difference (TD)** algorithm that learns a Q-Table (rows: states, columns: actions).

### The Update Rule
$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ R + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

- **TD Target:** $R + \gamma \max_{a'} Q(s', a')$. Our new estimate of reality (immediate reward + discounted future value).
- **TD Error:** The difference between the target and the current estimate $Q(s, a)$.
- **Learning Rate ($\alpha$):** How much the current estimate is adjusted toward the target.

### Off-Policy Learning
Q-Learning is **Off-Policy**. It learns the optimal policy $\pi^*$ even while the agent follows a different exploration policy (like $\epsilon$-greedy). The update uses the $\max$ over future actions, assuming optimal behavior in the future regardless of the agent's actual next exploratory step.

## SARSA: The On-Policy Alternative

**SARSA** stands for State-Action-Reward-State-Action. It is the **On-Policy** cousin of Q-Learning.

### The Update Rule
$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ R + \gamma Q(s', a') - Q(s, a) \right]$$
- **Difference:** Instead of using $\max_{a'}$, SARSA uses the action $a'$ that the agent **actually intends to take** next.
- **Behavior:** SARSA learns the value of the current policy (including its silly exploratory mistakes), whereas Q-Learning ignores the current policy to find the absolute optimal value.

## Scaling Up: Beyond Tabular RL

**Tabular Q-Learning** (storing every state in a table) fails in complex environments (e.g., Chess, driving) due to the "curse of dimensionality."
- **Generalization:** Instead of exact states, we use **features** (e.g., distance to the nearest obstacle).
- **Deep Reinforcement Learning:** Uses Deep Neural Networks to approximate Q-functions directly from high-dimensional inputs (like raw pixels), enabling AI to master games like Go and StarCraft.

## Quick Summary
- **Active RL** requires balancing exploration (learning the world) and exploitation (maximizing reward).
- **$\epsilon$-Greedy** provides a simple balancing mechanism, while **Exploration Functions** provide systematic optimism.
- **Q-Values** enable model-free control by evaluating state-action pairs rather than just states.
- **Q-Learning** is an **off-policy** algorithm using the $\max$ operator to find optimal values.
- **SARSA** is an **on-policy** algorithm that updates based on actual future actions.
- Large state spaces necessitate a shift from tables to **feature-based** or **Deep RL** for generalization.

