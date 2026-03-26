---
title: 'Probabilistic Reasoning: Basics and Bayes'' Theorem'
lecture_number: 1
lecture_name: 'Probabilistic Reasoning: The Deterministic Baseline, Uncertainty, and
  Bayes'' Theorem'
category: Module 3
sidebar_label: Lecture 1
sidebar_position: 1
last_updated: 26 March 2026
course: ES119 Principles of AI
topic:
- Deterministic vs. Probabilistic Reasoning
- Sources of Uncertainty
- Quantifying Belief
- Rational Agents
- Random Variables and Events
- Kolmogorov's Axioms
- Prior and Conditional Probability
- Joint Probability Distribution (JPD)
- The Product Rule
- Bayes' Theorem
tags:
- AI
- Probability
- Reasoning
- Uncertainty
- BayesTheorem
- JPD
- ConditionalProbability
summary: This lecture introduces the shift from deterministic logic to probabilistic
  reasoning in AI. It covers the sources and quantification of uncertainty, foundational
  concepts like random variables, sample spaces, and Kolmogorov's axioms. The lecture
  details prior, conditional, and joint probabilities, highlighting the limitations
  of JPDs and culminating in the introduction and application of Bayes' Theorem as
  the core AI engine for inferential reasoning under uncertainty.
math: true
---


# Probabilistic Reasoning: Foundations

## 1. The Deterministic Baseline & Its Limitations

### Deterministic Reasoning
- **Core Concept**: No randomness. Same input always yields same output.
- Assumes a "perfect" world model where all conditions are known and fixed.
- **Model**: `Input: X -$>$ Fixed Rules (Logic) -$>$ Output: Y`
- **Examples**: Logic gates, standard sorting algorithms.

### The Challenge of Reality
- Real-world scenarios introduce uncertainty, making deterministic rules fail.
- **Example**: `Leave(8:00) =$>$ Arrive(8:30)` is often false in reality due to unforeseen factors (traffic, flat tire).

### The Qualification Problem
- To make a logical rule strictly "True" in the real world, endless conditions are required.
- `Leave(8:00) ∧ ¬Traffic ∧ ¬FlatTire ∧ ... =$>$ Arrive(8:30)`
- **Issues**:
    - Infinite exceptions possible.
    - Impossible to pre-observe all conditions.
- Pure logic (rule-based systems) becomes intractable due to "too many exceptions."

## 2. Embracing Uncertainty: Probabilistic Systems

### Shift in Paradigm
- From **True/False** to **Degrees of Belief**.
- **Probabilistic Model**: `Input -$>$ Probabilistic Model -$>$ Probabilities of Outcomes`
- **Key Characteristics**:
    - Acknowledges missing information.
    - Assigns probability based on available data.

### Sources of Uncertainty
- Why AI systems aren't perfectly logical:
    1.  **Laziness**: Too much work to enumerate all rules/conditions.
    2.  **Theoretical Ignorance**: No perfect mathematical model exists for complex systems.
    3.  **Practical Ignorance**: Cannot deploy infinite sensors to measure all variables.
- **Engineering Takeaway**: Probability summarizes what we don't know or didn't measure.

### Quantifying Belief
- $P(A)$ represents the strength of belief that event $A$ is true.
- Values range from $0.0$ (disbelief/impossible) to $1.0$ (certainty/guaranteed).
- Beliefs are dynamic and update as new evidence arrives.

### Rational Agency
- A **Rational Agent** maximizes expected utility.
- Decision-making involves balancing probabilities of outcomes against their associated utilities (costs/benefits).
- **Rationality = Balancing Probability vs. Utility.**

## 3. Core Concepts in Probability

### Random Variable (RV)
- A **Random Variable ($X$)** is a function, not an algebraic variable.
- It maps an atomic event ($\omega$) from the Sample Space ($\Omega$) to a value in a specific domain ($D$).
- **Definition**: $X: \Omega \to D$
- **Domains (D)**:
    - **Boolean**: $\langle T, F \rangle$ (e.g., Cavity: True/False)
    - **Discrete**: $\{\text{Sunny}, \text{Rainy}, \text{Cloudy}\}$ (e.g., Weather)

### Sample Space ($\Omega$) & Atomic Events
- **Sample Space ($\Omega$)**: The set of all possible "worlds" or outcomes.
- **Atomic Event ($\omega$)**: A single, completely specified world state.
- **Constraints**: All atomic events are **Mutually Exclusive** (only one can occur) and **Exhaustive** (cover all possibilities).
- **Example (Dental Universe)**: For `Cavity` (C) and `Toothache` (T), there are 4 atomic events:
    - $\omega_1: (C=T \land T=T)$
    - $\omega_2: (C=T \land T=F)$
    - $\omega_3: (C=F \land T=T)$
    - $\omega_4: (C=F \land T=F)$

### Kolmogorov's Axioms
- Three fundamental rules governing probability:
    1.  **Non-negativity**: $0 \le P(\omega) \le 1$ for any atomic event $\omega$.
    2.  **Normalization**: $\sum_{\omega \in \Omega} P(\omega) = 1$. The sum of probabilities of all possible atomic events in the sample space is 1.
    3.  **Additivity (Inclusion-Exclusion Principle)**: For any two events $A$ and $B$:
        $P(A \lor B) = P(A) + P(B) - P(A \land B)$

## 4. Types of Probability

