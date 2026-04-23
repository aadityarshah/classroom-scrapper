---
title: Joint Expectation
lecture_number: 15
lecture_name: Joint Expectation and Correlation
category: Random Variables
sidebar_label: Lecture 15
sidebar_position: 15
course: ES 114 Probability, Statistics and Data Visualisation
topic:
- Joint Expectation
- Correlation
- Matrix Representation of Expectation
- Cauchy-Schwarz Inequality
tags:
- Random Variables
- Expectation
- Linear Algebra
- Inequalities
summary: This lecture defines joint expectation (correlation) for discrete and continuous
  random variables, provides a matrix-based geometric interpretation as a weighted
  inner product, and establishes the Cauchy-Schwarz inequality.
math: true
last_updated: '20 April 2026'
---


## Definition of Joint Expectation

The **joint expectation** of two random variables $X$ and $Y$ measures the average value of their product. In the context of probability theory, this quantity is also referred to as the **correlation**.

### Discrete Case
For discrete random variables $X$ and $Y$ with joint PMF $p_{X,Y}(x,y)$, the joint expectation is defined as:
$$\mathbb{E}[XY] = \sum_{y \in \Omega_Y} \sum_{x \in \Omega_X} xy \cdot p_{X,Y}(x, y)$$

### Continuous Case
For continuous random variables $X$ and $Y$ with joint PDF $f_{X,Y}(x,y)$, the joint expectation is:
$$\mathbb{E}[XY] = \int_{\Omega_Y} \int_{\Omega_X} xy \cdot f_{X,Y}(x, y) \, dx \, dy$$

---

## Matrix Representation and Inner Product

To understand the structure of $\mathbb{E}[XY]$, we can express the discrete sum in matrix form. This reveals that joint expectation is fundamentally a **weighted inner product** between the states of the random variables.

### The Joint PMF Matrix
Let $\mathbf{x} = [x_1, \dots, x_N]^T$ and $\mathbf{y} = [y_1, \dots, y_N]^T$ be vectors representing the possible states (outcomes) of $X$ and $Y$. We define a matrix $\mathbf{P}$ where the entry at $(i, j)$ is the joint probability:
$$\mathbf{P}_{ij} = p_{X,Y}(x_i, y_j)$$

The joint expectation is then calculated via the quadratic form:
$$\mathbb{E}[XY] = \mathbf{x}^T \mathbf{P} \mathbf{y}$$

### Interpretation as Similarity
In linear algebra, an inner product $\langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x}^T \mathbf{y}$ measures the similarity between two vectors. By introducing the probability matrix $\mathbf{P}$, the joint expectation $\mathbb{E}[XY]$ acts as a **weighted similarity measure**, where the weights are dictated by the joint distribution of the variables.

---

## Geometric Interpretation and Cosine Angle

The relationship between joint expectation and the individual second moments $\mathbb{E}[X^2]$ and $\mathbb{E}[Y^2]$ can be interpreted through geometry.

### Weighted Norms
The second moments can be viewed as squared "weighted norms" of the state vectors:
1.  **For X**: $\mathbb{E}[X^2] = \mathbf{x}^T \text{diag}(\mathbf{p}_X) \mathbf{x} = \|\mathbf{x}\|^2_{\mathbf{P}_X}$
2.  **For Y**: $\mathbb{E}[Y^2] = \mathbf{y}^T \text{diag}(\mathbf{p}_Y) \mathbf{y} = \|\mathbf{y}\|^2_{\mathbf{P}_Y}$

### The Cosine Similarity
The **cosine angle** $\theta$ between the random variables (interpreted as vectors in a Hilbert space) is defined as:
$$\cos \theta = \frac{\mathbb{E}[XY]}{\sqrt{\mathbb{E}[X^2]\mathbb{E}[Y^2]}}$$

*   If $\cos \theta = 1$, the variables are perfectly aligned (positively correlated).
*   If $\cos \theta = 0$, the variables are orthogonal ($\mathbb{E}[XY] = 0$).
*   If $\cos \theta = -1$, the variables are perfectly anti-aligned.

---

## Cauchy-Schwarz Inequality

Since the absolute value of a cosine function is bounded by 1 ($|\cos \theta| \leq 1$), we arrive at a fundamental theorem in probability.

**Theorem: Cauchy-Schwarz Inequality**
For any two random variables $X$ and $Y$:
$$(\mathbb{E}[XY])^2 \leq \mathbb{E}[X^2]\mathbb{E}[Y^2]$$

Equivalently, in terms of absolute expectation:
$$|\mathbb{E}[XY]| \leq \sqrt{\mathbb{E}[X^2]} \sqrt{\mathbb{E}[Y^2]}$$

This inequality guarantees that the correlation between two variables is always constrained by the energy (second moments) of the individual variables.

---

## Quick Summary
*   **Joint Expectation ($\mathbb{E}[XY]$)**: Also called correlation; computed as the sum/integral of the product of states weighted by their joint probability.
*   **Linear Algebra View**: $\mathbb{E}[XY] = \mathbf{x}^T \mathbf{P} \mathbf{y}$, representing a weighted inner product between state vectors.
*   **Geometric Similarity**: The ratio of joint expectation to the square root of the product of second moments defines the cosine of the angle between two random variables.
*   **Cauchy-Schwarz**: Provides the upper bound for joint expectation: $(\mathbb{E}[XY])^2 \leq \mathbb{E}[X^2]\mathbb{E}[Y^2]$.



