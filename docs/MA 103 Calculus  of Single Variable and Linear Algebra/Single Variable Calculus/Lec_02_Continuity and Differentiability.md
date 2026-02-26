---
title: |
  Continuity and Differentiability
lecture_number: 2
lecture_name: |
  Continuity and Differentiability
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 2
sidebar_position: 2
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Continuity, Differentiability, Theorems
  2023-10-27
tags:
  - Math
  - Calculus
  - Continuity
  - Differentiability
  - Theorems
summary: |
  This lecture introduces the core concepts of continuity and differentiability of functions, covering their definitions, key properties, and fundamental theorems like the Intermediate Value Theorem, Bolzano's Theorem, and Rolle's Theorem. It also details various differentiation rules and the relationship between continuity and differentiability.
math: true
---

# Continuity and Differentiability

## Table of Contents
*   Continuity Definition
*   Properties of Continuous Functions (Theorem 9)
*   Continuity of Composite Functions
*   Sign-Preserving Property
*   Bolzano's Theorem (Intermediate Value Theorem for Roots)
*   The Intermediate Value Theorem for Continuous Functions (Theorem 11)
*   Boundedness Theorem for Continuous Functions
*   Differentiability Definition
*   One-Sided Derivatives
*   Differentiation Rules
*   Higher-Order Derivatives
*   Velocity, Speed, and Acceleration
*   The Chain Rule (Theorem 3.13)
*   Differentiability Implies Continuity
*   Rolle's Theorem (Theorem 3)

## Continuity Definition
**Definition:** A function $f$ is continuous at point $p$ if for every $\epsilon $>$ 0$, there exists a $\delta $>$ 0$ such that $|f(x) - f(p)| $<$ \epsilon$ whenever $|x - p| $<$ \delta$.
*   Every polynomial $p(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$ is continuous for all $x \in \mathbb{R}$, for any $n \in \mathbb{N}$.

## Properties of Continuous Functions (Theorem 9)
If functions $f$ and $g$ are continuous at $x=c$, then the following combinations are also continuous at $x=c$:
*   **Sums:** $f+g$
*   **Differences:** $f-g$
*   **Products:** $f \cdot g$
*   **Constant Multiples:** $k \cdot f$ for any number $k$.
*   **Quotients:** $f/g$, provided $g(c) \neq 0$.
*   **Powers:** $f^{r/s}$, provided it is defined on an open interval containing $c$, where $r$ and $s$ are integers.

## Continuity of Composite Functions
**Theorem:** If $g$ is continuous at $b$ and $\lim_{x \to c} f(x) = b$, then $\lim_{x \to c} g(f(x)) = g(b) = g(\lim_{x \to c} f(x))$.

## Sign-Preserving Property
**Theorem:** Let $f$ be continuous at $c$ and suppose $f(c) \neq 0$. Then there is an interval $(c-\delta, c+\delta)$ about $c$ in which $f$ has the same sign as $f(c)$.

## Bolzano's Theorem (Intermediate Value Theorem for Roots)
**Theorem:** Let $f$ be continuous at each point of a closed interval $[a,b]$ and assume that $f(a)$ and $f(b)$ have opposite signs. Then there is at least one $c$ in the open interval $(a,b)$ such that $f(c) = 0$.

## The Intermediate Value Theorem for Continuous Functions (Theorem 11)
**Theorem:** A function $y = f(x)$ that is continuous on a closed interval $[a,b]$ takes on every value between $f(a)$ and $f(b)$. If $y_0$ is any value between $f(a)$ and $f(b)$, then $y_0 = f(c)$ for some $c \in [a,b]$.

## Boundedness Theorem for Continuous Functions
**Theorem:** Let $f$ be a continuous function on a closed interval $[a,b]$. Then $f$ is bounded on $[a,b]$. That is, there is a number $C $>$ 0$ such that $|f(x)| \leq C$ for all $x \in [a,b]$.

## Differentiability Definition
*   **Average Rate of Change:** For a function $f$ on $[a, a+h]$, $m_{sec} = \frac{f(a+h) - f(a)}{h}$.
*   **Instantaneous Rate of Change (Derivative):** The slope of the tangent line at $(a, f(a))$, $m_{tan} = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$, provided this limit exists.
*   **Derivative at a Point:** $f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$ or $f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$. If $f'(a)$ exists, $f$ is differentiable at $a$.
*   **The Derivative as a Function:** $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$. If $f'(x)$ exists, $f$ is differentiable at $x$. If $f$ is differentiable at every point of an open interval $I$, $f$ is differentiable on $I$.

## One-Sided Derivatives
*   **Left-hand derivative at $x_0$:** $\lim_{x \to x_0^-} \frac{f(x) - f(x_0)}{x - x_0}$
*   **Right-hand derivative at $x_0$:** $\lim_{x \to x_0^+} \frac{f(x) - f(x_0)}{x - x_0}$

## Differentiation Rules
*   **Constant Rule (Theorem 3.2):** $\frac{d}{dx}(c) = 0$.
*   **Power Rule (Theorem 3.3):** $\frac{d}{dx}(x^n) = nx^{n-1}$ for $n$ a nonnegative integer.
*   **Constant Multiple Rule (Theorem 3.4):** $\frac{d}{dx}(cf(x)) = cf'(x)$.
*   **Sum Rule (Theorem 3.5):** $\frac{d}{dx}(f(x)+g(x)) = f'(x)+g'(x)$.
*   **Derivative of $e^x$ (Theorem 3.6):** $\frac{d}{dx}(e^x) = e^x$.
*   **Product Rule (Theorem 3.7):** $\frac{d}{dx}(f(x)g(x)) = f'(x)g(x) + f(x)g'(x)$.
*   **Quotient Rule (Theorem 3.8):** $\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right) = \frac{g(x)f'(x) - f(x)g'(x)}{(g(x))^2}$, provided $g(x) \neq 0$.
*   **Power Rule (General Form) (Theorem 3.9):** $\frac{d}{dx}(x^n) = nx^{n-1}$ for any real number $n$.
*   **Derivatives of Trigonometric Functions (Theorem 3.12):**
    *   $\frac{d}{dx}(\sin x) = \cos x$
    *   $\frac{d}{dx}(\cos x) = -\sin x$
    *   $\frac{d}{dx}(\tan x) = \sec^2 x$
    *   $\frac{d}{dx}(\cot x) = -\csc^2 x$
    *   $\frac{d}{dx}(\sec x) = \sec x \tan x$
    *   $\frac{d}{dx}(\csc x) = -\csc x \cot x$

