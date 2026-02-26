---
title: |
  Antiderivatives and Definite Integrals
lecture_number: 5
lecture_name: |
  Antiderivatives and Definite Integrals
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 5
sidebar_position: 5
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Antiderivatives, Riemann Sums, Definite Integrals, Fundamental Theorem of Calculus
date: |
  2023-10-27
tags:
  - Math
  - Calculus
  - Antiderivatives
  - Integrals
  - Riemann Sums
  - FTC
summary: |
  This lecture introduces the concept of antiderivatives, indefinite and definite integrals, Riemann sums for approximating area, and the Fundamental Theorem of Calculus.
math: true
---

# Antiderivatives and Definite Integrals

## Table of Contents
*   Antiderivatives
*   Initial Value Problems
*   Indefinite Integrals
*   Approximating Area with Rectangles
*   Partitions and Riemann Sums
*   Net Area
*   Definite Integral
*   Properties of Riemann Integral
*   Fundamental Theorem of Calculus I
*   Fundamental Theorem of Calculus II

## Antiderivatives
**DEFINITION: Antiderivative**
A function $F$ is an **antiderivative** of $f$ on an interval $I$ if $F'(x) = f(x)$ for all $x$ in $I$.
If $F$ is an antiderivative of $f$ on an interval $I$, then the most general antiderivative of $f$ on $I$ is $F(x) + C$, where $C$ is an arbitrary constant.

## Initial Value Problems
**DEFINITION: Differential Equation**
An equation of the form $y' = \frac{dy}{dx} = f(x)$ is called a **differential equation**.
**DEFINITION: Initial Value Problem**
A **differential equation** combined with an **initial condition** $y(x_0) = y_0$ is called an **initial value problem**. The initial condition is used to determine the arbitrary constant $C$.

## Indefinite Integrals
**DEFINITION: Indefinite Integral, Integral Sign, Integrand, Variable of Integration**
The set of all antiderivatives of $f$ is the **indefinite integral** of $f$ with respect to $x$, denoted by $\int f(x) dx$.
The symbol $\int$ is an **integral sign**. The function $f$ is the **integrand** of the integral, and $x$ is the **variable of integration**.

## Approximating Area with Rectangles
To find the area under a curve $y = f(x)$, we can approximate this area using a sum of rectangles. Increasing the number of rectangles ($n$) generally leads to a better approximation.

## Partitions and Riemann Sums
**DEFINITION: Partition**
By a **partition** of an interval $[a, b]$ (where $a, b \in \mathbb{R}$ and $a < b$), we mean a finite set $\{a = x_0, x_1, \dots, x_{n-1}, x_n = b\}$ of points in $[a, b]$ such that $a = x_0 < x_1 < \dots < x_{n-1} < x_n = b$.
If the interval $[a, b]$ is divided into $n$ subintervals of equal length $\Delta x = \frac{b-a}{n}$:
**DEFINITION: Riemann Sum**
If $f$ is defined on a closed interval $[a, b]$, which is divided into $n$ subintervals of equal length $\Delta x$, and $x_k^*$ is any point in the $k$-th subinterval $[x_{k-1}, x_k]$, for $k=1, 2, \dots, n$, then the sum $\sum_{k=1}^{n} f(x_k^*) \Delta x$ is called a **Riemann sum** for $f$ on $[a, b]$.
*   A **left Riemann sum** if $x_k^* = a + (k-1)\Delta x$ (the left endpoint of $[x_{k-1}, x_k]$).
*   A **right Riemann sum** if $x_k^* = a + k\Delta x$ (the right endpoint of $[x_{k-1}, x_k]$).
*   A **midpoint Riemann sum** if $x_k^* = a + (k-\frac{1}{2})\Delta x$ (the midpoint of $[x_{k-1}, x_k]$).

## Net Area
**DEFINITION: Net Area**
Consider the region $R$ bounded by the graph of a continuous function $f$ and the $x$-axis between $x = a$ and $x = b$. The **net area** of $R$ is the sum of the areas of the parts of $R$ that lie above the $x$-axis minus the sum of the areas of the parts of $R$ that lie below the $x$-axis on $[a, b]$.
As the number of subintervals $n$ increases, the Riemann sums approach the net area.

## Definite Integral
**DEFINITION: General Riemann Sum**
Given a partition $P = \{x_0, x_1, \dots, x_n\}$ of $[a, b]$ with subintervals $[x_{k-1}, x_k]$ of length $\Delta x_k$, and a chosen point $x_k^*$ in each subinterval, the **general Riemann sum** is $\sum_{k=1}^{n} f(x_k^*) \Delta x_k$.
**DEFINITION: Definite Integral**
A function $f$ defined on $[a, b]$ is **integrable** on $[a, b]$ if the limit $\lim_{\Delta x_k \to 0} \sum_{k=1}^{n} f(x_k^*) \Delta x_k$ exists and is unique over all partitions of $[a, b]$ and all choices of $x_k^*$. This limit is the **definite integral of $f$ from $a$ to $b$**, written as:
$$ \int_a^b f(x) dx = \lim_{\Delta x_k \to 0} \sum_{k=1}^{n} f(x_k^*) \Delta x_k $$
When each partition has $n$ equal subintervals of width $\Delta x = \frac{b-a}{n}$, the definite integral can also be written as:
$$ \int_a^b f(x) dx = \lim_{n \to \infty} \sum_{k=1}^{n} f(c_k) \Delta x $$

