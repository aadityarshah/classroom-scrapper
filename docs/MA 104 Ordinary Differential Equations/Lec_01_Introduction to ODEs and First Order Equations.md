---
title: |
  MA 104: Ordinary Differential Equations
lecture_number: |
  1
lecture_name: |
  Introduction to ODEs and First Order Equations
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Introduction to ODEs, First Order ODEs
date: |
  January 7, 2026
tags:
  - |
    Ordinary Differential Equations
  - |
    ODEs
  - |
    First Order ODEs
  - |
    Modeling
  - |
    Solutions
  - |
    Initial Value Problems
  - |
    Homogeneous Equations
  - |
    Exact Equations
summary: |
  Introduction to Ordinary Differential Equations, their definition, order, the modeling process, and properties of solutions for first-order ODEs including implicit/explicit forms, existence, uniqueness, general, particular, and singular solutions. Key types of first-order ODEs such as homogeneous and exact equations are also introduced along with their solution approaches.
math: true
table_of_contents: true
---

# MA 104: Ordinary Differential Equations

## Table of Contents
- [Basic Concepts: Modeling](#basic-concepts-modeling)
- [Ordinary Differential Equations (ODEs)](#ordinary-differential-equations-odes)
- [First Order ODEs](#first-order-odes)
- [Types of Solutions and Initial Value Problems](#types-of-solutions-and-initial-value-problems)
- [Homogeneous First Order ODEs](#homogeneous-first-order-odes)
- [Exact Equations](#exact-equations)
- [Key Formulas](#key-formulas)
- [Quick Summary](#quick-summary)

## Basic Concepts: Modeling
The process of modeling involves:
1.  **Physical System**
2.  **Mathematical Model**
3.  **Mathematical Solution**
4.  **Physical Interpretation**

## Ordinary Differential Equations (ODEs)
*   **Definition: Ordinary Differential Equation (ODE)**
    An equation that contains one or more derivatives of an unknown function, usually denoted by $y(x)$ (or $y(t)$ when time $t$ is the independent variable).

*   **Definition: Order of an ODE**
    An ODE is said to be of **order $n$** if the $n^{th}$ derivative of the unknown function $y$ is the highest derivative of $y$ in the equation.

## First Order ODEs
*   **Implicit form**: $F(x, y, y') = 0$.
*   **Explicit form**: $y' = f(x, y)$.

*   **Definition: Solution of an ODE**
    A function $y = h(x)$ is called a **solution** of $F(x, y, y') = 0$ on an interval $(a, b)$ if:
    *   $h$ is differentiable on $(a, b)$.
    *   Substitution of $y = h(x)$ and $y' = h'(x)$ gives an identity.

*   **Definition: Solution Curve / Integral Curve**
    The graph of a solution $h(x)$ is called a solution curve or integral curve.

## Types of Solutions and Initial Value Problems
*   ODEs may not always have solutions.
*   Solutions can be:
    *   **General Solution**: A family of solutions containing an arbitrary constant.
    *   **Particular Solution**: Obtained from a general solution by applying an initial condition to determine the constant.
    *   **Singular Solution**: A solution that cannot be obtained from the general family of solutions by assigning a specific value to the arbitrary constant.

*   **Definition: Initial Value Problem (IVP)**
    An IVP consists of an ODE $y' = f(x, y)$ together with an initial condition $y(x_0) = y_0$.

*   **IVP Solution Behavior**: A first-order IVP may exhibit:
    *   No solution.
    *   A unique solution.
    *   Infinitely many solutions.

*   **Central Formula: Growth and Decay**
    The ODE $y' = ky$ has solutions $y = c e^{kt}$.
    *   **Exponential growth** (Malthus' law) if $k > 0$.
    *   **Exponential decay** if $k < 0$.

## Homogeneous First Order ODEs
*   **Definition: Homogeneous Function**
    A function $f(x, y)$ is called **homogeneous of degree $n$** if $f(tx, ty) = t^n f(x, y)$ for any $t$.

*   **Definition: Homogeneous ODE**
    A first-order ODE $y' = f(x, y)$ is **homogeneous** if $f(x, y)$ can be expressed as a function of $y/x$, i.e., $y' = g(y/x)$.
    Alternatively, an ODE $M(x,y)dx + N(x,y)dy = 0$ is homogeneous if $M(x,y)$ and $N(x,y)$ are homogeneous functions of the same degree.

*   **Method of Solution**: For a homogeneous ODE $y' = g(y/x)$, the substitution $u = y/x$ (implying $y = ux$ and $y' = u'x + u$) transforms the ODE into a separable form.

## Exact Equations
*   **Definition: Exact Equation**
    An ODE of the form $M(x, y) dx + N(x, y) dy = 0$ is **exact** if there exists a function $u(x, y)$ such that its total differential $du$ is equal to $M(x, y) dx + N(x, y) dy$.

*   **Theorem: Condition for Exactness**
    If $M(x, y)$ and $N(x, y)$ have continuous first partial derivatives on a simply connected region, then the ODE $M(x, y) dx + N(x, y) dy = 0$ is exact if and only if:
    $$ \frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} $$

*   **Method of Solution**: If an ODE $M(x, y) dx + N(x, y) dy = 0$ is exact, its solution is given implicitly by $u(x, y) = c$, where $u(x, y)$ satisfies:
    $$ \frac{\partial u}{\partial x} = M(x, y) \quad \text{and} \quad \frac{\partial u}{\partial y} = N(x, y) $$

## Key Formulas
*   Implicit form of First Order ODE: $F(x, y, y') = 0$
*   Explicit form of First Order ODE: $y' = f(x, y)$
*   Growth/Decay ODE: $y' = ky$
*   Growth/Decay Solution: $y = c e^{kt}$
*   Substitution for Homogeneous ODEs: $u = y/x \implies y' = u'x + u$
*   Separated form for Homogeneous ODEs: $\frac{du}{g(u)-u} = \frac{dx}{x}$
*   Exactness Condition: $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
*   Solution of Exact ODE: $u(x, y) = c$, where $du = M(x, y) dx + N(x, y) dy$

## Quick Summary
Ordinary Differential Equations (ODEs) involve derivatives of an unknown function, with their order defined by the highest derivative. The process of mathematical modeling involves translating a physical system into an ODE, solving it, and interpreting the solution physically. First-order ODEs can be expressed in implicit or explicit forms. Solutions to ODEs (and Initial Value Problems) may not always exist, or can be unique, or infinitely many; they can be general, particular, or singular. Specific types of first-order ODEs include homogeneous equations, which are solvable by the substitution $u=y/x$, and exact equations, identifiable by the condition $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$, leading to an implicit solution $u(x,y)=c$.