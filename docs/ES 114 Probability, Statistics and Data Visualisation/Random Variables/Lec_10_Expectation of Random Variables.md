---
title: Expectation of Random Variables
lecture_number: 10
lecture_name: Expectation of Random Variables
category: Random Variables
sidebar_label: Lecture 10
sidebar_position: 10
course: "ES 114 Probability, Statistics and Data Visualisation"
topic:
- Expectation
- Discrete Random Variables
- Probability Mass Functions (PMF)
tags:
- Probability
- Expectation
- Mean
- Random Variables
- Discrete Distributions
- Weighted Average
summary: This lecture rigorously defines the expectation of a discrete random variable,
  interpreting it as a weighted average. It clarifies the distinction between theoretical
  expectation and empirical sample average, and introduces the critical concept of
  absolute summability for expectation to exist. Practical examples illustrate calculation.
math: true
last_updated: "31 March 2026"
---

# Expectation of Random Variables

The concept of expectation is fundamental in probability theory, representing the "average" value of a random variable. It's not just a simple average but a *weighted* average, where each possible value of the random variable is weighted by its probability.

## 1. Defining Expectation

The **expectation** (or **expected value** or **mean**) of a discrete random variable $X$, denoted as $E[X]$, is a measure of the central tendency of the distribution.

### Definition
For a discrete random variable $X$ with a sample space $\Omega(X)$ and probability mass function (PMF) $p_X(x)$, the expectation is defined as:

$$E[X] = \sum_{x \in \Omega(X)} x p_X(x)$$

This definition implies summing over all possible values $x$ that $X$ can take, multiplying each value by its corresponding probability.

### Interpretation: Weighted Average
The expectation $E[X]$ is a **weighted average**. Each state (value $x$) is weighted by its "percentage" or probability $p_X(x)$. This means values that are more probable contribute more significantly to the expectation.

For instance, if a dataset is partitioned into bins, and each bin has a value $x_k$ and a percentage of samples $p_X(x_k)$, the "average" is effectively the expectation.

## 2. Expectation vs. Sample Average (Histogram)

It is crucial to distinguish between the theoretical expectation and the empirical sample average.

*   **Expectation ($E[X]$)**:
    *   A statistical property of the **random variable** itself.
    *   A **deterministic number** derived from the PMF.
    *   Often unknown; it's the target of estimation.
    *   Calculated "top-down" using the known probability distribution.

*   **Sample Mean ($\bar{X}$)**:
    *   A numerical value calculated from a **finite set of observed data**.
    *   **Itself a random variable** because it depends on the specific samples drawn.
    *   Has **uncertainty**, which decreases as more samples are used.
    *   Used to **estimate** the true mean ($E[X]$).
    *   Calculated "bottom-up" from data, without requiring knowledge of the true underlying distribution $X$.

The **Law of Large Numbers** states that as the number of samples $N$ increases, the sample mean $\bar{X}$ will converge to the true expectation $E[X]$. Similarly, the empirical histogram of observed data will increasingly resemble the underlying probability mass function (PMF) as $N \to \infty$.

## 3. Examples of Expectation Calculation

Let's apply the definition to various scenarios.

### Example 1: Simple PMF
Let $X$ be a random variable with PMF $p_X(0) = 1/4$, $p_X(1) = 1/2$, and $p_X(2) = 1/4$.
Find $E[X]$.

$$E[X] = \sum_{x \in \{0, 1, 2\}} x p_X(x) = (0)p_X(0) + (1)p_X(1) + (2)p_X(2)$$
$$E[X] = (0)\left(\frac{1}{4}\right) + (1)\left(\frac{1}{2}\right) + (2)\left(\frac{1}{4}\right) = 0 + \frac{1}{2} + \frac{1}{2} = 1$$

### Example 2: Unfair Coin
Flip an unfair coin where the probability of getting a head is $3/4$. Let $X$ be a random variable such that $X=1$ means getting a head, and $X=0$ means getting a tail. Find $E[X]$.

Given $P(\text{Head}) = P(X=1) = 3/4$.
Then $P(\text{Tail}) = P(X=0) = 1 - 3/4 = 1/4$.
$$E[X] = (0)P(X=0) + (1)P(X=1) = (0)\left(\frac{1}{4}\right) + (1)\left(\frac{3}{4}\right) = \frac{3}{4}$$

### Example 3: Infinite Series PMF
Let $X$ be a random variable with PMF $p_X(k) = \frac{c}{2^k}$, for $k=1, 2, \dots$.

