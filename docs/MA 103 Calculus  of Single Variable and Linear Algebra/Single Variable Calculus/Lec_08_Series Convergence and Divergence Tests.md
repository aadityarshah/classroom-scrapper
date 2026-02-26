---
title: |
  Series Convergence and Divergence Tests
lecture_number: 8
lecture_name: |
  Series Convergence and Divergence Tests
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 8
sidebar_position: 8
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Infinite Series, Convergence Tests
date: |
  2023-10-27
tags:
  - Math
  - Calculus
  - Series
  - Convergence
  - Divergence
  - Geometric Series
  - Integral Test
  - Comparison Test
  - Ratio Test
summary: |
  This lecture introduces various tests to determine the convergence or divergence of infinite series, including geometric series, telescoping series, the n-th term test, integral test, comparison tests, and the ratio test. Key properties of convergent series are also discussed.
math: true
---

# Series Convergence and Divergence Tests

## Table of Contents
* [Geometric Series](#geometric-series)
* [Telescoping Series](#telescoping-series)
* [Divergent Series & n-th Term Test](#divergent-series--n-th-term-test)
* [Properties of Convergent Series](#properties-of-convergent-series)
* [Bounded Partial Sums for Nonnegative Series](#bounded-partial-sums-for-nonnegative-series)
* [The Integral Test](#the-integral-test)
* [The Comparison Test](#the-comparison-test)
* [The Limit Comparison Test](#the-limit-comparison-test)
* [The Ratio Test](#the-ratio-test)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## Geometric Series
**Definition:** A geometric series is of the form $\sum_{n=1}^{\infty} ar^{n-1} = a + ar + ar^2 + \dots$ where $a$ and $r$ are fixed real numbers and $a \neq 0$.

*   **Partial Sum:** For $r \neq 1$, the $n$-th partial sum is $S_n = \frac{a(1-r^n)}{1-r}$.
*   **Convergence:** The series converges to $\frac{a}{1-r}$ if $|r| < 1$.
*   **Divergence:** The series diverges if $|r| \geq 1$.

## Telescoping Series
A telescoping series is one where most terms cancel out in the partial sums. This cancellation simplifies the partial sum $S_n$ to a finite number of terms, allowing for direct evaluation of the limit as $n \to \infty$. Often arises from partial fraction decomposition.

## Divergent Series & n-th Term Test
**Theorem 7 (Necessary Condition for Convergence):** If $\sum_{n=1}^{\infty} a_n$ converges, then $\lim_{n \to \infty} a_n = 0$.

**The n-th Term Test for Divergence:**
*   If $\lim_{n \to \infty} a_n$ fails to exist, or if $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ diverges.
*   **CRITICAL NOTE:** If $\lim_{n \to \infty} a_n = 0$, the test is inconclusive; the series might converge (e.g., p-series with $p>1$) or diverge (e.g., harmonic series).

## Properties of Convergent Series
**Theorem 8:** If $\sum a_n = A$ and $\sum b_n = B$ are convergent series, then:
1.  **Sum Rule:** $\sum(a_n + b_n) = \sum a_n + \sum b_n = A + B$.
2.  **Difference Rule:** $\sum(a_n - b_n) = \sum a_n - \sum b_n = A - B$.
3.  **Constant Multiple Rule:** $\sum k a_n = k \sum a_n = kA$ for any real number $k$.

**Corollary:**
1.  Any nonzero constant multiple of a divergent series diverges.
2.  If $\sum a_n$ converges and $\sum b_n$ diverges, then $\sum(a_n + b_n)$ and $\sum(a_n - b_n)$ both diverge.

## Bounded Partial Sums for Nonnegative Series
**Corollary of Theorem 6:** A series $\sum_{n=1}^{\infty} a_n$ of nonnegative terms converges if and only if its partial sums are bounded from above.

## The Integral Test
**Theorem 9 (The Integral Test):** Let $\{a_n\}$ be a sequence of positive terms. Suppose $a_n = f(n)$, where $f$ is a continuous, positive, decreasing function for all $x \geq N$ (for some positive integer $N$). Then the series $\sum_{n=N}^{\infty} a_n$ and the integral $\int_{N}^{\infty} f(x) dx$ both converge or both diverge.

*   **p-series:** A series of the form $\sum_{n=1}^{\infty} \frac{1}{n^p}$.
    *   Converges if $p > 1$.
    *   Diverges if $p \leq 1$. (The case $p=1$ is the harmonic series, which diverges.)

## The Comparison Test
**Theorem 10 (The Comparison Test):** Let $\sum a_n$ be a series with no negative terms ($a_n \geq 0$).
1.  **Convergence:** If there exists a convergent series $\sum c_n$ such that $a_n \leq c_n$ for all $n > N$ (for some integer $N$), then $\sum a_n$ converges.
2.  **Divergence:** If there exists a divergent series $\sum d_n$ of nonnegative terms such that $a_n \geq d_n$ for all $n > N$ (for some integer $N$), then $\sum a_n$ diverges.

## The Limit Comparison Test
**Theorem 11 (The Limit Comparison Test):** Suppose that $a_n > 0$ and $b_n > 0$ for all $n \geq N$.
1.  If $\lim_{n \to \infty} \frac{a_n}{b_n} = c$ where $c$ is a finite positive number ($c > 0$), then both $\sum a_n$ and $\sum b_n$ either converge or both diverge.
2.  If $\lim_{n \to \infty} \frac{a_n}{b_n} = 0$ and $\sum b_n$ converges, then $\sum a_n$ converges.
3.  If $\lim_{n \to \infty} \frac{a_n}{b_n} = \infty$ and $\sum b_n$ diverges, then $\sum a_n$ diverges.

## The Ratio Test
**Theorem 12 (The Ratio Test):** Let $\sum a_n$ be a series with positive terms, and suppose that $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = \rho$.
1.  **Convergence:** If $\rho < 1$, the series converges.
2.  **Divergence:** If $\rho > 1$ or $\rho = \infty$, the series diverges.
3.  **Inconclusive:** If $\rho = 1$, the test is inconclusive (another test must be used).

## Key Formulas
*   **Geometric Series Sum:** If $|r|<1$, $\sum_{n=1}^{\infty} ar^{n-1} = \frac{a}{1-r}$.
*   **p-series Convergence:** $\sum_{n=1}^{\infty} \frac{1}{n^p}$ converges if $p > 1$.

## Quick Summary
This lecture covered fundamental methods for determining the convergence or divergence of infinite series. We started with **Geometric Series** (sum and conditions for convergence based on common ratio $r$) and **Telescoping Series** (cancellation of terms). The **n-th Term Test** provides a necessary condition for convergence and a divergence test. For series with non-negative terms, the **Integral Test** (comparing with improper integrals), **Comparison Test** (direct comparison with known series), and **Limit Comparison Test** (evaluating the limit of the ratio of terms) are powerful tools. Finally, the **Ratio Test** uses the limit of consecutive term ratios to determine convergence or divergence, especially useful for series involving factorials or powers. Properties of convergent series allow algebraic manipulation, while understanding when tests are inconclusive is crucial.