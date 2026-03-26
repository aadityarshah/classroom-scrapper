---
course: ES119 Principles of AI
title: Bayesian Networks and Naive Bayes Classifier
lecture_number: 2
lecture_name: Bayesian Networks and Naive Bayes Classifier
category: Module 3
sidebar_label: Lecture 2
sidebar_position: 2
last_updated: 26 March 2026
topic:
- Bayes' Rule Recap
- Marginalization
- Normalization Trick
- Absolute Independence
- Conditional Independence
- Bayesian Networks
- Conditional Probability Tables (CPTs)
- Joint Probability Distribution (JPD)
- Causal vs. Diagnostic Reasoning
- Naive Bayes Classifier
tags:
- Probability
- BayesRule
- Marginalization
- Normalization
- ConditionalIndependence
- BayesianNetworks
- CPT
- NaiveBayes
- AI
summary: This lecture covers the recap of Bayes' Rule, the computational challenge
  of marginalization and its solution through normalization, the concepts of absolute
  and conditional independence, the introduction of Bayesian Networks, and the derivation
  and characteristics of the Naive Bayes Classifier.
math: true
---


## Recap: The Diagnostic Query

We revisit Bayes' Rule with a Dentist system to calculate the probability of a cause given an effect.

**Setup (Priors):**
-   Prior probability of Cavity: $P(c) = 0.2$.
-   Prior probability of No Cavity: $P(\neg c) = 0.8$.

**Sensor Model (Likelihoods):**
-   Probe catches if Cavity: $P(h|c) = 0.9$.
-   Probe catches if No Cavity: $P(h|\neg c) = 0.2$.

**Objective:** Find $P(c|h)$ (probability of cavity given probe catches).

## The Denominator Trap: Marginalization

To solve $P(c|h)$, Bayes' Rule requires calculating $P(h)$, the total evidence.
$$ P(c|h) = \frac{P(h|c)P(c)}{P(h)} $$

The denominator $P(h)$ is found by **Marginalization**: summing out all hidden variables.
$$ P(h) = \sum_{C \in \{c, \neg c\}} P(h \land C) = P(h \land c) + P(h \land \neg c) $$
$$ P(h) = P(h|c)P(c) + P(h|\neg c)P(\neg c) $$
For our example:
-   $P(h \land c) = 0.9 \times 0.2 = 0.18$
-   $P(h \land \neg c) = 0.2 \times 0.8 = 0.16$
-   Total Evidence $P(h) = 0.18 + 0.16 = 0.34$.

### Complexity Crisis
Calculating $P(h)$ for a system with $N$ binary hidden variables involves summing $2^N$ terms.
-   1 Variable: 2 terms
-   10 Variables: 1,024 terms
-   30 Variables: 1.07 Billion terms
This makes exact calculation for large-scale AI mathematically **unsolvable**.

## Beating the Trap: Normalization ($\alpha$)

The denominator $P(h)$ is a **constant** for all hypotheses ($P(c|h)$ and $P(\neg c|h)$).
We define a **Normalization Constant** $\alpha = 1/P(h)$.
Then, we can write the posterior distribution as:
$$ P(C|h) = \alpha \cdot P(h \land C) = \alpha \cdot P(h|C)P(C) $$
For our example:
$$ P(C|h) = \alpha (P(h|c)P(c), P(h|\neg c)P(\neg c)) $$
$$ P(C|h) = \alpha (0.18, 0.16) $$
Since $P(c|h) + P(\neg c|h) = 1$, we have $\alpha(0.18 + 0.16) = 1 \implies \alpha(0.34) = 1 \implies \alpha = 1/0.34 \approx 2.94$.
$$ P(c|h) = 2.94 \times 0.18 \approx 0.529 $$
$$ P(\neg c|h) = 2.94 \times 0.16 \approx 0.471 $$

