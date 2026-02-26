---
title: |
  Linear First Order ODEs, Bernoulli Equation, Existence & Uniqueness, and Orthogonal Trajectories
lecture_number: 3
lecture_name: |
  Linear First Order ODEs, Bernoulli Equation, Existence & Uniqueness, and Orthogonal Trajectories
category: |
sidebar_label: |
  Lecture 3
sidebar_position: 3
course: |
  MA 104 Ordinary Differential Equations
topic: |
  First Order ODEs
date: |
  2023-10-27
tags:
  - ODE
  - Linear ODE
  - Bernoulli Equation
  - Existence
  - Uniqueness
  - Orthogonal Trajectories
summary: |
  This lecture covers the definition and solution methods for first-order linear ODEs, introduces the Bernoulli equation and its transformation to a linear form, discusses existence and uniqueness theorems for initial value problems, and defines and outlines the method for finding orthogonal trajectories of a given family of curves.
math: true
---

# Linear First Order ODEs, Bernoulli Equation, Existence & Uniqueness, and Orthogonal Trajectories

## Table of Contents
*   First Order Linear ODEs
*   Solving First Order Linear ODEs (Integrating Factor Method)
*   Bernoulli Equation
*   Existence Theorem for First Order IVP
*   Uniqueness Theorem for First Order IVP
*   Existence and Uniqueness for Linear First Order IVP
*   Orthogonal Trajectories

## First Order Linear ODEs

**Definition (Linear First Order ODE)**
A first order Ordinary Differential Equation (ODE) of the form $y' = f(x,y)$ is called **linear** if $f(x,y)$ depends linearly on the variable $y$, i.e., $f(x,y) = a(x)y + b(x)$.

**Definition (Standard Form)**
The standard form of a linear first order ODE is:
$$y' + p(x)y = r(x)$$

**Simpler Case (Constant Coefficients)**
If $p(x) = p$ and $r(x) = r$ (constants), the equation is $y' + py = r$.
The solution is given by:
$$y = C e^{-px} + \frac{r}{p}$$
(where $C$ is an arbitrary constant).

## Solving First Order Linear ODEs (Integrating Factor Method)

For the general standard form $y' + p(x)y = r(x)$, the method of Leibniz (integrating factor) is used.

**Definition (Integrating Factor)**
An **integrating factor**, $\mu(x)$, for the linear first-order ODE $y' + p(x)y = r(x)$ is a function such that when the ODE is multiplied by $\mu(x)$, the left-hand side becomes the derivative of a product, $\frac{d}{dx}(\mu(x)y)$.

**Theorem (Finding the Integrating Factor)**
The integrating factor $\mu(x)$ for the ODE $y' + p(x)y = r(x)$ is given by:
$$\mu(x) = e^{\int p(x)dx}$$
(A constant of integration can be chosen as $C=1$).

**Theorem (General Solution of Linear First Order ODE)**
Given the ODE $y' + p(x)y = r(x)$:
1.  Calculate the integrating factor $\mu(x) = e^{\int p(x)dx}$.
2.  Multiply the ODE by $\mu(x)$: $\mu(x)y' + \mu(x)p(x)y = \mu(x)r(x)$.
3.  The left-hand side is $\frac{d}{dx}(\mu(x)y)$. So, $\frac{d}{dx}(\mu(x)y) = \mu(x)r(x)$.
4.  Integrate both sides with respect to $x$: $\mu(x)y = \int \mu(x)r(x)dx + C$.
5.  Solve for $y$:
    $$y = \frac{1}{\mu(x)} \left[ \int \mu(x)r(x)dx + C \right]$$

## Bernoulli Equation

**Definition (Bernoulli Equation)**
An equation of the form $y' + Q(x)y = R(x)y^\alpha$, for a given fixed real number $\alpha$, is called a **Bernoulli Differential Equation**.

**Note**
If $\alpha=0$ or $\alpha=1$, the Bernoulli equation is linear.

**Theorem (Transformation to Linear ODE)**
Let $\alpha \neq 0, 1$. The transformation $u = y^{1-\alpha}$ reduces the Bernoulli equation $y' + Q(x)y = R(x)y^\alpha$ to a linear first-order ODE in $u$.

