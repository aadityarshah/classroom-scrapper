---
title: |
  MA 104: Ordinary Differential Equations - Lecture 1
lecture_number: 1
lecture_name: |
  Introduction to Ordinary Differential Equations
category: |
sidebar_label: |
  Lecture 1
sidebar_position: 1
course: |
  MA 104
topic: |
  Ordinary Differential Equations
date: |
  January 7, 2026
tags: ['Ordinary Differential Equations', 'ODE', 'Calculus', 'MA104', 'Introduction']
summary: |
  This lecture introduces Ordinary Differential Equations (ODEs), covering basic definitions like order, implicit and explicit forms, and the concept of solutions and solution curves. It also touches upon modeling with ODEs, the existence and uniqueness of solutions, and the concept of initial value problems (IVPs). The concepts of homogeneous functions, homogeneous ODEs, and exact equations are also briefly introduced.
math: true
---

# MA 104: Ordinary Differential Equations - Lecture 1

## Table of Contents
* Course Logistics
* Basic Concepts: Modeling
* Ordinary Differential Equations (ODEs)
* First-Order ODEs
* Growth and Decay Curves
* Solutions to ODEs and Initial Value Problems (IVPs)
* Homogeneous First-Order ODEs
* Exact First-Order ODEs
* Key Formulas
* Quick Summary

## Course Logistics
*   **Lecture Day and Time:** Wednesday & Friday (10:00 AM – 11:20 AM)
*   **Tutorial Day and Time:** Wednesday (11:30 AM – 12:50 PM)
*   **Office Hour:** Monday (08:30 AM – 09:30 AM)
*   **Office No.:** AB 06/347 (by appointment)
*   **Google Classroom Code:** vmileaxf
*   **Grading Policy:** Relative grading policy.
    *   Quiz 1: 20%
    *   Quiz 2: 20%
    *   Final Examination: 40%
    *   Assignment: 10%
    *   Attendance: 10%
*   **Textbook:** E. Kreyszig, *Advanced Engineering Mathematics* (10th Edition), John Wiley, 2011.
*   **Reference Books:**
    *   W. E. Boyce and R. DiPrima, *Elementary Differential Equations* (8th Edition), John Wiley, 2005.
    *   G.F. Simmons, *Differential Equations with Applications and Historical Notes*, Tata McGraw-Hill Publishing Company Limited, 1974.

## Basic Concepts: Modeling
A physical system is translated into a mathematical model, which is then solved mathematically to obtain a physical interpretation.

## Ordinary Differential Equations (ODEs)
### Definition: Ordinary Differential Equation (ODE)
An ordinary differential equation (ODE) is an equation that contains one or more derivatives of an unknown function, usually denoted by $y(x)$ (or $y(t)$ when time $t$ is the independent variable).

### Definition: Order of an ODE
An ODE is said to be of **order** $n$ if the $n^{th}$ derivative of the unknown function $y$ is the highest derivative of $y$ in the equation.

## First-Order ODEs
Equations of this type involve only the first derivative and may include $y$ along with given functions of $x$.

### Implicit Form of First-Order ODE
$$F(x, y, y') = 0$$

### Explicit Form of First-Order ODE
$$y' = f(x, y)$$

### Definition: Solution of a First-Order ODE
A function $y = h(x)$ is called a **solution** of $F(x, y, y') = 0$ on an interval $a $<$ x $<$ b$ if:
*   $h$ is differentiable on $(a, b)$,
*   Substitution of $y = h(x)$ and $y' = h'(x)$ into the equation gives an identity.

### Definition: Solution Curve / Integral Curve
The graph of a solution $h(x)$ is called a **solution curve** or an **integral curve**.

## Growth and Decay Curves
The ODE $y' = ky$ models exponential growth (if $k $>$ 0$) or exponential decay (if $k $<$ 0$).

### Formula: Exponential Growth/Decay
$$y = ce^{kt}$$

## Solutions to ODEs and Initial Value Problems (IVPs)
### Definition: Particular Solution
A **particular solution** is obtained from the general solution by using an initial condition $y(x_0) = y_0$, which determines the constant $C$. Geometrically, the solution curve should pass through $(x_0, y_0)$.

### Definition: Initial Value Problem (IVP)
An ODE $y' = f(x, y)$ together with an initial condition $y(x_0) = y_0$ is called an **initial value problem (IVP)**.

### Existence and Uniqueness of Solutions for IVPs
A first-order IVP may exhibit:
1.  No solution.
2.  A unique solution.
3.  Infinitely many solutions.
This motivates the study of conditions under which solutions to an IVP exist and are unique.

## Homogeneous First-Order ODEs
### Definition: Homogeneous Function of Degree $n$
A function $f(x, y)$ is called **homogeneous of degree $n$** if $f(tx, ty) = t^n f(x, y)$.

### Homogeneous ODE Structure
If $y' = f(x, y)$ can be written as $y' = g(y/x)$, then it is a homogeneous ODE.
Such ODEs can be solved using the substitution $u = y/x$. This implies $y = ux$ and $y' = u'x + u$.

## Exact First-Order ODEs
### Definition: Exact Differential Equation
A differential equation of the form $M(x, y) \,dx + N(x, y) \,dy = 0$ is called **exact** if there exists a function $u(x, y)$ such that $du = M(x, y) \,dx + N(x, y) \,dy$. This means that $\frac{\partial u}{\partial x} = M(x, y)$ and $\frac{\partial u}{\partial y} = N(x, y)$.

### Condition for Exactness
The condition for exactness is $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$.

### Solution Form for Exact Equations
If the equation is exact, its solution is implicitly given by $u(x, y(x)) = c$, for an arbitrary constant $c$.

## Key Formulas
*   **Implicit Form (First-Order ODE):** $F(x, y, y') = 0$
*   **Explicit Form (First-Order ODE):** $y' = f(x, y)$
*   **Exponential Growth/Decay:** $y = ce^{kt}$
*   **Homogeneous ODE Substitution:** If $y' = g(y/x)$, use $u = y/x \implies y = ux, y' = u'x + u$.
*   **Exact ODE Condition:** For $M(x, y) \,dx + N(x, y) \,dy = 0$, it is exact if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$.
*   **Solution of Exact ODE:** $u(x, y) = c$, where $\frac{\partial u}{\partial x} = M$ and $\frac{\partial u}{\partial y} = N$.

## Quick Summary
Lecture 1 of MA 104 introduced Ordinary Differential Equations, defining them by the presence of derivatives of an unknown function and classifying them by order. We covered the implicit and explicit forms of first-order ODEs and the definition of a solution and solution curve. The lecture also touched upon how ODEs are used in modeling (e.g., exponential growth/decay), the concept of an Initial Value Problem (IVP), and noted that IVPs can have no, unique, or infinitely many solutions. Finally, the lecture briefly introduced homogeneous first-order ODEs and exact first-order ODEs, including their defining conditions and solution approaches.