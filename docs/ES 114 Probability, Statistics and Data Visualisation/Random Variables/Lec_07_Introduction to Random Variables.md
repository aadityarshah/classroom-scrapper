---
title: Random Variables Introduction
lecture_number: 7
lecture_name: Introduction to Random Variables
category: Random Variables
sidebar_label: Lecture 7
sidebar_position: 7
course: "ES 114 Probability, Statistics and Data Visualisation"
topic:
- Random Variables
- Sample Space Mapping
tags:
- Random Variables
- Probability
- Sample Space
- Inverse Mapping
- Functions
math: true
summary: This lecture introduces the fundamental concept of random variables as functions
  that map outcomes from a sample space to numerical values. It clarifies why random
  variables are necessary for mathematical convenience, details their formal definition,
  and explains how probabilities are calculated by utilizing the inverse mapping back
  to the original sample space.
last_updated: "31 March 2026"
---


# Introduction to Random Variables

In probability theory, experiments often yield outcomes that are descriptive rather than inherently numerical (e.g., "Head," "Tail," "rainy," "sunny"). While these can be analyzed directly, mathematical operations like averaging or calculating variance become complex. **Random variables** serve as a crucial bridge, translating these descriptive outcomes into numerical values, thereby simplifying mathematical analysis.

## 1. Why We Need Random Variables

Consider computing probabilities for events described verbally:
*   "Probability of getting a head": $P[\text{"Head"}]$
*   "Probability of getting 3 heads in 3 coin flips": $P[\text{"Head"} \cap \text{"Head"} \cap \text{"Head"}]$

This notation is often unwieldy. By introducing random variables, we assign numbers to outcomes. For instance, in a coin flip, we can define "Head" as 1 and "Tail" as 0. If $X$ is the sum of heads:
*   $P[\text{"Head"}]$ becomes $P[X=1]$.
*   $P[\text{"Head"} \cap \text{"Head"} \cap \text{"Head"}]$ becomes $P[X=3]$.

This numerical translation streamlines both notation and subsequent calculations for concepts like expectation and variance.

## 2. Formal Definition of a Random Variable

A **random variable** is a function that maps outcomes from a sample space to a numerical value on the real line.

**Definition:** A random variable $X$ is a function $X: \Omega \rightarrow \mathbb{R}$ that maps an outcome $\xi \in \Omega$ from the sample space to a number $X(\xi)$ on the real line $\mathbb{R}$.

*   **Sample Space ($\Omega$):** The set of all possible outcomes of a random experiment. Outcomes $\xi$ can be non-numerical or complex.
*   **Real Line ($\mathbb{R}$):** The set of all real numbers. Random variables transform outcomes into these numerical values.

The primary purpose is to convert qualitative descriptions into quantitative data.

### Example: Two Coin Flips

Consider flipping a fair coin two times.
The sample space is $\Omega = \{ \text{HH, HT, TH, TT} \}$.

Let's define a random variable $X$ as the **number of heads** observed.
*   For the outcome $\xi_1 = \text{HH}$, $X(\xi_1) = X(\text{HH}) = 2$.
*   For the outcome $\xi_2 = \text{HT}$, $X(\xi_2) = X(\text{HT}) = 1$.
*   For the outcome $\xi_3 = \text{TH}$, $X(\xi_3) = X(\text{TH}) = 1$.
*   For the outcome $\xi_4 = \text{TT}$, $X(\xi_4) = X(\text{TT}) = 0$.

Here, $X$ effectively translates textual outcomes into numerical counts.

## 3. Calculating Probabilities for Random Variables: The Inverse Mapping

When we seek to calculate the probability $P[X=a]$ (i.e., the probability that the random variable $X$ takes a specific numerical value $a$), we are referring to an event in the numerical domain. However, standard probability measures $P$ are defined over events within the original sample space $\Omega$. To bridge this, we use the concept of an **inverse image**.

The event $\{X=a\}$ signifies that the random variable $X$ evaluates to $a$. To find its probability, we must determine which outcomes in $\Omega$ correspond to this condition.

The **inverse image** of $a$, denoted $X^{-1}(a)$, is the set of all outcomes $\xi \in \Omega$ such that $X(\xi) = a$.
$$ X^{-1}(a) = \{ \xi \in \Omega \mid X(\xi) = a \} $$
Crucially, this set $X^{-1}(a)$ **is an event in the sample space $\Omega$**. Since it's an event within $\Omega$, its probability can be directly measured by the probability measure $P$.

Thus, the probability $P[X=a]$ is calculated as:
$$ P[X=a] = P(X^{-1}(a)) = P(\{ \xi \in \Omega \mid X(\xi) = a \}) $$

### Example: Probability of One Head in Two Coin Flips

Using our prior example where $X$ is the number of heads in two coin flips ($\Omega = \{ \text{HH, HT, TH, TT} \}$, with each outcome having probability $1/4$):
We want to find $P[X=1]$.

1.  **Identify $a$:** Here, $a=1$.
2.  **Find the inverse image $X^{-1}(1)$:** We identify outcomes $\xi \in \Omega$ where $X(\xi) = 1$.
    *   $X(\text{HT}) = 1$
    *   $X(\text{TH}) = 1$
    Therefore, $X^{-1}(1) = \{\text{HT, TH}\}$.
3.  **Calculate the probability:**
    $$ P[X=1] = P(\{\text{HT, TH}\}) = P(\text{HT}) + P(\text{TH}) = \frac{1}{4} + \frac{1}{4} = \frac{2}{4} = \frac{1}{2} $$

### Example: Probability of Sum 7 in Two Dice Rolls

Consider throwing a pair of fair dice.
The sample space $\Omega$ contains $6 \times 6 = 36$ equally likely outcomes: $\Omega = \{ (i,j) \mid i,j \in \{1, \dots, 6\} \}$. Each outcome has probability $1/36$.

Define a random variable $X$ as the **sum of the two numbers** shown on the dice.
We want to find $P[X=7]$.

1.  **Identify $a$:** Here, $a=7$.
2.  **Find the inverse image $X^{-1}(7)$:** We identify outcomes $(i,j) \in \Omega$ where $i+j=7$.
    $$ X^{-1}(7) = \{ (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) \} $$
3.  **Calculate the probability:** There are 6 outcomes in $X^{-1}(7)$.
    $$ P[X=7] = P(X^{-1}(7)) = \frac{\text{Number of outcomes in } X^{-1}(7)}{\text{Total number of outcomes in } \Omega} = \frac{6}{36} = \frac{1}{6} $$

## Quick Summary

*   A **random variable** is a function $X: \Omega \rightarrow \mathbb{R}$ that maps outcomes from a sample space to numerical values, providing a mathematical framework for qualitative events.
*   To calculate the probability $P[X=a]$ (that $X$ takes a specific value $a$), we first determine the **inverse image** $X^{-1}(a)$. This set comprises all original sample space outcomes $\xi$ that map to $a$.
*   The set $X^{-1}(a)$ is an event in $\Omega$, allowing its probability to be measured using the defined probability measure $P$.
*   In practical applications, while the inverse mapping is fundamental to the definition, we often work directly with $P[X=a]$ once the random variable's behavior is established, without explicitly detailing each inverse mapping step.

