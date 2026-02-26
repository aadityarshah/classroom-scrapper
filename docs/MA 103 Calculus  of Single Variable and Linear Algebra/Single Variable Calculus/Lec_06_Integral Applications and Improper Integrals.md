---
title: |
  Integral Applications and Improper Integrals
lecture_number: 6
lecture_name: |
  Integral Applications and Improper Integrals
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 6
sidebar_position: 6
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Integral Applications and Improper Integrals
  2023-10-27
tags:
  - Math
  - Calculus
  - Integrals
  - Improper Integrals
  - Area
  - Mean Value Theorem
summary: |
  This lecture covers the average value of a function, the Mean Value Theorem for Definite Integrals, substitution in definite integrals, area between curves (both with respect to x and y), and definitions and comparison tests for Type I and Type II improper integrals.
math: true
---

# Integral Applications and Improper Integrals

## Table of Contents
*   The Average or Mean Value of a Function
*   The Mean Value Theorem for Definite Integrals
*   Substitution in Definite Integrals
*   Area of a Region Between Two Curves (with respect to x)
*   Area of a Region Between Two Curves (with respect to y)
*   Type I Improper Integrals
*   Type II Improper Integrals
*   Direct Comparison Test for Improper Integrals
*   Limit Comparison Test for Improper Integrals

## The Average or Mean Value of a Function

**DEFINITION: The Average or Mean Value of a Function**
If $f$ is integrable on $[a, b]$, its average value, $av(f)$, is defined as:
$$av(f) = \frac{1}{b-a} \int_{a}^{b} f(x) dx$$
This value can be approximated by Riemann sums, representing the average height of the function over the interval.

## The Mean Value Theorem for Definite Integrals

**THEOREM 3: The Mean Value Theorem for Definite Integrals**
If $f$ is continuous on $[a, b]$, then there exists at least one point $c$ in $[a, b]$ such that:
$$f(c) = \frac{1}{b-a} \int_{a}^{b} f(x) dx$$
This theorem guarantees that a continuous function must attain its average value at some point within the interval.

## Substitution in Definite Integrals

**THEOREM 6: Substitution in Definite Integrals**
If $g'$ is continuous on the interval $[a, b]$ and $f$ is continuous on the range of $g$, then:
$$\int_{a}^{b} f(g(x)) g'(x) dx = \int_{g(a)}^{g(b)} f(u) du$$
This allows transforming a definite integral into a simpler form by changing variables and adjusting the limits of integration accordingly.

## Area of a Region Between Two Curves (with respect to x)

**DEFINITION: Area of a Region Between Two Curves**
Suppose $f$ and $g$ are continuous functions with $f(x) \geq g(x)$ on the interval $[a, b]$. The area $A$ of the region bounded by the graphs of $f$ and $g$ on $[a, b]$ is given by:
$$A = \int_{a}^{b} (f(x) - g(x)) dx$$

## Area of a Region Between Two Curves (with respect to y)

**DEFINITION: Area of a Region Between Two Curves with Respect to y**
Suppose $f$ and $g$ are continuous functions with $f(y) \geq g(y)$ on the interval $[c, d]$. The area $A$ of the region bounded by the graphs $x = f(y)$ and $x = g(y)$ on $[c, d]$ is given by:
$$A = \int_{c}^{d} (f(y) - g(y)) dy$$

## Type I Improper Integrals

**DEFINITION: Type I Improper Integrals**
Integrals with infinite limits of integration are improper integrals of Type I.
1.  If $f(x)$ is continuous on $[a, \infty)$:
    $$\int_{a}^{\infty} f(x) dx = \lim_{b \to \infty} \int_{a}^{b} f(x) dx$$
2.  If $f(x)$ is continuous on $(-\infty, b]$:
    $$\int_{-\infty}^{b} f(x) dx = \lim_{a \to -\infty} \int_{a}^{b} f(x) dx$$
