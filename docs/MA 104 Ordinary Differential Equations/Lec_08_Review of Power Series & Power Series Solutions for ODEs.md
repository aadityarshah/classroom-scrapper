---
title: |
  Review of Power Series & Power Series Solutions for ODEs
lecture_number: 8
lecture_name: |
  Review of Power Series & Power Series Solutions for ODEs
category: |
  
sidebar_label: |
  Lecture 8
sidebar_position: 8
course: |
  MA 104
topic: |
  Power Series Solutions
date: |
  2023-10-27
tags:
  - Mathematics
  - Differential Equations
  - Power Series
  - Convergence
summary: |
  This lecture reviews power series, their definitions, convergence properties (radius, interval, tests), algebraic and differential operations, Taylor series, analytic functions, and introduces the theorem for existence of power series solutions for Ordinary Differential Equations.
math: true
---

# Review of Power Series & Power Series Solutions for ODEs

## Table of Contents
* Review of Power Series
    * Definition of Power Series
    * Convergence of Power Series
    * Absolute Convergence
    * Radius and Interval of Convergence
    * Convergence Tests
    * Properties of Power Series
    * Taylor Series and Analytic Functions
    * Vanishing of Coefficients
    * Shifting Index of Summation
* Power Series Solutions for ODEs
    * Existence of Power Series Solutions Theorem
* Key Formulas
* Quick Summary

## Review of Power Series

### Definition of Power Series
A power series is an infinite series of the form:
$$ \sum_{m=0}^{\infty} a_m (x-x_0)^m = a_0 + a_1(x-x_0) + a_2(x-x_0)^2 + \dots $$
Here, $a_m$ are the coefficients of the series, and $x_0$ is the center of the series.

### Convergence of Power Series
A power series $\sum_{m=0}^{\infty} a_m (x-x_0)^m$ is said to converge at a point $x$ if the sequence $\{S_N(x)\}$ of partial sums $S_N(x) = \sum_{m=0}^{N} a_m (x-x_0)^m$ is convergent, i.e., $\lim_{N \to \infty} S_N(x)$ exists. The series certainly converges for $x=x_0$.

### Absolute Convergence
A series $\sum_{m=0}^{\infty} a_m (x-x_0)^m$ is said to converge absolutely at a point $x$ if the series $\sum_{m=0}^{\infty} |a_m (x-x_0)^m| = \sum_{m=0}^{\infty} |a_m| |x-x_0|^m$ converges.
**Note:** If a series converges absolutely, then the series also converges.

### Radius and Interval of Convergence
*   If a power series $\sum_{n=0}^{\infty} a_n (x-x_0)^n$ converges at $x=x_1$, it converges absolutely for $|x-x_0| $<$ |x_1-x_0|$.
*   If a power series $\sum_{n=0}^{\infty} a_n (x-x_0)^n$ diverges at $x=x_1$, it diverges for $|x-x_0| $>$ |x_1-x_0|$.
There exists a positive integer $\rho$, called the **radius of convergence**, such that $\sum_{n=0}^{\infty} a_n (x-x_0)^n$ converges for $|x-x_0| $<$ \rho$ and diverges for $|x-x_0| $>$ \rho$.
The interval $|x-x_0| $<$ \rho$ is called the **interval of convergence**.

### Convergence Tests
*   **Root Test:** The series converges if $C = \limsup_{n \to \infty} \sqrt[n]{|a_n (x-x_0)^n|} = \limsup_{n \to \infty} \sqrt[n]{|a_n|} |x-x_0| $<$ 1$. It diverges if $C $>$ 1$.
    The radius of convergence $\rho = \frac{1}{\limsup_{n \to \infty} \sqrt[n]{|a_n|}}$.
*   **Ratio Test:** The series converges if $L = \lim_{n \to \infty} \left| \frac{a_{n+1}(x-x_0)^{n+1}}{a_n(x-x_0)^n} \right| = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| |x-x_0| $<$ 1$. It diverges if $L $>$ 1$.
    The radius of convergence $\rho = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right|$.

