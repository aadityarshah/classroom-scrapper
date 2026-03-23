---
title: Bayes Theorem and Total Probability
lecture_number: 6
lecture_name: Bayes Theorem and Total Probability
category: Probability Theory
sidebar_label: Lecture 6
sidebar_position: 6
course: "ES 114 Probability, Statistics and Data Visualisation"
last_updated: "23 March 2026"
topic:
- Conditional Probability
- Bayesian Inference
tags:
- Bayes Theorem
- Total Probability
- Conditional Probability
- Prisoner's Dilemma
- Communication Channel
summary: This lecture introduces the fundamental Bayes Theorem and the Law of Total
  Probability. We explore how these powerful tools allow us to update our beliefs
  about events based on new evidence. We will apply these concepts to solve classic
  probabilistic puzzles like the Prisoner's Dilemma and analyze practical scenarios
  in communication and sports analytics.
math: true
---


## Introduction to Conditional Probability Revisited

In previous lectures, we established the foundations of probability theory, including the axioms of probability and the concept of conditional probability. Conditional probability, denoted as $P(A|B)$, quantifies the probability of event $A$ occurring given that event $B$ has already occurred. It is defined as:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad \text{provided } P(B) > 0$$

Today, we delve into two highly interconnected and immensely powerful theorems: **Bayes Theorem** and the **Law of Total Probability**. These theorems are cornerstones in statistical inference, machine learning, and many engineering applications, allowing us to reverse conditioning and systematically update our beliefs in light of new evidence.

## The Prisoner's Dilemma: A Motivating Example

Let's begin with a classic probability puzzle that highlights the counter-intuitive nature of conditional probabilities and sets the stage for Bayes Theorem.

Imagine three prisoners, A, B, and C, are awaiting their fate. The King has decided to release two of them and sentence one to death.

*   You are Prisoner A.
*   Initially, your chance of being released is $2/3$. This is because there are three possible outcomes for who is sentenced, each equally likely:
    1.  A is sentenced, B and C are released.
    2.  B is sentenced, A and C are released.
    3.  C is sentenced, A and B are released.
    Since you are A, in two out of three scenarios, you are released. Thus, $P(\text{A released}) = 2/3$, or $P(\text{A sentenced}) = 1/3$.

Now, suppose you know the guard well, and you can ask him a question. You ask the guard to name one of the other two prisoners (B or C) who will be released. The guard, being honest, tells you that B will be released.

Here's the puzzle: If you find out B is released, your initial intuition might suggest that your chance of being released changes from $2/3$ to $1/2$. This is because, with B released, it's now a choice between A and C for the remaining spot. But is this intuition correct? This problem, often called the **Three Prisoners Problem** or a variant of the Monty Hall Problem, demonstrates why careful application of conditional probability is crucial.

Let's define our events:
*   $X_A$: Prisoner A is sentenced to death.
*   $X_B$: Prisoner B is sentenced to death.
*   $X_C$: Prisoner C is sentenced to death.
*   $G_B$: The guard says B is released.

Our goal is to find $P(X_A | G_B)$, i.e., the probability that A is sentenced given the guard says B is released.

### Initial Probabilities

Since the King's decision is random, and one prisoner out of three is sentenced:
*   $P(X_A) = 1/3$
*   $P(X_B) = 1/3$
*   $P(X_C) = 1/3$

### Conditional Probabilities: Guard's Behavior

Now, let's consider the guard's behavior, $P(G_B | X_i)$:
*   **Case 1: $X_A$ (A is sentenced).** If A is sentenced, then B and C must be released. The guard is asked to name one of B or C who will be released. He can name B or C. We assume the guard chooses randomly if he has a choice. So, $P(G_B | X_A) = 1/2$.
*   **Case 2: $X_B$ (B is sentenced).** If B is sentenced, then A and C must be released. The guard cannot say B is released because B is sentenced. Therefore, the guard must say C is released. So, $P(G_B | X_B) = 0$.
*   **Case 3: $X_C$ (C is sentenced).** If C is sentenced, then A and B must be released. The guard is asked to name one of B or C who will be released. He must name B (since C is sentenced). So, $P(G_B | X_C) = 1$.

We are "stuck" if we only rely on the definition of conditional probability directly to find $P(X_A | G_B)$, as we would need $P(X_A \cap G_B)$ and $P(G_B)$. This is where Bayes Theorem comes to our rescue.