**Method of Transformation**
1.  Divide the Bernoulli equation by $y^\alpha$: $y'y^{-\alpha} + Q(x)y^{1-\alpha} = R(x)$.
2.  Let $u = y^{1-\alpha}$.
3.  Differentiate $u$ with respect to $x$: $u' = (1-\alpha)y^{-\alpha}y'$.
4.  Substitute $u$ and $u'$ into the modified equation:
    *   From $u' = (1-\alpha)y^{-\alpha}y'$, we have $y^{-\alpha}y' = \frac{1}{1-\alpha}u'$.
    *   Substitute this into step 1: $\frac{1}{1-\alpha}u' + Q(x)u = R(x)$.
    *   This rearranges to the linear ODE:
        $$u' + (1-\alpha)Q(x)u = (1-\alpha)R(x)$$
5.  Solve this linear ODE for $u(x)$ using the integrating factor method.
6.  Substitute back $u = y^{1-\alpha}$ to find $y(x)$.

## Existence Theorem for First Order IVP

**Definition (Initial Value Problem)**
A first-order Initial Value Problem (IVP) is defined as $y' = f(x,y)$ with an initial condition $y(x_0) = y_0$.

**Conclusion from Examples**
A first-order IVP may have no solution, a unique solution, or infinitely many solutions.

**Theorem (Peano, Existence Theorem)**
Consider the IVP: $y'(x) = f(x,y)$ with $y(x_0) = y_0$.
Suppose $f(x,y)$ is continuous for all points $(x,y)$ in some rectangle $D: |x-x_0| \leq a, |y-y_0| \leq b$.
And $f(x,y)$ is bounded in $D$, i.e., there exists $K $>$ 0$ such that $|f(x,y)| \leq K$ for all $(x,y) \in D$.
Then the IVP has **at least one** solution $y(x)$ for $x$ in the interval $|x-x_0| \leq \alpha$, where $\alpha = \min\{a, b/K\}$.

## Uniqueness Theorem for First Order IVP

**Theorem (Picard-Lindelöf, Uniqueness Theorem)**
Consider the IVP: $y'(x) = f(x,y)$ with $y(x_0) = y_0$.
Suppose $f(x,y)$ and its partial derivative $\frac{\partial f}{\partial y}$ are continuous for all $(x,y)$ in some rectangle $D: |x-x_0| \leq a, |y-y_0| \leq b$.
And $f(x,y)$ and $\frac{\partial f}{\partial y}$ are bounded in $D$, i.e., $|f(x,y)| \leq K$ and $|\frac{\partial f}{\partial y}(x,y)| \leq M$ for all $(x,y) \in D$.
Then the IVP has **at most one** solution $y(x)$ for $x$ in the interval $|x-x_0| \leq \alpha$, where $\alpha = \min\{a, b/K\}$.
*(Combining with the Existence Theorem, this guarantees a precisely one solution.)*

**Remark**
The condition $|\frac{\partial f}{\partial y}(x,y)| \leq M$ can be replaced by the **Lipschitz condition**: there exists $M $>$ 0$ such that $|f(x,y_2) - f(x,y_1)| \leq M|y_2 - y_1|$ for all $(x,y_1), (x,y_2) \in D$.

**Remark (Continuity is not enough for Uniqueness)**
Continuity of $f(x,y)$ alone is not sufficient to guarantee the uniqueness of the solution. For instance, the IVP $y' = \sqrt{|y|}$ with $y(0)=0$ has multiple solutions (e.g., $y(x)=0$ and $y(x) = \pm x^2/4$). In this case, $f(x,y) = \sqrt{|y|}$ is continuous, but $\frac{\partial f}{\partial y}$ is not continuous (or Lipschitz) at $y=0$.

## Existence and Uniqueness for Linear First Order IVP

**Theorem**
Consider the linear differential equation $y' + a(x)y = b(x)$, along with the initial value condition $y(x_0) = y_0$.
Let $a(x)$ and $b(x)$ be continuous functions for all $x$ with $|x-x_0| \leq a$.
Then the differential equation has a **unique solution** $y(x)$ on the interval $(x_0-a, x_0+a)$.

