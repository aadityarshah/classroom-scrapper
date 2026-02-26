---
title: |
  Laplace Transforms: Derivatives, IVPs, Shifting, and Convolution
lecture_number: 12
lecture_name: |
  Laplace Transforms: Derivatives, IVPs, Shifting, and Convolution
category: |
sidebar_label: |
  Lecture 12
sidebar_position: 12
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Laplace Transforms
  YYYY-MM-DD
tags: ['Math', 'Ordinary Differential Equations', 'Laplace Transform']
summary: |
  This lecture covers the Laplace transform of derivatives, its application in solving Initial Value Problems (IVPs), the Unit Step Function and the Second Shifting Theorem, differentiation and integration properties of Laplace transforms, and the Convolution Theorem.
math: true
---

# Laplace Transforms: Derivatives, IVPs, Shifting, and Convolution

## Table of Contents
*   Laplace Transform of Derivatives
*   Solving Initial Value Problems (IVPs) using Laplace Transforms
*   Unit Step Function
*   Second Shifting Theorem
*   Derivative and Integration of Laplace Transforms
*   Convolution and Convolution Theorem
*   Key Formulas
*   Quick Summary

## Laplace Transform of Derivatives

**Theorem:** Let $f: [0, \infty) \to \mathbb{R}$ be continuous and of exponential order $\alpha$. Let $f'$ be piecewise continuous on $[0, \infty)$. Then the Laplace transform for $f'$ exists for $s $>$ \alpha$ and is given by:
$$ \mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0) \quad \text{for } s $>$ \alpha $$

**Generalized Formula for Higher Order Derivatives:** With similar hypotheses on $f^{(k-1)}$ and $f^{(k)}$, we have:
$$ \mathcal{L}\{f^{(k)}(t)\} = s^k \mathcal{L}\{f(t)\} - s^{k-1}f(0) - s^{k-2}f'(0) - \dots - f^{(k-1)}(0) $$

**Remark (for $k=2$):**
$$ \mathcal{L}\{f''(t)\} = s^2\mathcal{L}\{f(t)\} - sf(0) - f'(0) $$

## Solving Initial Value Problems (IVPs) using Laplace Transforms

**Methodology:**
1.  Apply the Laplace transform to the given Ordinary Differential Equation (ODE).
2.  Use the Laplace transform of derivatives formula and substitute initial conditions at $t=0$.
3.  Solve the resulting algebraic equation for $\mathcal{L}\{y(t)\}$.
4.  Apply the inverse Laplace transform to find $y(t)$.

**Remark:** Solving IVPs with Laplace transforms requires initial conditions at $t=0$.

