---
title: |
  MA 104 Lecture 7: Variation of Parameters & Higher Order Linear ODEs
lecture_number: 7
lecture_name: |
  Variation of Parameters & Higher Order Linear ODEs
category: |
sidebar_label: |
  Lecture 7
sidebar_position: 7
course: |
  MA 104
topic: |
  Ordinary Differential Equations
  2023-10-27
tags:
  - Ordinary Differential Equations
  - Variation of Parameters
  - Higher Order ODEs
  - Wronskian
  - Characteristic Equation
summary: |
  This lecture introduces the method of variation of parameters for solving non-homogeneous second-order linear ODEs and establishes fundamental concepts for n-th order linear ODEs, including their classification, solution properties, the Wronskian, and methods for solving homogeneous equations with constant coefficients.
math: true
---

# MA 104 Lecture 7: Variation of Parameters & Higher Order Linear ODEs

## Table of Contents
- Method of Variation of Parameters
- Higher Order Linear ODEs
- Linearity Principle
- General Solutions and Initial Value Problems (IVPs)
- Existence and Uniqueness Theorem for IVPs
- Wronskian
- Homogeneous Linear ODEs with Constant Coefficients
- Non-homogeneous Linear ODEs
- Method of Undetermined Coefficients (Higher Order)

## Method of Variation of Parameters
This method solves general non-homogeneous linear second-order ODEs of the form $y'' + P(x)y' + Q(x)y = r(x)$ where $P(x)$, $Q(x)$, and $r(x)$ are continuous variables on an interval $I$. It is an alternative to the method of undetermined coefficients, which is limited to constant $P(x)$, $Q(x)$ and specific forms of $r(x)$. Given two linearly independent solutions $y_1(x)$ and $y_2(x)$ of the associated homogeneous equation $y'' + P(x)y' + Q(x)y = 0$, a particular solution $y_p(x)$ is sought in the form $y_p(x) = v_1(x)y_1(x) + v_2(x)y_2(x)$, where $v_1(x)$ and $v_2(x)$ are functions to be determined. The method involves setting $v_1'y_1 + v_2'y_2 = 0$ as a simplifying condition, leading to a system of equations for $v_1'$ and $v_2'$ which can be solved using the Wronskian.

## Higher Order Linear ODEs
An $n$-th order linear ODE is given by $P_n(x)y^{(n)} + P_{n-1}(x)y^{(n-1)} + \dots + P_1(x)y' + P_0(x)y = r(x)$. In standard form, this is $y^{(n)} + p_{n-1}(x)y^{(n-1)} + \dots + p_1(x)y' + p_0(x)y = r(x)$, where $p_i(x) = P_i(x)/P_n(x)$. The ODE is **homogeneous** if $r(x)=0$ and **non-homogeneous** if $r(x) \neq 0$. A **solution** is any $n$-times differentiable function $y=h(x)$ on an interval $I$ that satisfies the equation.

## Linearity Principle
For a homogeneous linear ODE, the **Fundamental Theorem** states that any sum or constant multiple of solutions is also a solution. A set of functions $y_1(x), \dots, y_n(x)$ is **linearly independent (L.I.)** on an interval $I$ if the equation $c_1y_1(x) + \dots + c_ny_n(x) = 0$ implies that all constants $c_1, \dots, c_n$ must be zero. Otherwise, the functions are **linearly dependent (L.D.)**. A **basis (or fundamental system)** of solutions for an $n$-th order homogeneous ODE consists of $n$ linearly independent solutions.

## General Solutions and Initial Value Problems (IVPs)
The **general solution** of a homogeneous $n$-th order linear ODE is $y_h = c_1y_1 + \dots + c_ny_n$, where $y_1, \dots, y_n$ form a basis of solutions and $c_1, \dots, c_n$ are arbitrary constants. The **general solution** of a non-homogeneous $n$-th order linear ODE is $y = y_p + y_h$, where $y_p$ is a particular solution of the non-homogeneous equation and $y_h$ is the general solution of the associated homogeneous equation. An **Initial Value Problem (IVP)** for an $n$-th order ODE includes $n$ initial conditions specified at a point $x_0$: $y(x_0)=y_0, y'(x_0)=y_1, \dots, y^{(n-1)}(x_0)=y_{n-1}$.

## Existence and Uniqueness Theorem for IVPs
For an $n$-th order linear ODE in standard form, if the coefficient functions $p_0(x), \dots, p_{n-1}(x)$ and $r(x)$ are continuous on an open interval $I$, and $x_0$ is any point in $I$, then the IVP associated with that ODE has a unique solution $y(x)$ on the interval $I$. The homogeneous linear ODE can be viewed as a linear map $L(y) := y^{(n)} + p_{n-1}(x)y^{(n-1)} + \dots + p_0(x)y$, and its solutions form the **null space** $N(L)$.

