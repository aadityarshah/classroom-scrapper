---
title: |
  MA 104 Lecture 10: Frobenius Method and Bessel's Equation
lecture_number: 10
lecture_name: |
  Frobenius Method and Bessel's Equation
category: |
  
sidebar_label: |
  Lecture 10
sidebar_position: 10
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Frobenius Method, Regular Singular Points, Cauchy-Euler Equation, Bessel's Equation
date: |
  2023-10-26
tags: ['Differential Equations', 'Frobenius Method', 'Cauchy-Euler', 'Bessel Equation', 'Special Functions']
summary: |
  Explores the Frobenius method for finding series solutions around regular singular points, including the indicial equation and the three cases for roots. Introduces Cauchy-Euler and Bessel's Equations as applications.
math: true
---
# MA 104 Lecture 10: Frobenius Method and Bessel's Equation

## Table of Contents
*   Extended Power Series Method: Frobenius Method
*   Regular Singular Points
*   Cauchy-Euler Equation
*   Frobenius Method Cases
*   Bessel's Equation
*   Bessel Functions of the First Kind

## Extended Power Series Method: Frobenius Method
**Definition: Frobenius Method**
The Frobenius method finds series solutions for second-order linear ODEs of the form:
$$y'' + \frac{b(x)}{x}y' + \frac{c(x)}{x^2}y = 0$$
where $b(x)$ and $c(x)$ are analytic at $x=0$. The method seeks solutions of the form:
$$y(x) = x^r \sum_{m=0}^\infty a_m x^m = x^r (a_0 + a_1 x + a_2 x^2 + \dots)$$
with $a_0 \ne 0$. The exponent $r$ can be any real or complex number. This method applies around regular singular points.

## Regular Singular Points
**Definition: Singular Point**
For $y'' + P(x)y' + Q(x)y = 0$, $x_0$ is a **singular point** if $P(x)$ or $Q(x)$ (or both) are not analytic at $x_0$.
**Definition: Regular Singular Point**
A singular point $x_0$ is a **regular singular point** if $(x-x_0)P(x)$ and $(x-x_0)^2Q(x)$ are both analytic at $x_0$. Otherwise, it is an **irregular singular point**.
**Theorem: Indicial Equation**
Substituting the Frobenius series into $x^2y'' + x b(x) y' + c(x) y = 0$ (where $b(x) = \sum b_m x^m$ and $c(x) = \sum c_m x^m$) leads to the **indicial equation**:
$$I(r) := r(r-1) + r b_0 + c_0 = 0$$
The roots $r_1, r_2$ determine the solution forms.
**Recurrence Relation:** Coefficients $a_n(r)$ are determined by:
$$I(r+n) a_n + \sum_{k=0}^{n-1} a_k [(r+k)b_{n-k} + c_{n-k}] = 0 \quad \text{for } n \ge 1 \text{ if } I(r+n) \ne 0$$

## Cauchy-Euler Equation
**Definition: Cauchy-Euler Equation**
A canonical ODE for the Frobenius method is:
$$x^2y'' + bxy' + cy = 0$$
where $b, c \in \mathbb{R}$. For this, $b(x)=b$ and $c(x)=c$. The indicial equation is $r(r-1)+br+c=0$.
Solutions are typically of the form $y=x^r$:
*   If $r_1 \ne r_2$ are real, $y_1(x) = x^{r_1}$, $y_2(x) = x^{r_2}$.
*   If $r_1 = r_2 = r$ (real double root), $y_1(x) = x^r$, $y_2(x) = x^r \ln x$.
*   If $r_{1,2} = \alpha \pm i\beta$ (complex conjugates), $y_1(x) = x^\alpha \cos(\beta \ln x)$, $y_2(x) = x^\alpha \sin(\beta \ln x)$.