## Properties of Riemann Integral
Let $f$ and $g$ be integrable functions on an interval that contains $a, b,$ and $p$.
1.  $\int_a^a f(x) dx = 0$
2.  $\int_a^b f(x) dx = - \int_b^a f(x) dx$
3.  $\int_a^b (f(x) \pm g(x)) dx = \int_a^b f(x) dx \pm \int_a^b g(x) dx$
4.  $\int_a^b c f(x) dx = c \int_a^b f(x) dx$ for any constant $c$
5.  $\int_a^b f(x) dx = \int_a^p f(x) dx + \int_p^b f(x) dx$
6.  The product $fg$ is also integrable.

**Comparison Properties:**
*   If $f(x) \ge g(x)$ on $[a, b]$, then $\int_a^b f(x) dx \ge \int_a^b g(x) dx$.
*   If $m \le f(x) \le M$ for all $x \in [a, b]$, then $m(b-a) \le \int_a^b f(x) dx \le M(b-a)$.

## Fundamental Theorem of Calculus I
**THEOREM (Fundamental Theorem of Calculus I - FTC I)**
If $F: [a, b] \to \mathbb{R}$ is a differentiable function on $[a, b]$ with $F' = f$ where $f: [a, b] \to \mathbb{R}$ is Riemann integrable, then:
$$ \int_a^b f(x) dx = F(b) - F(a) $$

## Fundamental Theorem of Calculus II
**THEOREM (Fundamental Theorem of Calculus II - FTC II)**
Suppose $f: [a, b] \to \mathbb{R}$ is Riemann integrable and $F: [a, b] \to \mathbb{R}$ is defined by:
$$ F(x) = \int_a^x f(t) dt $$
Then $F$ is continuous on $[a, b]$. Moreover, if $f$ is continuous at $c \in [a, b]$, $F$ is differentiable at $c$ and $F'(c) = f(c)$.

**THEOREM (Related Form)**
A function $F: [a, b] \to \mathbb{R}$ belongs to $C^1[a, b]$ if and only if there is a continuous function $f: [a, b] \to \mathbb{R}$ such that:
$$ F(x) = F(a) + \int_a^x f(t) dt, \quad \text{for all } x \in [a, b] $$
In this case, we have $F'(x) = f(x)$ for all $x \in [a, b]$.

## Key Formulas
*   **General Antiderivative:** $F(x) + C$, where $F'(x) = f(x)$.
*   **Indefinite Integral:** $\int f(x) dx = F(x) + C$.
*   **Antiderivative of $x^n$ ($n \neq -1$):** $\int x^n dx = \frac{x^{n+1}}{n+1} + C$.
*   **Antiderivative of $\sin(kx)$:** $\int \sin(kx) dx = - \frac{\cos(kx)}{k} + C$.
*   **Antiderivative of $\cos(kx)$:** $\int \cos(kx) dx = \frac{\sin(kx)}{k} + C$.
*   **Antiderivative of $\sec^2 x$:** $\int \sec^2 x dx = \tan x + C$.
*   **Antiderivative of $\csc^2 x$:** $\int \csc^2 x dx = - \cot x + C$.
*   **Antiderivative of $\sec x \tan x$:** $\int \sec x \tan x dx = \sec x + C$.
*   **Antiderivative of $\csc x \cot x$:** $\int \csc x \cot x dx = - \csc x + C$.
*   **Riemann Sum (General):** $\sum_{k=1}^{n} f(x_k^*) \Delta x_k$.
*   **Definite Integral:** $\int_a^b f(x) dx = \lim_{n \to \infty} \sum_{k=1}^{n} f(c_k) \Delta x$, where $\Delta x = \frac{b-a}{n}$.
*   **Fundamental Theorem of Calculus I (FTC I):** $\int_a^b f(x) dx = F(b) - F(a)$, where $F'(x) = f(x)$.
*   **Fundamental Theorem of Calculus II (FTC II):** If $F(x) = \int_a^x f(t) dt$, then $F'(x) = f(x)$ if $f$ is continuous.

## Quick Summary
This lecture covered the foundational concepts of integral calculus. We defined antiderivatives as functions whose derivative is the original function, noting that the general antiderivative includes an arbitrary constant $C$. Initial value problems combine a differential equation ($y' = f(x)$) with an initial condition ($y(x_0)=y_0$) to find a particular antiderivative. The indefinite integral $\int f(x) dx$ represents the set of all antiderivatives. We then explored how to approximate the area under a curve using Riemann sums (left, right, midpoint) over a partition of an interval. The concept of net area accounts for regions above and below the x-axis. Finally, the definite integral $\int_a^b f(x) dx$ was defined as the limit of Riemann sums, leading to the powerful Fundamental Theorem of Calculus. FTC I provides a direct method to evaluate definite integrals using antiderivatives, while FTC II establishes the relationship between differentiation and integration, showing that differentiation "undoes" integration.