## Bayes Theorem

Bayes Theorem provides a way to reverse the conditioning of probabilities. If we know $P(B|A)$ and want to find $P(A|B)$, Bayes Theorem gives us the relationship.

### Theorem (Bayes Theorem)

For any two events $A$ and $B$ such that $P(A) > 0$ and $P(B) > 0$, it holds that:

$$P(A|B) = \frac{P(B|A) P(A)}{P(B)}$$

**Proof:**
From the definition of conditional probability:
$P(A|B) = \frac{P(A \cap B)}{P(B)}$
And also, $P(B|A) = \frac{P(B \cap A)}{P(A)}$.
Since $P(A \cap B) = P(B \cap A)$, we can write $P(A \cap B) = P(B|A) P(A)$.
Substituting this into the first equation, we get:
$P(A|B) = \frac{P(B|A) P(A)}{P(B)}$.
$\blacksquare$

**Interpretation of Terms:**
*   $P(A|B)$: **Posterior probability** – the probability of event $A$ after observing event $B$. This is what we want to find.
*   $P(B|A)$: **Likelihood** – the probability of observing event $B$ given that event $A$ is true. This is often easier to model or measure.
*   $P(A)$: **Prior probability** – the initial probability of event $A$ before any evidence $B$ is observed.
*   $P(B)$: **Evidence probability** – the total probability of observing event $B$. This acts as a normalization constant.

Often, $P(B)$ is not directly known but can be computed using the Law of Total Probability, especially when $A$ is part of a partition of the sample space.

## Law of Total Probability

The Law of Total Probability is crucial for calculating the denominator $P(B)$ in Bayes Theorem when $B$ depends on several mutually exclusive events that form a partition of the sample space.

### Theorem (Law of Total Probability)

Let $\{A_1, A_2, \dots, A_n\}$ be a partition of the sample space $\Omega$. This means that $A_i$ are mutually exclusive ($A_i \cap A_j = \emptyset$ for $i \neq j$) and their union covers the entire sample space ($\bigcup_{i=1}^n A_i = \Omega$).
Then, for any event $B \subseteq \Omega$, the probability of $B$ can be expressed as:

$$P(B) = \sum_{i=1}^{n} P(B|A_i) P(A_i)$$

**Proof:**
Since $\{A_1, A_2, \dots, A_n\}$ is a partition of $\Omega$, we can write event $B$ as:
$B = B \cap \Omega = B \cap (\bigcup_{i=1}^n A_i) = \bigcup_{i=1}^n (B \cap A_i)$
Since $A_i$ are mutually exclusive, so are the events $(B \cap A_i)$. Therefore, by the third axiom of probability (additivity for disjoint events):
$P(B) = P(\bigcup_{i=1}^n (B \cap A_i)) = \sum_{i=1}^{n} P(B \cap A_i)$
Using the definition of conditional probability, $P(B \cap A_i) = P(B|A_i)P(A_i)$, we substitute this into the equation:
$P(B) = \sum_{i=1}^{n} P(B|A_i) P(A_i)$.
$\blacksquare$

### Visualizing the Law of Total Probability

Imagine the sample space $\Omega$ as a rectangle, partitioned into $n$ disjoint events $A_1, A_2, \dots, A_n$. Event $B$ is an arbitrary region within $\Omega$.

```
+---------------------------------+
| A1              | A2            |
|       .---------|---------.     |
|       |         |         |     |
|       |   B     |         |     |
|       |         |         |     |
|-------'---------|---------'-----|
| A3              | A4            |
|                 |               |
|                 |               |
|                 |               |
+---------------------------------+
```

The probability $P(B)$ can be thought of as the sum of the probabilities of $B$ intersecting with each partition $A_i$. Each $P(B \cap A_i)$ can then be broken down into $P(B|A_i) P(A_i)$. The Law of Total Probability essentially "decomposes" the probability of $B$ into contributions from each possible scenario ($A_i$).

## Resolving the Prisoner's Dilemma

Now, let's use Bayes Theorem and the Law of Total Probability to solve the Prisoner's Dilemma. We want to find $P(X_A | G_B)$.

Using Bayes Theorem:
$$P(X_A | G_B) = \frac{P(G_B | X_A) P(X_A)}{P(G_B)}$$

