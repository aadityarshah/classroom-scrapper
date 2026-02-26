---
title: |
  Concavity, Linear Approximation, and L'Hôpital's Rule
lecture_number: 4
lecture_name: |
  Concavity, Linear Approximation, and L'Hôpital's Rule
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 4
sidebar_position: 4
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Calculus
date: |
  2023-10-27
tags:
  - Calculus
  - Derivatives
  - Concavity
  - L'Hôpital's Rule
  - Approximation
  - Mean Value Theorem
summary: |
  This lecture explores the interpretation of the second derivative in determining function concavity and inflection points. It introduces the concept of linear approximation and its applications, followed by L'Hôpital's Rule for evaluating indeterminate forms. Finally, Cauchy's Mean Value Theorem and Darboux's Theorem on the intermediate value property for derivatives are discussed.
math: true
---

# Concavity, Linear Approximation, and L'Hôpital's Rule

## Table of Contents
- Concavity
- Second Derivative Test for Concavity
- Point of Inflection
- Second Derivative Test for Local Extrema
- Linear Approximation
- L'Hôpital's Rule for $0/0$ Indeterminate Forms
- L'Hôpital's Rule for $\infty/\infty$ Indeterminate Forms
- Cauchy's Mean Value Theorem
- Darboux's Theorem (Intermediate Value Property for $f'$)

## Concavity
**DEFINITION: Concave Up, Concave Down**
The graph of a differentiable function $y = f(x)$ is:
- **Concave Up** on an open interval $I$ if $f'$ is increasing on $I$.
- **Concave Down** on an open interval $I$ if $f'$ is decreasing on $I$.

## Second Derivative Test for Concavity
**THEOREM: Second Derivative Test for Concavity**
Let $y = f(x)$ be twice-differentiable on an interval $I$.
1.  If $f''(x) $>$ 0$ on $I$, the graph of $f$ over $I$ is **concave up**.
2.  If $f''(x) $<$ 0$ on $I$, the graph of $f$ over $I$ is **concave down**.

## Point of Inflection
**DEFINITION: Point of Inflection**
A point where the graph of a function has a tangent line and where the concavity changes is a **point of inflection**. A point of inflection may occur where $f''(x) = 0$ or where $f''(x)$ does not exist, provided the concavity actually changes sign around that point.

## Second Derivative Test for Local Extrema
**THEOREM: Second Derivative Test for Local Extrema**
Suppose $f''(x)$ is continuous on an open interval containing $c$ with $f'(c) = 0$.
- If $f''(c) $>$ 0$, then $f$ has a local **minimum** at $c$.
- If $f''(c) $<$ 0$, then $f$ has a local **maximum** at $c$.
- If $f''(c) = 0$, the test is inconclusive; $f$ may have a local maximum, a local minimum, or neither at $c$.

## Linear Approximation
**DEFINITION: Linear Approximation to $f$ at $a$**
If $f$ is differentiable on an interval $I$ containing $a$, the linear approximation to $f$ at $a$ is the linear function:
$$L(x) = f(a) + f'(a)(x-a)$$
Graphically, $L(x)$ represents the tangent line to $f(x)$ at $x=a$. If $f$ is concave up at $(a, f(a))$, $L(x)$ underestimates $f(x)$ near $a$. If $f$ is concave down at $(a, f(a))$, $L(x)$ overestimates $f(x)$ near $a$.

## L'Hôpital's Rule for $0/0$ Indeterminate Forms
**THEOREM: L'Hôpital's Rule**
Suppose $f$ and $g$ are differentiable on an open interval $I$ containing $a$ with $g'(x) \neq 0$ on $I$ when $x \neq a$. If $\lim_{x \to a} f(x) = 0$ and $\lim_{x \to a} g(x) = 0$, then:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
This rule applies provided the limit on the right exists (or is $\pm \infty$). It also applies when $x \to \pm \infty$, $x \to a^+$, or $x \to a^-$.

## L'Hôpital's Rule for $\infty/\infty$ Indeterminate Forms
**THEOREM: L'Hôpital's Rule ($\infty/\infty$)**
Suppose $f$ and $g$ are differentiable on an open interval $I$ containing $a$ with $g'(x) \neq 0$ on $I$ when $x \neq a$. If $\lim_{x \to a} f(x) = \pm \infty$ and $\lim_{x \to a} g(x) = \pm \infty$, then:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
This rule applies provided the limit on the right exists (or is $\pm \infty$). It also applies when $x \to \pm \infty$, $x \to a^+$, or $x \to a^-$.

## Cauchy's Mean Value Theorem
**THEOREM: Cauchy's Mean Value Theorem**
Suppose functions $f$ and $g$ are continuous on $[a, b]$ and differentiable throughout $(a, b)$, and $g'(x) \neq 0$ throughout $(a, b)$. Then there exists a number $c$ in $(a, b)$ at which:
$$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

## Darboux's Theorem (Intermediate Value Property for $f'$)
**THEOREM: Darboux's Theorem**
Let $I$ be a closed interval, and $f: I \to \mathbb{R}$ be a differentiable function. Then $f'$ has an intermediate value property: if $a, b \in I$ with $a $<$ b$, then for every $y$ between $f'(a)$ and $f'(b)$, there exists $x \in [a, b]$ such that $f'(x) = y$.

## Key Formulas
- **Concavity:**
  - $f''(x) $>$ 0 \implies$ Concave Up
  - $f''(x) $<$ 0 \implies$ Concave Down
- **Local Extrema (Second Derivative Test):**
  - If $f'(c) = 0$ and $f''(c) $>$ 0 \implies$ Local Minimum at $c$.
  - If $f'(c) = 0$ and $f''(c) $<$ 0 \implies$ Local Maximum at $c$.
- **Linear Approximation:**
  $$L(x) = f(a) + f'(a)(x-a)$$
- **L'Hôpital's Rule:** (for $0/0$ or $\infty/\infty$ forms)
  $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
- **Cauchy's Mean Value Theorem:**
  $$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

## Quick Summary
This lecture clarified how the second derivative dictates a function's concavity (upward or downward) and the identification of inflection points where concavity shifts. The Second Derivative Test was detailed for classifying critical points as local maxima or minima based on the sign of $f''(c)$. Linear approximation, defined as the tangent line $L(x) = f(a) + f'(a)(x-a)$, was presented as a method for local estimation. L'Hôpital's Rule provided a crucial tool for evaluating indeterminate limits of the $0/0$ or $\infty/\infty$ forms by examining the ratio of derivatives. Finally, the lecture introduced Cauchy's Mean Value Theorem, extending the Mean Value Theorem to two functions, and Darboux's Theorem, which establishes the Intermediate Value Property for derivatives.