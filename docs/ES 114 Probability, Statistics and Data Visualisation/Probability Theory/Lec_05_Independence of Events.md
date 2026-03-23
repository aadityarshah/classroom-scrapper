---
title: "Independence"
lecture_number: 5
lecture_name: "Independence of Events"
category: "Probability Theory"
sidebar_label: "Lecture 5"
sidebar_position: 5
course: "ES 114 Probability, Statistics and Data Visualisation"
last_updated: "23 March 2026"
topic:
  - "Probability"
  - "Event Independence"
  - "Conditional Probability"
tags:
  - "Probability"
  - "Events"
  - "Independence"
  - "Conditional Probability"
  - "Dice Rolling"
summary: "This lecture introduces the fundamental concept of statistical independence between events. We explore both an intuitive understanding and the rigorous mathematical definition, contrasting it with disjoint events. Through various examples involving dice rolls, we demonstrate how to determine if two events are independent using both the product rule and conditional probability definitions, highlighting its importance in probabilistic modeling."
math: true
---

## Introduction to Event Independence

Welcome to Lecture 5 of ECE 302, where we delve into one of the most crucial concepts in probability theory: **independence of events**. Understanding independence is fundamental for simplifying probabilistic calculations and accurately modeling real-world phenomena.

Previously, we've discussed set theory, probability spaces, axioms of probability, and conditional probability. Today, we build upon these foundations to define and identify independent events.

### Lecture Outline
This lecture will cover:
*   **What is independence?** - An intuitive understanding.
*   **Mathematical Definition** - The rigorous formulation.
*   **Independence via Conditional Probability** - An alternative perspective.
*   **Examples** - Practical applications and calculations using dice rolls.

---

## What is Independence? Intuition Through Examples

At its core, two events are independent if the occurrence of one does not influence the probability of the other. Let's explore this with dice-rolling scenarios.

### The Game of Throw Dices — Easy Case

Consider throwing a fair six-sided die twice. Let's define two events:
*   Event $A$: The first die is a 3.
*   Event $B$: The second die is a 4.

**Are $A$ and $B$ independent?**
Intuitively, the outcome of the first die roll should not affect the outcome of the second die roll. If you know the first die was a 3, it doesn't change your belief about the probability of the second die being a 4. In this case, it feels natural to say these events are independent.

### The Game of Throw Dices — Hard Case

Now, let's consider a slightly more complex scenario with two fair dice rolls:
*   Event $A$: The first die is a 1.
*   Event $B$: The sum of the two dice is 7.

**Are $A$ and $B$ independent?**
Let's think about this:
*   The probability of $A$ (first die is 1) is $1/6$.
*   If you know that the sum of the two dice is 7, the possible pairs are $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$. There are 6 such outcomes.
*   Among these 6 outcomes where the sum is 7, how many have the first die as 1? Only one: $(1,6)$.
*   So, the probability of the first die being 1, *given* that the sum is 7, is $1/6$.
*   Since $P(\text{1st die is 1 } | \text{ sum is 7}) = 1/6$, and $P(\text{1st die is 1}) = 1/6$, the probability of $A$ hasn't changed knowing $B$ occurred. This suggests $A$ and $B$ are independent.

This "hard case" demonstrates that intuition can sometimes be misleading, and we need a precise mathematical definition.

---

## Mathematical Definition of Independence

Two events $A$ and $B$ are **statistically independent** if and only if:

$$
P(A \cap B) = P(A)P(B)
$$

This is the foundational definition. If this equality holds, the events are independent; otherwise, they are dependent.

### Disjoint VS Independent

It is crucial to distinguish between **disjoint** (mutually exclusive) and **independent** events.
*   **Disjoint events:** Two events $A$ and $B$ are disjoint if $A \cap B = \emptyset$. This means they cannot occur at the same time. If $A$ occurs, $B$ cannot, and vice versa.
    *   For disjoint events (assuming $P(A) > 0$ and $P(B) > 0$), $P(A \cap B) = P(\emptyset) = 0$.
    *   For them to also be independent, $P(A)P(B)$ would have to be 0, which implies either $P(A)=0$ or $P(B)=0$.
    *   Therefore, non-trivial disjoint events (events with non-zero probability) are always **dependent**. The occurrence of one makes the other impossible, thus strongly affecting its probability.

---

## Independence Via Conditional Probability

Recall the definition of conditional probability:
$$
P(A|B) = \frac{P(A \cap B)}{P(B)} \quad \text{provided } P(B) > 0
$$