**Formula for $y'' + ay' + by = r(t)$ with $y(0)=k_0, y'(0)=k_1$:**
$$ \mathcal{L}\{y(t)\} = \frac{\mathcal{L}\{r(t)\} + k_0(s+a) + k_1}{s^2+as+b} $$
$$ y(t) = \mathcal{L}^{-1}\left( \frac{\mathcal{L}\{r(t)\} + (s+a)y(0) + y'(0)}{s^2+as+b} \right) $$

**Theorem (IVP with Piecewise Continuous Function $r(t)$):** Let $r(t)$ be a piecewise continuous function with discontinuities at $0 $<$ t_1 $<$ \dots $<$ t_n$. Let $k_0, k_1$ be arbitrary real numbers. Consider the ODE $ay'' + by' + cy = r(t)$ with $a,b,c \in \mathbb{R}$. Then there exists a unique function $y$ defined on $[0, \infty)$ such that:
1.  $y(0)=k_0$ and $y'(0)=k_1$.
2.  $y$ and $y'$ are continuous on $[0, \infty)$.
3.  $y''$ is defined on every subinterval $I$ of $[0, \infty)$ that does not contain any of the points $t_1, \dots, t_n$.
4.  $y$ satisfies the ODE on every such sub-interval $I$ of $[0, \infty)$.
5.  $y''$ has left and right limits at $t_1, \dots, t_n$.

## Unit Step Function

**Definition (Unit Step Function / Heaviside Function):** The unit step function $u_a(t)$ is defined as:
$$ u_a(t) = \begin{cases} 0 & t $<$ a \\ 1 & t \ge a \end{cases} $$
This represents a jump of size 1 at $t=a$.

**Remark:** $u_a(t) = u_0(t-a)$, where $u_0(t) = \begin{cases} 0 & t $<$ 0 \\ 1 & t \ge 0 \end{cases}$.

**Laplace Transform of Unit Step Function:**
$$ \mathcal{L}\{u_a(t)\} = \frac{e^{-as}}{s} $$

## Second Shifting Theorem

**Theorem (First Form):** If $a \ge 0$ and $F(s) = \mathcal{L}\{f(t)\}$ exists for $s $>$ s_0$, then $\mathcal{L}\{u_a(t)f(t-a)\}$ exists for $s $>$ s_0$ and is given by:
$$ \mathcal{L}\{u_a(t)f(t-a)\} = e^{-as}\mathcal{L}\{f(t)\} = e^{-as}F(s) $$

**Inverse Second Shifting Theorem (First Form):**
$$ u_a(t)f(t-a) = \mathcal{L}^{-1}\{e^{-as}F(s)\} $$

**Theorem (Second Form):** If $a \ge 0$ and $G(s) = \mathcal{L}\{g(t+a)\}$ exists for $s $>$ s_0$, then $\mathcal{L}\{u_a(t)g(t)\}$ exists for $s $>$ s_0$ and is given by:
$$ \mathcal{L}\{u_a(t)g(t)\} = e^{-as}\mathcal{L}\{g(t+a)\} = e^{-as}G(s) $$

## Derivative and Integration of Laplace Transforms

**Theorem (Derivative of Laplace Transform):** If $F(s) = \mathcal{L}\{f(t)\}$, then:
$$ \mathcal{L}\{-tf(t)\} = F'(s) $$

**Inverse Theorem:**
$$ \mathcal{L}^{-1}\{F'(s)\} = -tf(t) $$

**Theorem (Integration of Laplace Transform):** If $\mathcal{L}\{f(t)\} = F(s)$ and the limit $\lim_{t \to 0^+} \frac{f(t)}{t}$ exists, then:
$$ \mathcal{L}\left\{\frac{f(t)}{t}\right\} = \int_s^\infty F(\tilde{s}) d\tilde{s} $$

**Inverse Theorem:**
$$ \mathcal{L}^{-1}\left\{\int_s^\infty F(\tilde{s}) d\tilde{s}\right\} = \frac{f(t)}{t} $$

## Convolution and Convolution Theorem

**Definition (Convolution):** Let $f$ and $g$ be two functions defined on $[0, \infty)$. The convolution of $f$ and $g$, denoted by $f * g$, is defined by:
$$ (f*g)(t) = \int_0^t f(\tau)g(t-\tau)d\tau $$

**Theorem (Convolution Theorem):** If $\mathcal{L}\{f(t)\} = F(s)$ and $\mathcal{L}\{g(t)\} = G(s)$, then $\mathcal{L}\{f*g\}$ exists and:
$$ \mathcal{L}\{f*g\} = \mathcal{L}\left\{\int_0^t f(\tau)g(t-\tau)d\tau\right\} = F(s)G(s) $$

**Inverse Convolution Theorem:**
$$ \mathcal{L}^{-1}\{F(s)G(s)\} = (f*g)(t) $$

## Key Formulas

*   **Laplace Transform of Derivatives:** $\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0)$
*   **Generalized Derivatives:** $\mathcal{L}\{f^{(k)}(t)\} = s^k \mathcal{L}\{f(t)\} - s^{k-1}f(0) - \dots - f^{(k-1)}(0)$
*   **Laplace Transform of Unit Step Function:** $\mathcal{L}\{u_a(t)\} = \frac{e^{-as}}{s}$
*   **Second Shifting Theorem:** $\mathcal{L}\{u_a(t)f(t-a)\} = e^{-as}F(s)$
*   **Inverse Second Shifting Theorem:** $\mathcal{L}^{-1}\{e^{-as}F(s)\} = u_a(t)f(t-a)$
*   **Derivative of Laplace Transform:** $\mathcal{L}\{-tf(t)\} = F'(s)$
*   **Integration of Laplace Transform:** $\mathcal{L}\left\{\frac{f(t)}{t}\right\} = \int_s^\infty F(\tilde{s}) d\tilde{s}$
*   **Convolution Definition:** $(f*g)(t) = \int_0^t f(\tau)g(t-\tau)d\tau$
*   **Convolution Theorem:** $\mathcal{L}\{f*g\} = F(s)G(s)$

## Quick Summary

This lecture established key properties of the Laplace transform crucial for solving Ordinary Differential Equations. We covered the Laplace transform of derivatives, enabling the transformation of ODEs into algebraic equations. The Unit Step Function and the Second Shifting Theorem provide tools for handling piecewise continuous functions and time-delayed signals. Properties relating to differentiation and integration of the Laplace transform were introduced, facilitating the transformation of functions multiplied or divided by $t$. Finally, the Convolution Theorem was defined, providing a method for finding the inverse Laplace transform of a product of two functions in the $s$-domain. These concepts collectively form a powerful framework for analyzing and solving IVPs.