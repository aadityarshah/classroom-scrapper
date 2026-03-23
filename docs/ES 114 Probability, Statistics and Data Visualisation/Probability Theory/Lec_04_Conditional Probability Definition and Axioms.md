---
title: Conditional Probability Definition and Axioms
lecture_number: 4
lecture_name: Conditional Probability Definition and Axioms
category: Probability Theory
sidebar_label: Lecture 4
sidebar_position: 4
course: "ES 114 Probability, Statistics and Data Visualisation"
last_updated: "23 March 2026"
topic:
- Conditional Probability
- Definition of Conditional Probability
- Joint Probability vs. Conditional Probability
- Kolmogorov Axioms
- Axioms of Conditional Probability
tags:
- Probability
- Conditional Probability
- Axioms
- Probability Theory
- Events
- Sample Space
- Kolmogorov
summary: This lecture introduces the formal definition of conditional probability,
  distinguishes it from joint probability, illustrates it with conceptual Venn diagrams
  and practical examples, and explores its fundamental properties by verifying that
  it satisfies the axioms of probability.
math: true
---


# Conditional Probability: Definition and Axioms

This lecture formalizes the concept of conditional probability, a cornerstone of probabilistic reasoning. We will define it, differentiate it from joint probability, visualize it, and verify that it adheres to the fundamental axioms of probability theory.

## Definition of Conditional Probability

Let $A$ and $B$ be two events in a sample space $\Omega$.
The **conditional probability** of event $A$ occurring given that event $B$ has already occurred is denoted as $P[A|B]$.
It is formally defined under the assumption that $P[B] \neq 0$.

$$ P[A|B] \stackrel{\text{def}}{=} \frac{P[A \cap B]}{P[B]} \quad (1) $$

This definition implies that when we condition on event $B$, our sample space effectively shrinks to $B$, and we are interested in the proportion of $A$ within this new, restricted sample space $B$.

### Distinction from Joint Probability

It is crucial to understand the difference between conditional probability $P[A|B]$ and the joint probability $P[A \cap B]$.

*   $P[A \cap B]$ represents the probability that *both* events $A$ and $B$ occur within the entire sample space $\Omega$.
    $$ P[A \cap B] = \frac{P[A \cap B]}{P[\Omega]} \quad (2) $$
    Since $P[\Omega] = 1$, this simplifies to $P[A \cap B]$.
*   $P[A|B]$ represents the probability of $A$ occurring *given that $B$ has already occurred*. The sample space is effectively restricted to $B$.

### Visual Illustration

Consider the conceptual illustration of conditional probability using Venn diagrams:
Imagine a Venn diagram with two overlapping circles, $A$ and $B$, within a rectangle representing the entire sample space $\Omega$.

*   When considering $P[A \cap B]$, we are looking at the area of overlap between $A$ and $B$ relative to the total area of $\Omega$.
*   When considering $P[A|B]$, we are effectively shrinking our "universe" to only include event $B$. Within this new universe (the circle $B$), we then measure the proportion of $A$ that is present. This proportion is precisely the overlap region $A \cap B$ relative to the size of $B$.

## Examples of Conditional Probability

Let's explore several examples to solidify our understanding of conditional probability.

### Example 1: Burgers and Football

Let's define two events:
*   $A = \{"\text{Eat 2 burgers}"\}$
*   $B = \{"\text{Finish a football game}"\}$

In this context:
*   $P[A]$ = The overall probability that you eat 2 burgers.
*   $P[B]$ = The overall probability that you just finish a football game.
*   $P[A \cap B]$ = The probability that you finish a football game *and* you eat 2 burgers.
*   $P[A|B]$ = The probability that you eat 2 burgers *given that you have just finished a football game*. Intuitively, having just finished a strenuous game might influence the likelihood of eating a certain amount of food.

### Example 2: Rolling a Die

Consider rolling a standard six-sided die.
Let $A = \{"\text{Get 3}"\}$ and $B = \{"\text{odd numbers}"\}$.
We want to find $P[A|B]$ and $P[B|A]$.

The sample space is $\Omega = \{1, 2, 3, 4, 5, 6\}$. Each outcome has a probability of $1/6$.
*   Event $A = \{3\}$. So $P[A] = 1/6$.
*   Event $B = \{1, 3, 5\}$. So $P[B] = 3/6 = 1/2$.
*   The intersection $A \cap B = \{3\}$. So $P[A \cap B] = 1/6$.

Now, let's calculate the conditional probabilities using the definition:
*   $P[A|B] = \frac{P[A \cap B]}{P[B]} = \frac{1/6}{1/2} = \frac{1}{3}$.
    This means if we know the outcome is an odd number (which could be 1, 3, or 5), there's a 1 in 3 chance that the outcome is a 3.
*   $P[B|A] = \frac{P[A \cap B]}{P[A]} = \frac{1/6}{1/6} = 1$.
    This means if we know the outcome is a 3, it is certain that the outcome is an odd number.

### Example 3: Discrete Sample Space (12 Points)

Consider a sample space $\Omega$ composed of 12 equally likely points. Let's define events A and B based on a visual representation (e.g., a Venn diagram with points).

From the visual, assume:
*   Total points in $\Omega = 12$. Each point has probability $1/12$.
*   Points belonging to event A: 5 points. So $P[A] = 5/12$.
*   Points belonging to event B: 6 points. So $P[B] = 6/12 = 1/2$.
*   Points in the intersection $A \cap B$: 2 points. So $P[A \cap B] = 2/12 = 1/6$.