### Why $\alpha$ is Enough for Decisions
For decision-making, an AI agent often only needs to identify the most likely state. The normalization constant does not change the relative order of probabilities. If $P(h \land A) > P(h \land B)$, then $P(A|h) > P(B|h)$.
This allows an engineering shortcut: calculate unnormalized terms, compare, and normalize only at the very end if exact probabilities are needed.

## Defining Absolute Independence

**Purpose:** Simplify systems by identifying variables that do not influence each other.

**Mathematical Definition:** Variables $A$ and $B$ are absolutely independent if:
$$ P(A|B) = P(A) $$
or equivalently:
$$ P(A \land B) = P(A)P(B) $$

**AI Interpretation:** Learning the value of $B$ provides **zero new information** about $A$. The probability of $A$ remains the same.

**Rarity:** Absolute independence is rare in real-world AI systems where variables are often correlated (e.g., Toothache and Catch).

## Defining Conditional Independence

Most variables are correlated. **Conditional independence** provides a mechanism to break these correlations given a common cause.

**Scenario:** Flight Delay (A) and Crowded Lounge (B) appear dependent. A common cause like a Snowstorm (C) links them.

**Mathematical Definition:** Variables $A$ and $B$ are **conditionally independent given $C$** if their joint probability factors into separate parts once $C$ is known:
$$ P(A, B | C) = P(A | C) \cdot P(B | C) $$

**Equivalent Equality (Redundancy Property):**
If $A$ and $B$ are conditionally independent given $C$, then:
$$ P(A | B, C) = P(A | C) $$
This means that if we already know $C$, learning $B$ provides no additional information about $A$. $B$ becomes **redundant data** given $C$.

**Proof of Equivalence:**
Start with the general product rule: $P(A, B | C) = P(A | B, C) \cdot P(B | C)$.
Substitute the product definition for conditional independence: $P(A | C) \cdot P(B | C) = P(A | B, C) \cdot P(B | C)$.
Divide both sides by $P(B | C)$ (assuming $P(B|C) > 0$): $P(A | C) = P(A | B, C)$.
Both definitions describe the same lack of direct connection between $A$ and $B$ when $C$ is known.

## Introduction to Bayesian Networks

Bayesian Networks are graphical models that represent probabilistic relationships among variables.

**Formal Definition:** A Bayesian Network is a **Directed Acyclic Graph (DAG)** where:
-   **Nodes** represent random variables.
-   **Arrows** represent direct causal influence.
-   **Missing Arrows** explicitly represent assumptions of conditional independence.

**Construction Principle:** Conditional independence is used to remove unnecessary arrows, replacing direct links between correlated effects with a shared causal parent.
(e.g., Delay $\leftarrow$ Snowstorm $\rightarrow$ Crowd).

## Storing Knowledge in Conditional Probability Tables (CPTs)

The quantitative knowledge in a Bayesian Network is stored in **Conditional Probability Tables (CPTs)**.

**CPT Definition:** For every node $X_i$, we store its probability distribution conditional on its direct parents:
$$ P(X_i | Parents(X_i)) $$

**Benefit:** Due to conditional independence assumptions encoded in the graph, we only need to define a node's probability relative to its direct parents, drastically simplifying dependencies and storage requirements compared to a full Joint Probability Distribution.

## Global Semantics: The Chain Rule

A Bayesian Network represents the full Joint Probability Distribution (JPD) of all variables through **factorization** using the **Chain Rule**.

**Product Formula:** For variables $X_1, \dots, X_n$:
$$ P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i | Parents(X_i)) $$

**Dental Example:** For Cavity (C), Toothache (T), and Catch (H), with $C \to T$ and $C \to H$:
$$ P(C, T, H) = P(C) \times P(T | C) \times P(H | C) $$

## Causal vs. Diagnostic Reasoning

**Causal Reasoning:** Bayesian Networks are typically constructed based on causal relationships, storing $P(\text{Effect} | \text{Cause})$ in CPTs (e.g., $P(\text{Toothache} | \text{Cavity})$). Predicting symptoms from a known disease is a straightforward lookup.

