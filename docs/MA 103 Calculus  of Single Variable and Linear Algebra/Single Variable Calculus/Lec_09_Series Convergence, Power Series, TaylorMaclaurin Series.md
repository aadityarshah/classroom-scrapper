---
title: |
  Series Convergence, Power Series, Taylor/Maclaurin Series
lecture_number: 9
lecture_name: |
  Series Convergence, Power Series, Taylor/Maclaurin Series
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 9
sidebar_position: 9
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Series Convergence and Power Series
date: |
  2023-10-27
tags:
  - Math
  - Calculus
  - Series
  - Convergence
  - PowerSeries
  - TaylorSeries
  - MaclaurinSeries
summary: |
  This lecture covers advanced convergence tests for series, including the Root Test and Alternating Series Test, and introduces concepts of absolute and conditional convergence. It then transitions to power series, defining their structure, center, and coefficients, and explores their convergence properties, including radius and interval of convergence. Key theorems for term-by-term differentiation and integration of power series are discussed. Finally, Taylor and Maclaurin series are introduced as powerful tools for approximating functions, along with Taylor polynomials and methods for estimating the remainder term.
math: true
---

# Series Convergence, Power Series, Taylor/Maclaurin Series

## Table of Contents
* [The Root Test](#the-root-test)
* [Alternating Series Test](#alternating-series-test)
* [Absolute and Conditional Convergence](#absolute-and-conditional-convergence)
* [The Absolute Convergence Test](#the-absolute-convergence-test)
* [Power Series Definitions](#power-series-definitions)
* [Geometric Power Series](#geometric-power-series)
* [The Convergence Theorem for Power Series](#the-convergence-theorem-for-power-series)
* [Radius and Interval of Convergence](#radius-and-interval-of-convergence)
* [Term-by-Term Differentiation Theorem](#term-by-term-differentiation-theorem)
* [Term-by-Term Integration Theorem](#term-by-term-integration-theorem)
* [The Series Multiplication Theorem for Power Series](#the-series-multiplication-theorem-for-power-series)
* [Taylor and Maclaurin Series Definitions](#taylor-and-maclaurin-series-definitions)
* [Taylor Polynomial of Order $n$](#taylor-polynomial-of-order-n)
* [Taylor's Theorem and Formula](#taylors-theorem-and-formula)
* [Remainder Estimation Theorem](#remainder-estimation-theorem)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## The Root Test
**THEOREM 13 (The Root Test):** Let $\sum a_n$ be a series with $a_n \geq 0$ for $n \geq N$, and suppose that $\rho = \lim_{n \to \infty} \sqrt[n]{|a_n|}$.
*   If $\rho < 1$, the series converges.
*   If $\rho > 1$ or $\rho$ is infinite, the series diverges.
*   If $\rho = 1$, the test is inconclusive.

## Alternating Series Test
**THEOREM 14 (The Alternating Series Test / Leibniz's Theorem):** An alternating series of the form $\sum (-1)^{n+1} u_n$ or $\sum (-1)^n u_n$ converges if the following three conditions are satisfied for $n \geq N$:
1.  The terms $u_n$ are all positive.
2.  The terms are non-increasing in magnitude, i.e., $u_n \geq u_{n+1}$.
3.  The limit of the terms is zero, i.e., $\lim_{n \to \infty} u_n = 0$.

## Absolute and Conditional Convergence
**DEFINITION (Absolutely Convergent):** A series $\sum a_n$ converges absolutely if the corresponding series of absolute values, $\sum |a_n|$, converges.
**DEFINITION (Conditionally Convergent):** A series converges conditionally if it converges but does not converge absolutely.

## The Absolute Convergence Test
**THEOREM 16 (The Absolute Convergence Test):** If the series of absolute values $\sum |a_n|$ converges, then the series $\sum a_n$ also converges.

## Power Series Definitions
**DEFINITION (Power Series about $x=0$):** A series of the form $\sum_{n=0}^{\infty} c_n x^n = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n + \dots$.
**DEFINITION (Power Series about $x=a$):** A series of the form $\sum_{n=0}^{\infty} c_n (x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \dots + c_n(x-a)^n + \dots$, where $a$ is the **center** and $c_0, c_1, c_2, \dots, c_n, \dots$ are **coefficients**.

## Geometric Power Series
A geometric power series, such as $\sum_{n=0}^{\infty} x^n$, converges to $\frac{1}{1-x}$ for $|x|<1$. Generally, a power series of the form $\sum_{n=0}^{\infty} r_0^n (\frac{x-a}{r_0})^n$ will converge for $|\frac{x-a}{r_0}| < 1$.

## The Convergence Theorem for Power Series
**THEOREM 18 (The Convergence Theorem for Power Series):**
*   If a power series $\sum a_n x^n$ converges for some $x=c \neq 0$, then it converges absolutely for all $x$ with $|x| < |c|$.
*   If it diverges for some $x=d$, then it diverges for all $x$ with $|x| > |d|$.

## Radius and Interval of Convergence
**COROLLARY TO THEOREM 18:** For a power series $\sum c_n (x-a)^n$, one of three possibilities holds:
1.  There is a positive number $R$ (the **radius of convergence**) such that the series converges absolutely for $|x-a|<R$ and diverges for $|x-a|>R$. Convergence at the endpoints $x=a \pm R$ must be checked separately.
2.  The series converges absolutely for all $x$ ($R=\infty$).
3.  The series converges only at $x=a$ ($R=0$).
The **interval of convergence** is the set of all $x$ values for which the series converges, centered at $x=a$ with radius $R$. The Ratio Test is commonly used to find the radius of convergence.

## Term-by-Term Differentiation Theorem
**THEOREM 19 (The Term-by-Term Differentiation Theorem):** If $f(x) = \sum_{n=0}^{\infty} c_n (x-a)^n$ converges for $a-R < x < a+R$ (where $R>0$), then $f$ has derivatives of all orders on this interval. The derivatives can be obtained by differentiating the original series term by term:
$$ f'(x) = \sum_{n=1}^{\infty} n c_n (x-a)^{n-1} $$
$$ f''(x) = \sum_{n=2}^{\infty} n(n-1) c_n (x-a)^{n-2} $$
Each derived series converges at every interior point of the original series' interval of convergence, maintaining the same radius $R$.

## Term-by-Term Integration Theorem
**THEOREM 20 (The Term-by-Term Integration Theorem):** Suppose $f(x) = \sum_{n=0}^{\infty} c_n (x-a)^n$ converges for $a-R < x < a+R$ (where $R>0$). Then $f$ is integrable on this interval, and its integral can be found by integrating term by term:
$$ \int f(x)dx = \sum_{n=0}^{\infty} c_n \frac{(x-a)^{n+1}}{n+1} + C $$
The integrated series also converges for $a-R < x < a+R$, maintaining the same radius $R$.

## The Series Multiplication Theorem for Power Series
**THEOREM 21 (The Series Multiplication Theorem for Power Series):** If $A(x) = \sum_{n=0}^{\infty} a_n x^n$ and $B(x) = \sum_{n=0}^{\infty} b_n x^n$ converge absolutely for $|x|<R$, then their product $A(x)B(x) = \sum_{n=0}^{\infty} c_n x^n$ also converges absolutely for $|x|<R$, where the coefficients $c_n$ are given by $c_n = a_0 b_n + a_1 b_{n-1} + \dots + a_{n-1} b_1 + a_n b_0 = \sum_{k=0}^{n} a_k b_{n-k}$.

## Taylor and Maclaurin Series Definitions
**DEFINITION (Taylor Series):** For a function $f$ with derivatives of all orders throughout some interval containing $a$ as an interior point, the Taylor series generated by $f$ at $x=a$ is:
$$ \sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!} (x-a)^k = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots $$
The coefficient $a_n$ for $(x-a)^n$ is $\frac{f^{(n)}(a)}{n!}$.
**DEFINITION (Maclaurin Series):** A Taylor series generated by $f$ at $x=0$ ($a=0$) is called a Maclaurin series:
$$ \sum_{k=0}^{\infty} \frac{f^{(k)}(0)}{k!} x^k = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \dots $$

## Taylor Polynomial of Order $n$
**DEFINITION (Taylor Polynomial of Order $n$):** For a function $f$ with derivatives of order up to $N$ in an interval containing $a$, the Taylor polynomial of order $n$ (for $0 \leq n \leq N$) generated by $f$ at $x=a$ is:
$$ P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(x-a)^n $$
This polynomial provides a local approximation of $f(x)$ near $x=a$. The linearization $P_1(x) = f(a) + f'(a)(x-a)$ is a special case.

## Taylor's Theorem and Formula
**THEOREM 22 (Taylor's Theorem):** If $f$ and its first $n$ derivatives are continuous on a closed interval between $a$ and $b$, and $f^{(n)}$ is differentiable on the open interval $(a,b)$, then there exists a number $c$ between $a$ and $b$ such that:
$$ f(b) = f(a) + f'(a)(b-a) + \frac{f''(a)}{2!}(b-a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(b-a)^n + \frac{f^{(n+1)}(c)}{(n+1)!}(b-a)^{n+1} $$
**Taylor's Formula:** If $f$ has derivatives of all orders in an open interval $I$ containing $a$, then for each positive integer $n$ and each $x$ in $I$:
$$ f(x) = P_n(x) + R_n(x) $$
where $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ is the **remainder term**, for some $c$ between $a$ and $x$.

## Remainder Estimation Theorem
**THEOREM 23 (The Remainder Estimation Theorem):** If there is a positive constant $M$ such that $|f^{(n+1)}(t)| \leq M$ for all $t$ between $x$ and $a$ (inclusive), then the remainder term $R_n(x)$ in Taylor's Theorem satisfies the inequality:
$$ |R_n(x)| \leq M \frac{|x-a|^{n+1}}{(n+1)!} $$
If this condition holds for every $n$, and other conditions of Taylor's Theorem are met, the Taylor series converges to $f(x)$.

## Key Formulas
*   **Root Test Limit:** $\rho = \lim_{n \to \infty} \sqrt[n]{|a_n|}$
*   **Taylor Series at $x=a$:** $\sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!} (x-a)^k$
*   **Maclaurin Series (Taylor at $x=0$):** $\sum_{k=0}^{\infty} \frac{f^{(k)}(0)}{k!} x^k$
*   **Taylor Polynomial of Order $n$:** $P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!} (x-a)^k$
*   **Taylor's Remainder Term:** $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$ (for some $c$ between $a$ and $x$)
*   **Remainder Estimation:** $|R_n(x)| \leq M \frac{|x-a|^{n+1}}{(n+1)!}$ (where $|f^{(n+1)}(t)| \leq M$)
*   **Term-by-Term Differentiation:** $\frac{d}{dx} \left( \sum c_n (x-a)^n \right) = \sum n c_n (x-a)^{n-1}$
*   **Term-by-Term Integration:** $\int \left( \sum c_n (x-a)^n \right) dx = \sum c_n \frac{(x-a)^{n+1}}{n+1} + C$

## Quick Summary
This lecture introduced sophisticated tests for series convergence, including the Root Test for non-negative series and the Alternating Series Test for alternating series. It defined absolute and conditional convergence, along with the Absolute Convergence Test. The core of the lecture focused on power series, their general forms centered at $x=0$ or $x=a$, and crucial theorems governing their convergence: the Convergence Theorem for Power Series, and the concepts of radius and interval of convergence. We also covered the Term-by-Term Differentiation and Integration Theorems, which allow manipulating power series while preserving their convergence radius. Finally, Taylor and Maclaurin series were defined as power series representations of functions, along with Taylor polynomials for function approximation and Taylor's Theorem for analyzing the error (remainder term) in these approximations.