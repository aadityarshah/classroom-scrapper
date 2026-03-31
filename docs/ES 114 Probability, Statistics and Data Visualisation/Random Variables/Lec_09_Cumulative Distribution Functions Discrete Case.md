---
title: Cumulative Distribution Functions (Discrete Case)
lecture_number: 9
lecture_name: Cumulative Distribution Functions (Discrete Case)
category: Random Variables
sidebar_label: Lecture 9
sidebar_position: 9
course: "ES 114 Probability, Statistics and Data Visualisation"
topic:
- Probability Distributions
- Cumulative Distribution Function
- Discrete Random Variables
tags:
- CDF
- Discrete Probability
- Random Variables
- PMF
summary: This lecture introduces the Cumulative Distribution Function (CDF) for discrete
  random variables, exploring its definition, properties, and its role in generating
  arbitrary random numbers and relating to the Probability Mass Function (PMF).
math: true
last_updated: "31 March 2026"
---


## 1. Introduction: Generating Arbitrary Random Numbers

A fundamental problem in probability and computation is how to generate random numbers following an arbitrary probability mass function (PMF), $p_X(k)$. While computers can typically generate uniformly distributed random numbers (e.g., in $[0,1]$), direct generation from an arbitrary discrete PMF is not straightforward.

Consider a PMF $p_X(k) = [0.1, 0.4, 0.2, 0.3]$ for $k = [1, 2, 3, 4]$. The "trick" to generate samples from this distribution using a uniform random number generator lies in computing the **cumulative sum**.

By mapping segments of the $[0,1]$ interval to the possible outcomes based on their cumulative probabilities, we can simulate the desired distribution. If a uniformly distributed random number $U \in [0,1)$ falls into a certain segment, we output the corresponding $k$.

## 2. Cumulative Distribution Function (CDF) Definition

The **Cumulative Distribution Function (CDF)**, denoted $F_X(x)$, for a discrete random variable $X$ is defined as the probability that $X$ takes a value less than or equal to $x$:

$$
F_X(x) \triangleq P[X \le x] = \sum_{x' \le x} p_X(x')
$$

**Interpretation:**
*   The CDF is conceptually an "integration" or cumulative sum of the PMF.
*   The CDF is always well-defined, unlike the PMF which is typically defined only at discrete points for discrete variables.
*   The CDF framework works universally for both discrete and continuous random variables, providing a unified view of probability distributions.

## 3. Examples of CDF for Discrete Random Variables

Let's illustrate the CDF with examples.

**Example 1: Simple PMF**
Consider a random variable $X$ with the following PMF:
$p_X(0) = \frac{1}{4}$, $p_X(1) = \frac{1}{2}$, $p_X(4) = \frac{1}{4}$.
The corresponding CDF $F_X(x)$ would be a step function:
*   For $x < 0$, $F_X(x) = 0$.
*   For $0 \le x < 1$, $F_X(x) = P(X \le 0) = p_X(0) = \frac{1}{4}$.
*   For $1 \le x < 4$, $F_X(x) = P(X \le 1) = p_X(0) + p_X(1) = \frac{1}{4} + \frac{1}{2} = \frac{3}{4}$.
*   For $x \ge 4$, $F_X(x) = P(X \le 4) = p_X(0) + p_X(1) + p_X(4) = \frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1$.

This forms a "staircase" function, where the steps occur at the values $X$ can take, and the height of each step corresponds to the probability of that value.

**Example 2: English Letter Frequencies**
If $p_X(k)$ represents the frequency of English letters (a-z), the CDF $F_X(k)$ would show the cumulative probability of observing a letter up to $k$. This also results in a staircase function, with each step representing the probability of a specific letter.

## 4. Properties of CDFs (Discrete Case)

For any cumulative distribution function $F_X(x)$ of a discrete random variable $X$:

1.  **Monotonically Non-decreasing:** If $x_1 < x_2$, then $F_X(x_1) \le F_X(x_2)$. The cumulative probability can never decrease.
2.  **Limits:**
    *   $\lim_{x \to -\infty} F_X(x) = 0$
    *   $\lim_{x \to +\infty} F_X(x) = 1$
