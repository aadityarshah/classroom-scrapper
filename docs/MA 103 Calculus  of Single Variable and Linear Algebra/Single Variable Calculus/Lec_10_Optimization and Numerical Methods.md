---
title: |
  Optimization and Numerical Methods
lecture_number: 10
lecture_name: |
  Optimization and Numerical Methods
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 10
sidebar_position: 10
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Optimization | Numerical Methods
date: |
  2023-10-27
tags:
  - Math
  - Calculus
  - Optimization
  - Numerical Methods
summary: |
  This lecture covers the fundamentals of optimization, including defining different types of extrema and utilizing first and second derivative tests. It also introduces numerical methods like Bisection and Newton's method for solving optimization problems and finding roots, particularly for critical points.
math: true
---

# Optimization and Numerical Methods

## Table of Contents
* [Introduction to Optimization](#introduction-to-optimization)
* [Definitions of Optimization Problems](#definitions-of-optimization-problems)
* [Types of Extrema and First-Order Condition](#types-of-extrema-and-first-order-condition)
* [Second Derivative Test for Local Extrema](#second-derivative-test-for-local-extrema)
* [Considerations for Optimization](#considerations-for-optimization)
* [Numerical Solution Methods](#numerical-solution-methods)
* [Bisection Method for Finding Zeros](#bisection-method-for-finding-zeros)
* [Bisection Method for Optimization](#bisection-method-for-optimization)
* [Newton's Method for Finding Zeros](#newtons-method-for-finding-zeros)
* [Newton's Method for Optimization](#newtons-method-for-optimization)
* [Numerical Optimization in Practice](#numerical-optimization-in-practice)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## Introduction to Optimization
Optimization problems involve finding the maximum or minimum value of a function, often subject to certain constraints. This typically requires identifying critical points where the derivative is zero.

## Definitions of Optimization Problems
An optimization problem aims to find $\min f(x)$ for $x \in \mathbb{R}$, subject to:
*   **Equality Constraints:** $c_i(x) = 0$, for $i \in \mathcal{E}$
*   **Inequality Constraints:** $c_i(x) \ge 0$, for $i \in \mathcal{I}$
If no constraints are present, it is an **Unconstrained Optimization** problem. The maximum of a function $f$ can be found by minimizing $-f$, i.e., $\max f = - \min (-f)$.

## Types of Extrema and First-Order Condition
Let $x^*$ be a point in $\mathbb{R}$:
*   **Global Minimizer:** $f(x^*) \le f(x)$ for all $x \in \mathbb{R}$.
*   **Local Minimizer:** There exists a neighborhood $N$ of $x^*$ such that $f(x^*) \le f(x)$ for all $x \in N(x^*)$.
*   **Strict Local Minimizer:** There exists a neighborhood $N$ of $x^*$ such that $f(x^*) < f(x)$ for all $x \in N(x^*)$, $x \ne x^*$.

**First-Order Necessary Condition:** If $x^*$ is a local minimizer (or maximizer) of a continuously differentiable function $f$ in an open neighborhood of $x^*$, then $f'(x^*) = 0$. This condition is necessary but not sufficient (e.g., $f(x)=x^3$ at $x=0$).

## Second Derivative Test for Local Extrema
Suppose $f''$ is continuous on an open interval containing $x=c$:
1.  If $f'(c)=0$ and $f''(c) < 0$, then $f$ has a **local maximum** at $x=c$.
2.  If $f'(c)=0$ and $f''(c) > 0$, then $f$ has a **local minimum** at $x=c$.
3.  If $f'(c)=0$ and $f''(c) = 0$, the test fails; $f$ may have a local maximum, local minimum, or neither.

## Considerations for Optimization
When optimizing, it is critical to be aware of:
*   **Discontinuities:** Functions with discontinuities may require restricting the domain or careful analysis.
*   **Unbounded Functions:** Some functions may not have a finite minimum or maximum over their entire domain.

## Numerical Solution Methods
When analytical solutions are not available, **Iterative Algorithms** provide numerical approximations. An iterative method generates a sequence of approximations $\{x_0, x_1, x_2, \dots, x_n\}$ that converges to the true solution $x^*$. Each iteration typically requires evaluating the objective function and/or its derivatives. Algorithms stop based on **convergence criteria**, such as changes in function value, argument value, or gradient falling below a tolerance ($|\Delta f(x)| < \text{tol}$, $|\Delta x| < \text{tol}$, or $|\nabla f(x)| < \text{tol}$). If criteria are not met within a maximum number of iterations, convergence is not achieved.

## Bisection Method for Finding Zeros
The Bisection Method is used to find zeros of a continuous function $f(x)$ on an interval $[a,b]$ based on the Intermediate Value Theorem.
**Assumptions:**
1.  $f(x)$ is continuous on $[a,b]$.
2.  $f(a) \cdot f(b) < 0$ (i.e., $f(a)$ and $f(b)$ have opposite signs), guaranteeing at least one root in $(a,b)$.
**Steps:**
1.  Find the midpoint $x_0 = \frac{a+b}{2}$.
2.  If $f(x_0) = 0$, then $x_0$ is the root.
3.  If $f(x_0) \neq 0$:
    *   If $f(a) \cdot f(x_0) < 0$, the root lies in $[a, x_0]$. Update $b = x_0$.
    *   If $f(b) \cdot f(x_0) < 0$, the root lies in $[x_0, b]$. Update $a = x_0$.
4.  Repeat until the interval of uncertainty $[a,b]$ is sufficiently small.

## Bisection Method for Optimization
To find critical points (zeros of $f'(x)$) for optimization, the Bisection Method can be applied to the derivative function $f'(x)$.
**Steps:**
1.  Start with an interval $[a,b]$ where $f'(a) \cdot f'(b) < 0$. This ensures a root (critical point) of $f'$ exists.
2.  In each iteration, evaluate $f'$ at the midpoint $x_0 = \frac{a+b}{2}$.
3.  Reduce the interval: if $f'(a) \cdot f'(x_0) < 0$, the new interval is $[a, x_0]$; otherwise, it's $[x_0, b]$.

## Newton's Method for Finding Zeros
Newton's Method is an iterative technique for finding successively better approximations to the roots (or zeros) of a real-valued function.
**Formula:**
$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$
This formula derives from approximating the function by its tangent line at $x_k$ and finding where the tangent line intersects the x-axis.

## Newton's Method for Optimization
To find local extrema, Newton's method can be applied to find the zeros of the first derivative, $f'(x)$.
**Formula:**
$$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$
This effectively uses Newton's method on the derivative of $f(x)$ to find critical points.

## Numerical Optimization in Practice
Computational tools like `scipy.optimize.minimize_scalar` implement sophisticated numerical methods (e.g., Brent's method) to find minima of functions. These tools iteratively refine an estimate for $x$ until a minimum is found within a specified tolerance, providing the optimal value and the function's value at that optimum.

## Key Formulas
*   **Optimization Problem General Form:** $\min f(x)$ s.t. $c_i(x)=0, c_i(x) \ge 0$.
*   **Relationship between Max and Min:** $\max f = - \min (-f)$.
*   **First-Order Necessary Condition:** $f'(x^*) = 0$.
*   **Second Derivative Test (Local Max):** $f'(c)=0, f''(c) < 0$.
*   **Second Derivative Test (Local Min):** $f'(c)=0, f''(c) > 0$.
*   **Bisection Method Midpoint:** $x_0 = \frac{a+b}{2}$.
*   **Newton's Method for Zeros of $f(x)$:** $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$.
*   **Newton's Method for Zeros of $f'(x)$ (Optimization):** $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$.

## Quick Summary
Optimization involves identifying extrema using first and second derivative tests, or numerical methods for complex functions. The First-Order Necessary Condition ($f'(x^*)=0$) identifies critical points, classified by the Second Derivative Test ($f''(c) < 0$ for max, $f''(c) > 0$ for min). Numerical methods like the Bisection Method and Newton's Method provide iterative approximations for roots (critical points), essential when analytical solutions are intractable. These methods apply directly to $f(x)$ for zeros or to $f'(x)$ for optimization.