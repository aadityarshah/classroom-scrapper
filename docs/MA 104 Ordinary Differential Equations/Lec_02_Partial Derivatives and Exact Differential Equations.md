---
title: |
  MA 104: Ordinary Differential Equations - Lecture 2 Notes
lecture_number: 2
lecture_name: |
  Partial Derivatives and Exact Differential Equations
category:
sidebar_label: |
  Lecture 2
sidebar_position: 2
course: |
  MA 104 Ordinary Differential Equations
topic: |
  Partial Derivatives, Chain Rule, Exact Equations, Integrating Factors
date: |
  January 09, 2026
tags: ['ODE', 'Differential Equations', 'Calculus', 'Partial Derivatives', 'Chain Rule', 'Exact Equations', 'Integrating Factors']
summary: |
  Concise lecture notes on partial derivatives, the chain rule for multivariable functions, definitions and theorems for exact differential equations, and methods for finding integrating factors.
math: true
---

# MA 104: Ordinary Differential Equations - Lecture 2 Notes

## Table of Contents
* Introduction to Partial Derivatives
* Formal Definition of Partial Derivatives
* Higher-Order Partial Derivatives and Mixed Derivatives
* Chain Rule for Multivariable Functions
* Geometric Meaning of Derivatives
* Total Differential
* Exact Differential Equations
* Integrating Factors
* Methods for Finding Integrating Factors
* Useful Exact Differential Forms

## Introduction to Partial Derivatives

**Definition: Directional Derivative**
Let $f: \mathbb{R}^2 \to \mathbb{R}$, $(a,b) \in \mathbb{R}^2$ and let $U := (u,v) \in \mathbb{R}^2$ be a unit vector, i.e., $||U|| = \sqrt{u^2+v^2} = 1$. The directional derivative of $f$ at $(a,b)$ in the direction $U$ is defined by (provided the limit exists):
$$D_{(a,b)}f(U) := \lim_{h \to 0} \frac{f((a,b)+h(u,v)) - f(a,b)}{h} = \lim_{h \to 0} \frac{f(a+hu, b+hv) - f(a,b)}{h}$$
In particular, $D_{(a,b)}f(e_1) = f_x(a,b)$ and $D_{(a,b)}f(e_2) = f_y(a,b)$.

## Formal Definition of Partial Derivatives

**Definition: Partial Derivative with Respect to x**
The partial derivative of $f(x,y)$ with respect to $x$ at the point $(x_0, y_0)$ is (provided the limit exists):
$$\frac{\partial f}{\partial x} \bigg|_{(x_0, y_0)} = \lim_{h \to 0} \frac{f(x_0+h, y_0) - f(x_0, y_0)}{h}$$

**Definition: Partial Derivative with Respect to y**
The partial derivative of $f(x,y)$ with respect to $y$ at the point $(x_0, y_0)$ is (provided the limit exists):
$$\frac{\partial f}{\partial y} \bigg|_{(x_0, y_0)} = \lim_{h \to 0} \frac{f(x_0, y_0+h) - f(x_0, y_0)}{h}$$

## Higher-Order Partial Derivatives and Mixed Derivatives

**Notation 1** | **Notation 2**
:---------------|:---------------
$\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial x^2}$ | $(f_x)_x = f_{xx}$
$\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial y^2}$ | $(f_y)_y = f_{yy}$
$\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial x \partial y}$ | $(f_y)_x = f_{yx}$
$\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial y \partial x}$ | $(f_x)_y = f_{xy}$

**Theorem: The Mixed Derivative Theorem (Clairaut's Theorem)**
If $f(x,y)$ and its partial derivatives $f_x, f_y, f_{xy}$, and $f_{yx}$ are defined throughout an open region containing a point $(a,b)$ and are all continuous at $(a,b)$, then:
$$f_{xy}(a,b) = f_{yx}(a,b)$$

## Chain Rule for Multivariable Functions

**Theorem: Chain Rule for Functions of One Independent Variable and Two Intermediate Variables**
If $z = f(x,y)$ is differentiable and $x$ and $y$ are differentiable functions of $t$, then $z$ is a differentiable function of $t$ and:
$$\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}$$

**Note:** If $x=t$, the formula simplifies to:
$$\frac{dz}{dt} = \frac{\partial z}{\partial x} + \frac{\partial z}{\partial y}\frac{dy}{dt}$$

## Geometric Meaning of Derivatives

The derivative $f'(a)$ represents the slope of the tangent line to the curve $y=f(x)$ at the point $(a, f(a))$.
$$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x-a}$$

## Total Differential

**Definition: Total Differential**
Let $F: \mathbb{R}^2 \to \mathbb{R}$ be a two-variable function that admits continuous first-order partial derivatives in a region $D$. The total differential, denoted by $dF$, is defined as:
$$dF = \frac{\partial F}{\partial x}dx + \frac{\partial F}{\partial y}dy$$
The total differential $dF$ signifies the change in the function $F(x,y)$ as a linear combination of changes in each variable.

## Exact Differential Equations

