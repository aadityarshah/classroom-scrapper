---
title: "Axioms of Probability and Their Corollaries"
lecture_number: 3
lecture_name: "Axioms of Probability and Fundamental Properties"
category: "Probability Theory"
sidebar_label: "Lecture 3"
sidebar_position: 3
course: "ES 114 Probability, Statistics and Data Visualisation"
last_updated: "23 March 2026"
topic:
  - Axioms of Probability
  - Probability Law
  - Properties of Probability
  - Set Theory in Probability
tags:
  - probability
  - axioms
  - set theory
  - events
  - sample space
  - corollaries
  - union bound
  - addition rule
math: true
summary: "This lecture introduces the foundational Kolgomorov axioms of probability, which define how probabilities are assigned to events. We explore the three core axioms—non-negativity, normalization, and countable additivity—and derive several essential properties (corollaries) that are crucial for solving probability problems, including the complement rule, the general addition rule, and the union bound. We conclude with illustrative examples to solidify understanding."
---

## Introduction to Probability Theory

In the previous lectures, we established the fundamental concepts of set theory and the probability space, which comprises a sample space $\Omega$, a sigma-algebra of events $\mathcal{F}$, and a probability measure $P$. This lecture delves into the core principles governing the assignment of probabilities: the **Axioms of Probability**. These axioms, first formalized by Andrey Kolmogorov, provide a rigorous mathematical foundation for the entire field of probability theory. They are minimal and non-redundant, yet powerful enough to derive all other useful properties of probability.

## Defining Probability Law

A **probability law**, or **probability measure**, is a function $P: \mathcal{F} \rightarrow [0, 1]$ that maps an event $A \in \mathcal{F}$ to a real number $P(A)$ in the interval $[0, 1]$. This function quantifies the likelihood of event $A$ occurring. For $P$ to be a valid probability law, it must satisfy three fundamental axioms.

### The Three Axioms of Probability

The three axioms ensure consistency and allow for the derivation of more complex probability rules.

### Axiom I: Non-negativity

The probability of any event must be non-negative.
For any event $A \in \mathcal{F}$:
$$ P(A) \ge 0 $$
This axiom simply states that probabilities cannot be negative. The least likely an event can be is impossible, which is assigned a probability of 0.

### Axiom II: Normalization

The probability of the entire sample space $\Omega$ must be equal to 1.
$$ P(\Omega) = 1 $$
This axiom asserts that something in the sample space must occur. The sample space $\Omega$ represents the set of all possible outcomes, so the total probability of all possible outcomes must be 1.

### Axiom III: Countable Additivity

For any sequence of disjoint events $A_1, A_2, \ldots, A_n, \ldots$ (meaning $A_i \cap A_j = \emptyset$ for $i \ne j$), the probability of their union is the sum of their individual probabilities.
$$ P\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n) $$
This axiom is crucial for handling situations with an infinite number of outcomes or composite events. A special case of this axiom is for a finite number of disjoint events: if $A$ and $B$ are disjoint (i.e., $A \cap B = \emptyset$), then $P(A \cup B) = P(A) + P(B)$. This property is visually represented by Venn diagrams where the areas of disjoint events simply add up.

## Corollaries and Properties Derived from the Axioms

From these three fundamental axioms, we can derive numerous other useful properties and rules of probability. These are often referred to as corollaries or propositions.

### 1. Probability of the Complement

For any event $A \in \mathcal{F}$, the probability of its complement $A^c$ (the event that $A$ does not occur) is:
$$ P(A^c) = 1 - P(A) $$
This is derived by noting that $A$ and $A^c$ are disjoint, and their union is the entire sample space $\Omega$. Thus, $P(A \cup A^c) = P(\Omega)$. By Axiom III, $P(A) + P(A^c) = P(\Omega)$, and by Axiom II, $P(\Omega) = 1$. Therefore, $P(A) + P(A^c) = 1$.

### 2. Probability of the Empty Set

The probability of the empty set $\emptyset$ (the impossible event) is 0.
$$ P(\emptyset) = 0 $$
This can be proven using the complement rule: $P(\emptyset) = P(\Omega^c) = 1 - P(\Omega) = 1 - 1 = 0$.

### 3. Monotonicity of Probability

If event $A$ is a subset of event $B$ (i.e., $A \subseteq B$), then the probability of $A$ is less than or equal to the probability of $B$.
$$ \text{If } A \subseteq B, \text{ then } P(A) \le P(B) $$
**Proof:**
If $A \subseteq B$, we can write $B$ as the union of two disjoint events: $B = A \cup (B \cap A^c)$.
Then, by Axiom III (finite additivity):
$P(B) = P(A) + P(B \cap A^c)$.
Since $B \cap A^c$ is an event, by Axiom I, $P(B \cap A^c) \ge 0$.
Therefore, $P(B) \ge P(A)$.

