---
title: Joint PDF and CDF
lecture_number: 14
lecture_name: Joint Probability Distributions
category: Random Variables
sidebar_label: Lecture 14
sidebar_position: 14
course: ES 114 Probability, Statistics and Data Visualisation
topic:
- Joint Probability Mass Functions
- Joint Probability Density Functions
- Marginal Distributions
- Statistical Independence
- Joint Cumulative Distribution Functions
tags:
- Random Variables
- Joint Distributions
- Multivariate Calculus
- Independence
summary: An intensive overview of joint probability mass and density functions, marginalization
  techniques, statistical independence, and the properties of joint cumulative distribution
  functions.
math: true
last_updated: '20 April 2026'
---


## Introduction to Joint Distributions

Joint distributions extend the concept of a single random variable to **high-dimensional spaces**. In modern data analysis, objects (like images) are represented as high-dimensional vectors $\mathbf{x} = [x_1, \dots, x_N]^T$. The likelihood of observing a specific vector is governed by a joint Probability Density Function (PDF) $f_{\mathbf{X}}(\mathbf{x})$.

## Joint Probability Mass Function (PMF)

For two discrete random variables $X$ and $Y$, the **joint PMF** $p_{X,Y}(x, y)$ describes the probability that $X$ and $Y$ take on specific values simultaneously:

$$p_{X,Y}(x, y) = P[X = x \text{ and } Y = y]$$

To find the probability of an event $\mathcal{A}$ in the joint space, we sum the impulses (probabilities) of all points $(x,y)$ contained within $\mathcal{A}$:
$$P[\mathcal{A}] = \sum_{(x,y) \in \mathcal{A}} p_{X,Y}(x, y)$$

## Joint Probability Density Function (PDF)

For two continuous random variables $X$ and $Y$, the **joint PDF** $f_{X,Y}(x, y)$ is a surface such that the volume under the surface over a region $\mathcal{A}$ equals the probability of the event $\mathcal{A}$:

$$P[\mathcal{A}] = \iint_{\mathcal{A}} f_{X,Y}(x, y) dx dy$$

### Normalization Property
The total volume under any valid joint PDF must be unity:
$$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) dx dy = 1$$

### Example: Non-Rectangular Integration
Consider $f_{X,Y}(x, y) = ce^{-x}e^{-y}$ for $0 \le y \le x < \infty$. To find $c$:
$$\int_{0}^{\infty} \int_{0}^{x} ce^{-x}e^{-y} dy dx = \int_{0}^{\infty} ce^{-x}(1 - e^{-x}) dx = \frac{c}{2} = 1 \implies c = 2$$

## Marginal Distributions

**Marginalization** is the process of recovering the distribution of a single random variable from a joint distribution by "summing out" or "integrating out" the other variables.

### Marginal PMF
$$p_X(x) = \sum_{y \in \Omega_Y} p_{X,Y}(x, y) \quad \text{and} \quad p_Y(y) = \sum_{x \in \Omega_X} p_{X,Y}(x, y)$$

### Marginal PDF
$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dy \quad \text{and} \quad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) dx$$

## Statistical Independence

Two random variables $X$ and $Y$ are **independent** if and only if their joint distribution factors into the product of their marginals:

1.  **Discrete:** $p_{X,Y}(x, y) = p_X(x)p_Y(y)$
2.  **Continuous:** $f_{X,Y}(x, y) = f_X(x)f_Y(y)$

### Independent and Identically Distributed (i.i.d.)
A collection $X_1, \dots, X_N$ is i.i.d. if:
1.  All $X_i$ are mutually independent.
2.  All $X_i$ share the same marginal distribution $f_X$.

For i.i.d. variables, the joint PDF is:
$$f_{X_1, \dots, X_N}(x_1, \dots, x_N) = \prod_{i=1}^N f_X(x_i)$$

## Joint Cumulative Distribution Function (CDF)

The **joint CDF** $F_{X,Y}(x, y)$ is defined as the probability that $X \le x$ AND $Y \le y$:
$$F_{X,Y}(x, y) = P[X \le x \cap Y \le y]$$

### Calculation
*   **Discrete:** $F_{X,Y}(x, y) = \sum_{y' \le y} \sum_{x' \le x} p_{X,Y}(x', y')$
*   **Continuous:** $F_{X,Y}(x, y) = \int_{-\infty}^{y} \int_{-\infty}^{x} f_{X,Y}(x', y') dx' dy'$

### Fundamental Properties
1.  **Marginal CDFs:** $F_X(x) = F_{X,Y}(x, \infty)$ and $F_Y(y) = F_{X,Y}(\infty, y)$.
2.  **Relationship to PDF:** The joint PDF is the mixed partial derivative of the joint CDF:
    $$f_{X,Y}(x, y) = \frac{\partial^2}{\partial x \partial y} F_{X,Y}(x, y)$$
3.  **Independence:** If $X$ and $Y$ are independent, $F_{X,Y}(x, y) = F_X(x)F_Y(y)$.

## Quick Summary
*   **Joint Distribution:** Describes multiple variables simultaneously; probabilities are found via double summation (discrete) or double integration (continuous).
*   **Marginalization:** Integrate/Sum over the unwanted variable to find the individual distribution.
*   **Independence:** $X$ and $Y$ are independent if $f_{X,Y}(x, y) = f_X(x)f_Y(y)$.
*   **i.i.d.:** Variables that are both independent and follow the same marginal distribution.
*   **CDF to PDF:** Use mixed partial derivatives to convert a joint CDF back into a joint PDF.



