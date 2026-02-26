---
title: |
  Laplace Transform: Definition, Properties, and Inverse
lecture_number: 11
lecture_name: |
  Laplace Transform: Definition, Properties, and Inverse
category: |
sidebar_label: |
  Lecture 11
sidebar_position: 11
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Laplace Transform
date: 2023-10-27
tags: ['Math', 'ODE', 'Laplace Transform']
summary: |
  This lecture introduces the Laplace transform as a method to solve Ordinary Differential Equations (ODEs). It covers the definition of the Laplace transform, improper integrals, piecewise continuous functions, and functions of exponential order. Key properties such as linearity and the first shifting theorem are discussed, along with a table of elementary Laplace transforms. Finally, the inverse Laplace transform, its linearity, and the uniqueness theorem are presented.
math: true
---

# Laplace Transform: Definition, Properties, and Inverse

## Table of Contents
* [Process of Solving an ODE using the Laplace Transform](#process-of-solving-an-ode-using-the-laplace-transform)
* [Improper Integrals and Convergence](#improper-integrals-and-convergence)
* [Definition of the Laplace Transform](#definition-of-the-laplace-transform)
* [Piecewise Continuous Functions](#piecewise-continuous-functions)
* [Functions of Exponential Order](#functions-of-exponential-order)
* [Existence Theorem for the Laplace Transform](#existence-theorem-for-the-laplace-transform)
* [Properties of the Laplace Transform](#properties-of-the-laplace-transform)
* [Elementary Laplace Transforms](#elementary-laplace-transforms)
* [Inverse Laplace Transform](#inverse-laplace-transform)
* [Uniqueness of Continuous Inverse Laplace Transform](#uniqueness-of-continuous-inverse-laplace-transform)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## Process of Solving an ODE using the Laplace Transform
**Steps:**
1.  The given ODE is transformed into an algebraic equation, called the **subsidiary equation**.
2.  The subsidiary equation is solved by purely algebraic manipulations.
3.  The solution from Step 2 is transformed back, yielding the solution of the given ODE.

**Motivation:** Simplifies solving an ODE to an algebraic problem and transformations.

**Remarks:**
*   Initial Value Problems (IVPs) are solved without first determining a general solution.
*   Non-homogeneous ODEs are solved without solving the corresponding homogeneous ODE.

## Improper Integrals and Convergence
**Definition:**
If $f$ is integrable over the interval $[a,T]$ for every $T>a$, then the integral of $f$ over $[a, \infty)$ is defined as:
$$ \int_a^\infty f(t) dt := \lim_{T \to \infty} \int_a^T f(t) dt $$
**Convergence:**
The integral **converges** if the limit exists and is finite. Otherwise, the integral ** diverges** or fails to exist.

## Definition of the Laplace Transform
**Definition:**
Let $f(t)$ be given for $t>0$. Suppose that $f$ satisfies "certain conditions". Then the Laplace transform of $f$, denoted by $\mathcal{L}\{f(t)\}$ or $F(s)$, is defined by the equation:
$$ \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt $$
whenever this improper integral converges.

**Remark:** There may be functions for which the Laplace transform does not exist for any value of $s$.

## Piecewise Continuous Functions
**Definition:**
A function $f: [a,b] \to \mathbb{R}$ is said to be **piecewise continuous** if:
1.  There exist $a=t_0 < t_1 < \dots < t_{n+1}=b$ such that $f$ is continuous on $(t_i, t_{i+1})$ for all $i$.
2.  $f(t_i^+)$ and $f(t_{i+1}^-)$ exist and are finite for $i=0, \dots, n+1$.

**Extension:** A function $f: [a, \infty) \to \mathbb{R}$ is called piecewise continuous if it is piecewise continuous on $[a,T]$ for every $T>a$.

## Functions of Exponential Order
**Definition:**
A function $f$ is of **exponential order** if there exist $\alpha \in \mathbb{R}$, $t_0 \in \mathbb{R}$, and $M>0$ such that for all $t \ge t_0$:
$$ |f(t)| \le M e^{\alpha t} $$
This implies $-M e^{\alpha t} \le f(t) \le M e^{\alpha t}$.

**Examples of Functions of Exponential Order:**
*   All bounded functions (with $\alpha=0$).
*   $f(t) = t^n$ for any $n \ge 0$.
*   $f(t) = \sin(\omega t)$ and $f(t) = \cos(\omega t)$.

**Example of Function Not of Exponential Order:**
*   $f(t) = e^{t^2}$ is not of exponential order.

## Existence Theorem for the Laplace Transform
**Theorem:**
If $f$ is a piecewise continuous function on $[0, \infty)$ and of exponential order, say $\alpha$, then the Laplace transform $\mathcal{L}\{f(t)\}$ is defined for $s > \alpha$.

## Properties of the Laplace Transform
### Linearity
**Theorem:**
The Laplace transform is **linear**, i.e., for constants $c_1, c_2$:
$$ \mathcal{L}\{c_1 f_1(t) + c_2 f_2(t)\} = c_1 \mathcal{L}\{f_1(t)\} + c_2 \mathcal{L}\{f_2(t)\} $$

### First Shifting Theorem
**Theorem:**
If the Laplace transform of $f$ exists for $s>\alpha$, then for any given $a \in \mathbb{R}$:
$$ \mathcal{L}\{e^{at}f(t)\}(s) = \mathcal{L}\{f(t)\}(s-a) $$
for $s > a+\alpha$.

## Elementary Laplace Transforms
1.  $\mathcal{L}\{1\} = \frac{1}{s}$, $s>0$
2.  $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$, $s>a$
3.  $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$, $s>0$ (for $n \in \mathbb{Z}_{\ge 0}$)
4.  $\mathcal{L}\{t^\alpha\} = \frac{\Gamma(\alpha+1)}{s^{\alpha+1}}$, $s>0$ (for $\alpha \in \mathbb{R}_{\ge 0}$)
    *   **Gamma function:** $\Gamma(z) = \int_0^\infty e^{-t} t^{z-1} dt$, for $\text{Re}(z)>0$.
5.  $\mathcal{L}\{t^n e^{at}\} = \frac{n!}{(s-a)^{n+1}}$, $s>a$
6.  $\mathcal{L}\{\sin(\omega t)\} = \frac{\omega}{s^2+\omega^2}$, $s>0$
7.  $\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2+\omega^2}$, $s>0$
8.  $\mathcal{L}\{e^{at} \sin(\omega t)\} = \frac{\omega}{(s-a)^2+\omega^2}$, $s>a$
9.  $\mathcal{L}\{e^{at} \cos(\omega t)\} = \frac{s-a}{(s-a)^2+\omega^2}$, $s>a$
10. $\mathcal{L}\{\sinh(bt)\} = \frac{b}{s^2-b^2}$, $s>|b|$
11. $\mathcal{L}\{\cosh(bt)\} = \frac{s}{s^2-b^2}$, $s>|b|$
12. $\mathcal{L}\{e^{at} \sinh(bt)\} = \frac{b}{(s-a)^2-b^2}$, $s>a+|b|$
13. $\mathcal{L}\{e^{at} \cosh(bt)\} = \frac{s-a}{(s-a)^2-b^2}$, $s>a+|b|$

## Inverse Laplace Transform
**Definition:**
The **inverse Laplace transform** of $F(s)$, denoted by $\mathcal{L}^{-1}\{F(s)\}$, is defined as:
$$ \mathcal{L}^{-1}\{F(s)\}(t) = f(t) $$
where $\mathcal{L}\{f(t)\}(s) = F(s)$.

**Note:**
*   $\mathcal{L}^{-1}\{\mathcal{L}\{f(t)\}\} = f(t)$
*   $\mathcal{L}\{\mathcal{L}^{-1}\{F(s)\}\} = F(s)$

### Linearity Property of Inverse Laplace Transform
If $F_1(s)$ and $F_2(s)$ are Laplace transforms of $f_1(t)$ and $f_2(t)$ respectively, then for constants $c_1, c_2 \in \mathbb{R}$:
$$ \mathcal{L}^{-1}\{c_1 F_1(s) + c_2 F_2(s)\} = c_1 \mathcal{L}^{-1}\{F_1(s)\} + c_2 \mathcal{L}^{-1}\{F_2(s)\} $$

### Shifting Theorem for Inverse Laplace Transform
Using the First Shifting Theorem:
$$ \mathcal{L}^{-1}\{F(s-a)\} = e^{at} f(t) $$

### Heaviside Method Remark
If $\frac{P(s)}{Q(s)}$ are polynomials with $\text{deg }P < \text{deg }Q$, then $\mathcal{L}^{-1}\left\{\frac{P(s)}{Q(s)}\right\}$ is found by partial fractions, often using the Heaviside method.

## Uniqueness of Continuous Inverse Laplace Transform
**Theorem (Uniqueness):**
Let $f(t)$ and $g(t)$ be two functions such that $\mathcal{L}\{f(t)\} = \mathcal{L}\{g(t)\}$ for $s>\alpha$. Then $f(t)=g(t)$ for all $t$, where both functions are continuous.

**Alternatively:** If a continuous inverse transform exists for $F(s)$, then it has a unique continuous inverse transform.

## Key Formulas
*   **Laplace Transform Definition:** $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt$
*   **Linearity:** $\mathcal{L}\{c_1 f_1(t) + c_2 f_2(t)\} = c_1 \mathcal{L}\{f_1(t)\} + c_2 \mathcal{L}\{f_2(t)\}$
*   **First Shifting Theorem:** $\mathcal{L}\{e^{at}f(t)\}(s) = F(s-a)$
*   **Inverse Laplace Transform Definition:** $\mathcal{L}^{-1}\{F(s)\}(t) = f(t)$ where $\mathcal{L}\{f(t)\} = F(s)$
*   **Inverse Shifting Theorem:** $\mathcal{L}^{-1}\{F(s-a)\} = e^{at} f(t)$
*   **Elementary Transforms (Common):**
    *   $\mathcal{L}\{1\} = \frac{1}{s}$
    *   $\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$
    *   $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$
    *   $\mathcal{L}\{\sin(\omega t)\} = \frac{\omega}{s^2+\omega^2}$
    *   $\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2+\omega^2}$
    *   $\mathcal{L}\{e^{at} \sin(\omega t)\} = \frac{\omega}{(s-a)^2+\omega^2}$
    *   $\mathcal{L}\{e^{at} \cos(\omega t)\} = \frac{s-a}{(s-a)^2+\omega^2}$
    *   $\mathcal{L}\{\sinh(bt)\} = \frac{b}{s^2-b^2}$
    *   $\mathcal{L}\{\cosh(bt)\} = \frac{s}{s^2-b^2}$

## Quick Summary
The Laplace transform is a powerful tool to convert ODEs into algebraic equations, simplify their solution, and then transform back. Its existence requires functions to be piecewise continuous and of exponential order. Key properties include linearity and the first shifting theorem, which allow for a wide range of functions to be transformed. The inverse Laplace transform reverses this process, aided by linearity and inverse shifting, often using partial fractions for rational functions. A crucial uniqueness theorem ensures that if a continuous inverse transform exists, it is unique.