Now, calculate the conditional probabilities:
*   $P[A|B] = \frac{P[A \cap B]}{P[B]} = \frac{2/12}{6/12} = \frac{2}{6} = \frac{1}{3}$.
*   $P[B|A] = \frac{P[A \cap B]}{P[A]} = \frac{2/12}{5/12} = \frac{2}{5}$.

### Example 4: Two 4-Sided Dice Rolls

Let $X$ be the outcome of the first 4-sided die roll, and $Y$ be the outcome of the second. The sample space consists of $4 \times 4 = 16$ equally likely pairs $(X, Y)$.

Let $B$ be the event that $\min(X, Y) = 2$.
Let $M$ be the event that $\max(X, Y) = 3$.
We want to find $P[M|B]$.

First, identify the outcomes for each event:
*   The entire sample space $\Omega = \{(x,y) | x,y \in \{1,2,3,4\}\}$ has $|\Omega|=16$ outcomes.
*   Event $B = \{(x,y) | \min(x,y)=2\}$:
    $B = \{(2,2), (2,3), (2,4), (3,2), (4,2)\}$.
    $|B| = 5$. So $P[B] = 5/16$.
*   Event $M = \{(x,y) | \max(x,y)=3\}$:
    $M = \{(1,3), (2,3), (3,3), (3,2), (3,1)\}$.
    $|M| = 5$. So $P[M] = 5/16$.
*   The intersection $M \cap B$: outcomes common to both $M$ and $B$.
    $M \cap B = \{(2,3), (3,2)\}$.
    $|M \cap B| = 2$. So $P[M \cap B] = 2/16 = 1/8$.

Finally, calculate $P[M|B]$ using the conditional probability definition:
$$ P[M|B] = \frac{P[M \cap B]}{P[B]} = \frac{2/16}{5/16} = \frac{2}{5} $$

## Axioms of Conditional Probability

A crucial property of conditional probability is that it itself satisfies the three Kolmogorov axioms of probability. This means that if we restrict our sample space to event $B$, the function $P[\cdot|B]$ behaves like a valid probability measure on this new space.

**Proposition:** Let $B$ be an event such that $P[B] > 0$. The conditional probability $P[A|B]$ for any event $A$ satisfies Axiom I, Axiom II, and Axiom III of probability.

Let's verify each axiom:

### Axiom 1: Non-negativity

For any event $A$, $P[A|B] \ge 0$.

**Proof:**
By definition, $P[A|B] = \frac{P[A \cap B]}{P[B]}$.
From the original Axiom I of probability, we know that the probability of any event is non-negative. Therefore, $P[A \cap B] \ge 0$.
We are given that $P[B] > 0$.
A non-negative number divided by a positive number must be non-negative. Hence, $P[A|B] \ge 0$.

### Axiom 2: Normalization

For the sample space $\Omega$, $P[\Omega|B] = 1$.

**Proof:**
By definition, $P[\Omega|B] = \frac{P[\Omega \cap B]}{P[B]}$.
The intersection of the sample space $\Omega$ with any event $B$ is simply $B$ itself (i.e., $\Omega \cap B = B$).
Thus, $P[\Omega|B] = \frac{P[B]}{P[B]}$.
Since we assumed $P[B] > 0$, we can simplify this to $P[\Omega|B] = 1$.

### Axiom 3: Countable Additivity

For a sequence of mutually exclusive (disjoint) events $A_1, A_2, \ldots$,
$$ P[A_1 \cup A_2 \cup \dots | B] = P[A_1|B] + P[A_2|B] + \dots = \sum_{i=1}^{\infty} P[A_i|B] $$

**Proof:**
Let $A = A_1 \cup A_2 \cup \dots = \bigcup_{i=1}^{\infty} A_i$.
By the definition of conditional probability, $P[A|B] = \frac{P[A \cap B]}{P[B]} = \frac{P[(\bigcup_{i=1}^{\infty} A_i) \cap B]}{P[B]}$.
Using the distributive property of set intersection over union, we can write $(\bigcup_{i=1}^{\infty} A_i) \cap B = \bigcup_{i=1}^{\infty} (A_i \cap B)$.
Since $A_1, A_2, \ldots$ are mutually exclusive events, their intersections with $B$, i.e., $A_1 \cap B, A_2 \cap B, \ldots$, are also mutually exclusive.
Applying the original Axiom III (countable additivity for disjoint events) to the numerator $P[(\bigcup_{i=1}^{\infty} (A_i \cap B))]$, we get:
$P[\bigcup_{i=1}^{\infty} (A_i \cap B)] = \sum_{i=1}^{\infty} P[A_i \cap B]$.
Substituting this back into the conditional probability expression:
$$ P[A|B] = \frac{\sum_{i=1}^{\infty} P[A_i \cap B]}{P[B]} = \sum_{i=1}^{\infty} \frac{P[A_i \cap B]}{P[B]} $$
Recognizing each term in the sum as the definition of $P[A_i|B]$:
$$ P[A|B] = \sum_{i=1}^{\infty} P[A_i|B] $$
Thus, conditional probability satisfies Axiom III.

## Quick Summary

This lecture defined **conditional probability** $P[A|B]$ as the probability of event $A$ occurring given that event $B$ has already occurred, formally expressed as $P[A|B] = P[A \cap B] / P[B]$, assuming $P[B] > 0$. We distinguished it from joint probability $P[A \cap B]$, emphasizing that conditional probability conceptually redefines the sample space to the conditioning event $B$. Through various examples, including dice rolls and discrete point spaces, we applied this definition to calculate conditional probabilities. Crucially, we demonstrated that conditional probability itself adheres to the three **Kolmogorov axioms of probability**, proving its validity as a probability measure within the restricted sample space defined by the conditioning event.