If events $A$ and $B$ are independent, we know that $P(A \cap B) = P(A)P(B)$. Substituting this into the conditional probability formula:
$$
P(A|B) = \frac{P(A)P(B)}{P(B)} = P(A)
$$

This leads to an equally important interpretation of independence:
**Interpretation:** Two events $A$ and $B$ are independent if $P(A|B) = P(A)$ (provided $P(B) > 0$), and similarly, $P(B|A) = P(B)$ (provided $P(A) > 0$).
In words, the occurrence of event $B$ does not change the probability of event $A$ occurring. The ratio of $A$'s probability within $B$ is the same as $A$'s probability within the entire sample space $\Omega$.

### Pictorial Illustration

Imagine event $A$ and event $B$ as regions in a sample space $\Omega$.
*   $P(A)$ represents the "proportion" of $A$ relative to $\Omega$.
*   $P(A|B)$ represents the "proportion" of $A$ (specifically, $A \cap B$) relative to $B$.
*   If $A$ and $B$ are independent, then $P(A|B) = P(A)$, meaning the relative proportion of $A$ within $B$ is the same as its relative proportion within the entire sample space $\Omega$.

---

## Examples of Independence

Let's apply our definitions to some concrete examples using two fair six-sided dice. The total sample space $\Omega$ consists of $6 \times 6 = 36$ equally likely outcomes.

### Example 1: Independent Dice Rolls

**Problem:** Throw a dice twice. Let $A = \{\text{1st dice is 3}\}$ and $B = \{\text{2nd dice is 4}\}$. Are $A$ and $B$ independent?

**Solution:**
1.  **Calculate $P(A)$:**
    The outcomes for $A$ are $\{(3,1), (3,2), (3,3), (3,4), (3,5), (3,6)\}$. There are 6 such outcomes.
    $P(A) = 6/36 = 1/6$.
2.  **Calculate $P(B)$:**
    The outcomes for $B$ are $\{(1,4), (2,4), (3,4), (4,4), (5,4), (6,4)\}$. There are 6 such outcomes.
    $P(B) = 6/36 = 1/6$.
3.  **Calculate $P(A \cap B)$:**
    The event $A \cap B$ means the first die is 3 AND the second die is 4.
    The only outcome is $\{(3,4)\}$.
    $P(A \cap B) = 1/36$.
4.  **Check for independence:** Is $P(A \cap B) = P(A)P(B)$?
    $P(A)P(B) = (1/6)(1/6) = 1/36$.
    Since $1/36 = 1/36$, events $A$ and $B$ are **independent**. This confirms our intuition from the "easy case".

### Example 2: First Die vs. Sum (Sum is 7)

**Problem:** Throw a dice twice. Let $A = \{\text{1st dice is 1}\}$ and $B = \{\text{sum is 7}\}$. Are $A$ and $B$ independent?

**Solution:**
1.  **Calculate $P(A)$:**
    $P(A) = 6/36 = 1/6$.
