---
title: |
  Mean Value Theorem and Monotonic Functions
lecture_number: 3
lecture_name: |
  Mean Value Theorem and Monotonic Functions
category: |
  Single Variable Calculus
sidebar_label: |
  Lecture 3
sidebar_position: 3
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Calculus
date: |
  2023-10-27
tags:
  - Math
  - Calculus
  - Mean Value Theorem
  - Monotonic Functions
  - Derivatives
summary: |
  This lecture introduces the Mean Value Theorem (MVT) and its corollaries, essential for understanding the relationship between a function's derivative and its behavior. It also covers the definitions of increasing, decreasing, and monotonic functions, culminating in the First Derivative Test for identifying local extrema.
math: true
---

# Mean Value Theorem and Monotonic Functions

## Table of Contents
- The Mean Value Theorem
- Corollaries of the Mean Value Theorem
- Monotonic Functions
- First Derivative Test for Local Extrema
- Key Formulas
- Quick Summary

## The Mean Value Theorem

**Definition: The Mean Value Theorem (MVT)**
If $y = f(x)$ is continuous on a closed interval $[a, b]$ and differentiable on the open interval $(a, b)$, then there exists at least one point $c$ in $(a, b)$ such that:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$
This means the instantaneous rate of change at $c$ is equal to the average rate of change over the interval $[a, b]$. Geometrically, there is a tangent line at $c$ that is parallel to the secant line connecting $(a, f(a))$ and $(b, f(b))$.

**Remark on MVT Hypotheses:**
Continuity at the endpoints of the interval is essential for the Mean Value Theorem, while differentiability is only required for the interval's interior $(a, b)$, not necessarily at the endpoints $a$ and $b$.

## Corollaries of the Mean Value Theorem

**Corollary 1: Functions with Zero Derivatives Are Constant**
If $f'(x) = 0$ at each point $x$ of an open interval $(a, b)$, then $f(x) = C$ for all $x \in (a, b)$, where $C$ is a constant.

**Corollary 2: Functions with the Same Derivative Differ by a Constant**
If $f'(x) = g'(x)$ at each point $x$ in an open interval $(a, b)$, then there exists a constant $C$ such that $f(x) = g(x) + C$ for all $x \in (a, b)$. This implies that the difference function $f - g$ is constant on $(a, b)$.

## Monotonic Functions

**Definitions: Increasing, Decreasing, and Monotonic Functions**
Let $f$ be a function defined on an interval $I$, and let $x_1, x_2$ be any two points in $I$:
*   **Increasing Function:** If $f(x_1) $<$ f(x_2)$ whenever $x_1 $<$ x_2$, then $f$ is said to be increasing on $I$.
*   **Decreasing Function:** If $f(x_2) $<$ f(x_1)$ whenever $x_1 $<$ x_2$, then $f$ is said to be decreasing on $I$.
*   **Monotonic Function:** A function that is either increasing or decreasing on an interval $I$ is called monotonic on $I$.

## First Derivative Test for Local Extrema

**Test for Local Extrema**
Suppose $c$ is a critical point of a continuous function $f$, and $f$ is differentiable at every point in some interval containing $c$ (except possibly at $c$ itself). As $x$ moves across $c$ from left to right:
1.  If $f'(x)$ changes from negative to positive at $c$, then $f$ has a **local minimum** at $c$.
2.  If $f'(x)$ changes from positive to negative at $c$, then $f$ has a **local maximum** at $c$.
3.  If $f'(x)$ does not change sign at $c$ (i.e., $f'(x)$ is positive on both sides of $c$ or negative on both sides), then $f$ has **no local extremum** at $c$.

## Key Formulas
*   **Mean Value Theorem:** $f'(c) = \frac{f(b) - f(a)}{b - a}$

## Quick Summary
The Mean Value Theorem states that for a continuous and differentiable function on a closed interval, there exists at least one point where the instantaneous rate of change equals the overall average rate of change. Its corollaries demonstrate that functions with a zero derivative are constant, and functions with identical derivatives differ only by a constant. A function is defined as monotonic if it is either consistently increasing or consistently decreasing over an interval. The First Derivative Test uses the change in sign of the first derivative around critical points to precisely identify local maxima and minima.