We already have $P(X_A) = 1/3$ and $P(G_B | X_A) = 1/2$.
We need to calculate $P(G_B)$, the probability that the guard says B is released. We use the Law of Total Probability, partitioning the sample space by who is sentenced ($X_A, X_B, X_C$):

$$P(G_B) = P(G_B | X_A) P(X_A) + P(G_B | X_B) P(X_B) + P(G_B | X_C) P(X_C)$$

Substitute the values we found:
*   $P(G_B | X_A) = 1/2$
*   $P(G_B | X_B) = 0$
*   $P(G_B | X_C) = 1$
*   $P(X_A) = P(X_B) = P(X_C) = 1/3$

So,
$$P(G_B) = (1/2)(1/3) + (0)(1/3) + (1)(1/3) = 1/6 + 0 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2$$

Now, substitute $P(G_B)$ back into Bayes Theorem:
$$P(X_A | G_B) = \frac{P(G_B | X_A) P(X_A)}{P(G_B)} = \frac{(1/2)(1/3)}{1/2} = 1/3$$

The result $P(X_A | G_B) = 1/3$ means that the probability of you (Prisoner A) being sentenced *remains* $1/3$, even after the guard tells you B is released. Your chance of being released remains $2/3$. The guard's information (that B is released) is not new information about your fate but rather about C's fate.
If $P(X_A | G_B) = 1/3$, then $P(\text{A released} | G_B) = 1 - P(X_A | G_B) = 1 - 1/3 = 2/3$.

**Why is this counter-intuitive?**
When the guard says B is released, you might think only A and C are left. However, the guard's statement is not symmetric. He *could not* have said B was sentenced if B was going to be sentenced. The information "B is released" tells you nothing about A, but it strongly implies that C is the one more likely to be sentenced.
Let's calculate $P(X_C | G_B)$:
$$P(X_C | G_B) = \frac{P(G_B | X_C) P(X_C)}{P(G_B)} = \frac{(1)(1/3)}{1/2} = \frac{1/3}{1/2} = 2/3$$
So, after the guard's revelation, C's probability of being sentenced jumps from $1/3$ to $2/3$, while A's remains $1/3$. This is the power of updating beliefs with Bayes Theorem.

## Example 1: Tennis Tournament

Consider a tennis tournament. Your probability of winning against an opponent depends on their skill level. Suppose opponents are categorized into three types:

*   **Event A:** Opponent is a top-tier player. This accounts for $1/2$ of the players. Your probability of winning against such a player is $P(\text{Win} | A) = 0.3$.
*   **Event B:** Opponent is a mid-tier player. This accounts for $1/4$ of the players. Your probability of winning against such a player is $P(\text{Win} | B) = 0.4$.
*   **Event C:** Opponent is a novice player. This accounts for $1/4$ of the players. Your probability of winning against such a player is $P(\text{Win} | C) = 0.5$.

What is your overall probability of winning the next game?

Let $W$ be the event that you win the game. Let $A, B, C$ be the events that your opponent is a top-tier, mid-tier, or novice player, respectively. These three events form a partition of the sample space of opponents (an opponent must be one of these types, and cannot be more than one).

We are given:
*   $P(A) = 1/2$
*   $P(B) = 1/4$
*   $P(C) = 1/4$
*   $P(W|A) = 0.3$
*   $P(W|B) = 0.4$
*   $P(W|C) = 0.5$

We want to find $P(W)$. We can use the Law of Total Probability:
$$P(W) = P(W|A)P(A) + P(W|B)P(B) + P(W|C)P(C)$$

Plugging in the given values:
$$P(W) = (0.3)(1/2) + (0.4)(1/4) + (0.5)(1/4)$$
$$P(W) = (0.3)(0.5) + (0.4)(0.25) + (0.5)(0.25)$$
$$P(W) = 0.15 + 0.10 + 0.125$$
$$P(W) = 0.375$$

So, your overall probability of winning the next game is $0.375$ or $37.5\%$.

## Example 2: Communication Channel

Consider a noisy communication channel. We send binary data (0s and 1s).

*   The probability of sending a **1** is $P(\text{Send 1}) = p$.
*   The probability of sending a **0** is $P(\text{Send 0}) = 1-p$.

