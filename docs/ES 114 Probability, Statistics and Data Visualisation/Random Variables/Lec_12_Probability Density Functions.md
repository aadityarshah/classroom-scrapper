---
course: ECE 302 Probabilistic Methods
title: Probability Density Functions
lecture_number: 12
lecture_name: Probability Density Functions
category: Random Variables
sidebar_label: Lecture 12
sidebar_position: 12
topic:
- Probability Density Functions (PDF)
- Continuous Random Variables
- Properties of Density
- Dirac Delta Functions in Probability
tags:
- PDF
- Continuous RV
- Integration
- Delta Function
summary: This lecture defines the Probability Density Function (PDF) for continuous
  random variables, establishes its properties, and demonstrates how to represent
  discrete Probability Mass Functions (PMFs) as PDFs using Dirac delta functions.
math: true
last_updated: 23 April 2026
---


## Intuition: Probability as a Measure of Size

For continuous sample spaces, we define the probability of an event $A$ by measuring the "size" of $A$ relative to the sample space $\Omega$. 

In the simplest case of **equiprobable** outcomes (Uniform distribution) over an interval:
$$
\mathbb{P}[\{x \in A\}] = \frac{\text{"size" of } A}{\text{"size" of } \Omega} = \frac{\int_A dx}{\int_\Omega dx} = \int_A \frac{1}{|\Omega|} dx
$$

Where $|\Omega|$ is the length (or area/volume) of the sample space. To relax the equiprobable assumption, we replace the constant weight $1/|\Omega|$ with a varying weight function $f_X(x)$.

## Formal Definition of the PDF

Let $X$ be a continuous random variable. The **Probability Density Function (PDF)** $f_X: \Omega \to \mathbb{R}$ is a mapping that, when integrated over an interval $[a, b]$, yields the probability that $X$ falls within that interval.

### Axiomatic Properties
1.  **Non-negativity:** $f_X(x) \geq 0$ for all $x \in \Omega$.
2.  **Unity (Normalization):** $\int_{-\infty}^{\infty} f_X(x) dx = 1$.
3.  **Measure of a Set:** $\mathbb{P}[X \in A] = \int_A f_X(x) dx$.

### Key Interpretations
*   **Density vs. Probability:** $f_X(x)$ is **not** the probability $\mathbb{P}[X=x]$. It represents **probability per unit length**.
*   **Approximation:** For small $\delta$, $\mathbb{P}[x \leq X \leq x + \delta] \approx f_X(x) \cdot \delta$.
*   **Magnitudes:** Unlike PMFs, $f_X(x)$ can be greater than 1, and can even approach infinity, provided the integral remains equal to 1.

## Point Probabilities and Intervals

In continuous spaces, the probability of a single point is zero:
$$
\mathbb{P}[X = x] = \int_x^x f_X(t) dt = 0
$$

**Implication:** For any continuous random variable, the inclusion or exclusion of endpoints does not change the probability of the interval:
$$
\mathbb{P}[a \leq X \leq b] = \mathbb{P}[a < X < b] = \mathbb{P}[a \leq X < b] = \mathbb{P}[a < X \leq b]
$$

### Example: PDF with a Singularity
Consider $f_X(x) = \frac{1}{2\sqrt{x}}$ for $0 < x \leq 1$, and $0$ otherwise. 
As $x \to 0$, $f_X(x) \to \infty$. However, the total probability is still valid:
$$
\int_0^1 \frac{1}{2\sqrt{x}} dx = \left[ \sqrt{x} \right]_0^1 = 1
$$

## Connecting PDF and PMF

Discrete random variables can be represented in the continuous framework using the **Dirac delta function** $\delta(x)$. A PMF can be viewed as a PDF consisting of a "train" of deltas.

### General Delta Representation
If $X$ is a discrete random variable with PMF $p_X(x_k)$, its PDF is:
$$
f_X(x) = \sum_{x_k \in \Omega} p_X(x_k) \delta(x - x_k)
$$

### Discrete Examples in Continuous Form
1.  **Bernoulli RV:** $f_X(x) = p\delta(x-1) + (1-p)\delta(x-0)$.
2.  **Binomial RV:** $f_X(x) = \sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} \delta(x-k)$.

### Calculating Probability with Deltas
When integrating a PDF containing deltas over an interval $[a, b]$, the result is the sum of the weights of all deltas located within that interval:
$$
\mathbb{P}[a \leq X \leq b] = \int_a^b \left( \sum p_X(x_k) \delta(x - x_k) \right) dx = \sum_{x_k \in [a, b]} p_X(x_k)
$$

## Quick Summary
*   The **PDF** $f_X(x)$ defines the distribution of a continuous random variable; its integral over a set gives the probability.
*   **Total area** under the PDF curve must always be exactly $1$.
*   **Probability at any point** $x$ is $0$ for continuous distributions.
*   **$f_X(x)$ is a density**, not a probability; it can exceed $1$.
*   **Discrete PMFs** can be unified with the PDF framework using **Dirac delta functions**, allowing discrete and continuous variables to be treated with the same calculus-based tools.