3.  **Right-Continuity:** The CDF is always continuous from the right. That is, $\lim_{\epsilon \to 0^+} F_X(x+\epsilon) = F_X(x)$. For discrete CDFs, this implies that the solid dot on a graph of the CDF is always on the right side of the jump.
4.  **Jumps at Probable Values:** At any position $x_k$ where $p_X(x_k) > 0$, the CDF will have a jump.
5.  **Height of Each Jump:** The height of a jump at $x_k$ is equal to the probability $p_X(x_k)$. Specifically, $P(X=x_k) = F_X(x_k) - F_X(x_k^-)$, where $F_X(x_k^-)$ is the limit of $F_X(x)$ as $x$ approaches $x_k$ from the left.

## 5. Converting Between PMF and CDF

For a discrete random variable $X$, the PMF can be obtained from its CDF.
If $X$ can take values $x_1, x_2, \dots, x_N$ in increasing order, then:

$$
p_X(x_k) = F_X(x_k) - F_X(x_{k-1}) \quad \text{for } k=1, \dots, N
$$

For $x_0$ (the value just before the smallest possible value $x_1$), we define $F_X(x_0) = F_X(-\infty) = 0$.

**A simpler version for integer-valued random variables:**

$$
p_X(k) = F_X(k) - F_X(k-1)
$$

**Example: Finding PMF from CDF**
Given the CDF: $F_X(0)=\frac{1}{4}$, $F_X(1)=\frac{3}{4}$, $F_X(4)=1$.
We know the PMF will have non-negative values only at $x=0, 1, 4$.
*   $p_X(0) = F_X(0) - F_X(-\infty) = \frac{1}{4} - 0 = \frac{1}{4}$.
*   $p_X(1) = F_X(1) - F_X(0) = \frac{3}{4} - \frac{1}{4} = \frac{2}{4} = \frac{1}{2}$.
*   $p_X(4) = F_X(4) - F_X(1) = 1 - \frac{3}{4} = \frac{1}{4}$.

This successfully recovers the PMF from Example 1.

## 6. Expressing PMF as Delta Functions (Advanced View)

A PMF for a discrete random variable can be formally expressed using Dirac delta functions. This perspective clarifies why the PMF is not a "function" in the traditional sense of mapping real numbers to probabilities everywhere, while the CDF is.

$$
p_X(x) = \sum_{k \in X(\Omega)} p_X(k) \cdot \delta(x-k)
$$

Here, $\delta(x-k)$ is the Dirac delta function, which is zero everywhere except at $x=k$, where it is infinitely high such that its integral is 1.

For instance, using the PMF from Example 1:
$$
p_X(x) = \frac{1}{4}\delta(x) + \frac{1}{2}\delta(x-1) + \frac{1}{4}\delta(x-4)
$$

Integrating this gives the CDF in terms of the Heaviside step function $u(x)$:
$$
F_X(x) = \frac{1}{4}u(x) + \frac{1}{2}u(x-1) + \frac{1}{4}u(x-4)
$$
This further emphasizes that $p_X(x)$ (as a sum of delta functions) is a generalized function (or distribution), while $F_X(x)$ (as a sum of step functions) is a well-behaved function.

## Quick Summary

*   The **Cumulative Distribution Function (CDF)**, $F_X(x) = P[X \le x]$, is the cumulative sum of the Probability Mass Function (PMF) for discrete random variables.
*   CDFs are always defined and serve as a unified way to describe probability distributions for both discrete and continuous random variables.
*   For discrete random variables, CDFs are **staircase functions**, where jumps occur at the values the random variable can take.
*   Key properties of CDFs include being non-decreasing, having limits of 0 at $-\infty$ and 1 at $+\infty$, and being right-continuous.
*   The PMF can be derived from the CDF by $p_X(k) = F_X(k) - F_X(k-1)$ for integer-valued $k$.
*   CDFs are crucial for **generating random numbers** from arbitrary discrete distributions using uniform random number generators.
*   We will revisit CDFs extensively when discussing continuous random variables.

