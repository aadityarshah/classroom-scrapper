---
title: |
  Limit and Continuity
lecture_number: 1
lecture_name: |
  Limit and Continuity
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 1
sidebar_position: 1
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Limit and Continuity
date: |
  2023-10-27
tags:
  - Math
  - Calculus
  - Limits
  - Continuity
  - Average Rate of Change
  - Epsilon-Delta
math: true
summary: |
  This lecture introduces the fundamental concepts of limits and continuity, covering average and instantaneous rates of change, preliminary and formal definitions of limits, one-sided and infinite limits, key limit laws, the Sandwich Theorem, and definitions and types of discontinuities.
---

# Limit and Continuity

## Table of Contents
* [Average Rate of Change](#average-rate-of-change)
* [Instantaneous Rate of Change](#instantaneous-rate-of-change)
* [Definition of Limit (Preliminary)](#definition-of-limit-preliminary)
* [One-Sided Limits](#one-sided-limits)
* [Infinite Limits](#infinite-limits)
* [Relationship Between One-Sided and Two-Sided Limits](#relationship-between-one-sided-and-two-sided-limits)
* [Limit Laws](#limit-laws)
* [The Sandwich Theorem](#the-sandwich-theorem)
* [Limit of the Ratio $\sin \theta / \theta$ as $\theta \to 0$](#limit-of-the-ratio-sin-theta-theta-as-theta-to-0)
* [Epsilon-Delta Definition of Limit](#epsilon-delta-definition-of-limit)
* [Epsilon-Delta Definitions of One-Sided Limits](#epsilon-delta-definitions-of-one-sided-limits)
* [Epsilon-B Definition of Infinite Limits](#epsilon-b-definition-of-infinite-limits)
* [Continuity Definitions](#continuity-definitions)
* [Types of Discontinuity](#types-of-discontinuity)

## Average Rate of Change
**Definition:** The average rate of change of $y = f(x)$ with respect to $x$ over the interval $[x_1, x_2]$ is the slope of the secant line connecting $(x_1, f(x_1))$ and $(x_2, f(x_2))$.
$$ \frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1} = \frac{f(x_1 + h) - f(x_1)}{h}, \quad h \neq 0 $$
where $h = x_2 - x_1$.

## Instantaneous Rate of Change
The instantaneous rate of change represents how fast a quantity is changing at a specific moment. It is approached by examining average rates of change over increasingly smaller intervals, leading to the concept of limits and the slope of a tangent line.

## Definition of Limit (Preliminary)
**Definition:** Suppose a function $f(x)$ is defined for all $x$ near a point $a$, except possibly at $a$ itself. If $f(x)$ gets arbitrarily close to a number $L$ as $x$ gets sufficiently close to $a$ (but not equal to $a$), we say that $f$ approaches the limit $L$ as $x$ approaches $a$, and write:
$$ \lim_{x \to a} f(x) = L $$
The existence of a limit at $a$ does not depend on the function's value at $a$.

## One-Sided Limits
**Definition (Right-sided limit):** If $f$ is defined for all $x$ near $a$ with $x > a$, and $f(x)$ is arbitrarily close to $L$ for $x$ sufficiently close to $a$ with $x > a$, we write:
$$ \lim_{x \to a^+} f(x) = L $$
**Definition (Left-sided limit):** If $f$ is defined for all $x$ near $a$ with $x < a$, and $f(x)$ is arbitrarily close to $L$ for $x$ sufficiently close to $a$ with $x < a$, we write:
$$ \lim_{x \to a^-} f(x) = L $$

## Infinite Limits
**Definition:** Suppose $f$ is defined for all $x$ near $a$.
*   If $f(x)$ grows arbitrarily large for all $x$ sufficiently close (but not equal) to $a$, we write:
    $$ \lim_{x \to a} f(x) = \infty $$
*   If $f(x)$ is negative and grows arbitrarily large in magnitude for all $x$ sufficiently close (but not equal) to $a$, we write:
    $$ \lim_{x \to a} f(x) = -\infty $$
In both cases, the limit does not exist.

## Relationship Between One-Sided and Two-Sided Limits
**Theorem:** Assume $f$ is defined for all $x$ near $a$ except possibly at $a$. Then, the two-sided limit $\lim_{x \to a} f(x) = L$ if and only if both the right-sided limit and the left-sided limit exist and are equal to $L$:
$$ \lim_{x \to a} f(x) = L \quad \text{iff} \quad \lim_{x \to a^+} f(x) = L \quad \text{and} \quad \lim_{x \to a^-} f(x) = L $$
If one-sided limits differ or do not exist, the two-sided limit does not exist.

## Limit Laws
**Theorem 1:** If $L, M, c,$ and $k$ are real numbers, and $\lim_{x \to c} f(x) = L$ and $\lim_{x \to c} g(x) = M$, then:
1.  **Sum Rule:** $\lim_{x \to c}(f(x) + g(x)) = L + M$
2.  **Difference Rule:** $\lim_{x \to c}(f(x) - g(x)) = L - M$
3.  **Constant Multiple Rule:** $\lim_{x \to c}(k \cdot f(x)) = k \cdot L$
4.  **Product Rule:** $\lim_{x \to c}(f(x) \cdot g(x)) = L \cdot M$
5.  **Quotient Rule:** $\lim_{x \to c}\frac{f(x)}{g(x)} = \frac{L}{M}$, provided $M \neq 0$
6.  **Power Rule:** $\lim_{x \to c}[f(x)]^n = L^n$, for a positive integer $n$
7.  **Root Rule:** $\lim_{x \to c}\sqrt[n]{f(x)} = \sqrt[n]{L} = L^{1/n}$, for a positive integer $n$. If $n$ is even, assume $L > 0$.

## The Sandwich Theorem
**Theorem 4 (Also known as Squeeze Theorem or Pinching Theorem):** Suppose that $g(x) \le f(x) \le h(x)$ for all $x$ in some open interval containing $c$, except possibly at $x = c$ itself. If also $\lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L$, then:
$$ \lim_{x \to c} f(x) = L $$

## Limit of the Ratio $\sin \theta / \theta$ as $\theta \to 0$
**Theorem 7:** For $\theta$ in radians:
$$ \lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1 $$

## Epsilon-Delta Definition of Limit
**Definition:** Let $f(x)$ be defined on an open interval about $c$, except possibly at $c$ itself. We say that the limit of $f(x)$ as $x$ approaches $c$ is the number $L$, and write $\lim_{x \to c} f(x) = L$, if for every number $\epsilon > 0$, there exists a corresponding number $\delta > 0$ such that for all $x$:
$$ 0 < |x - c| < \delta \implies |f(x) - L| < \epsilon $$
This means that $f(x)$ can be made arbitrarily close to $L$ (within $\epsilon$) by taking $x$ sufficiently close to $c$ (within $\delta$), but not equal to $c$.

## Epsilon-Delta Definitions of One-Sided Limits
**Definition (Right-hand limit):** We say that $f(x)$ has right-hand limit $L$ at $c$, and write $\lim_{x \to c^+} f(x) = L$, if for every $\epsilon > 0$ there exists a corresponding $\delta > 0$ such that for all $x$:
$$ c < x < c + \delta \implies |f(x) - L| < \epsilon $$
**Definition (Left-hand limit):** We say that $f(x)$ has left-hand limit $L$ at $c$, and write $\lim_{x \to c^-} f(x) = L$, if for every $\epsilon > 0$ there exists a corresponding $\delta > 0$ such that for all $x$:
$$ c - \delta < x < c \implies |f(x) - L| < \epsilon $$

## Epsilon-B Definition of Infinite Limits
**Definition:**
*   $\lim_{x \to c} f(x) = \infty$: For every large positive real number $B$, there exists a corresponding $\delta > 0$ such that for all $x$:
    $$ 0 < |x - c| < \delta \implies f(x) > B $$
*   $\lim_{x \to c} f(x) = -\infty$: For every large positive real number $B$, there exists a corresponding $\delta > 0$ such that for all $x$:
    $$ 0 < |x - c| < \delta \implies f(x) < -B $$

## Continuity Definitions
Let $c$ be a real number on the $x$-axis.
*   **Continuous at $c$**: The function $f$ is continuous at $c$ if:
    1.  $f(c)$ is defined.
    2.  $\lim_{x \to c} f(x)$ exists.
    3.  $\lim_{x \to c} f(x) = f(c)$.
*   **Right-continuous at $c$**: The function $f$ is right-continuous at $c$ if:
    $$ \lim_{x \to c^+} f(x) = f(c) $$
*   **Left-continuous at $c$**: The function $f$ is left-continuous at $c$ if:
    $$ \lim_{x \to c^-} f(x) = f(c) $$

## Types of Discontinuity
1.  **Removable Discontinuity**: Occurs when $\lim_{x \to c} f(x)$ exists, but $f(c)$ is either undefined or $f(c) \neq \lim_{x \to c} f(x)$. This can often be "removed" by redefining $f(c)$.
2.  **Jump Discontinuity**: Occurs when the one-sided limits exist but are not equal, i.e., $\lim_{x \to c^-} f(x) \neq \lim_{x \to c^+} f(x)$. Example: the greatest integer function at integer values.
3.  **Infinite Discontinuity**: Occurs when $\lim_{x \to c} f(x) = \pm \infty$. This is characterized by a vertical asymptote at $x=c$. Example: $f(x) = 1/x^2$ at $x=0$.
4.  **Oscillating Discontinuity**: Occurs when the function values oscillate infinitely often as $x$ approaches $c$, preventing any limit (even one-sided) from existing. Example: $f(x) = \sin(1/x)$ at $x=0$.

## Key Formulas
*   Average Rate of Change: $\frac{\Delta y}{\Delta x} = \frac{f(x_2) - f(x_1)}{x_2 - x_1}$
*   Preliminary Limit Definition: $\lim_{x \to a} f(x) = L$
*   One-Sided Limits: $\lim_{x \to a^+} f(x) = L$, $\lim_{x \to a^-} f(x) = L$
*   Limit Laws (Sum, Difference, Constant Multiple, Product, Quotient, Power, Root)
*   Sandwich Theorem: If $g(x) \le f(x) \le h(x)$ and $\lim g(x) = \lim h(x) = L$, then $\lim f(x) = L$.
*   Special Limit: $\lim_{\theta \to 0} \frac{\sin \theta}{\theta} = 1$
*   Epsilon-Delta Limit Definition: $0 < |x - c| < \delta \implies |f(x) - L| < \epsilon$
*   Continuity at $c$: $\lim_{x \to c} f(x) = f(c)$

## Quick Summary
This lecture established limits as a fundamental concept for understanding instantaneous rates of change and tangent lines. We defined limits, including one-sided and infinite limits, and explored their properties through limit laws and the Sandwich Theorem. The formal epsilon-delta definition provided a rigorous basis. Finally, continuity was defined based on limits, and various types of discontinuities were categorized.