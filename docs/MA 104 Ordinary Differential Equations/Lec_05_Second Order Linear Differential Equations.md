---
title: |
  Second Order Linear Differential Equations
lecture_number: 5
lecture_name: |
  Second Order Linear Differential Equations
category: |
sidebar_label: |
  Lecture 5
sidebar_position: 5
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Second Order Linear Differential Equations
date: |
  2023-10-27
tags: ['Differential Equations', 'Second Order ODEs', 'Homogeneous ODEs', 'Nonhomogeneous ODEs', 'Linear ODEs', 'Constant Coefficients', 'Euler-Cauchy']
summary: |
  A concise overview of second-order linear differential equations, covering definitions, homogeneous and nonhomogeneous forms, existence and uniqueness theorems, reduction of order, constant coefficient equations, and Euler-Cauchy equations.
math: true
---

# Second Order Linear Differential Equations

## Table of Contents
*   Introduction to Second Order Linear ODEs
*   General Solution Structure
*   Reduction of Order
*   Homogeneous Linear ODEs with Constant Coefficients
*   Euler-Cauchy Equations
*   Key Formulas
*   Quick Summary

## Introduction to Second Order Linear ODEs

### Definition of Linear and Nonlinear ODEs
A second-order Ordinary Differential Equation (ODE) is **linear** if it can be written as:
$$y'' + p(x)y' + q(x)y = r(x) \quad (1)$$
where $p(x)$, $q(x)$, and $r(x)$ are functions of $x$. A second-order ODE is **nonlinear** if it cannot be written in this form.
In a linear ODE, $y$ and its derivatives ($y', y''$) appear linearly (i.e., to the power of one, not multiplied by each other or transformed by nonlinear functions).

### Homogeneous and Nonhomogeneous Forms
If $r(x) = 0$, then Equation (1) reduces to:
$$y'' + p(x)y' + q(x)y = 0 \quad (2)$$
Equation (2) is called a **homogeneous** second-order linear ODE. If $r(x) \neq 0$, Equation (1) is called a **nonhomogeneous** second-order linear ODE.

## General Solution Structure

### Superposition Principle
If $y_1(x)$ and $y_2(x)$ are two solutions of a homogeneous linear ODE (2), then any linear combination $c_1y_1(x) + c_2y_2(x)$ is also a solution for arbitrary constants $c_1, c_2$.
If $y_g$ is the general solution of the homogeneous equation (2) and $y_p$ is any particular solution of the nonhomogeneous equation (1), then $y_g + y_p$ is the general solution of the nonhomogeneous equation (1).

### Initial Value Problems
For a second-order linear ODE, an Initial Value Problem (IVP) consists of the ODE and two initial conditions: $y(x_0)=y_0$ and $y'(x_0)=y_1$. These conditions are used to determine the specific values of arbitrary constants in the general solution.

### Existence and Uniqueness Theorem
Consider the IVP: $y''(x) + P(x)y'(x) + Q(x)y(x) = R(x)$ with $y(x_0)=y_0, y'(x_0)=y_1$.
If $P(x)$, $Q(x)$, and $R(x)$ are continuous functions on an open interval $I$ containing $x_0$, then the IVP admits a unique solution on $I$.

### Basis of Solutions and Linear Independence
For a homogeneous linear ODE (2), if $y_1(x)$ and $y_2(x)$ are two solutions on an interval $I$ that are not proportional (i.e., linearly independent), they form a **basis** of solutions. In this case, the **general solution** of the homogeneous ODE is $y(x) = c_1y_1(x) + c_2y_2(x)$, where $c_1, c_2$ are arbitrary constants.
The null space of the linear operator $L[y] = y'' + P(x)y' + Q(x)y$ is a vector space of dimension 2.

## Reduction of Order
If one solution $y_1(x)$ of the homogeneous linear ODE $y'' + P(x)y' + Q(x)y = 0$ is known, a second linearly independent solution $y_2(x)$ can be found using the method of reduction of order. Assume $y_2(x) = u(x)y_1(x)$ for some non-constant function $u(x)$. Substituting this into the ODE yields a first-order ODE for $u'(x)$.
The function $U = u'$ is given by:
$$U(x) = \frac{1}{y_1(x)^2} e^{-\int P(x)dx}$$
Then, $u(x) = \int U(x) dx$, and the second solution is $y_2(x) = y_1(x) \int \frac{1}{y_1(x)^2} e^{-\int P(x)dx} dx$.

## Homogeneous Linear ODEs with Constant Coefficients

Consider the ODE: $y'' + Py' + Qy = 0$, where $P$ and $Q$ are constants.
The **characteristic equation** (or auxiliary equation) is formed by substituting $y=e^{\lambda x}$:
$$\lambda^2 + P\lambda + Q = 0$$
The roots of this quadratic equation, $\lambda_{1,2} = \frac{-P \pm \sqrt{P^2-4Q}}{2}$, determine the form of the general solution.

### Case I: Distinct Real Roots ($P^2-4Q > 0$)
If $\lambda_1$ and $\lambda_2$ are distinct real roots, the general solution is:
$$y(x) = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$$

### Case II: Repeated Real Roots ($P^2-4Q = 0$)
If $\lambda_1 = \lambda_2 = \lambda = -P/2$ is a repeated real root, the general solution is:
$$y(x) = (c_1 + c_2x)e^{\lambda x}$$

### Case III: Distinct Complex Conjugate Roots ($P^2-4Q < 0$)
If the roots are complex conjugates, $\lambda_{1,2} = \alpha \pm i\beta$, where $\alpha = -P/2$ and $\beta = \frac{\sqrt{4Q-P^2}}{2}$, the general solution is:
$$y(x) = e^{\alpha x}(c_1 \cos(\beta x) + c_2 \sin(\beta x))$$

## Euler-Cauchy Equations

Consider the ODE: $x^2y'' + axy' + by = 0$, where $a$ and $b$ are constants.
The **auxiliary equation** (or characteristic equation) is formed by substituting $y=x^n$:
$$n(n-1) + an + b = 0 \implies n^2 + (a-1)n + b = 0$$
The roots of this quadratic equation, $n_1, n_2$, determine the form of the general solution.

### Case I: Distinct Real Roots ($n_1 \neq n_2$)
If $n_1$ and $n_2$ are distinct real roots, the general solution is:
$$y(x) = c_1x^{n_1} + c_2x^{n_2}$$

### Case II: Repeated Real Roots ($n_1 = n_2 = n$)
If $n$ is a repeated real root, the general solution is:
$$y(x) = (c_1 + c_2 \ln|x|)x^n$$

### Case III: Distinct Complex Conjugate Roots ($n_{1,2} = \alpha \pm i\beta$)
If the roots are complex conjugates, $n_{1,2} = \alpha \pm i\beta$, the general solution is:
$$y(x) = x^{\alpha}(c_1 \cos(\beta \ln|x|) + c_2 \sin(\beta \ln|x|))$$

## Key Formulas

*   **Second-Order Linear ODE:** $y'' + p(x)y' + q(x)y = r(x)$
*   **Homogeneous Form:** $y'' + p(x)y' + q(x)y = 0$
*   **Reduction of Order Formula:** $y_2(x) = y_1(x) \int \frac{1}{y_1(x)^2} e^{-\int P(x)dx} dx$
*   **Constant Coefficient ODE Characteristic Equation:** $\lambda^2 + P\lambda + Q = 0$
    *   **Distinct Real Roots ($\lambda_1, \lambda_2$):** $y(x) = c_1e^{\lambda_1 x} + c_2e^{\lambda_2 x}$
    *   **Repeated Real Root ($\lambda$):** $y(x) = (c_1 + c_2x)e^{\lambda x}$
    *   **Complex Conjugate Roots ($\alpha \pm i\beta$):** $y(x) = e^{\alpha x}(c_1 \cos(\beta x) + c_2 \sin(\beta x))$
*   **Euler-Cauchy Auxiliary Equation:** $n^2 + (a-1)n + b = 0$
    *   **Distinct Real Roots ($n_1, n_2$):** $y(x) = c_1x^{n_1} + c_2x^{n_2}$
    *   **Repeated Real Root ($n$):** $y(x) = (c_1 + c_2 \ln|x|)x^n$
    *   **Complex Conjugate Roots ($\alpha \pm i\beta$):** $y(x) = x^{\alpha}(c_1 \cos(\beta \ln|x|) + c_2 \sin(\beta \ln|x|))$

## Quick Summary

Second-order linear ODEs are fundamental, defined by the form $y'' + p(x)y' + q(x)y = r(x)$, where $r(x)=0$ denotes homogeneity. The superposition principle applies to homogeneous linear ODEs. Existence and uniqueness of solutions for IVPs are guaranteed if coefficient functions are continuous. If one solution is known, a second can be found via reduction of order. For constant coefficient equations ($y'' + Py' + Qy = 0$), solutions are determined by the roots of the characteristic equation $\lambda^2 + P\lambda + Q = 0$, leading to distinct real, repeated real, or complex conjugate root cases. Euler-Cauchy equations ($x^2y'' + axy' + by = 0$) similarly use an auxiliary equation $n^2 + (a-1)n + b = 0$ to find solutions, with analogous cases for its roots.