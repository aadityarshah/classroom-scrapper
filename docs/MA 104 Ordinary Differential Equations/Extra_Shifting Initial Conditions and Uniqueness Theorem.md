---
title: |
  Extra Material: Shifting Initial Conditions and Uniqueness
lecture_number: 999
lecture_name: |
  Shifting Initial Conditions and Uniqueness Theorem
category: |
  
sidebar_label: |
  Extra: Shifting IVP & Uniqueness
sidebar_position: 999
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Initial Value Problems, Uniqueness
  2023-10-27
tags: ['ODE', 'Initial Value Problem', 'Uniqueness Theorem', 'Transformation']
summary: |
  Covers the technique of shifting initial conditions to the origin for easier IVP solutions and reviews the Uniqueness Theorem for ODEs.
math: true
---

# Extra Material: Shifting Initial Conditions and Uniqueness

## Table of Contents
* Shifting Initial Conditions to the Origin
* Uniqueness Theorem for Initial Value Problems
* Key Formulas
* Quick Summary

## Shifting Initial Conditions to the Origin

### Definition: Original Initial Value Problem (IVP)
An IVP is given by $dy/dx = f(x,y)$ with an initial condition $y(x_0)=y_0$.

### Definition: Transformation
To shift the initial condition $(x_0, y_0)$ to the origin $(0,0)$, define new variables:
*   $\tilde{x} = x - x_0$
*   $\tilde{y} = y - y_0$

### Derivative Relationship
The derivative with respect to the new variables relates to the original derivative as:
$$ \frac{d\tilde{y}}{d\tilde{x}} = \frac{dy}{dx} $$

### Theorem: Transformed IVP
The original IVP can be rewritten in terms of the transformed variables as:
$$ \frac{d\tilde{y}}{d\tilde{x}} = f(\tilde{x}+x_0, \tilde{y}+y_0) \quad \text{with} \quad \tilde{y}(0)=0 $$

### Theorem: Solution Relationship
If $\tilde{y}=\phi(\tilde{x})$ is a solution to the transformed IVP, then the solution to the original IVP is $y=\phi(x-x_0)+y_0$.

## Uniqueness Theorem for Initial Value Problems

### Theorem: Uniqueness Theorem
Consider the IVP: $y'=f(x,y)$ with $y(x_0)=y_0$.
*   **Conditions:**
    *   Let $f(x,y)$ and its partial derivative $\partial f/\partial y$ be continuous in a rectangular domain $D = \{(x,y) : |x-x_0|<a, |y-y_0|<b\}$.
    *   Assume $f$ and $\partial f/\partial y$ are bounded on $D$, such that $|f(x,y)| \leq K$ and $|\partial f/\partial y| \leq M$ for all $(x,y) \in D$.
*   **Conclusion:** The IVP has at most one solution $y(x)$ for $x$ such that $|x-x_0| $<$ \alpha$, where $\alpha = \min\{a, b/K\}$.

### Remark: Global Uniqueness from Local Solutions
If $f(x,y)$ and $\partial f/\partial y$ are continuous for all $(x,y) \in \mathbb{R}^2$, and bounded on any finite rectangular domain $D_L = (x_0-L, x_0+L) \times (y_0-b, y_0+b)$ for any real number $L $>$ 0$, then a unique global solution $y(x)$ for all $x \in \mathbb{R}$ can be constructed by patching together local unique solutions defined on increasingly larger intervals $(x_0-n, x_0+n)$ for $n \in \mathbb{N}$.

## Key Formulas
*   **Variable Transformation:**
    *   $\tilde{x} = x - x_0$
    *   $\tilde{y} = y - y_0$
*   **Transformed IVP:**
    *   $d\tilde{y}/d\tilde{x} = f(\tilde{x}+x_0, \tilde{y}+y_0)$
    *   $\tilde{y}(0)=0$
*   **Solution Conversion:**
    *   $y(x) = \phi(x-x_0)+y_0$ (where $\tilde{y}=\phi(\tilde{x})$ is the solution to the transformed IVP)
*   **Uniqueness Theorem Conditions (Boundedness):**
    *   $|f(x,y)| \leq K$
    *   $|\partial f/\partial y| \leq M$
    *   Interval of uniqueness: $|x-x_0| $<$ \min\{a, b/K\}$

## Quick Summary
The technique of shifting initial conditions simplifies solving an IVP by transforming it into an equivalent problem with the initial condition at the origin. The Uniqueness Theorem establishes conditions (continuity and boundedness of $f$ and $\partial f/\partial y$) under which an IVP is guaranteed to have at most one solution locally, and these local solutions can sometimes be extended to prove global uniqueness.