---
course: ES119 Principles of AI
title: 'Sequential Decision Making: Utilities and MDPs'
lecture_name: 'Sequential Decision Making: Utilities and MDPs'
category: Module 3
lecture_number: 5
sidebar_label: Lecture 5
sidebar_position: 5
topic:
- Markov Decision Processes
- Policies vs. Plans
- Stochastic Environments
- Reward Functions
- Utility Theory
- Bellman Equation
tags:
- AI
- Reinforcement Learning
- MDP
- Sequential Decision Making
- Utility
- Bellman Equation
- Stochastic Environments
math: true
summary: This lecture introduces Markov Decision Processes (MDPs) as a framework for
  sequential decision making in stochastic environments. It covers the formal definition
  of an MDP, the role of reward functions in shaping agent behavior, the concept of
  utility for evaluating action sequences, and culminates in the fundamental Bellman
  Equation for calculating optimal state utilities.
last_updated: 12 April 2026
---


# Sequential Decision Making: Utilities and MDPs

## From Static Plans to Dynamic Policies

In classical search algorithms like A\*, an agent determines a **plan** – a fixed sequence of actions to reach a goal. However, in stochastic (random) environments, a fixed plan is brittle. If an action doesn't lead to the intended state ("slip"), the plan breaks.

To address this, we need a **policy** ($\pi$). A policy is a universal strategy: a mapping from every possible state to an optimal action. This allows an agent to adapt to unexpected outcomes, ensuring it always knows the optimal move, regardless of where it ends up.

**Key Distinction:**
*   **Search** $\longrightarrow$ **Plan** (Static sequence)
*   **MDP** $\longrightarrow$ **Policy** (Dynamic strategy)

## The Gridworld: An Illustrative Example

Consider an agent navigating a grid with the following "physics":
*   **Movement:** Four cardinal directions (North, South, East, West).
*   **Walls:** Impassable obstacles.
*   **Boundaries:** Hitting a wall or edge keeps the agent in its current square.

### Stochasticity: The "Slip" Factor

Actions are not perfectly reliable. For instance, intending to move North might result in:
*   80% probability: Move North (intended).
*   10% probability: Slip East.
*   10% probability: Slip West.

This inherent uncertainty means an agent cannot simply follow a path; it requires a strategy (policy) that accounts for all contingencies.

### The Navigation Dilemma & Expected Value

Agents often face trade-offs, like a "shortcut" that is shorter but riskier (e.g., adjacent to a "pit" with negative reward) versus a "safe path" that is longer but less dangerous.