**(a) Find $c$.**
The sum of all probabilities must equal 1:
$$\sum_{k=1}^{\infty} p_X(k) = \sum_{k=1}^{\infty} \frac{c}{2^k} = c \sum_{k=1}^{\infty} \left(\frac{1}{2}\right)^k = 1$$
This is a geometric series sum: $\sum_{k=1}^{\infty} r^k = \frac{r}{1-r}$ for $|r|<1$. Here $r=1/2$.
$$c \cdot \frac{1/2}{1-1/2} = c \cdot \frac{1/2}{1/2} = c \cdot 1 = 1 \implies c=1$$

**(b) Find $E[X]$.**
$$E[X] = \sum_{k=1}^{\infty} k p_X(k) = \sum_{k=1}^{\infty} k \frac{1}{2^k}$$
This is a known series sum: $\sum_{k=1}^{\infty} k r^k = \frac{r}{(1-r)^2}$ for $|r|<1$. Here $r=1/2$.
$$E[X] = \frac{1/2}{(1-1/2)^2} = \frac{1/2}{(1/2)^2} = \frac{1/2}{1/4} = 2$$

### Example 4: Game Reward
Consider a game where you flip a coin 3 times. Let $H$ be the number of heads. The rewards are:
*   1 dollar if there are 2 heads
*   8 dollars if there are 3 heads
*   0 dollars if there are 0 or 1 head
The cost to enter the game is 1.5 dollars. On average, what is the net gain?

First, calculate the probabilities for the number of heads, assuming a fair coin: $P(H=k) = \binom{3}{k} (0.5)^3$.
*   $P(H=0) = \binom{3}{0}(0.5)^3 = 1 \cdot 0.125 = 0.125$
*   $P(H=1) = \binom{3}{1}(0.5)^3 = 3 \cdot 0.125 = 0.375$
*   $P(H=2) = \binom{3}{2}(0.5)^3 = 3 \cdot 0.125 = 0.375$
*   $P(H=3) = \binom{3}{3}(0.5)^3 = 1 \cdot 0.125 = 0.125$

Let $R$ be the reward random variable.
*   $R=0$ if $H=0$ or $H=1$. So $P(R=0) = P(H=0) + P(H=1) = 0.125 + 0.375 = 0.5$.
*   $R=1$ if $H=2$. So $P(R=1) = P(H=2) = 0.375$.
*   $R=8$ if $H=3$. So $P(R=8) = P(H=3) = 0.125$.

Expected reward $E[R]$:
$$E[R] = (0)P(R=0) + (1)P(R=1) + (8)P(R=8)$$
$$E[R] = (0)(0.5) + (1)(0.375) + (8)(0.125) = 0 + 0.375 + 1 = 1.375$$
The average reward is 1.375 dollars.
The net gain is
$$E[R] - 1.5 = 1.375 - 1.5 = -0.125$$
On average, you lose 0.125 dollars per game.

## 4. Existence of Expectation: Absolutely Summable

Does the expectation always exist? No.
For $E[X]$ to exist, the sum $\sum x p_X(x)$ must converge. More formally, we require the random variable to be **absolutely summable**.

### Definition: Absolutely Summable
A discrete random variable $X$ is **absolutely summable** if the expectation of its absolute value is finite:
$$E[|X|] \overset{\text{def}}{=} \sum_{x \in X(\Omega)} |x| p_X(x) < \infty$$
Only those absolutely summable random variables have finite expectations. If $E[|X|]$ diverges, then $E[X]$ does not exist or is undefined.

### Example: Non-existent Expectation
Consider a random variable $X$ with the following PMF:
$$p_X(k) = \frac{6}{\pi^2 k^2}, \quad k = 1, 2, \dots$$
Let's check if $E[X]$ exists by evaluating $E[|X|]$:
$$E[|X|] = \sum_{k=1}^{\infty} |k| p_X(k) = \sum_{k=1}^{\infty} k \frac{6}{\pi^2 k^2} = \frac{6}{\pi^2} \sum_{k=1}^{\infty} \frac{1}{k}$$
The sum $\sum_{k=1}^{\infty} \frac{1}{k}$ is the **harmonic series**, which is known to diverge to infinity.
Since $E[|X|] = \infty$, the expectation $E[X]$ for this random variable does not exist.

---

## Quick Summary

*   **Expectation $E[X]$** is the weighted average of a discrete random variable's possible values, where each value is weighted by its probability $p_X(x)$.
*   **Formula**: $E[X] = \sum_{x \in \Omega(X)} x p_X(x)$.
*   **Distinct from Sample Mean $\bar{X}$**: $E[X]$ is a theoretical, deterministic property of the random variable, while $\bar{X}$ is an empirical, random value calculated from data, used to estimate $E[X]$.
*   **Existence**: Expectation only exists if the random variable is **absolutely summable**, meaning $E[|X|] = \sum |x| p_X(x) < \infty$. If this sum diverges, $E[X]$ does not exist.
