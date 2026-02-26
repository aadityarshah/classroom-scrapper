---
title: |
  Homogeneous Systems, Rank, and Linear Transformations
lecture_number: 5
lecture_name: |
  Homogeneous Systems, Rank, and Linear Transformations
category: |
  Linear Algebra
sidebar_label: |
  Lecture 5
sidebar_position: 5
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Linear Algebra
  2025-08-29
tags:
  - Linear Algebra
  - Systems of Equations
  - Rank
  - Homogeneous Systems
  - Linear Transformations
  - Matrix Representation
summary: |
  This lecture establishes conditions for the existence of non-trivial solutions to homogeneous linear systems based on matrix rank and linear dependence of column vectors. It defines the consistency condition for general linear systems ($Ax=b$) using augmented matrix rank, describes the structure of their solution sets, and introduces linear transformations (operators) with their defining properties and matrix representations.
math: true
---

# Homogeneous Systems, Rank, and Linear Transformations

## Table of Contents
* [Homogeneous Systems and Rank](#homogeneous-systems-and-rank)
* [Existence of Solutions for $Ax=b$](#existence-of-solutions-for-axb)
* [Structure of Solution Sets](#structure-of-solution-sets)
* [Linear Transformations (Operators)](#linear-transformations-operators)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## Homogeneous Systems and Rank

**Definition: System of Linear Equations**
A system $Ax=b$ involves a coefficient matrix $A$, a vector of unknowns $x$, and a constant vector $b$.

**Definition: Homogeneous System**
A linear system is **homogeneous** if $b=0$, i.e., $Ax=0$. This system always has the **zero solution** ($x=0$).

**Theorem: Non-Zero Solutions for Homogeneous Systems**
A homogeneous system $Ax=0$ has a non-zero solution if and only if:
1.  $\text{rank}(A) $<$ n$, where $n$ is the number of unknowns (columns of $A$).
2.  The column vectors of $A$ are linearly dependent.

**Definition: Rank of a Matrix**
The **rank** of a matrix $A$, denoted $\text{rank}(A)$, is defined as:
$$ \text{rank}(A) = \text{row-rank}(A) = \text{column-rank}(A) $$
The rank satisfies $\text{rank}(A) \leq \min\{m, n\}$, where $m$ is the number of rows and $n$ is the number of columns.

## Existence of Solutions for $Ax=b$

**Theorem: Consistency Condition (Rouché-Capelli / Rank Theorem)**
A system of linear equations $Ax=b$ has at least one solution if and only if the rank of the coefficient matrix $A$ is equal to the rank of the augmented matrix $(A|b)$:
$$ \text{rank}(A) = \text{rank}(A|b) $$
The augmented matrix $(A|b)$ is formed by appending the column vector $b$ to the matrix $A$.

## Structure of Solution Sets

The solution set for a consistent system $Ax=b$ can be expressed as the sum of a particular solution $x_p$ to $Ax=b$ and the general solution $S_0$ to the corresponding homogeneous system $Ax=0$:
$$ S = \{x \mid Ax=b\} = \{x_p + x_h \mid Ax_p=b, Ax_h=0 \} $$
The solution set $S_0 = \{x \mid Ax=0\}$ is a vector subspace of $\mathbb{R}^n$. A basis for $S_0$ consists of linearly independent vectors that span the null space of $A$, and its dimension is the nullity of $A$, given by $\text{nullity}(A) = n - \text{rank}(A)$.

## Linear Transformations (Operators)

**Definition: Linear Transformation**
A function $T: \mathbb{R}^n \to \mathbb{R}^m$ is called a **linear transformation** (or **linear operator**) if, for all vectors $x, y \in \mathbb{R}^n$ and all scalars $\lambda \in \mathbb{R}$, it satisfies the following two properties:
1.  **Additivity:** $T(x+y) = T(x) + T(y)$
2.  **Homogeneity:** $T(\lambda x) = \lambda T(x)$

**Properties of Linear Transformations**
*   $T(0) = 0$ (The zero vector in $\mathbb{R}^n$ maps to the zero vector in $\mathbb{R}^m$).
*   $T(-x) = -T(x)$.
*   Linear transformations map lines passing through the origin in $\mathbb{R}^n$ to lines passing through the origin in $\mathbb{R}^m$.

**Matrix Representation of a Linear Transformation**
Any linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ can be represented by an $m \times n$ matrix $A$. If $e_1, e_2, \ldots, e_n$ are the standard basis vectors for $\mathbb{R}^n$, then the matrix $A$ has its columns given by $T(e_1), T(e_2), \ldots, T(e_n)$. Thus, $T(x) = Ax$.

## Key Formulas

*   **Homogeneous System Non-Zero Solution Condition:** $Ax=0 \text{ has non-zero solution } \iff \text{rank}(A) $<$ n$.
*   **Consistency Condition for $Ax=b$:** $Ax=b \text{ has solution } \iff \text{rank}(A) = \text{rank}(A|b)$.
*   **Structure of Solution Set:** $S = \{ x_p + x_h \mid Ax_p=b, Ax_h=0 \}$, where $x_p$ is a particular solution and $x_h$ is a solution to the homogeneous system.
*   **Linear Transformation Properties:**
    *   $T(x+y) = T(x) + T(y)$
    *   $T(\lambda x) = \lambda T(x)$
*   **Matrix Representation:** For a linear $T: \mathbb{R}^n \to \mathbb{R}^m$, $T(x) = Ax$, where $A = [T(e_1) \ T(e_2) \ \dots \ T(e_n)]$.

## Quick Summary

Homogeneous systems $Ax=0$ always have the zero solution; non-zero solutions exist if $\text{rank}(A)$ is less than the number of unknowns ($n$), implying linearly dependent column vectors. For non-homogeneous systems $Ax=b$, a solution exists if and only if $\text{rank}(A) = \text{rank}(A|b)$. The general solution to $Ax=b$ is the sum of a particular solution and the general solution to $Ax=0$. Linear transformations $T: \mathbb{R}^n \to \mathbb{R}^m$ preserve vector addition and scalar multiplication, satisfy $T(0)=0$, and can always be represented by an $m \times n$ matrix whose columns are the images of the standard basis vectors.