## Higher-Order Derivatives
*   **Second Derivative:** $f''(x) = \frac{d}{dx}(f'(x))$.
*   **$n^{th}$ Derivative:** $f^{(n)}(x) = \frac{d}{dx}(f^{(n-1)}(x))$ for integers $n \geq 1$.

## Velocity, Speed, and Acceleration
Given position $s = f(t)$:
*   **Velocity:** $v(t) = \frac{ds}{dt} = f'(t)$.
*   **Speed:** $|v(t)| = |f'(t)|$.
*   **Acceleration:** $a(t) = \frac{dv}{dt} = \frac{d^2s}{dt^2} = f''(t)$.

## The Chain Rule (Theorem 3.13)
If $y = f(u)$ is differentiable at $u=g(x)$ and $u=g(x)$ is differentiable at $x$, then the composite function $y=f(g(x))$ is differentiable at $x$, and its derivative is:
*   $\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}$
*   $\frac{d}{dx}(f(g(x))) = f'(g(x)) \cdot g'(x)$

## Differentiability Implies Continuity
**Theorem:** If a function $f$ has a derivative at $x=c$, then $f$ is continuous at $x=c$. (The converse is not true; continuity does not imply differentiability, e.g., $f(x)=|x|$ at $x=0$).

## Rolle's Theorem (Theorem 3)
**Theorem:** Suppose that $y = f(x)$ is continuous at every point of the closed interval $[a,b]$ and differentiable at every point of its interior $(a,b)$. If $f(a) = f(b)$, then there is at least one number $c$ in $(a,b)$ at which $f'(c) = 0$.

## Key Formulas
*   **Continuity Definition:** $|f(x) - f(p)| $<$ \epsilon$ whenever $|x - p| $<$ \delta$
*   **Derivative at a Point:** $f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$
*   **Derivative as a Function:** $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$
*   **Constant Rule:** $\frac{d}{dx}(c) = 0$
*   **Power Rule:** $\frac{d}{dx}(x^n) = nx^{n-1}$
*   **Constant Multiple Rule:** $\frac{d}{dx}(cf(x)) = cf'(x)$
*   **Sum Rule:** $\frac{d}{dx}(f(x)+g(x)) = f'(x)+g'(x)$
*   **Derivative of $e^x$:** $\frac{d}{dx}(e^x) = e^x$
*   **Product Rule:** $\frac{d}{dx}(f(x)g(x)) = f'(x)g(x) + f(x)g'(x)$
*   **Quotient Rule:** $\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right) = \frac{g(x)f'(x) - f(x)g'(x)}{(g(x))^2}$
*   **Chain Rule:** $\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}$ or $\frac{d}{dx}(f(g(x))) = f'(g(x)) \cdot g'(x)$
*   **Velocity:** $v(t) = f'(t)$
*   **Acceleration:** $a(t) = f''(t)$

## Quick Summary
This lecture covered the fundamental definitions of continuity (epsilon-delta) and differentiability (limit definitions), establishing the relationship where differentiability implies continuity. Key theorems such as the Intermediate Value Theorem (including Bolzano's Theorem) and Rolle's Theorem were introduced, providing existence guarantees for function values or derivatives under specific conditions. Essential differentiation rules for sums, products, quotients, constants, powers, and trigonometric functions were detailed, along with the powerful Chain Rule for composite functions and the concept of higher-order derivatives.