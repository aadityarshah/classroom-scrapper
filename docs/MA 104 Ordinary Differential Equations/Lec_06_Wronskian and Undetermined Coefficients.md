---
title: |
  Wronskian and Method of Undetermined Coefficients for ODEs
lecture_number: 6
lecture_name: |
  Wronskian and Undetermined Coefficients
category: |
sidebar_label: |
  Lecture 6
sidebar_position: 6
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Wronskian, Linear Independence, Abel's Theorem, Nonhomogeneous ODEs, Method of Undetermined Coefficients, Annihilator Method
tags:
  - ODE
  - Wronskian
  - Linear Independence
  - Abel's Theorem
  - Nonhomogeneous ODEs
  - Undetermined Coefficients
  - Annihilator Method
summary: |
  This lecture introduces the Wronskian for checking linear independence of solutions to second-order linear homogeneous ODEs, including Abel's Theorem. It then shifts to nonhomogeneous ODEs, defining the general solution structure and detailing the Method of Undetermined Coefficients and its underlying Annihilator Method.
math: true
---

# Wronskian and Method of Undetermined Coefficients for ODEs

## Table of Contents
- Wronskian Definition
- Wronskian and Linear Independence
- Abel's Theorem (Vanishing Property of Wronskian)
- Nonhomogeneous Linear ODEs
- Method of Undetermined Coefficients
- Annihilator Method

## Wronskian Definition

**Definition: Wronskian**
For two differentiable functions $y_1(x)$ and $y_2(x)$, their Wronskian is defined as the determinant:
$$W(y_1, y_2)(x) = \begin{vmatrix} y_1(x) & y_2(x) \\ y_1'(x) & y_2'(x) \end{vmatrix} = y_1(x)y_2'(x) - y_2(x)y_1'(x)$$
The Wronskian is a function $W(y_1, y_2): I \to \mathbb{R}$, where $I$ is the interval on which $y_1$ and $y_2$ are defined and differentiable.

## Wronskian and Linear Independence

**Theorem (Linear Dependence Implies Vanishing Wronskian)**
If $y_1(x)$ and $y_2(x)$ are linearly dependent and differentiable on an interval $I$, then $W(y_1, y_2)(x) = 0$ for all $x \in I$.

**Note**
If $W(y_1, y_2)(x_0) \neq 0$ for some $x_0 \in I$, then $y_1$ and $y_2$ are linearly independent.
The converse (if $W(y_1, y_2)(x) = 0$ for all $x \in I$, then $y_1, y_2$ are linearly dependent) is **not always true** for arbitrary functions but holds true if $y_1, y_2$ are solutions of a second-order linear homogeneous ODE with continuous coefficients.

**Theorem (Converse for Solutions of an ODE)**
Suppose $y_1(x)$ and $y_2(x)$ are solutions of the second-order linear homogeneous ODE $y'' + P(x)y' + Q(x)y = 0$ on an interval $I$, where $P(x)$ and $Q(x)$ are continuous on $I$. Then $y_1(x)$ and $y_2(x)$ are linearly dependent if and only if $W(y_1, y_2)(x) = 0$ for all $x \in I$.

## Abel's Theorem (Vanishing Property of Wronskian)