**Diagnostic Reasoning:** Real-world queries are often diagnostic; we observe symptoms (Effects) and want to infer the probability of the underlying Disease (Cause). This requires "reversing the arrows" using Bayes' Rule: moving from $P(E|C)$ to $P(C|E)$.

**Example: Diagnostic Inference $P(c|t)$**
Given: $P(c)=0.2$, $P(\neg c)=0.8$, $P(t|c)=0.6$, $P(t|\neg c)=0.1$.
1.  **Calculate Unnormalized Weights (Numerator terms):**
    -   $W(c) = P(t|c)P(c) = 0.6 \times 0.2 = 0.12$
    -   $W(\neg c) = P(t|\neg c)P(\neg c) = 0.1 \times 0.8 = 0.08$
2.  **Normalize:** Sum of weights $= 0.12 + 0.08 = 0.20$.
    -   $P(c|t) = \frac{W(c)}{W(c) + W(\neg c)} = \frac{0.12}{0.20} = 0.60$
**Takeaway:** Observing a toothache updates the prior belief of a cavity from 20% to 60%.

## The Naive Bayes Classifier

Bayesian Networks structured as a Cause leading to multiple Effects are used for **Bayesian Classifiers**. The goal is to predict the most likely cause given observed effects.

**Problem:** To find $P(C | E_1, \dots, E_n)$, Bayes' Rule is:
$$ P(C | E_1, \dots, E_n) = \frac{P(E_1, \dots, E_n | C)P(C)}{P(E_1, \dots, E_n)} $$
Using normalization:
$$ P(C | E_1, \dots, E_n) = \alpha P(C) P(E_1, \dots, E_n | C) $$
The term $P(E_1, \dots, E_n | C)$ still requires an exponentially large joint probability table ($2^n$ entries).

### The Naive Assumption (Conditional Independence)
To overcome the computational/storage issue, the Naive Bayes Classifier assumes:
**Every Effect ($E_i$) is conditionally independent of any other Effect ($E_j$), given the Cause ($C$).**
$$ E_i \perp E_j | C $$
This allows the joint probability of effects to factorize into a simple product:
$$ P(E_1, \dots, E_n | C) \approx \prod_{i=1}^n P(E_i | C) $$
**Impact:** Complexity for calculating $P(E_1, \dots, E_n | C)$ drops from exponential ($2^n$) to linear ($n$).

### The Final Formula
Combining Bayes' Rule with the Naive Assumption, the Naive Bayes Classifier formula is:
$$ P(C | E_1, \dots, E_n) = \alpha P(C) \prod_{i=1}^n P(E_i | C) $$
Where $\alpha$ is the normalization constant.

### Key Characteristics:
-   **Robust:** Works surprisingly well even if the independence assumptions are technically violated in practice.
-   **Efficient:** Requires minimal data to train, as only individual CPTs ($P(E_i|C)$) and priors ($P(C)$) are needed.
-   **Scalable:** Easily handles a large number of evidence variables (e.g., hundreds of words in an email for spam classification).

## Quick Summary

-   **Marginalization** leads to exponential complexity in Bayes' Rule's denominator.
-   **Normalization ($\alpha$)** provides a computational shortcut for decision-making by focusing on proportional likelihoods.
-   **Absolute Independence** is rare; **Conditional Independence** ($P(A,B|C)=P(A|C)P(B|C)$) is key for simplifying dependencies.
-   **Bayesian Networks** are DAGs using nodes for variables, arrows for direct influence, and missing arrows for conditional independence.
-   **CPTs ($P(X_i | Parents(X_i))$)** store local knowledge efficiently.
-   The **Chain Rule** allows a BN to represent the full JPD: $P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i | Parents(X_i))$.
-   **Diagnostic Reasoning** (Cause from Effect) uses Bayes' Rule to reverse causal arrows.
-   The **Naive Bayes Classifier** applies conditional independence of effects given a cause, leading to an efficient and scalable classification model: $P(C | E_1, \dots, E_n) = \alpha P(C) \prod_{i=1}^n P(E_i | C)$.
