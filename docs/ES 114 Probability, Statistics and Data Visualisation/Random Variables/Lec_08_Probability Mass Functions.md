---
title: Probability Mass Functions (PMF)
lecture_number: 8
lecture_name: Probability Mass Functions
category: Random Variables
sidebar_label: Lecture 8
sidebar_position: 8
course: "ES 114 Probability, Statistics and Data Visualisation"
topic:
- Random Variables
- Probability Mass Functions (PMF)
- Histograms
- Properties of PMF
- Discrete Probability Distributions
tags:
- probability
- random variables
- PMF
- discrete probability
- histogram
- statistics
math: true
summary: This lecture introduces the fundamental concept of Probability Mass Functions
  (PMFs) for discrete random variables, differentiating them from ordinary variables
  and explaining their relationship to histograms. Key properties and illustrative
  examples are covered to build a solid foundation.
last_updated: "31 March 2026"
---

---

## Introduction to Random Variables

A **random variable** (RV), denoted as $X$, is a function that maps outcomes from a sample space $\Omega$ to real numbers. Essentially, it translates "words" (events) into "numbers" for mathematical analysis.

For an outcome $\xi \in \Omega$, the random variable $X$ assigns a numerical value $X(\xi)$.

**Key Idea**: While a sample space can have many events, and a random variable can map these to many numbers (states), the goal is to systematically describe the probabilities associated with these numerical outcomes.

## Probability Mass Functions (PMF)

The **probability mass function (PMF)** of a discrete random variable $X$ is a function that quantifies the probability of the random variable taking on a specific numerical value. We denote the PMF as $p_X(a)$.

**Definition**:
For a discrete random variable $X$, its PMF is defined as:
$$ p_X(a) = P[X = a] $$
where $P[X = a]$ is the probability of the event $\{\xi \in \Omega \mid X(\xi) = a\}$.

**Distinction between $X$ and $a$**:
*   $X$: This is the **random variable** itself, a function from the sample space to numbers. Technically, it should be $X(\xi)$.
*   $a$: This is a specific **state** or value that the random variable $X$ can take. So, $X=a$ means the random variable $X$ takes on the state $a$.

A random variable is considered "random" precisely because it can adopt various states, each with an associated probability.

### Example: Coin Flip

Consider flipping a fair coin twice. Let $X$ be the random variable representing the number of heads. The sample space is $\Omega = \{TT, TH, HT, HH\}$.

The PMF for $X$ is:
*   $p_X(0) = P[X = 0] = P[\text{"TT"}] = \frac{1}{4}$ (0 heads)
*   $p_X(1) = P[X = 1] = P[\text{"TH", "HT"}] = \frac{2}{4} = \frac{1}{2}$ (1 head)
*   $p_X(2) = P[X = 2] = P[\text{"HH"}] = \frac{1}{4}$ (2 heads)

The PMF values graphically represent the probability distribution across the possible states of $X$.

## Ordinary Variable vs. Random Variable

The distinction between an ordinary variable and a random variable is crucial:

| Feature          | Ordinary Variable ($x$)     | Random Variable ($X$)               |
| :--------------- | :-------------------------- | :---------------------------------- |
| **Equation**     | $2x + 1 = 0$                | $2X + 1 = 0$ (or $2X + 0 = 0$, etc.) |
| **Solution**     | $x = -\frac{1}{2}$          | $X \in \{-\frac{1}{2}, 0, \frac{1}{2}\}$ (multiple states possible) |
| **Random?**      | No                          | Yes                                 |
| **No. of States**| 1 (deterministic)           | Multiple states                     |
| **PMF**          | Not applicable              | $p_X(x) = \frac{1}{3}$, for $x \in \{-\frac{1}{2}, 0, \frac{1}{2}\}$ (if each state is equally likely from multiple possibilities) |

An ordinary variable has a single, fixed value in a given context, while a random variable can take on multiple values, each with a certain probability.

## Histograms

A **histogram** is a graphical representation of the distribution of numerical data. It groups data into bins and shows the frequency (or relative frequency/probability) of values falling into each bin.

For example, a histogram of letter frequencies in English shows the observed relative frequency (empirical probability) of each letter.

## PMF vs. Histogram

The relationship between a PMF and a histogram is profound:

*   A **histogram** is an *empirical* representation of data. It shows the observed frequencies or probabilities from a finite set of trials.
*   A **PMF** is the *ideal* or theoretical histogram. It represents the true underlying probability distribution of a random variable, often derived from a probabilistic model.

As the number of observations ($N$) in a histogram increases, the histogram tends to converge towards the true PMF of the underlying random variable. For instance, repeatedly rolling a fair die and plotting the histogram of outcomes will approach a uniform PMF of $1/6$ for each face as the number of rolls approaches infinity.

### Why Study PMF?

1.  **Ideal vs. Empirical**: We seek an ideal mathematical description of randomness, not just empirical observations.
2.  **Data Modeling**: PMFs provide a parametric model for data, allowing us to understand the underlying process that generates the data, unlike non-parametric histograms.
3.  **Data Generation and Testing**: Once a PMF is known, we can synthesize new data that adheres to the established probability distribution. This is crucial for simulations, testing algorithms, and statistical inference.

## Properties of a PMF

A valid Probability Mass Function $p_X(x)$ must satisfy two fundamental properties:

**Theorem**: For a discrete random variable $X$ with possible values $x \in \mathcal{X}$ (the support of $X$), its PMF $p_X(x)$ must satisfy:

1.  **Non-negativity**: $p_X(x) \geq 0$ for all $x \in \mathcal{X}$.
2.  **Normalization**: $\sum_{x \in \mathcal{X}} p_X(x) = 1$.

**Proof of Normalization**:
Let $\mathcal{X}$ be the set of all possible values that $X$ can take.
The sum of probabilities for all possible values of $X$ is:
$$ \sum_{x \in \mathcal{X}} p_X(x) = \sum_{x \in \mathcal{X}} P[X=x] $$
By definition, $P[X=x]$ is the probability of the event $\{\xi \in \Omega \mid X(\xi)=x\}$. Since these events are mutually exclusive (a random variable cannot take two different values simultaneously) and exhaustive (it must take *some* value), their union covers the entire sample space $\Omega$.
$$ \sum_{x \in \mathcal{X}} P[X=x] = P\left[ \bigcup_{x \in \mathcal{X}} \{\xi \in \Omega \mid X(\xi)=x\} \right] $$
The union of all these disjoint events constitutes the entire sample space $\Omega$.
$$ P\left[ \bigcup_{x \in \mathcal{X}} \{\xi \in \Omega \mid X(\xi)=x\} \right] = P[\Omega] $$
By the axioms of probability, the probability of the sample space is 1.
$$ P[\Omega] = 1 $$
Thus, $\sum_{x \in \mathcal{X}} p_X(x) = 1$.

## Examples

### Example 1: Finding a Normalizing Constant

Let $X$ be a random variable with PMF given by $p_X(k) = c \left(\frac{1}{2}\right)^k$, for $k = 1, 2, 3, \ldots$. Find the constant $c$.

To find $c$, we use the normalization property: $\sum_{k=1}^{\infty} p_X(k) = 1$.
$$ \sum_{k=1}^{\infty} c \left(\frac{1}{2}\right)^k = 1 $$
Factor out $c$:
$$ c \sum_{k=1}^{\infty} \left(\frac{1}{2}\right)^k = 1 $$
This is a geometric series with first term $a = \frac{1}{2}$ and common ratio $r = \frac{1}{2}$. The sum of an infinite geometric series $ar + ar^2 + \ldots$ (starting from $k=1$) is $\frac{a}{1-r}$ for $|r| < 1$.
Here, the sum $\sum_{k=1}^{\infty} \left(\frac{1}{2}\right)^k = \frac{1/2}{1 - 1/2} = \frac{1/2}{1/2} = 1$.
Therefore:
$$ c \cdot 1 = 1 \implies c = 1 $$
So, the PMF is $p_X(k) = \left(\frac{1}{2}\right)^k$ for $k=1, 2, \ldots$.

### Example 2: Invalid PMF Example

Let $X$ be a random variable with PMF given by $p_X(k) = c \sin\left(\frac{\pi}{2} k\right)$, for $k = 0, 1, 2, \ldots$. Find the constant $c$.

Let's evaluate $\sin\left(\frac{\pi}{2} k\right)$ for small integer values of $k$:
*   $k=0: \sin(0) = 0$
*   $k=1: \sin(\pi/2) = 1$
*   $k=2: \sin(\pi) = 0$
*   $k=3: \sin(3\pi/2) = -1$
*   $k=4: \sin(2\pi) = 0$
*   $k=5: \sin(5\pi/2) = 1$
*   ...and so on.

The sequence of $\sin\left(\frac{\pi}{2} k\right)$ values is $0, 1, 0, -1, 0, 1, 0, -1, \ldots$.
For $p_X(k)$ to be a valid PMF, it must satisfy $p_X(k) \geq 0$ for all $k$.
If $c > 0$, then $p_X(k)$ would be negative for $k=3, 7, 11, \ldots$ (where $\sin(\frac{\pi}{2} k) = -1$).
If $c < 0$, then $p_X(k)$ would be negative for $k=1, 5, 9, \ldots$ (where $\sin(\frac{\pi}{2} k) = 1$).
The only way for $p_X(k) \geq 0$ for all $k$ is if $c=0$.
However, if $c=0$, then $p_X(k) = 0$ for all $k$. In this case, $\sum_{k=0}^{\infty} p_X(k) = \sum_{k=0}^{\infty} 0 = 0$, which violates the normalization property ($\sum p_X(k) = 1$).

Therefore, there is **no value of $c$** that can make $p_X(k) = c \sin\left(\frac{\pi}{2} k\right)$ a valid Probability Mass Function, as it violates the non-negativity property unless $c=0$, which then violates normalization. This example highlights the importance of the non-negativity condition for PMFs.

---

## Quick Summary

A **Probability Mass Function (PMF)**, $p_X(a) = P[X=a]$, defines the probability of a discrete random variable $X$ taking on a specific numerical value $a$. Unlike an ordinary variable with a single state, a random variable can assume multiple states, each with a given probability. PMFs are the theoretical, "ideal" counterpart to empirical histograms, which they converge to with an increasing number of observations. Essential properties for any valid PMF are **non-negativity** ($p_X(x) \geq 0$) and **normalization** ($\sum p_X(x) = 1$), ensuring that probabilities are valid and sum to certainty over all possible outcomes.

