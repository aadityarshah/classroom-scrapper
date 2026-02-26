---
title: |
  Gaussian Elimination and Solution Spaces
lecture_number: 1
lecture_name: |
  Gaussian Elimination and Solution Spaces
category: |
  Linear Algebra
sidebar_label: |
  Lecture 1
sidebar_position: 1
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Linear Algebra
  2025-08-18
tags:
  - Math
  - Linear Algebra
  - Gaussian Elimination
  - Systems of Equations
  - Solution Spaces
summary: |
  Introduces systems of linear equations, matrix notation, elementary row operations, and the structure of solution spaces, distinguishing between affine and vector spaces.
math: true
---

# Gaussian Elimination and Solution Spaces

## Table of Contents
* [Systems of Linear Equations](#systems-of-linear-equations)
* [Matrix Notation](#matrix-notation)
* [Elementary Row Operations](#elementary-row-operations)
* [The Solution Space of a System](#the-solution-space-of-a-system)

## Systems of Linear Equations
A system of $m$ linear equations in $n$ unknowns $x_1, \dots, x_n$ is expressed as:
$$
\begin{cases}
a_{11} x_1 + \dots + a_{1n} x_n = b_1 \\
a_{21} x_1 + \dots + a_{2n} x_n = b_2 \\
\quad \vdots \\
a_{m1} x_1 + \dots + a_{mn} x_n = b_m
\end{cases}
$$
Here, $a_{ij}$ are the **coefficients** and $b_i$ are the **constants**, all real numbers. A linear equation implies its solution set has an affine space structure.

## Matrix Notation
A system of linear equations (E) can be concisely represented in matrix form as $A \mathbf{x} = \mathbf{b}$.
*   $A$ is the **coefficient matrix**: An $m \times n$ matrix where $A = [a_{ij}]$.
*   $\mathbf{x}$ is the **matrix of unknowns/variables**: An $n \times 1$ column vector containing $(x_1, \dots, x_n)^T$.
*   $\mathbf{b}$ is the **matrix of constants**: An $m \times 1$ column vector containing $(b_1, \dots, b_m)^T$.
A system is **homogeneous** if $\mathbf{b} = \mathbf{0}$.

## Elementary Row Operations
These operations are fundamental for transforming matrices, particularly in Gaussian elimination, to find solutions or simplify systems.
1.  **Interchanging two rows:** $R_i \leftrightarrow R_j$.
2.  **Multiplying a row by a non-zero real number:** $R_i \rightarrow \alpha R_i$, where $\alpha \in \mathbb{R}$ and $\alpha \neq 0$.
3.  **Adding a multiple of one row to another row:** $R_i \rightarrow R_i + \beta R_j$, where $\beta \in \mathbb{R}$.
These operations reveal linear dependencies among rows, which can lead to zero rows in the row-reduced form of the matrix.

## The Solution Space of a System
A **solution** to a system (E) is an $n$-tuple $\alpha = (\alpha_1, \dots, \alpha_n) \in \mathbb{R}^n$ that satisfies all equations in (E) when $x_i = \alpha_i$.
*   $S_E$: Denotes the set of all solutions to the system (E).
*   $S_{E^0}$: Denotes the set of all solutions to the corresponding homogeneous system $E^0$ ($A\mathbf{x} = \mathbf{0}$).
**Theorem:** If $\alpha_p$ is any particular solution to a non-homogeneous system (E), then the entire solution set $S_E$ is given by $S_E = S_{E^0} + \alpha_p$.
$S_{E^0}$ possesses a **vector space** structure, while $S_E$ (for a non-homogeneous system) is an **affine space**.

## Key Formulas
*   **System of Linear Equations (Matrix Form):** $A \mathbf{x} = \mathbf{b}$
*   **Elementary Row Operations:**
    *   $R_i \leftrightarrow R_j$
    *   $R_i \rightarrow \alpha R_i$, $\alpha \neq 0$
    *   $R_i \rightarrow R_i + \beta R_j$
*   **Solution Set Relationship:** $S_E = S_{E^0} + \alpha_p$

## Quick Summary
Gaussian Elimination is a method for solving systems of linear equations, which can be represented compactly in matrix form $A \mathbf{x} = \mathbf{b}$. The process relies on elementary row operations to transform the matrix. The set of all solutions $S_E$ to a non-homogeneous system forms an affine space, directly related to the vector space of solutions $S_{E^0}$ for its corresponding homogeneous system by adding a particular solution $\alpha_p$.