**Theorem (Abel's Theorem)**
Suppose $y_1(x)$ and $y_2(x)$ are two solutions of the second-order linear homogeneous ODE $y'' + P(x)y' + Q(x)y = 0$ on an interval $I$. If $P(x)$ and $Q(x)$ are continuous on $I$, then the Wronskian $W(y_1, y_2)(x)$ is given by:
$$W(y_1, y_2)(x) = C e^{-\int P(x) dx}$$
where $C$ is a constant that depends on $y_1$ and $y_2$ but not on $x$.

**Remarks**
1.  From Abel's Theorem, for solutions of $y'' + P(x)y' + Q(x)y = 0$:
    -   Either $W(y_1, y_2)(x) = 0$ for all $x \in I$ (if $C=0$).
    -   Or $W(y_1, y_2)(x) \neq 0$ for all $x \in I$ (if $C \neq 0$).
2.  If $W(y_1, y_2)(x_0) = 0$ for just one point $x_0 \in I$, then $W(y_1, y_2)(x) = 0$ for all $x \in I$.
3.  If $y_1, y_2$ are linearly independent solutions of an ODE $y''+P(x)y'+Q(x)y=0$ (with $P, Q$ continuous), then for any $x_0 \in I$:
    -   It is not possible for both $y_1(x_0)=0$ and $y_2(x_0)=0$.
    -   It is not possible for both $y_1'(x_0)=0$ and $y_2'(x_0)=0$.

## Nonhomogeneous Linear ODEs

A second-order linear nonhomogeneous ODE has the form:
$$y'' + P(x)y' + Q(x)y = r(x)$$
where $r(x) \neq 0$.

**General Solution Structure**
The general solution $y(x)$ to a nonhomogeneous ODE is the sum of a particular solution $y_p(x)$ and the general solution to the associated homogeneous ODE $y_h(x)$:
$$y(x) = y_p(x) + y_h(x)$$
where $y_h(x) = c_1y_1(x) + c_2y_2(x)$ and $y_1, y_2$ are linearly independent solutions to $y'' + P(x)y' + Q(x)y = 0$.

## Method of Undetermined Coefficients

This method is suitable for linear ODEs with constant coefficients ($y'' + py' + qy = r(x)$) where $r(x)$ is a specific type of function (exponential, polynomial, sine/cosine, or products/sums thereof).

**Procedure**
1.  **Basic Rule:** If $r(x)$ is one of the functions in Table 2.1 (P.82, Kreyszig), choose the corresponding form for $y_p(x)$ with undetermined coefficients.
    -   If $r(x) = k e^{\gamma x}$, choose $y_p = C e^{\gamma x}$.
    -   If $r(x) = k x^n$ ($n=0,1,\dots$), choose $y_p = K_n x^n + K_{n-1} x^{n-1} + \dots + K_1 x + K_0$.
    -   If $r(x) = k \cos(\omega x)$ or $k \sin(\omega x)$, choose $y_p = K \cos(\omega x) + M \sin(\omega x)$.
    -   If $r(x) = k e^{\alpha x} \cos(\omega x)$ or $k e^{\alpha x} \sin(\omega x)$, choose $y_p = e^{\alpha x} (K \cos(\omega x) + M \sin(\omega x))$.
2.  **Modification Rule:** If any term in the chosen $y_p(x)$ (from the Basic Rule) is a solution of the associated homogeneous ODE, multiply $y_p(x)$ by $x$. If that term corresponds to a double root of the characteristic equation of the homogeneous ODE, multiply by $x^2$.
3.  **Sum Rule:** If $r(x)$ is a sum of functions (e.g., $r(x) = r_1(x) + r_2(x)$), choose $y_p$ as the sum of the corresponding particular solutions for each term ($y_p = y_{p1} + y_{p2}$).
4.  Substitute $y_p$ and its derivatives into the nonhomogeneous ODE to determine the unknown coefficients.

## Annihilator Method

This method provides the theoretical basis for the Method of Undetermined Coefficients by transforming the nonhomogeneous ODE into a higher-order homogeneous ODE.

**Definition: Annihilator**
A differential operator $A$ is an annihilator of a function $f(x)$ if $A f(x) = 0$.

**Common Annihilators**
-   For $f(x) = e^{mx}$, $A = D-m$.
-   For $f(x) = x^n$, $A = D^{n+1}$.
-   For $f(x) = \sin(ax+b)$ or $f(x) = \cos(ax+b)$, $A = D^2+a^2$.
-   For $f(x) = x^n e^{mx}$, $A = (D-m)^{n+1}$.
-   For $f(x) = x^n \sin(ax+b)$ or $f(x) = x^n \cos(ax+b)$, $A = (D^2+a^2)^{n+1}$.

**Procedure for Solving $Ly=r(x)$ using Annihilators**
1.  Identify the differential operator $L$ for the given ODE $Ly=r(x)$.
2.  Find a differential operator $A$ that annihilates $r(x)$, i.e., $A r(x) = 0$.
3.  Apply $A$ to the ODE: $A(Ly) = A(r(x)) \implies (A \circ L)y = 0$. This is a higher-order homogeneous ODE.
4.  Find the characteristic equation and its roots for $(A \circ L)y = 0$. This gives the general solution form for $y$.
5.  The terms in this general solution that are solutions to the associated homogeneous ODE $Ly=0$ constitute $y_h$. The remaining terms, with arbitrary coefficients, form the structure of $y_p$.
6.  Substitute this form of $y_p$ (with undetermined coefficients) into the original nonhomogeneous ODE $Ly=r(x)$ to solve for the coefficients.

## Key Formulas
-   **Wronskian:** $W(y_1, y_2)(x) = y_1(x)y_2'(x) - y_2(x)y_1'(x)$
-   **Abel's Theorem:** For $y'' + P(x)y' + Q(x)y = 0$, $W(y_1, y_2)(x) = C e^{-\int P(x) dx}$
-   **General Solution of Nonhomogeneous ODE:** $y(x) = y_p(x) + y_h(x)$
-   **Annihilators:**
    -   $D-m$ for $e^{mx}$
    -   $D^{n+1}$ for $x^n$
    -   $D^2+a^2$ for $\sin(ax+b), \cos(ax+b)$

## Quick Summary
The Wronskian determines the linear independence of two functions, especially solutions to a second-order linear homogeneous ODE. Abel's Theorem shows that for such solutions, the Wronskian is either identically zero or never zero, depending on a constant. For nonhomogeneous ODEs, the general solution is the sum of a particular solution and the homogeneous solution. The Method of Undetermined Coefficients provides a systematic way to find particular solutions for specific $r(x)$ functions, using a set of rules (basic, modification, sum). The Annihilator Method is a more formal approach, converting the nonhomogeneous ODE into a higher-order homogeneous one by applying an operator that "annihilates" the nonhomogeneous term $r(x)$.