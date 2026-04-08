---
title: Moments and Variance of Random Variables
lecture_number: 11
lecture_name: Moments and Variance of Random Variables
category: Random Variables
sidebar_label: Lecture 11
sidebar_position: 11
course: 'ECE 302: Principles of AI'
topic:
- Expectation Properties
- Moments
- Variance
- Standard Deviation
- Variance Properties
tags:
- Random Variables
- Expectation
- Moments
- Variance
- Statistics
- Discrete Probability
math: true
summary: This lecture revisits key properties of expectation and introduces the concepts
  of moments and variance for discrete random variables, including their definitions
  and properties. It covers the k-th moment, variance, and standard deviation, along
  with how scaling and shifting affect these statistical measures.
last_updated: 08 April 2026
---


# Moments and Variance

This lecture extends the concept of expectation by introducing moments and variance, fundamental measures for characterizing random variables. We begin by reviewing essential properties of expectation.

## Properties of Expectation $E[X]$

Let $X$ be a discrete random variable with PMF $p_X(x)$.

### 1. Function of $X$
For any function $g$:
$$E[g(X)] = \sum_x g(x)p_X(x)$$

### 2. Linearity
For any functions $g$ and $h$:
$$E[g(X) + h(X)] = E[g(X)] + E[h(X)]$$

### 3. Scale
For any constant $c$:
$$E[cX] = cE[X]$$

### 4. DC Shift
For any constant $c$:
$$E[X + c] = E[X] + c$$

## Moment

### Definition
The **k-th moment** of a random variable $X$ is the expectation of $X^k$:
$$E[X^k] = \sum_x x^k p_X(x)$$
The first moment, $E[X]$, is the mean or expectation.

### Example Context
For $X$ representing the number of heads in 3 coin flips, with $p_X(0)=1/8, p_X(1)=3/8, p_X(2)=3/8, p_X(3)=1/8$. The second moment is $E[X^2]$.

## Variance

### Definition
The **variance** of a random variable $X$ measures the spread of its distribution around its mean. It is defined as:
$$\text{Var}[X] = E[(X - \mu_X)^2]$$
where $\mu_X = E[X]$ is the expectation (mean) of $X$.

The **standard deviation** is the square root of the variance:
$$\sigma_X = \sqrt{\text{Var}[X]}$$

### Example Context
For $X$ being a coin flip with probability $p$ of heads, $\text{Var}[X]$ describes the spread of outcomes.

## Properties of Variance

Let $X$ be a random variable and $c$ be a constant.

### 1. Alternative Formula (Moment Relation)
Variance can be expressed in terms of moments:
$$\text{Var}[X] = E[X^2] - (E[X])^2$$

### 2. Scale Property
Multiplying a random variable by a constant scales its variance by the square of the constant:
$$\text{Var}[cX] = c^2 \text{Var}[X]$$
This implies $\sigma_{cX} = |c|\sigma_X$.

### 3. DC Shift Property
Adding a constant to a random variable does not change its variance:
$$\text{Var}[X + c] = \text{Var}[X]$$
This means adding a constant shifts the mean but does not affect the spread of the data. Consequently, $\sigma_{X+c} = \sigma_X$.

### Application Example
If 10 points are added to everyone's score ($X+10$):
*   The mean changes: $E[X+10] = E[X] + 10$.
*   The standard deviation does not change: $\sqrt{\text{Var}[X+10]} = \sqrt{\text{Var}[X]}$.
*   Curving grades (a non-linear transformation) would change relative grades, unlike a simple DC shift.

## Quick Summary

*   **Expectation Properties**: Linearity $E[g(X)+h(X)] = E[g(X)]+E[h(X)]$, scaling $E[cX] = cE[X]$, and DC shift $E[X+c] = E[X]+c$.
*   **k-th Moment**: $E[X^k] = \sum_x x^k p_X(x)$.
*   **Variance**: $\text{Var}[X] = E[(X - \mu_X)^2]$, measures spread.
*   **Standard Deviation**: $\sigma_X = \sqrt{\text{Var}[X]}$.
*   **Variance Properties**:
    *   $\text{Var}[X] = E[X^2] - (E[X])^2$.
    *   $\text{Var}[cX] = c^2 \text{Var}[X]$.
    *   $\text{Var}[X + c] = \text{Var}[X]$.