To evaluate such risks, we calculate the **Expected Value**. For an action $a$ taken from state $s$, leading to various possible next states $s'$ with probabilities $P(s'|s, a)$, and associated rewards $R(s, a, s')$:

$$E[U(s, a)] = \sum_{s'} P(s'|s, a) \times \text{Reward for } s'$$

**Example:** From state (3,2), attempting to move North:
*   Reward for Goal: +1.0
*   Reward for Pit: -1.0
*   Living Reward (Step Cost): -0.04 (incurred regardless of outcome)

If an action 'North' from (3,2) leads to:
*   Goal (80%): Reward of (+1.0)
*   Pit (10%): Reward of (-1.0)
*   (3,2) [hitting wall] (10%): Reward of (-0.04)

Then, $E[U(3,2, \text{North})] = (0.8 \times 1.0) + (0.1 \times -1.0) + (0.1 \times -0.04) = 0.8 - 0.1 - 0.004 = 0.696$.

This single-step expected value helps assess the immediate risk-reward trade-off.

## Formalizing the World: The Markov Decision Process (MDP)

A **Markov Decision Process (MDP)** is a mathematical framework for modeling sequential decision making in situations where outcomes are partly random and partly under the control of a decision maker. It is defined by the tuple $(S, A, P, R)$:

1.  **States ($S$):** A set of all possible configurations of the world.
    *   **Discrete:** e.g., grid coordinates $(x,y)$.
    *   **Continuous:** e.g., velocity, angle, temperature.
    *   **Terminal States:** States where the "game" ends (e.g., Goal, Pit). Once entered, an agent cannot leave.

2.  **Actions ($A$):** A set of actions available to the agent in each state. $A(s)$ denotes the set of actions available from state $s$.

3.  **Transition Model ($P(s'|s, a)$):** The probability of reaching state $s'$ from state $s$ when taking action $a$. This embodies "Nature's Dice."
    *   **Markov Property:** The future is independent of the past given the present state and action.
        $P(s_{t+1}|s_t, a_t, s_{t-1}, a_{t-1}, \dots, s_0) = P(s_{t+1}|s_t, a_t)$
    *   If $P(s'|s, a) = 1$ for all $s, a, s'$, the world is deterministic (classical search).
    *   If $P(s'|s, a) < 1$ for some $s, a, s'$, the world is stochastic (MDPs).

4.  **Reward Function ($R(s, a, s')$):** The numeric signal (reward) received for transitioning from state $s$ to state $s'$ via action $a$.
    *   **Terminal Rewards:** Rewards received upon entering a terminal state (e.g., Goal = +1, Pit = -1).
    *   **Living Rewards:** Rewards (often negative, acting as costs) incurred for each step of the journey. In some simplified cases, $R(s)$ can be used if the reward depends only on the state landed in.

### Reward Engineering: Shaping Agent Personality

The "Living Reward" ($R(s, a, s')$) plays a crucial role in defining an agent's "personality" or preferences for different behaviors. By adjusting this cost, we can drastically alter the optimal policy:

*   **"Suicidal" Agent ($R = -2.0$):** High living cost makes the agent prefer the immediate "Pit" (-1.0) over a long, costly path to the Goal.
*   **"Risk-Taker" Agent ($R = -0.4$):** Moderate living cost encourages the agent to take shortcuts, risking a slip into the Pit to avoid the guaranteed higher cost of a longer, safe path.
*   **"Conservative" Agent ($R = -0.01$):** Low living cost makes steps practically free. The agent chooses the longest, safest path, avoiding any risk of the Pit.
*   **"Eternal" Agent ($R = +0.01$):** Positive living reward means the agent is paid to stay alive. It avoids terminal states (Goal and Pit) and might find a way to stay in a non-terminal state indefinitely to collect infinite positive rewards.

## The Goal: Optimal Policy $\pi^*$

The ultimate goal in an MDP is to find an **optimal policy $\pi^*$**. This is the policy that, if followed, results in the highest expected sum of rewards over time.
An optimal policy is:
*   Not a fixed path, but a mapping from *every* state $s$ to an action $a$.
*   Robust: It must handle every possible "slip" and unexpected outcome the agent might encounter.

## Utility and Discounting

An agent evaluates and prefers entire sequences of states and actions, known as **histories** ($h = [s_0, a_0, s_1, a_1, s_2, a_2, \dots]$). We express these preferences using a **Utility Function $U_h$**.

### The Utility of a History ($U_h$)

For a *finite* history, the utility is simply the sum of rewards accumulated along that sequence:
$$U_h = R(s_0, a_0, s_1) + R(s_1, a_1, s_2) + R(s_2, a_2, s_3) + \dots$$
A negative living reward means a longer history directly yields a lower $U_h$, thus motivating the agent to reach a goal quickly.

### The Infinite Horizon Problem and Discounting

If the agent's task never ends, the sum of rewards for an infinite history can be infinite, making comparison impossible. To keep utilities finite and comparable, we introduce **discounting**.

The **Discount Factor ($\gamma$)** is a value $0 \le \gamma < 1$. It weighs future rewards less than immediate rewards:
$$U_h = \sum_{t=0}^\infty \gamma^t R(s_t, a_t, s_{t+1})$$
*   $\gamma$ ensures the infinite sum converges to a finite value.
*   **High $\gamma$ (close to 1):** The agent cares significantly about distant future rewards.
*   **Low $\gamma$ (close to 0):** The agent primarily cares about immediate rewards.

### Stationarity of Preferences

The choice of exponential discounting ($\gamma^t$) is not arbitrary. It is mathematically justified by the **Stationarity Principle**: If an agent prefers History 1 ($h_1$) over History 2 ($h_2$), then attaching the exact same starting state and action to both should not flip its preference ($[s_0, a_0, h_1] \succ [s_0, a_0, h_2]$ if and only if $h_1 \succ h_2$). This fundamental principle mathematically forces the use of exponential discounting.

### From History to Expected Utility

Because the world is stochastic, the agent cannot guarantee experiencing one specific history $h$. Therefore, we cannot calculate a fixed $U_h$. Instead, we must calculate the **Expected Utility**.

## The Utility of a State: $U(s)$

We define $U(s)$ as the **expected discounted utility of the optimal history starting at state $s$**. It represents the long-term "worth" of being in a specific state, assuming the agent acts perfectly (optimally) from that point onward.

## The Bellman Equation

The utility of a state $U(s)$ cannot be arbitrary; it must be consistent with the utilities of its neighboring states and the rewards obtained from transitioning between them. This consistency is formalized by the **Bellman Equation**:

$$U(s) = \max_a \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma U(s')]$$

### Unpacking the Bellman Equation:

1.  **Term inside brackets $[R(s, a, s') + \gamma U(s')]$:** This represents the total utility of a *single transition* from $s$ to $s'$ via action $a$.
    *   $R(s, a, s')$: The **Immediate Reward** obtained for making this specific transition.
    *   $\gamma U(s')$: The **Discounted Future Utility** that the agent expects to receive if it lands in state $s'$ and acts optimally from there.

2.  **Summation $\sum_{s'} P(s'|s, a) [\dots]$:** This calculates the **expected utility of taking a specific action $a$** from state $s$. We multiply the total utility of each possible transition (to $s'$) by its probability $P(s'|s, a)$ and sum over all possible next states $s'$.

3.  **Max Operator $\max_a (\dots)$:** Since the agent wants to maximize its long-term utility, it will choose the action $a$ that yields the highest expected utility.
    *   $U(s)$ becomes this maximum expected utility.
    *   The action $a$ that produces this maximum value is the **optimal action for state $s$**, denoted $\pi^*(s)$.

### Example Calculation (from previous slides):

Let's calculate the expected utility of taking the action **North** from a specific state $s$, given parameters:
*   Action $a = \text{North}$
*   Discount Factor $\gamma = 0.9$
*   Living Reward $R(s, a, s') = -0.04$ for all transitions
*   Known utilities: $U(\text{Goal}) = 1.0$, $U(\text{Pit}) = -1.0$, $U(\text{Safe}) = 0.5$

Assuming the specific state $s$ (labeled as "State s" in the original slide) has the following transition probabilities for action 'North':
*   **Intended (80% North to Goal):**
    $0.8 \times [-0.04 + 0.9 \times U(\text{Goal})] = 0.8 \times [-0.04 + 0.9 \times 1.0] = 0.8 \times 0.86 = 0.688$
*   **Slip Left (10% West to Safe):**
    $0.1 \times [-0.04 + 0.9 \times U(\text{Safe})] = 0.1 \times [-0.04 + 0.9 \times 0.5] = 0.1 \times 0.41 = 0.041$
*   **Slip Right (10% East to Pit):**
    $0.1 \times [-0.04 + 0.9 \times U(\text{Pit})] = 0.1 \times [-0.04 + 0.9 \times -1.0] = 0.1 \times -0.94 = -0.094$

The total expected utility of moving North from state $s$ is:
$0.688 + 0.041 - 0.094 = \mathbf{0.635}$

To find $U(s)$, this calculation must be repeated for all possible actions (East, South, West). The highest resulting expected utility value will be $U(s)$, and the action that produced it will be $\pi^*(s)$.

## Quick Summary

Markov Decision Processes (MDPs) provide a powerful framework for **sequential decision making** in environments with **stochastic outcomes**. Unlike classical search, MDPs yield a **policy** ($\pi^*$), a dynamic mapping of optimal actions to states, robust to "slips." An MDP is defined by its states ($S$), actions ($A$), **transition model** ($P(s'|s,a)$), and **reward function** ($R(s,a,s')$), which crucially shapes an agent's "personality." The concept of **utility** evaluates entire histories of states and actions. For infinite horizons, a **discount factor** ($\gamma$) ensures finite, comparable utilities, grounded by the **Stationarity Principle**. Due to stochasticity, we seek **expected utility**. The fundamental **Bellman Equation** $U(s) = \max_a \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma U(s')]$ recursively defines the optimal utility of a state $U(s)$ by linking immediate rewards and future discounted utilities, and concurrently identifies the **optimal policy** $\pi^*(s)$.