## Wronskian
The **Wronskian** of $n$ functions $y_1, \dots, y_n$, which are $n-1$ times differentiable on an interval $I$, is defined as the determinant:
$$W(y_1, \dots, y_n)(x) = \det \begin{pmatrix} y_1 & y_2 & \dots & y_n \\ y_1' & y_2' & \dots & y_n' \\ \vdots & \vdots & \ddots & \vdots \\ y_1^{(n-1)} & y_2^{(n-1)} & \dots & y_n^{(n-1)} \end{pmatrix}$$
For solutions $y_1, \dots, y_n$ of a homogeneous linear ODE with continuous coefficients on $I$: they are linearly dependent on $I$ if and only if their Wronskian is zero for some $x_0 \in I$. If $W(x_0) = 0$ for any $x_0 \in I$, then $W(x)$ is identically zero on $I$. Conversely, if $W(x_0) \neq 0$ for some $x_0 \in I$, then the solutions are linearly independent and form a basis. If the coefficients are continuous, a general solution for the homogeneous ODE always exists.

## Homogeneous Linear ODEs with Constant Coefficients
For homogeneous linear ODEs with constant coefficients, $y^{(n)} + a_{n-1}y^{(n-1)} + \dots + a_1y' + a_0y = 0$, solutions are found by substituting $y=e^{\lambda x}$ to obtain the **characteristic equation**: $\lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_1\lambda + a_0 = 0$. If $\lambda_0$ is a root of this polynomial, then $e^{\lambda_0 x}$ is a solution.
-   **Distinct Real Roots:** If $\lambda_1, \dots, \lambda_n$ are distinct real roots, then $e^{\lambda_1 x}, \dots, e^{\lambda_n x}$ form a basis of solutions. Their Wronskian is non-zero, affirming linear independence.
-   **Simple Complex Roots:** If $\lambda = \alpha \pm i\beta$ are a conjugate pair of simple complex roots (occurring because coefficients are real), then $e^{\alpha x}\cos(\beta x)$ and $e^{\alpha x}\sin(\beta x)$ are two linearly independent real solutions.
-   **Multiple Real Roots:** If $\lambda_1$ is a real root of multiplicity $m$, then $e^{\lambda_1 x}, xe^{\lambda_1 x}, x^2e^{\lambda_1 x}, \dots, x^{m-1}e^{\lambda_1 x}$ are $m$ linearly independent solutions.
-   **Multiple Complex Roots:** If $\lambda = \alpha \pm i\beta$ are complex conjugate roots, each with multiplicity $m$, then $e^{\alpha x}\cos(\beta x), e^{\alpha x}\sin(\beta x), xe^{\alpha x}\cos(\beta x), xe^{\alpha x}\sin(\beta x), \dots, x^{m-1}e^{\alpha x}\cos(\beta x), x^{m-1}e^{\alpha x}\sin(\beta x)$ form $2m$ linearly independent solutions.

## Non-homogeneous Linear ODEs
The general solution to a non-homogeneous linear ODE $L(y) = r(x)$ is $y = y_p + y_h$, where $y_p$ is any particular solution to the non-homogeneous equation and $y_h$ is the general solution to the associated homogeneous equation $L(y)=0$. The set of all solutions to $L(y)=r(x)$ forms a translation of the null space $N(L)$ by $y_p$.

## Method of Undetermined Coefficients (Higher Order)
This method for finding a particular solution $y_p$ for non-homogeneous ODEs with constant coefficients and specific forms of $r(x)$ extends from second-order ODEs.
-   **Basic Rule & Sum Rule:** Similar to second-order cases, an initial guess for $y_p$ is made based on the form of $r(x)$, and if $r(x)$ is a sum of terms, $y_p$ is a sum of corresponding guesses.
-   **Modification Rule:** If any term in the initial guess for $y_p$ is a solution to the associated homogeneous equation, then that term in the guess must be multiplied by $x^k$, where $k$ is the smallest positive integer such that the modified term is no longer a solution of the homogeneous equation.

## Key Formulas
-   **Wronskian for two functions $y_1, y_2$**: $W(y_1, y_2)(x) = y_1y_2' - y_2y_1'$
-   **Wronskian for $n$ functions**: $W(y_1, \dots, y_n)(x) = \det(Y(x))$ where $Y(x)$ is the matrix of functions and their derivatives up to order $n-1$.
-   **Particular solution $y_p$ (Variation of Parameters)**:
    -   $v_1'(x) = -\frac{y_2(x)r(x)}{W(y_1, y_2)(x)}$
    -   $v_2'(x) = \frac{y_1(x)r(x)}{W(y_1, y_2)(x)}$
    -   $y_p(x) = y_1(x) \int -\frac{y_2(x)r(x)}{W(y_1, y_2)(x)} \,dx + y_2(x) \int \frac{y_1(x)r(x)}{W(y_1, y_2)(x)} \,dx$
-   **Characteristic Equation for constant coefficients**: $\lambda^n + a_{n-1}\lambda^{n-1} + \dots + a_1\lambda + a_0 = 0$

## Quick Summary
Lecture 7 covered two main topics: the **Method of Variation of Parameters** for solving general second-order non-homogeneous linear ODEs, which utilizes the Wronskian of homogeneous solutions to construct a particular solution. It also delved into **Higher Order Linear ODEs**, defining their forms (homogeneous/non-homogeneous, standard), the **Linearity Principle**, and crucial theorems regarding **Existence and Uniqueness of Solutions for IVPs**. The **Wronskian** was introduced as a determinant to assess the linear independence of solutions. Finally, methods for solving **Homogeneous Linear ODEs with Constant Coefficients** were detailed based on the roots of the characteristic equation (distinct real, simple complex, multiple real, multiple complex), and the **Method of Undetermined Coefficients** was extended to higher order equations, including its modification rule.