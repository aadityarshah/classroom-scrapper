---
title: Probability Space
lecture_number: 2
lecture_name: 'Probability Space Fundamentals: Sample Space, Events, and Probability
  Laws'
category: Probability Theory
sidebar_label: Lecture 2
sidebar_position: 2
course: "ES 114 Probability, Statistics and Data Visualisation"
last_updated: "23 March 2026"
topic:
- Sample Space
- Event Space (Sigma-Field)
- Probability Law (Measure)
- Probability Space Definition
tags:
- probability
- sample space
- outcome
- event
- event space
- sigma-field
- probability law
- probability measure
- measure zero
- almost surely
summary: 'This lecture introduces the foundational components of a probability model:
  the sample space (collection of all possible outcomes), the event space (a collection
  of subsets of the sample space called events), and the probability law (a function
  that assigns probabilities to events). It culminates in defining a complete probability
  space as a triplet.'
math: true
---


Welcome to Lecture 2 of ES 114. Today, we embark on a journey into the fundamental building blocks of probability theory: the **Probability Space**. Understanding these core concepts is paramount for anyone delving into the fascinating world of uncertainty and random phenomena.

## What is Probability?

At its most basic, probability is:
*   A **number**.
*   Always between $0$ and $1$, inclusive ($0 \le P(A) \le 1$).
*   Always associated with an **event**.

For instance, consider the probability of getting a Head when tossing a fair coin. We denote this as $P(\text{"H"})$. If the coin is fair, $P(\text{"H"}) = 0.5$.

## Three Elements of a Probability Model

A complete probability model, often called a probability space, is constructed from three fundamental elements:

1.  **Sample Space ($\Omega$):** The set of all possible outcomes of a random experiment.
2.  **Event Space ($\mathcal{F}$):** A collection of subsets of the sample space, where each subset is called an **event**, and for which we can assign a probability.
3.  **Probability Law ($P$):** A function that assigns a probability to each event in the event space.

Let's dissect each of these elements in detail.

## The Sample Space ($\Omega$)

### Definition

The **sample space**, denoted by $\Omega$ (uppercase Omega), is the collection of all possible outcomes of a random experiment. Each individual outcome within $\Omega$ is typically denoted by $\omega$ (lowercase omega).

### Examples

1.  **Coin Flip:**
    *   $\Omega = \{\text{Head (H)}, \text{Tail (T)}\}$

2.  **Throw a Dice:**
    *   $\Omega = \{1, 2, 3, 4, 5, 6\}$

3.  **Waiting Time for a Bus:** (in minutes, assuming a maximum wait of 30 minutes)
    *   $\Omega = \{t \in \mathbb{R} \mid 0 \le t \le 30\}$
    *   This is a continuous sample space.

### Elements in the Sample Space

The nature of the elements in a sample space can vary widely:
*   **Discrete Numbers:** Such as $\{1, 2, 3, \ldots, N\}$.
*   **Continuous Intervals:** For example, $[a, b]$ on the real number line.
*   **Functions:** In advanced stochastic processes, outcomes can be entire functions or sequences.

## The Event Space ($\mathcal{F}$)

### Definition (Event)

An **event**, denoted by $F$, is a subset of the sample space $\Omega$. Events are specific collections of outcomes for which we want to determine a probability.

### Outcome vs. Event

An **outcome** $\omega$ is a single result of the experiment. An **event** $F$ is a set of outcomes.
For example, in a dice roll, 'getting a 3' is an outcome. 'Getting an even number' is an event composed of multiple outcomes.

### Examples

1.  **Throw a Dice:** Let $\Omega = \{1, 2, 3, 4, 5, 6\}$.
    *   $F_1 = \{\text{even numbers}\} = \{2, 4, 6\}$
    *   $F_2 = \{\text{less than } 3\} = \{1, 2\}$

2.  **Wait a Bus:** Let $\Omega = \{t \in \mathbb{R} \mid 0 \le t \le 30\}$.
    *   $F_1 = \{0 < t < 10\}$ (waiting time is less than 10 minutes)
    *   $F_2 = \{0 < t < 5\} \cup \{20 < t \le 30\}$ (waiting time is less than 5 minutes or between 20 and 30 minutes)

### Definition (Event Space)

The collection of all events for a given sample space is called the **event space**, denoted as $\mathcal{F}$. It is a set of subsets of $\Omega$.

### How Many Events?

**Question:** If you have $n$ elements in the sample space $\Omega$, how many distinct events can you construct?

**Solution:** Each element $\omega \in \Omega$ can either be included in an event or not. Since there are $n$ elements, and each has two choices, the total number of possible subsets (events) is $2^n$. This includes the empty set $\emptyset$ (the impossible event) and the sample space $\Omega$ itself (the sure event).

### Sigma-Field (Optional)

The event space is often referred to as a **$\sigma$-field** (or $\sigma$-algebra) to emphasize its structural properties. A collection of subsets $\mathcal{F}$ of $\Omega$ is a $\sigma$-field if it satisfies the following two properties:

1.  **Closure under Complementation:** If an event $F \in \mathcal{F}$, then its complement $F^c = \Omega \setminus F$ must also be in $\mathcal{F}$.
2.  **Closure under Countable Unions:** If $F_1, F_2, \ldots$ is a countable sequence of events in $\mathcal{F}$, then their union $\bigcup_{i=1}^\infty F_i$ must also be in $\mathcal{F}$. (Note: This property implies closure under countable intersections as well, by De Morgan's laws: $(\bigcup F_i)^c = \bigcap F_i^c$).

**Example:** For $\Omega = \{\text{H}, \text{T}\}$, the $\sigma$-field is:
$\mathcal{F} = \{\emptyset, \{\text{H}\}, \{\text{T}\}, \{\text{H}, \text{T}\}\}$.
Here, $n=2$, so $2^n = 2^2 = 4$ events. This example perfectly illustrates a $\sigma$-field for a finite sample space.

## The Probability Law ($P$)

### Definition

A **probability law** (or probability measure), denoted by $P$, is a function that maps an event $A \in \mathcal{F}$ to a real number in the interval $[0, 1]$.
$$ P: \mathcal{F} \to [0, 1] $$
The probability law quantifies the likelihood of an event occurring.

### Example: Flipping a Coin

Consider flipping a coin. The sample space is $\Omega = \{\text{H}, \text{T}\}$.
The event space is $\mathcal{F} = \{\emptyset, \{\text{H}\}, \{\text{T}\}, \Omega\}$.

A sensible probability law for a fair coin would be:
*   $P(\emptyset) = 0$ (probability of no outcome is 0)
*   $P(\{\text{H}\}) = 0.5$
*   $P(\{\text{T}\}) = 0.5$
*   $P(\Omega) = P(\{\text{H}, \text{T}\}) = 1$ (probability of getting any outcome is 1)

## Probability Law as a Measure (Optional)

In more advanced contexts, the probability law is often seen as a specific type of **measure**. A measure, in general, assigns a "size" or "quantity" to subsets of a set. For probability, this "size" is normalized to be between 0 and 1.

Probability can be thought of as the **relative size of an event (set) with respect to the sample space**.
$$ P[E] = \frac{\text{Size of } E}{\text{Size of } \Omega} $$

### Examples of "Size"

*   **Discrete Numbers:** For discrete sample spaces, the "size" of an event is often the **count** of outcomes it contains. For example, if $\Omega = \{1,2,3,4,5,6\}$ and $E_1 = \{2,4,6\}$, then $\text{Size}(E_1) = 3$ and $\text{Size}(\Omega) = 6$. So, $P[E_1] = 3/6 = 0.5$.
*   **1D Intervals:** For continuous sample spaces on a line, the "size" is often the **length** of the interval. If $\Omega = [0, 10]$ and $E_1 = [1, 4]$, then $\text{Size}(E_1) = 3$ and $\text{Size}(\Omega) = 10$. So, $P[E_1] = 3/10 = 0.3$.
*   **2D Sets:** For continuous sample spaces in two dimensions, the "size" is often the **area** of the region.

### Measure Zero (Optional)

An important consequence of thinking about probability as a measure (especially for continuous spaces) is the concept of **measure zero**.

An isolated point in a continuous interval has zero probability. For example, if $\Omega = [0, 1]$, the probability of observing exactly $0.5$ is $P[\{0.5\}] = 0$. This is because the "length" of a single point is zero.

**Examples of Measure Zero Sets:**

1.  Let $\Omega = [0, 1]$. The set $\{0.5\}$ has measure zero, $P[\{0.5\}] = 0$.
2.  Let $\Omega = \{1, 2, 3, 4, 5, 6\}$. Here, discrete outcomes have non-zero probability. The set $\{1\}$ has a probability of $1/6$, not zero.
3.  For any intervals, $P[[a, b]] = P[(a, b)]$ because the two end points $a$ and $b$ have measure zero: $P[\{a\}] = P[\{b\}] = 0$. This means including or excluding the endpoints of an interval does not change its probability in a continuous distribution.

### Almost Surely (a.s.)

In continuous probability, a concept called **"almost surely"** is crucial.

**Definition:** An event $A \in \mathcal{F}$ is said to hold **almost surely (a.s.)** if $P[A] = 1$, even if the event $A$ does not include *all* outcomes in $\Omega$. This means the outcomes *not* in $A$ form a set of measure zero.

For example, if you pick a random real number in $[0,1]$, the probability that it is *not* exactly $0.5$ is $1$. So, "the number is not $0.5$" happens almost surely.

## The Probability Space

Finally, we unify these three components.

### Definition

A **probability space** consists of a triplet $(\Omega, \mathcal{F}, P)$, where:

1.  $\Omega$ is the **sample space**, the set of all possible outcomes.
2.  $\mathcal{F}$ is the **event space** (or $\sigma$-field), a collection of subsets of $\Omega$ called events, which satisfies the properties of a $\sigma$-field.
3.  $P$ is the **probability law** (or probability measure), a function $P: \mathcal{F} \to [0, 1]$ that assigns a probability to each event in $\mathcal{F}$ and satisfies the axioms of probability (which we will cover in the next lecture).

This triplet provides the mathematical framework for rigorously defining and analyzing random phenomena. Every problem in probability theory ultimately operates within the context of a defined probability space.

## Quick Summary

This lecture established the three foundational components of a probability model:
*   The **sample space ($\Omega$)** is the complete set of all possible outcomes of an experiment. Outcomes can be discrete numbers, continuous values, or even complex functions.
*   An **event ($F$)** is any subset of the sample space for which we wish to assign a probability. The collection of all such events forms the **event space ($\mathcal{F}$)**, which mathematically is a $\sigma$-field, ensuring closure under set operations like complementation and countable unions.
*   The **probability law ($P$)** is a function that maps events from the event space to a value between $0$ and $1$, quantifying their likelihood. It can be intuitively understood as a measure of the relative "size" of an event within the sample space, leading to concepts like measure zero sets and "almost surely" events for continuous distributions.
Together, these three elements form the **probability space ($\Omega, \mathcal{F}, P$)**, the essential framework for all probability calculations.
---

