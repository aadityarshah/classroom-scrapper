---
title: |
  Infinite Sequences and Series
lecture_number: 7
lecture_name: |
  Infinite Sequences and Series
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 7
sidebar_position: 7
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Infinite Sequences and Series
date: |
  2023-10-27
tags:
  - Mathematics
  - Calculus
  - Sequences
  - Series
summary: |
  Concise notes on definitions, theorems, and formulas related to infinite sequences and series, including convergence, divergence, limits, and the Sandwich and Continuous Function Theorems.
math: true
---

# Infinite Sequences and Series

## Table of Contents
* [Infinite Sequences](#infinite-sequences)
* [Convergence and Divergence of Sequences](#convergence-and-divergence-of-sequences)
* [Properties of Convergent Sequences (Theorem 1)](#properties-of-convergent-sequences-theorem-1)
* [Sandwich Theorem for Sequences (Theorem 2)](#sandwich-theorem-for-sequences-theorem-2)
* [Continuous Function Theorem for Sequences (Theorem 3)](#continuous-function-theorem-for-sequences-theorem-3)
* [Function-Sequence Limit Theorem (Theorem 4)](#function-sequence-limit-theorem-theorem-4)
* [Common Sequence Limits (Theorem 5)](#common-sequence-limits-theorem-5)
* [Monotonic and Bounded Sequences](#monotonic-and-bounded-sequences)
* [Infinite Series](#infinite-series)
* [Partial Sums and Series Convergence](#partial-sums-and-series-convergence)
* [Geometric Series](#geometric-series)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## Infinite Sequences
**DEFINITION: Infinite Sequence**
An infinite sequence of numbers is a function $f: \mathbb{N} \to \mathbb{R}$ whose domain is the set of positive integers. It is denoted by $\{a_n\}_{n=1}^\infty$ where $a_n = f(n)$ is the $n$-th term.

## Convergence and Divergence of Sequences
**DEFINITIONS: Converges, Diverges, Limit**
A sequence $\{a_n\}$ converges to a number $L$ if for every positive number $\epsilon$ there corresponds an integer $N$ such that for all $n $>$ N$, $|a_n - L| $<$ \epsilon$. We write $\lim_{n \to \infty} a_n = L$. If no such number $L$ exists, the sequence $\{a_n\}$ diverges.

**DEFINITION: Diverges to Infinity**
A sequence $\{a_n\}$ diverges to infinity if for every number $M$ there is an integer $N$ such that for all $n $>$ N$, $a_n $>$ M$. We write $\lim_{n \to \infty} a_n = \infty$. Similarly, it diverges to negative infinity if for every number $m$ there is an integer $N$ such that for all $n $>$ N$, $a_n $<$ m$. We write $\lim_{n \to \infty} a_n = -\infty$.

## Properties of Convergent Sequences (Theorem 1)
Let $\{a_n\}$ and $\{b_n\}$ be sequences of real numbers with $\lim_{n \to \infty} a_n = A$ and $\lim_{n \to \infty} b_n = B$.
1.  **Sum Rule**: $\lim_{n \to \infty}(a_n + b_n) = A + B$
2.  **Difference Rule**: $\lim_{n \to \infty}(a_n - b_n) = A - B$
3.  **Product Rule**: $\lim_{n \to \infty}(a_n b_n) = A \cdot B$
4.  **Constant Multiple Rule**: $\lim_{n \to \infty}(k b_n) = k \cdot B$ (for any number $k$)
5.  **Quotient Rule**: $\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{A}{B}$ (if $B \ne 0$)

## Sandwich Theorem for Sequences (Theorem 2)
Let $\{a_n\}$, $\{b_n\}$, and $\{c_n\}$ be sequences of real numbers. If $a_n \le b_n \le c_n$ for all $n$ beyond some index $N$, and if $\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = L$, then $\lim_{n \to \infty} b_n = L$.

## Continuous Function Theorem for Sequences (Theorem 3)
Let $\{a_n\}$ be a sequence of real numbers. If $a_n \to L$ and if $f$ is a function that is continuous at $L$ and defined at all $a_n$, then $f(a_n) \to f(L)$. This can be written as $\lim_{n \to \infty} f(a_n) = f(\lim_{n \to \infty} a_n)$.

## Function-Sequence Limit Theorem (Theorem 4)
Suppose that $f(x)$ is a function defined for all $x \ge n_0$ and that $\{a_n\}$ is a sequence of real numbers such that $a_n = f(n)$ for $n \ge n_0$. Then, if $\lim_{x \to \infty} f(x) = L$, it implies $\lim_{n \to \infty} a_n = L$.

## Common Sequence Limits (Theorem 5)
The following six sequences converge to the limits listed below:
1.  $\lim_{n \to \infty} \frac{\ln n}{n} = 0$
2.  $\lim_{n \to \infty} \sqrt[n]{n} = 1$
3.  $\lim_{n \to \infty} x^{1/n} = 1$ ($x $>$ 0$)
4.  $\lim_{n \to \infty} x^n = 0$ ($|x| $<$ 1$)
5.  $\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x$ (any $x$)
6.  $\lim_{n \to \infty} \frac{x^n}{n!} = 0$ (any $x$)
In formulas (3) through (6), $x$ remains fixed as $n \to \infty$.

## Monotonic and Bounded Sequences
**DEFINITION: Nondecreasing Sequence**
A sequence $\{a_n\}$ is nondecreasing if $a_n \le a_{n+1}$ for all $n$. Similarly, it is nonincreasing if $a_n \ge a_{n+1}$. A sequence is monotonic if it is either nondecreasing or nonincreasing.

**DEFINITIONS: Bounded, Upper Bound, Least Upper Bound**
A sequence $\{a_n\}$ is bounded from above if there exists a number $M$ such that $a_n \le M$ for all $n$. $M$ is an upper bound. If no number less than $M$ is an upper bound, $M$ is the least upper bound.
A sequence $\{a_n\}$ is bounded from below if there exists a number $m$ such that $m \le a_n$ for all $n$. $m$ is a lower bound. The greatest lower bound is the largest of all lower bounds.
A sequence is bounded if it is both bounded from above and bounded from below.

## Infinite Series
**DEFINITION: Infinite Series**
Given a sequence of numbers $\{a_n\}$, an infinite series is an expression of the form $a_1 + a_2 + a_3 + \dots + a_n + \dots$, denoted by $\sum_{n=1}^\infty a_n$. $a_n$ is called the $n$-th term of the series.

## Partial Sums and Series Convergence
**DEFINITION: Sequence of Partial Sums**
For an infinite series $\sum_{n=1}^\infty a_n$, the sequence of partial sums $\{S_n\}$ is defined as $S_1 = a_1$, $S_2 = a_1 + a_2$, $S_3 = a_1 + a_2 + a_3$, and generally $S_n = \sum_{k=1}^n a_k$.

**DEFINITION: Convergence and Divergence of a Series**
If the sequence of partial sums $\{S_n\}$ converges to a limit $L$, i.e., $\lim_{n \to \infty} S_n = L$, then the series $\sum_{n=1}^\infty a_n$ converges, and its sum is $L$. If the sequence of partial sums diverges, the series diverges.

## Geometric Series
A geometric series is of the form $a + ar + ar^2 + \dots + ar^{n-1} + \dots = \sum_{n=1}^\infty ar^{n-1}$.
The $n$-th partial sum is $S_n = \frac{a(1-r^n)}{1-r}$, provided $r \ne 1$.
If $|r| $<$ 1$, the series converges to the sum $\frac{a}{1-r}$. If $|r| \ge 1$, the series diverges (unless $a=0$).

---

## Key Formulas

*   **Infinite Sequence**: A function $f: \mathbb{N} \to \mathbb{R}$, denoted $\{a_n\}_{n=1}^\infty$.
*   **Limit of a Sequence (Definition)**: $\lim_{n \to \infty} a_n = L \iff \forall \epsilon $>$ 0, \exists N \in \mathbb{Z}^+ \text{ s.t. } \forall n $>$ N, |a_n - L| $<$ \epsilon$.
*   **Sequence Limit Rules**:
    *   $\lim (a_n \pm b_n) = \lim a_n \pm \lim b_n = A \pm B$
    *   $\lim (k \cdot a_n) = k \cdot \lim a_n = kA$
    *   $\lim (a_n \cdot b_n) = (\lim a_n) \cdot (\lim b_n) = AB$
    *   $\lim \frac{a_n}{b_n} = \frac{\lim a_n}{\lim b_n} = \frac{A}{B}$ (if $B \ne 0$)
*   **Sandwich Theorem**: If $a_n \le b_n \le c_n$ for $n $>$ N_0$ and $\lim a_n = \lim c_n = L$, then $\lim b_n = L$.
*   **Continuous Function Theorem**: If $a_n \to L$ and $f$ is continuous at $L$, then $\lim f(a_n) = f(\lim a_n) = f(L)$.
*   **Function-Sequence Limit Theorem**: If $a_n = f(n)$ and $\lim_{x \to \infty} f(x) = L$, then $\lim_{n \to \infty} a_n = L$.
*   **Common Limits (Theorem 5)**:
    1.  $\lim_{n \to \infty} \frac{\ln n}{n} = 0$
    2.  $\lim_{n \to \infty} \sqrt[n]{n} = 1$
    3.  $\lim_{n \to \infty} x^{1/n} = 1 \quad (x $>$ 0)$
    4.  $\lim_{n \to \infty} x^n = 0 \quad (|x| $<$ 1)$
    5.  $\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x$
    6.  $\lim_{n \to \infty} \frac{x^n}{n!} = 0$
*   **Nondecreasing Sequence**: $a_n \le a_{n+1}$ for all $n$.
*   **Bounded from above**: $a_n \le M$ for all $n$.
*   **Infinite Series**: $\sum_{n=1}^\infty a_n = a_1 + a_2 + a_3 + \dots$
*   **Partial Sums**: $S_n = \sum_{k=1}^n a_k$.
*   **Series Convergence**: $\sum_{n=1}^\infty a_n = L \iff \lim_{n \to \infty} S_n = L$.
*   **Geometric Series Sum**: For $\sum_{n=1}^\infty ar^{n-1}$:
    *   Partial sum: $S_n = \frac{a(1-r^n)}{1-r}$ (if $r \ne 1$).
    *   Converges to $\frac{a}{1-r}$ if $|r| $<$ 1$.
    *   Diverges if $|r| \ge 1$.

---

## Quick Summary
This lecture introduces infinite sequences as functions on positive integers and defines their convergence or divergence using the epsilon-N criterion. Key theorems for sequence limits include rules for sums, differences, products, and quotients, as well as the Sandwich Theorem and the Continuous Function Theorem for evaluating limits. The relationship between function limits and sequence limits is established. The concept extends to infinite series, defined as sums of sequence terms, whose convergence is determined by the limit of their partial sums. Finally, the specific case of geometric series is discussed, including its partial sum and convergence formula.