2.  **Calculate $P(B)$:**
    The outcomes for $B$ (sum is 7) are $\{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$. There are 6 such outcomes.
    $P(B) = 6/36 = 1/6$.
3.  **Calculate $P(A \cap B)$:**
    The event $A \cap B$ means the first die is 1 AND the sum is 7.
    The only outcome is $\{(1,6)\}$.
    $P(A \cap B) = 1/36$.
4.  **Check for independence:** Is $P(A \cap B) = P(A)P(B)$?
    $P(A)P(B) = (1/6)(1/6) = 1/36$.
    Since $1/36 = 1/36$, events $A$ and $B$ are **independent**. This aligns with our earlier "hard case" analysis.

### Example 3: First Die vs. Sum (Sum is 8)

**Problem:** Throw a dice twice. Let $A = \{\text{1st dice is 2}\}$ and $B = \{\text{sum is 8}\}$. Are $A$ and $B$ independent?

**Solution:**
1.  **Calculate $P(A)$:**
    $P(A) = 6/36 = 1/6$.
2.  **Calculate $P(B)$:**
    The outcomes for $B$ (sum is 8) are $\{(2,6), (3,5), (4,4), (5,3), (6,2)\}$. There are 5 such outcomes.
    $P(B) = 5/36$.
3.  **Calculate $P(A \cap B)$:**
    The event $A \cap B$ means the first die is 2 AND the sum is 8.
    The only outcome is $\{(2,6)\}$.
    $P(A \cap B) = 1/36$.
4.  **Check for independence:** Is $P(A \cap B) = P(A)P(B)$?
    $P(A)P(B) = (1/6)(5/36) = 5/216$.
    We compare $1/36$ with $5/216$. To do this, we can write $1/36$ as $6/216$.
    Since $1/36 = 6/216 \ne 5/216$, events $A$ and $B$ are **dependent**.

**Interpretation using Conditional Probability:**
Let's verify this using $P(A|B) = P(A)$.
$P(A|B) = P(A \cap B) / P(B) = (1/36) / (5/36) = 1/5$.
Since $P(A|B) = 1/5$ and $P(A) = 1/6$, and $1/5 \ne 1/6$, we confirm that $A$ and $B$ are dependent. Knowing the sum is 8 *changes* the probability that the first die was 2.

### Example 4: Max vs. Min of Two Dice

**Problem:** Throw a dice twice. Let $A = \{\max \text{ is 2}\}$ and $B = \{\min \text{ is 2}\}$. Are $A$ and $B$ independent?

**Solution:**
1.  **Calculate $P(A)$:**
    Event $A = \{\max \text{ is 2}\}$. This means the highest value rolled is 2. The possible outcomes are both dice being $\le 2$, with at least one die being exactly 2.
    Outcomes: $(1,2), (2,1), (2,2)$. There are 3 such outcomes.
    $P(A) = 3/36 = 1/12$.
2.  **Calculate $P(B)$:**
    Event $B = \{\min \text{ is 2}\}$. This means the lowest value rolled is 2. The possible outcomes are both dice being $\ge 2$, with at least one die being exactly 2.
    Outcomes:
    $(2,2), (2,3), (2,4), (2,5), (2,6)$
    $(3,2), (4,2), (5,2), (6,2)$
    There are $1+5+4 = 9$ such outcomes (excluding (2,2) from the second row to avoid double counting, or simply count them: 5 for first row + 4 for second row (3,2),(4,2),(5,2),(6,2)).
    $P(B) = 9/36 = 1/4$.
3.  **Calculate $P(A \cap B)$:**
    Event $A \cap B = \{\max \text{ is 2 AND } \min \text{ is 2}\}$. This means both the highest and lowest values are 2, which implies both dice must be 2.
    Outcome: $(2,2)$.
    $P(A \cap B) = 1/36$.
4.  **Check for independence:** Is $P(A \cap B) = P(A)P(B)$?
    $P(A)P(B) = (1/12)(1/4) = 1/48$.
    Since $1/36 \ne 1/48$, events $A$ and $B$ are **dependent**.

---

## Why Is Independence Important?

The concept of independence is fundamental across various fields for several reasons:
*   **Simplification of Calculations:** When events are independent, calculating the probability of their intersection becomes a simple product of their individual probabilities ($P(A \cap B) = P(A)P(B)$), which greatly simplifies complex problems.
*   **Modeling Real-World Phenomena:** Many natural processes and engineered systems involve components whose behaviors are independent (e.g., successive coin flips, failures of redundant systems). Understanding independence allows for accurate probabilistic modeling of these systems.
*   **Statistical Inference:** In statistics, assumptions of independence (e.g., independent and identically distributed random variables) are common and allow for powerful analytical tools and hypothesis testing.
*   **Causality:** While independence does not imply causation (or lack thereof), it's a key concept in reasoning about causal relationships. If events are dependent, there might be an underlying causal link or a common cause.

The graphical representation of dependent versus independent data (as seen in Slide 14) illustrates how dependent data might show patterns or correlations, while independent data often appears more random or uninfluenced by other factors.

---

## Quick Summary

*   **Definition:** Two events $A$ and $B$ are statistically independent if $P(A \cap B) = P(A)P(B)$.
*   **Conditional Probability Equivalence:** If $A$ and $B$ are independent, then $P(A|B) = P(A)$ (if $P(B) > 0$) and $P(B|A) = P(B)$ (if $P(A) > 0$). This means knowing one event occurred does not change the probability of the other.
*   **Disjoint vs. Independent:** Non-trivial disjoint events (events with non-zero probability that cannot occur simultaneously) are always dependent, as the occurrence of one makes the other impossible ($P(A \cap B) = 0$ but $P(A)P(B) \ne 0$).
*   **Importance:** Independence simplifies probability calculations, is crucial for modeling various real-world systems, and forms a cornerstone of statistical inference.