This property also implies that for any event $A$, $P(A) \le P(\Omega)$, which means $P(A) \le 1$. Coupled with Axiom I ($P(A) \ge 0$), this confirms that probabilities always lie within the range $[0, 1]$.

### 4. The General Addition Rule (Principle of Inclusion-Exclusion for two events)

For any two events $A$ and $B$ (not necessarily disjoint), the probability of their union is:
$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$
This rule accounts for the overlap between $A$ and $B$. If we simply add $P(A)$ and $P(B)$, the probability of their intersection $P(A \cap B)$ is counted twice, so it must be subtracted once.

**Proof for Property 4:**
We can express the union $A \cup B$ as a union of disjoint events:
$A \cup B = A \cup (B \cap A^c)$.
Since $A$ and $(B \cap A^c)$ are disjoint, by Axiom III:
$$ P(A \cup B) = P(A) + P(B \cap A^c) \quad (*)$$
Now, consider event $B$. We can express $B$ as the union of two disjoint events:
$B = (A \cap B) \cup (A^c \cap B)$.
By Axiom III:
$$ P(B) = P(A \cap B) + P(A^c \cap B) $$
Rearranging this, we get:
$$ P(A^c \cap B) = P(B) - P(A \cap B) $$
Substitute this back into equation $(*)$:
$$ P(A \cup B) = P(A) + (P(B) - P(A \cap B)) $$
$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$
This completes the proof.

### 5. The Union Bound

For any two events $A$ and $B$, the probability of their union is less than or equal to the sum of their individual probabilities.
$$ P(A \cup B) \le P(A) + P(B) $$
This is a direct consequence of the General Addition Rule because $P(A \cap B) \ge 0$ (by Axiom I), so removing it from $P(A) + P(B)$ can only make the value smaller or keep it the same.

## Examples

Let the events $A$ and $B$ have probabilities $P(A) = x$, $P(B) = y$, and $P(A \cup B) = z$. We will use the axioms and derived properties to find the following probabilities.

**(a) Find $P(A \cap B)$**

Using the General Addition Rule:
$P(A \cup B) = P(A) + P(B) - P(A \cap B)$
Substituting the given values:
$z = x + y - P(A \cap B)$
Solving for $P(A \cap B)$:
$P(A \cap B) = x + y - z$

**(b) Find $P(A^c \cap B^c)$**

We can use De Morgan's Laws, which state that $(A \cup B)^c = A^c \cap B^c$.
Therefore, $P(A^c \cap B^c) = P((A \cup B)^c)$.
Using the Probability of the Complement rule:
$P((A \cup B)^c) = 1 - P(A \cup B)$
Substituting the given value for $P(A \cup B)$:
$P(A^c \cap B^c) = 1 - z$

**(c) Find $P(A^c \cup B^c)$**

Again, using De Morgan's Laws, we know that $(A \cap B)^c = A^c \cup B^c$.
Therefore, $P(A^c \cup B^c) = P((A \cap B)^c)$.
Using the Probability of the Complement rule:
$P((A \cap B)^c) = 1 - P(A \cap B)$
From part (a), we found $P(A \cap B) = x + y - z$.
Substituting this into the equation:
$P(A^c \cup B^c) = 1 - (x + y - z) = 1 - x - y + z$

**(d) Find $P(A \cap B^c)$**

The event $A \cap B^c$ represents the outcomes that are in $A$ but not in $B$. This is often denoted as $A \setminus B$.
We can express $A$ as the union of two disjoint events: $A = (A \cap B) \cup (A \cap B^c)$.
By Axiom III (additivity for disjoint events):
$P(A) = P(A \cap B) + P(A \cap B^c)$
Solving for $P(A \cap B^c)$:
$P(A \cap B^c) = P(A) - P(A \cap B)$
Substituting the given value $P(A) = x$ and the result from part (a) $P(A \cap B) = x + y - z$:
$P(A \cap B^c) = x - (x + y - z)$
$P(A \cap B^c) = x - x - y + z$
$P(A \cap B^c) = z - y$

## Quick Summary

This lecture established the three fundamental **Kolmogorov Axioms of Probability**:
1.  **Non-negativity**: $P(A) \ge 0$ for any event $A$.
2.  **Normalization**: $P(\Omega) = 1$, where $\Omega$ is the sample space.
3.  **Countable Additivity**: For disjoint events $A_1, A_2, \ldots$, $P\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} P(A_n)$.

From these axioms, we derived several critical **properties (corollaries)**:
*   **Complement Rule**: $P(A^c) = 1 - P(A)$.
*   **Probability of Impossible Event**: $P(\emptyset) = 0$.
*   **Monotonicity**: If $A \subseteq B$, then $P(A) \le P(B)$, implying $0 \le P(A) \le 1$.
*   **General Addition Rule**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
*   **Union Bound**: $P(A \cup B) \le P(A) + P(B)$.

These axioms and properties form the bedrock of probability theory, enabling us to calculate probabilities for various complex scenarios, as demonstrated by the examples in this lecture.
