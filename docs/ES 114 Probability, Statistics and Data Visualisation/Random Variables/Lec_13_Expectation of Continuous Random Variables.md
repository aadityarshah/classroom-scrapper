---
course: ES 114 Probability, Statistics and Data Visualisation
title: "Expectation of Continuous Random Variables"
lecture_number: 13
lecture_name: "Expectation of Continuous Random Variables"
category: "Random Variables"
sidebar_label: Lecture 13
sidebar_position: 13
topic:
  - "Expectation"
  - "Properties of Expectation"
  - "Existence of Expectation"
  - "Moments"
  - "Variance"
tags:
  - "Probability"
  - "Random Variables"
  - "Expectation"
  - "Mean"
  - "Variance"
  - "Continuous Random Variables"
  - "PDF"
math: true
last_updated: '20 April 2026'
summary: "This lecture introduces the definition of expectation for continuous random variables, its key properties, the condition for its existence (absolute integrability), and defines moments and variance. Crucial examples like the Uniform, Exponential, and Cauchy distributions illustrate these concepts."
---

In previous lectures, we established the framework for continuous random variables and their Probability Density Functions (PDFs). Today, we delve into one of the most fundamental concepts in probability theory: **Expectation**, which represents the average or mean value of a random variable.

## Expectation of a Continuous Random Variable

The **expectation** (or mean) of a continuous random variable $X$, denoted $E[X]$, is defined as:

$$ E[X] = \int_{\Omega} x f_X(x)dx $$

where $f_X(x)$ is the PDF of $X$ and $\Omega$ is the sample space (typically $\mathbb{R}$).

**Examples:**

1.  **Uniform Random Variable:** For $X \sim U(a,b)$, with PDF $f_X(x) = \frac{1}{b-a}$ for $a \le x \le b$ (and $0$ otherwise), its expectation is $E[X] = \frac{a+b}{2}$.
2.  **Exponential Random Variable:** For $X \sim \text{Exp}(\lambda)$, with PDF $f_X(x) = \lambda e^{-\lambda x}$ for $x \ge 0$ (and $0$ otherwise), its expectation is $E[X] = \frac{1}{\lambda}$.

## Expectation of a Function of a Random Variable

If $g(X)$ is a function of a continuous random variable $X$, the expectation of $g(X)$, denoted $E[g(X)]$, is given by:

$$ E[g(X)] = \int_{\Omega} g(x) f_X(x)dx $$

This theorem allows us to calculate the average value of any transformation of a random variable without first finding the PDF of $Y = g(X)$.

**Examples:**

1.  **Expectation of $X^2$ (Uniform RV):** For $X \sim U(a,b)$, $E[X^2] = \int_a^b x^2 \frac{1}{b-a} dx = \frac{a^2+ab+b^2}{3}$.
2.  **Expectation of an Indicator Function:** Let $I_A(X)$ be an indicator function such that $I_A(X) = 1$ if $X \in A$ and $I_A(X) = 0$ if $X \notin A$. Then, $E[I_A(X)] = \int_{\Omega} I_A(x) f_X(x)dx = \int_A f_X(x)dx = P(X \in A)$. This links expectation to probability.

## Properties of Expectation

Expectation is a linear operator:

*   **Scalar Multiple:** $E[aX] = aE[X]$ for any constant $a$.
*   **Constant Addition:** $E[X+a] = E[X]+a$ for any constant $a$.
*   **Linear Transformation:** $E[aX+b] = aE[X]+b$ for any constants $a, b$.

## Existence of Expectation

A random variable $X$ has an expectation if and only if it is **absolutely integrable**. That is, $E[X]$ exists if:

$$ E[|X|] = \int_{\Omega} |x|f_X(x)dx < \infty $$

If this condition is not met, the expectation is undefined (or said to "not exist").

**Example: Cauchy Random Variable**
Consider the Cauchy distribution with PDF $f_X(x) = \frac{1}{\pi(1+x^2)}$ for $x \in \mathbb{R}$.
To check for existence of $E[X]$, we evaluate $E[|X|]$:
$$ E[|X|] = \int_{-\infty}^{\infty} |x| \frac{1}{\pi(1+x^2)}dx $$
Due to symmetry, this integral can be written as:
$$ E[|X|] = \frac{2}{\pi} \int_0^{\infty} \frac{x}{1+x^2}dx $$
This integral diverges:
$$ \int_0^{\infty} \frac{x}{1+x^2}dx = \left[ \frac{1}{2}\log(1+x^2) \right]_0^{\infty} = \infty $$
Since $E[|X|] = \infty$, the expectation of a Cauchy random variable does not exist.

## Moments and Variance

### Moments
The **$k$-th moment** of a continuous random variable $X$ is defined as:

$$ E[X^k] = \int_{\Omega} x^k f_X(x)dx $$
The first moment ($k=1$) is the expectation $E[X]$.

### Variance
The **variance** of a continuous random variable $X$, denoted $\text{Var}[X]$, measures the spread or dispersion of the distribution around its mean. It is defined as:

$$ \text{Var}[X] = E[(X-\mu)^2] = \int_{\Omega} (x-\mu)^2 f_X(x)dx $$
where $\mu = E[X]$ is the mean of $X$.

A useful computational formula for variance is:
$$ \text{Var}[X] = E[X^2] - (E[X])^2 = E[X^2] - \mu^2 $$

**Example: Variance of a Uniform Random Variable**
For $X \sim U(a,b)$:
We know $E[X] = \frac{a+b}{2}$ and $E[X^2] = \frac{a^2+ab+b^2}{3}$.
Using the formula $\text{Var}[X] = E[X^2] - (E[X])^2$:
$$ \text{Var}[X] = \frac{a^2+ab+b^2}{3} - \left(\frac{a+b}{2}\right)^2 $$
$$ \text{Var}[X] = \frac{4(a^2+ab+b^2) - 3(a^2+2ab+b^2)}{12} $$
$$ \text{Var}[X] = \frac{4a^2+4ab+4b^2 - 3a^2-6ab-3b^2}{12} $$
$$ \text{Var}[X] = \frac{a^2-2ab+b^2}{12} = \frac{(b-a)^2}{12} $$

## Quick Summary

*   **Expectation $E[X]$:** The mean value of a continuous random variable $X$, calculated as $E[X] = \int_{\Omega} x f_X(x)dx$.
*   **Expectation of a Function $E[g(X)]$:** The average value of a function of $X$, calculated as $E[g(X)] = \int_{\Omega} g(x) f_X(x)dx$.
*   **Properties of Expectation:** Expectation is a linear operator: $E[aX+b] = aE[X]+b$.
*   **Existence of Expectation:** $E[X]$ exists if $E[|X|] = \int_{\Omega} |x|f_X(x)dx < \infty$ (absolutely integrable). The Cauchy distribution is a counter-example where expectation does not exist.
*   **$k$-th Moment:** $E[X^k] = \int_{\Omega} x^k f_X(x)dx$.
*   **Variance $\text{Var}[X]$:** Measures the spread, defined as $\text{Var}[X] = E[(X-\mu)^2]$ or computationally as $\text{Var}[X] = E[X^2] - (E[X])^2$.