The channel introduces noise:
*   Given that a **1** is sent, the probability of receiving a **1** is $P(\text{Receive 1} | \text{Send 1}) = 1-\eta$. This implies $P(\text{Receive 0} | \text{Send 1}) = \eta$.
*   Given that a **0** is sent, the probability of receiving a **0** is $P(\text{Receive 0} | \text{Send 0}) = 1-\epsilon$. This implies $P(\text{Receive 1} | \text{Send 0}) = \epsilon$.

This can be visualized with a diagram:

```
          1-ε
  Send 0 ------$>$ Receive 0
     ^         ^
     | ε       | η
     |         |
     v         v
  Send 1 ------$>$ Receive 1
          1-η
```

Let's denote $S_1$ as "Send 1", $S_0$ as "Send 0", $R_1$ as "Receive 1", and $R_0$ as "Receive 0".

We are given:
*   $P(S_1) = p$
*   $P(S_0) = 1-p$
*   $P(R_1 | S_1) = 1-\eta$
*   $P(R_0 | S_1) = \eta$
*   $P(R_0 | S_0) = 1-\epsilon$
*   $P(R_1 | S_0) = \epsilon$

Let's find the required probabilities:

1.  **Find $P(R_1)$ (Probability of receiving a 1):**
    We use the Law of Total Probability, partitioning by what was sent ($S_0$ and $S_1$):
    $$P(R_1) = P(R_1 | S_0) P(S_0) + P(R_1 | S_1) P(S_1)$$
    $$P(R_1) = \epsilon (1-p) + (1-\eta) p$$
    $$P(R_1) = \epsilon - \epsilon p + p - \eta p$$
    $$P(R_1) = p(1-\epsilon-\eta) + \epsilon$$

2.  **Find $P(S_1)$ (Probability of sending a 1):**
    This is directly given:
    $$P(S_1) = p$$

3.  **Find $P(R_1 | S_1)$ (Probability of receiving a 1 given a 1 was sent):**
    This is also directly given:
    $$P(R_1 | S_1) = 1-\eta$$

4.  **Find $P(S_1 | R_1)$ (Probability of having sent a 1 given a 1 was received):**
    This is a classic application of Bayes Theorem. We want to infer what was sent given what was received.
    $$P(S_1 | R_1) = \frac{P(R_1 | S_1) P(S_1)}{P(R_1)}$$
    We have all the components from the previous calculations:
    *   $P(R_1 | S_1) = 1-\eta$
    *   $P(S_1) = p$
    *   $P(R_1) = p(1-\epsilon-\eta) + \epsilon$

    Substitute these into the Bayes Theorem formula:
    $$P(S_1 | R_1) = \frac{(1-\eta) p}{p(1-\epsilon-\eta) + \epsilon}$$

This value $P(S_1 | R_1)$ is crucial for channel decoding: it tells us, upon observing a '1' at the receiver, what is the most probable original transmitted symbol. If this probability is high, we can be confident that a '1' was indeed sent.

## Quick Summary

This lecture formalized two indispensable theorems in probability:
*   **Bayes Theorem:** $P(A|B) = \frac{P(B|A) P(A)}{P(B)}$. It allows us to update our prior belief about an event $A$ ($P(A)$) to a posterior belief ($P(A|B)$) after observing new evidence $B$, using the likelihood $P(B|A)$.
*   **Law of Total Probability:** $P(B) = \sum_{i=1}^{n} P(B|A_i) P(A_i)$. This theorem is essential for calculating the marginal probability of an event $B$ when the sample space is partitioned by a set of mutually exclusive and exhaustive events $A_i$. It often serves as the denominator in Bayes Theorem.

We demonstrated their application through:
1.  The **Prisoner's Dilemma**, illustrating how seemingly intuitive probability updates can be misleading without careful application of these theorems. We found that the guard's information about one prisoner being released doesn't change the probability of the *other* remaining prisoner (you) being sentenced, but rather shifts the probability of the *third* prisoner.
2.  A **Tennis Tournament** example, showing how to calculate an overall probability of winning by conditioning on different opponent types.
3.  A **Communication Channel** example, where we computed key probabilities for designing reliable communication systems, including inferring the transmitted signal given a received signal, a core concept in detection theory.

These theorems are fundamental for understanding how information is processed and how beliefs are updated in the face of uncertainty, forming the basis for many advanced topics in statistical inference, machine learning, and artificial intelligence.