3.  If $f(x)$ is continuous on $(-\infty, \infty)$:
    $$\int_{-\infty}^{\infty} f(x) dx = \int_{-\infty}^{c} f(x) dx + \int_{c}^{\infty} f(x) dx$$
    for any real number $c$.
If the limit is finite, the integral **converges** to that value; otherwise, it **diverges**.

## Type II Improper Integrals

**DEFINITION: Type II Improper Integrals**
Integrals of functions that become infinite at a point within the interval of integration are improper integrals of Type II.
1.  If $f(x)$ is continuous on $(a, b]$ and discontinuous at $a$:
    $$\int_{a}^{b} f(x) dx = \lim_{c \to a^+} \int_{c}^{b} f(x) dx$$
2.  If $f(x)$ is continuous on $[a, b)$ and discontinuous at $b$:
    $$\int_{a}^{b} f(x) dx = \lim_{c \to b^-} \int_{a}^{c} f(x) dx$$
3.  If $f(x)$ is discontinuous at $c$, where $a $<$ c $<$ b$, and continuous on $[a, c) \cup (c, b]$:
    $$\int_{a}^{b} f(x) dx = \int_{a}^{c} f(x) dx + \int_{c}^{b} f(x) dx$$
If the limit is finite, the integral **converges** to that value; otherwise, it **diverges**.

## Direct Comparison Test for Improper Integrals

**THEOREM 1: Direct Comparison Test**
Let $f$ and $g$ be continuous on $[a, \infty)$ with $0 \leq f(x) \leq g(x)$ for all $x \geq a$.
1.  If $\int_{a}^{\infty} g(x) dx$ converges, then $\int_{a}^{\infty} f(x) dx$ converges.
2.  If $\int_{a}^{\infty} f(x) dx$ diverges, then $\int_{a}^{\infty} g(x) dx$ diverges.

## Limit Comparison Test for Improper Integrals

**THEOREM 2: Limit Comparison Test**
If the positive functions $f$ and $g$ are continuous on $[a, \infty)$ and $\lim_{x \to \infty} \frac{f(x)}{g(x)} = L$, where $0 $<$ L $<$ \infty$.
Then $\int_{a}^{\infty} f(x) dx$ and $\int_{a}^{\infty} g(x) dx$ either both converge or both diverge.

## Key Formulas

**General Integration Formulas**
1.  $\int \cos ax \, dx = \frac{1}{a} \sin ax + C$
2.  $\int \sin ax \, dx = -\frac{1}{a} \cos ax + C$
3.  $\int \sec^2 ax \, dx = \frac{1}{a} \tan ax + C$
4.  $\int \csc^2 ax \, dx = -\frac{1}{a} \cot ax + C$
5.  $\int \sec ax \tan ax \, dx = \frac{1}{a} \sec ax + C$
6.  $\int \csc ax \cot ax \, dx = -\frac{1}{a} \csc ax + C$
7.  $\int e^{ax} \, dx = \frac{1}{a} e^{ax} + C$
8.  $\int b^x \, dx = \frac{b^x}{\ln b} + C$, for $b $>$ 0$, $b \neq 1$
9.  $\int \frac{dx}{a^2 + x^2} = \frac{1}{a} \tan^{-1} \frac{x}{a} + C$
10. $\int \frac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1} \frac{x}{a} + C$, for $a $>$ 0$
11. $\int \frac{dx}{x\sqrt{x^2 - a^2}} = \frac{1}{a} \sec^{-1} \left| \frac{x}{a} \right| + C$, for $a $>$ 0$

## Quick Summary

This lecture established the concept of a function's **average value** and the **Mean Value Theorem for Definite Integrals**, guaranteeing this value is attained. We reviewed **substitution for definite integrals** and explored methods for calculating the **area between curves**, both with respect to $x$ and $y$. A significant portion covered **improper integrals**, defining **Type I** (infinite limits) and **Type II** (discontinuities within the interval) integrals by their limit definitions for convergence or divergence. Finally, the **Direct Comparison Test** and **Limit Comparison Test** were introduced as powerful tools to determine the convergence or divergence of improper integrals by comparing them to known integrals.