**Definition: Exact Differential Equation**
An ordinary differential equation of the form $M(x,y)dx + N(x,y)dy = 0$ is called an **exact differential equation** if there exists a function $u(x,y)$ such that its total differential $du$ is equal to $M(x,y)dx + N(x,y)dy$. That is, $du = Mdx + Ndy$.
This implies $\frac{\partial u}{\partial x} = M(x,y)$ and $\frac{\partial u}{\partial y} = N(x,y)$.
The solution to an exact ODE is given implicitly by $u(x,y) = c$, where $c$ is an arbitrary constant.

**Theorem: Condition for Exactness**
If $M(x,y)$, $N(x,y)$, $\frac{\partial M}{\partial y}$, and $\frac{\partial N}{\partial x}$ are continuous in a rectangular region $R = (a,b) \times (c,d)$, then the differential equation $M(x,y)dx + N(x,y)dy = 0$ is exact in $R$ if and only if:
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

## Integrating Factors

**Definition: Integrating Factor**
An integrating factor for the ordinary differential equation $M(x,y)dx + N(x,y)dy = 0$ is a function $\mu(x,y)$ such that when the original equation is multiplied by $\mu(x,y)$, the resulting equation $\mu(x,y)M(x,y)dx + \mu(x,y)N(x,y)dy = 0$ is exact.

The condition for exactness of $\mu M dx + \mu N dy = 0$ is:
$$\frac{\partial (\mu M)}{\partial y} = \frac{\partial (\mu N)}{\partial x}$$
Expanding this gives:
$$\mu \frac{\partial M}{\partial y} + M \frac{\partial \mu}{\partial y} = \mu \frac{\partial N}{\partial x} + N \frac{\partial \mu}{\partial x}$$
Rearranging the terms, we get:
$$\frac{1}{\mu} \left( N \frac{\partial \mu}{\partial x} - M \frac{\partial \mu}{\partial y} \right) = \frac{\partial M}{\partial y} - \frac{\partial N}{\partial x}$$
If the original ODE is exact, $\mu=1$ is an integrating factor. Integrating factors are not unique.

## Methods for Finding Integrating Factors

**Theorem: Integrating Factor Dependent on x Only**
If $\frac{1}{N} \left( \frac{\partial M}{\partial y} - \frac{\partial N}{\partial x} \right)$ is a function of $x$ alone, say $P(x)$, then an integrating factor is given by:
$$\mu(x) = e^{\int P(x)dx}$$

**Theorem: Integrating Factor Dependent on y Only**
If $\frac{1}{M} \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right)$ is a function of $y$ alone, say $Q(y)$, then an integrating factor is given by:
$$\mu(y) = e^{\int Q(y)dy}$$

## Useful Exact Differential Forms

Certain combinations of differentials are useful for converting non-exact ODEs into exact ones.
1. $d\left(\frac{y}{x}\right) = \frac{xdy - ydx}{x^2}$
2. $d\left(\frac{x}{y}\right) = \frac{ydx - xdy}{y^2}$
3. $d(xy) = xdy + ydx$
4. $d(x^2+y^2) = 2(xdx+ydy)$
5. $d\left(\arctan\left(\frac{y}{x}\right)\right) = \frac{xdy - ydx}{x^2+y^2}$
6. $d\left(\ln\left(\frac{y}{x}\right)\right) = \frac{xdy - ydx}{xy}$

## Key Formulas
* **Directional Derivative:** $D_{(a,b)}f(U) := \lim_{h \to 0} \frac{f(a+hu, b+hv) - f(a,b)}{h}$
* **Partial Derivative w.r.t. x:** $\frac{\partial f}{\partial x} \bigg|_{(x_0, y_0)} = \lim_{h \to 0} \frac{f(x_0+h, y_0) - f(x_0, y_0)}{h}$
* **Partial Derivative w.r.t. y:** $\frac{\partial f}{\partial y} \bigg|_{(x_0, y_0)} = \lim_{h \to 0} \frac{f(x_0, y_0+h) - f(x_0, y_0)}{h}$
* **Mixed Derivative Theorem:** $f_{xy}(a,b) = f_{yx}(a,b)$ (under continuity conditions)
* **Chain Rule for $z=f(x,y)$:** $\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}$
* **Total Differential:** $dF = \frac{\partial F}{\partial x}dx + \frac{\partial F}{\partial y}dy$
* **Exactness Condition for $Mdx+Ndy=0$:** $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
* **Integrating Factor $\mu(x)$ if $\frac{1}{N} \left( \frac{\partial M}{\partial y} - \frac{\partial N}{\partial x} \right) = P(x)$:** $\mu(x) = e^{\int P(x)dx}$
* **Integrating Factor $\mu(y)$ if $\frac{1}{M} \left( \frac{\partial N}{\partial x} - \frac{\partial M}{\partial y} \right) = Q(y)$:** $\mu(y) = e^{\int Q(y)dy}$

## Quick Summary
This lecture introduced partial derivatives, their formal definitions, and notations for higher-order derivatives, culminating in the Mixed Derivative Theorem. The Chain Rule for multivariable functions was presented. We then transitioned to Ordinary Differential Equations, defining exact differential equations and establishing the necessary and sufficient condition for exactness. Finally, the concept of integrating factors was introduced as a method to transform non-exact ODEs into exact ones, with specific formulas for integrating factors dependent on a single variable.