## Frobenius Method Cases
Given roots $r_1, r_2$ of $I(r)=0$ (assume $r_1 \ge r_2$):
**Case 1: Distinct Roots Not Differing by an Integer ($r_1 - r_2 \notin \mathbb{Z}$)**
A basis of solutions is:
$$y_1(x) = x^{r_1} \sum_{n=0}^\infty a_n(r_1)x^n$$
$$y_2(x) = x^{r_2} \sum_{n=0}^\infty a_n(r_2)x^n$$

**Case 2: Double Root ($r_1 = r_2 = r$)**
A basis of solutions is:
$$y_1(x) = x^r \sum_{n=0}^\infty a_n(r)x^n$$
$$y_2(x) = y_1(x) \ln x + x^r \sum_{n=1}^\infty a'_n(r)x^n$$
where $a'_n(r)$ are coefficients obtained by differentiating the recurrence relation with respect to $r$.

**Case 3: Roots Differing by an Integer ($r_1 - r_2 \in \mathbb{Z}$ with $r_1 > r_2$)**
A basis of solutions is:
$$y_1(x) = x^{r_1} \sum_{n=0}^\infty a_n(r_1)x^n$$
$$y_2(x) = k y_1(x) \ln x + x^{r_2} \sum_{n=0}^\infty A_n x^n$$
where $k$ may be zero, determined by the recurrence relation.

## Bessel's Equation
**Definition: Bessel's Equation of Order $\nu$**
A second-order linear ODE arising in cylindrical symmetry problems:
$$x^2y'' + xy' + (x^2-\nu^2)y = 0$$
where $\nu \in \mathbb{R}_{\ge 0}$. (Standard form: $y'' + \frac{1}{x}y' + \left(1-\frac{\nu^2}{x^2}\right)y = 0$).
The point $x=0$ is a regular singular point.

## Bessel Functions of the First Kind
**Theorem: Bessel Function of the First Kind**
Applying the Frobenius method to Bessel's Equation yields the indicial equation $r^2-\nu^2=0$, with roots $r_1=\nu$ and $r_2=-\nu$.
For $r=\nu$, the recurrence relation is $(n+2\nu)na_n + a_{n-2}=0$, leading to $a_1=0$ and all odd coefficients being zero. The even coefficients are:
$$a_{2m} = \frac{(-1)^m a_0}{2^{2m} m! (\nu+1)(\nu+2)\dots(\nu+m)}$$
By choosing $a_0 = \frac{1}{2^\nu \nu!}$ (for integer $\nu$), the particular solution is the **Bessel Function of the First Kind of order $\nu$**, denoted $J_\nu(x)$:
$$J_n(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! (n+m)!} \left(\frac{x}{2}\right)^{2m+n} \quad (\text{for integer } n \ge 0)$$
If $\nu$ is an integer, $J_{-\nu}(x) = (-1)^\nu J_\nu(x)$, requiring a second linearly independent solution (Bessel Function of the Second Kind, $Y_\nu(x)$) from Case 2 or 3 of the Frobenius method.

## Key Formulas
*   **Frobenius Series Solution:** $y(x) = x^r \sum_{m=0}^\infty a_m x^m$
*   **Indicial Equation:** $I(r) = r(r-1) + r b_0 + c_0 = 0$
*   **Cauchy-Euler Equation:** $x^2y'' + bxy' + cy = 0$
*   **Bessel's Equation:** $x^2y'' + xy' + (x^2-\nu^2)y = 0$
*   **Bessel Function of the First Kind (integer order $n$):** $J_n(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! (n+m)!} \left(\frac{x}{2}\right)^{2m+n}$

## Quick Summary
Lecture 10 covered the Frobenius method for solving ODEs around regular singular points. We defined regular singular points, derived the indicial equation, and explored the three cases for its roots, outlining the form of corresponding solutions. The Cauchy-Euler equation served as a foundational example. Finally, Bessel's Equation was analyzed, leading to the series definition of Bessel Functions of the First Kind, $J_\nu(x)$.