**Remark**
For $y' + a(x)y = b(x)$, we can define $f(x,y) = b(x) - a(x)y$.
Since $a(x)$ and $b(x)$ are continuous, $f(x,y)$ is continuous.
The partial derivative $\frac{\partial f}{\partial y} = -a(x)$ is also continuous.
Thus, the conditions for both the general Existence and Uniqueness theorems are satisfied, guaranteeing a unique solution.

## Orthogonal Trajectories

**Definition (Orthogonal Trajectories)**
A new family of curves that intersect a given family of curves at right angles are called **orthogonal trajectories** of the given curves.

**Definition (Angle of Intersection)**
The angle of intersection between two curves is defined as the angle between their tangent lines at the intersection point. For orthogonal curves, this angle is $90^\circ$. If the slope of one curve is $m_1$, and the slope of the orthogonal curve is $m_2$, then $m_1 m_2 = -1$.

**Method to Find Orthogonal Trajectories**
Given a one-parameter family of curves $G(x,y,c)=0$:
1.  **Form the Differential Equation of the Given Family**:
    *   Differentiate $G(x,y,c)=0$ with respect to $x$ to get an equation involving $x, y, y'$, and $c$.
    *   Eliminate the parameter $c$ from $G(x,y,c)=0$ and its derivative to obtain the differential equation of the family: $y' = f(x,y)$.
2.  **Form the Differential Equation of the Orthogonal Trajectories**:
    *   The slope of an orthogonal trajectory is the negative reciprocal of the slope of the original family.
    *   Replace $y'$ in $y' = f(x,y)$ with $-\frac{1}{y'}$ (or $\frac{dy}{dx}$ with $-\frac{dx}{dy}$).
    *   This yields the differential equation for the orthogonal trajectories: $y' = -\frac{1}{f(x,y)}$.
3.  **Solve the New Differential Equation**:
    *   Solve the differential equation $y' = -\frac{1}{f(x,y)}$ to find the family of orthogonal trajectories.

## Key Formulas

*   **Standard Form of Linear 1st Order ODE**: $y' + p(x)y = r(x)$
*   **Integrating Factor**: $\mu(x) = e^{\int p(x)dx}$
*   **General Solution of Linear 1st Order ODE**: $y = \frac{1}{\mu(x)} \left[ \int \mu(x)r(x)dx + C \right]$
*   **Bernoulli Equation**: $y' + Q(x)y = R(x)y^\alpha$
*   **Bernoulli Transformation**: $u = y^{1-\alpha}$
*   **Linear Form of Bernoulli Equation**: $u' + (1-\alpha)Q(x)u = (1-\alpha)R(x)$
*   **Existence Condition**: $f(x,y)$ is continuous and bounded in a rectangle $D$.
*   **Uniqueness Condition**: $f(x,y)$ and $\frac{\partial f}{\partial y}$ are continuous and bounded (or $f(x,y)$ satisfies a Lipschitz condition) in a rectangle $D$.
*   **Orthogonal Trajectory Slope Relation**: If original family has $y' = f(x,y)$, orthogonal trajectories have $y' = -\frac{1}{f(x,y)}$.

## Quick Summary

Lecture 3 introduced first-order linear ODEs, their standard form, and a direct solution for constant coefficients. The **integrating factor method** was detailed for general linear ODEs, deriving the integrating factor $\mu(x) = e^{\int p(x)dx}$ and the general solution. The **Bernoulli equation**, a non-linear first-order ODE, was then presented with a transformation ($u = y^{1-\alpha}$) to convert it into a solvable linear ODE. The concepts of **existence and uniqueness** for solutions to initial value problems were explored through theorems, stating conditions on $f(x,y)$ and $\frac{\partial f}{\partial y}$ in a rectangular domain around $(x_0, y_0)$. For linear IVPs, the continuity of $a(x)$ and $b(x)$ guarantees a unique solution. Finally, the lecture defined **orthogonal trajectories** and provided a step-by-step method to find them by deriving the differential equation for the given family, then replacing $y'$ with its negative reciprocal to find the ODE for the orthogonal trajectories.