---
title: |
  MA 104 Lecture 9: Power Series and Legendre's Equation
lecture_number: 9
lecture_name: |
  Power Series and Legendre's Equation
category: |
  
sidebar_label: |
  Lecture 9
sidebar_position: 9
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Power Series Solutions, Legendre's Equation, Legendre Polynomials
  2023-10-26
tags: ['Differential Equations', 'Power Series', 'Legendre Equation', 'Special Functions']
summary: |
  Covers the method of power series solutions around ordinary points, focusing on Legendre's Equation, its series solutions, Legendre Polynomials, Rodrigues' formula, and their orthogonality properties.
math: true
---
# MA 104 Lecture 9: Power Series and Legendre's Equation

## Table of Contents
*   Power Series about an Initial Point
*   Legendre's Equation
*   Legendre Polynomials
*   Rodrigues' Formula
*   Orthogonality of Legendre Polynomials

## Power Series about an Initial Point
**Definition: Power Series Solution around $x_0$**
If initial conditions for an ODE are prescribed at $x=x_0$, and $P(x)$, $Q(x)$ (from $y''+P(x)y'+Q(x)y=0$) are analytic at $x_0$, the power series solution is around $x=x_0$:
$$y(x) = \sum_{k=0}^\infty a_k (x-x_0)^k$$
**Remark:** One can apply the method directly or use a change of variable $\tilde{x} = x-x_0$ to solve around $\tilde{x}=0$.

## Legendre's Equation
**Definition: Legendre's Equation**
A second-order linear ordinary differential equation (ODE):
$$(1-x^2)y'' - 2xy' + \alpha(\alpha+1)y = 0$$
where $\alpha$ is a fixed real number. Any solution is a **Legendre function**.

**Theorem: Power Series Solution for Legendre's Equation**
For Legendre's Equation, $P(x) = \frac{-2x}{1-x^2}$ and $Q(x) = \frac{\alpha(\alpha+1)}{1-x^2}$ are analytic at $x=0$. Applying the power series method $y(x) = \sum_{n=0}^\infty a_n x^n$ yields the recurrence relation for coefficients:
$$a_{n+2} = -\frac{(\alpha-n)(\alpha+n+1)}{(n+1)(n+2)} a_n \quad \text{for } n=0, 1, 2, \dots$$
The general solution is $y(x) = a_0 y_1(x) + a_1 y_2(x)$, where $y_1(x)$ (even powers) and $y_2(x)$ (odd powers) are linearly independent and converge for $|x|<1$.

## Legendre Polynomials
**Definition: Legendre Polynomials**
If $\alpha \in \mathbb{Z}_{\ge 0}$, one of the power series ($y_1(x)$ if $\alpha$ is even, $y_2(x)$ if $\alpha$ is odd) terminates, resulting in a polynomial solution of degree $\alpha$. Scaled such that $P_\alpha(1)=1$, these are **Legendre Polynomials**, denoted $P_\alpha(x)$.
**Property:** $P_\alpha(-x) = (-1)^\alpha P_\alpha(x)$.

## Rodrigues' Formula
**Theorem: Rodrigues' Formula**
For a non-negative integer $n$, the Legendre Polynomial $P_n(x)$ is given by:
$$P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n} (x^2-1)^n$$

## Orthogonality of Legendre Polynomials
**Definition: Inner Product for Polynomials**
For polynomials $f(x)$ and $g(x)$, an inner product is defined as:
$$\langle f,g \rangle = \int_{-1}^1 f(x)g(x)dx$$
**Definition: Norm for Polynomials**
The norm $||f||$ of a polynomial $f(x)$ is:
$$||f|| = \langle f,f \rangle^{1/2} = \left(\int_{-1}^1 (f(x))^2 dx\right)^{1/2}$$
**Theorem: Orthogonality Relation**
Legendre Polynomials form an orthogonal basis for the vector space of polynomials $P(x)$. For integers $m, n \ge 0$:
$$\langle P_m(x), P_n(x) \rangle = \int_{-1}^1 P_m(x)P_n(x)dx = \begin{cases} 0 & \text{if } m \ne n \\ \frac{2}{2n+1} & \text{if } m=n \end{cases}$$
**Theorem: Expansion in Legendre Polynomials**
Any polynomial $f(x)$ of degree $n$ can be expressed as:
$$f(x) = \sum_{k=0}^n \alpha_k P_k(x)$$
where the coefficients $\alpha_k$ are given by:
$$\alpha_k = \frac{\langle f(x), P_k(x) \rangle}{\langle P_k(x), P_k(x) \rangle} = \frac{2k+1}{2} \int_{-1}^1 f(x)P_k(x)dx$$

## Key Formulas
*   **Power Series Solution around $x_0$:** $y(x) = \sum_{k=0}^\infty a_k (x-x_0)^k$
*   **Legendre's Equation:** $(1-x^2)y'' - 2xy' + \alpha(\alpha+1)y = 0$
*   **Legendre Recurrence Relation:** $a_{n+2} = -\frac{(\alpha-n)(\alpha+n+1)}{(n+1)(n+2)} a_n$
*   **Rodrigues' Formula:** $P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n} (x^2-1)^n$
*   **Orthogonality Relation:** $\int_{-1}^1 P_m(x)P_n(x)dx = \begin{cases} 0 & \text{if } m \ne n \\ \frac{2}{2n+1} & \text{if } m=n \end{cases}$

## Quick Summary
Lecture 9 introduced power series solutions for ODEs around ordinary points, focusing on Legendre's Equation. We derived its series solutions, identified Legendre Polynomials as special cases, and learned Rodrigues' Formula for generating them. A key takeaway is their orthogonality property over $[-1,1]$, making them a fundamental basis for polynomial expansions.