### Prior (Unconditional) Probability
- **Definition**: The baseline belief in a state **before** any evidence or sensors activate.
- Represents the historical background rate or prevalence of an event.
- **Notation**:
    - Scalar: $P(\text{Cavity}=\text{true}) = 0.1$
    - Vector (Distribution): $P(\text{Weather}) = (0.7, 0.2, 0.1)$ (for Sunny, Rainy, Cloudy)

### Joint Probability Distribution (JPD)
- **Definition**: A complete look-up table specifying the probability of **every possible atomic event** (every combination of variable values).
- Each row represents an atomic event with its probability.
- **Power**: Theoretically, an AI holding the JPD can answer **any** probabilistic query by summing relevant rows.
- **Anatomy Example (Cavity and Toothache)**:
    |               | Toothache (T) | ¬Toothache (¬T) |
    |---------------|---------------|-----------------|
    | Cavity (C)    | 0.12          | 0.08            |
    | ¬Cavity (¬C)  | 0.04          | 0.76            |
- **Operations**:
    - Verify Axiom 2: $0.12 + 0.08 + 0.04 + 0.76 = 1.0$
    - Extract Prior $P(C)$: $P(C) = P(C \land T) + P(C \land \neg T) = 0.12 + 0.08 = 0.20$

### The Complexity Crisis of JPDs
- JPD assumes every variable affects every other variable.
- For $n$ Boolean variables, the JPD requires $2^n$ rows/entries.
- **Scalability Issue**:
    - $n=2$ (Dentist): 4 entries
    - $n=20$: $\approx 1$ Million entries
    - $n=100$ (Autonomous Vehicle): $1.26 \times 10^{30}$ entries
- **Engineering Reality**: JPDs are a catastrophic failure at scale; they cannot be stored or computed for complex real-world problems.

### Conditional (Posterior) Probability
- **Concept**: Belief **after** observing evidence. The probability of event $A$ given that event $B$ has occurred.
- **Formula**:
    $$P(A | B) = \frac{P(A \land B)}{P(B)}$$
- The sample space is effectively reduced to only include states where $B$ is true.
- **Example (Dental)**: If $P(C \land T) = 0.12$ and $P(T) = 0.16$, then $P(C | T) = \frac{0.12}{0.16} = 0.75$.

### The Product Rule
- Rearrangement of the conditional probability formula.
- Allows calculation of joint probabilities from smaller, local rules.
- **Formulas**:
    $$P(A \land B) = P(A | B)P(B)$$
    $$P(A \land B) = P(B | A)P(A)$$
- **Engineering Value**: Enables building complex joint probabilities from prior and conditional probabilities without a full JPD.

## 5. Bayes' Theorem: The AI Engine

### Inverting Probabilities
- Equating the two forms of the Product Rule ($P(A|B)P(B) = P(B|A)P(A)$) allows us to "invert" conditional probabilities.
- This is crucial for diagnostic reasoning (inferring cause from effect).

### Bayes' Rule
- **Formula**:
    $$P(A | B) = \frac{P(B | A)P(A)}{P(B)}$$
- **AI Terminology**:
    - $P(A | B)$: **Posterior Probability** (What we want to know; probability of hypothesis $A$ given evidence $B$)
    - $P(B | A)$: **Likelihood** (How likely is the evidence $B$ given the hypothesis $A$)
    - $P(A)$: **Prior Probability** (Initial belief in hypothesis $A$ before seeing evidence)
    - $P(B)$: **Evidence / Marginal Likelihood** (Probability of observing evidence $B$)
    $$ \text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}} $$

### Applying Bayes' Theorem (Dentist Example)
- **Goal**: Find diagnostic rate $P(\text{cavity} | \text{toothache})$.
- **Given (Medical Knowledge)**:
    - Likelihood: $P(\text{toothache} | \text{cavity}) = 0.6$
    - Prior: $P(\text{cavity}) = 0.2$
    - Evidence: $P(\text{toothache}) = 0.16$
- **Calculation**:
    $$P(\text{cavity} | \text{toothache}) = \frac{P(\text{toothache} | \text{cavity})P(\text{cavity})}{P(\text{toothache})} = \frac{0.6 \times 0.2}{0.16} = \frac{0.12}{0.16} = 0.75$$

## Quick Summary

-   **Deterministic Logic Fails**: Real-world uncertainty creates infinite exceptions, making pure logic intractable.
-   **Probabilistic AI**: Shifts from True/False to Degrees of Belief, acknowledging missing information.
-   **Uncertainty Sources**: Laziness (too many rules), Theoretical Ignorance (no perfect model), Practical Ignorance (limited sensors).
-   **Random Variable (RV)**: Maps atomic events ($\omega$) to domain values ($D$).
-   **Sample Space ($\Omega$)**: Set of all mutually exclusive, exhaustive atomic events.
-   **Kolmogorov's Axioms**: Define valid probabilities ($0 \le P(\omega) \le 1$, $\sum P(\omega) = 1$, Inclusion-Exclusion).
-   **Prior Probability**: Baseline belief before evidence.
-   **Joint Probability Distribution (JPD)**: Table of all atomic event probabilities; powerful but fails catastrophically at scale ($2^n$ entries).
-   **Conditional Probability**: $P(A | B) = \frac{P(A \land B)}{P(B)}$, belief in A given B.
-   **Product Rule**: $P(A \land B) = P(A | B)P(B)$, for building complex joint probabilities.
-   **Bayes' Theorem**: $P(A | B) = \frac{P(B | A)P(A)}{P(B)}$, the AI engine for inverting probabilities and diagnostic reasoning (Posterior = Likelihood x Prior / Evidence).