### Properties of Power Series
*   **Algebra:** Suppose $\sum_{n=0}^{\infty} a_n (x-x_0)^n$ converges to $f(x)$ and $\sum_{n=0}^{\infty} b_n (x-x_0)^n$ converges to $g(x)$ for $|x-x_0| $<$ \rho$, where $\rho $>$ 0$.
    *   **Addition/Subtraction:** $f(x) \pm g(x) = \sum_{n=0}^{\infty} (a_n \pm b_n) (x-x_0)^n$.
    *   **Multiplication:** $f(x)g(x) = \sum_{n=0}^{\infty} c_n (x-x_0)^n$, where $c_n = a_0b_n + a_1b_{n-1} + \dots + a_nb_0$.
    Both series for $f(x) \pm g(x)$ and $f(x)g(x)$ converge at least for $|x-x_0| $<$ \rho$.
*   **Differentiation:** Suppose $\sum_{n=0}^{\infty} a_n (x-x_0)^n$ converges to $f(x)$ for $|x-x_0| $<$ \rho$, where $\rho $>$ 0$.
    *   Then $f$ is continuous and has derivatives of all orders for $|x-x_0| $<$ \rho$.
    *   Derivatives can be computed term-wise:
        *   $f'(x) = \sum_{n=1}^{\infty} n a_n (x-x_0)^{n-1}$
        *   $f''(x) = \sum_{n=2}^{\infty} n(n-1) a_n (x-x_0)^{n-2}$
    *   Each differentiated series converges absolutely for $|x-x_0| $<$ \rho$.
*   **Note on Absolute Convergence of Derivatives:** If a power series $\sum_{n=0}^{\infty} a_n x^n$ converges to $f(x)$ for $|x|<\rho$, and its derivative series $\sum_{n=1}^{\infty} n a_n x^{n-1}$ converges absolutely at some $x$, then the original series $\sum_{n=0}^{\infty} a_n x^n$ also converges absolutely for that $x$.

### Taylor Series and Analytic Functions
*   The value of $a_n$ is given by $a_n = \frac{f^{(n)}(x_0)}{n!}$.
*   The series $f(x) = \sum_{n=0}^{\infty} a_n (x-x_0)^n = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x-x_0)^n$ is called the **Taylor series** for the function $f(x)$ about $x=x_0$.
*   A function $h(x)$ is called **analytic** at a point $x=x_0$ if it can be represented by a power series (Taylor series) in powers of $(x-x_0)$ with a positive radius of convergence ($\rho $>$ 0$).

### Vanishing of Coefficients
If $\rho $>$ 0$ and $\sum_{n=0}^{\infty} a_n (x-x_0)^n = 0$ for $|x-x_0| $<$ \rho$, then $a_n = 0$ for all $n \ge 0$.

### Shifting Index of Summation
It is immaterial which letter is used for the index of summation. It is often convenient to change summation indices to align powers of $x$ in calculations for series solutions of differential equations. This involves substituting a new index variable (e.g., $m=n-k$) and adjusting the summation limits accordingly.

## Power Series Solutions for ODEs

### Existence of Power Series Solutions Theorem
Consider the Ordinary Differential Equation (ODE):
$$ y'' + P(x)y' + Q(x)y = R(x) $$
If $P(x)$, $Q(x)$, and $R(x)$ are analytic at $x=x_0$, then every solution of the ODE is analytic at $x=x_0$ and can thus be represented by a power series in powers of $(x-x_0)$ with a positive radius of convergence ($\rho $>$ 0$).

## Key Formulas
*   **Power Series:** $\sum_{m=0}^{\infty} a_m (x-x_0)^m$
*   **Radius of Convergence (Root Test):** $\rho = \frac{1}{\limsup_{n \to \infty} \sqrt[n]{|a_n|}}$
*   **Radius of Convergence (Ratio Test):** $\rho = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right|$
*   **Taylor Series Coefficient:** $a_n = \frac{f^{(n)}(x_0)}{n!}$
*   **First Derivative of Power Series:** $f'(x) = \sum_{n=1}^{\infty} n a_n (x-x_0)^{n-1}$
*   **Second Derivative of Power Series:** $f''(x) = \sum_{n=2}^{\infty} n(n-1) a_n (x-x_0)^{n-2}$

## Quick Summary
This lecture covered the fundamental definitions and properties of power series, including convergence, absolute convergence, radius and interval of convergence, and key tests (Root and Ratio Tests). We explored how power series can be added, multiplied, and differentiated term-wise. The concepts of Taylor series and analytic functions, crucial for representing functions as power series, were defined. Finally, we introduced a fundamental theorem for Ordinary Differential Equations, stating that if the coefficient functions are analytic, power series solutions exist.