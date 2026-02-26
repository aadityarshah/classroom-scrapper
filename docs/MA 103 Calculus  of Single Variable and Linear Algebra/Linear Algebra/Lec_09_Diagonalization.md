---
title: |
  MA 103 Linear Algebra: Diagonalization
lecture_number: 9
lecture_name: |
  Diagonalization
category: |
  Linear Algebra
sidebar_label: |
  Lecture 9
sidebar_position: 9
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Diagonalization
date: |
  2025-09-17
tags:
  - Linear Algebra
  - Diagonalization
  - Eigenvalues
  - Eigenvectors
  - Multiplicity
summary: |
  This lecture introduces the concept of diagonalization for linear operators, defining diagonalizable operators and eigenbases. It covers the characteristic polynomial, eigenvalues, geometric and algebraic multiplicities, and the critical condition for a matrix or operator to be diagonalizable: geometric multiplicity must equal algebraic multiplicity for all eigenvalues.
math: true
---

# MA 103 Linear Algebra: Diagonalization

## Table of Contents
* [Diagonalization Definition](#diagonalization-definition)
* [Characteristic Polynomial and Eigenvalues](#characteristic-polynomial-and-eigenvalues)
* [Geometric Multiplicity](#geometric-multiplicity)
* [Algebraic Multiplicity](#algebraic-multiplicity)
* [Criteria for Diagonalization](#criteria-for-diagonalization)
* [Example: Non-Diagonalizable Matrix](#example-non-diagonalizable-matrix)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## Diagonalization Definition

A linear operator $T: V \to V$ on a finite-dimensional vector space $V$ (dimension $n$) over a field $F$ is **diagonalizable** if there exists a basis $\mathcal{B} = \{v_1, \ldots, v_n\}$ of $V$ such that each $v_i$ is an eigenvector of $T$ for some eigenvalue $\lambda_i \in F$. This basis is called an **eigenbasis**. When such a basis exists, the matrix representation of $T$ with respect to this eigenbasis is a diagonal matrix with entries $[\lambda_1, \lambda_2, \ldots, \lambda_n]$ along the main diagonal.

## Characteristic Polynomial and Eigenvalues

For a linear operator $T$ with matrix $A$ (relative to some basis), its **characteristic polynomial** is $\chi(\lambda) = \det(A - \lambda I)$. The roots of the characteristic equation $\chi(\lambda) = 0$ are the **eigenvalues** of $T$. A theorem states that if $T$ has $n = \dim(V)$ distinct eigenvalues, then $T$ is diagonalizable. The converse is not necessarily true; for example, the identity operator is diagonalizable but may have only one distinct eigenvalue.

## Geometric Multiplicity

For an eigenvalue $\lambda \in F$, the **eigenspace** $N_\lambda = \ker(T - \lambda I) = \{v \in V \mid T(v) = \lambda v\}$ is a subspace of $V$ comprising all eigenvectors corresponding to $\lambda$ (and the zero vector). The **geometric multiplicity** of $\lambda$, denoted $g_\lambda$, is defined as the dimension of its eigenspace: $g_\lambda = \dim(N_\lambda)$. It signifies the maximum number of linearly independent eigenvectors associated with $\lambda$.

## Algebraic Multiplicity

Assuming the characteristic polynomial $\chi(\lambda)$ has all its roots in the field $F$, it can be factored as $\chi(\lambda) = (\lambda - \lambda_1)^{e_1} \cdots (\lambda - \lambda_r)^{e_r}$, where $\lambda_1, \ldots, \lambda_r$ are the distinct eigenvalues. The exponent $e_j \geq 1$ is called the **algebraic multiplicity** of the eigenvalue $\lambda_j$. The sum of all algebraic multiplicities equals the dimension of the vector space: $\sum_{j=1}^r e_j = n = \dim(V)$.

## Criteria for Diagonalization

For any eigenvalue $\lambda_i$, its geometric multiplicity is always less than or equal to its algebraic multiplicity: $g_i \leq e_i$. A linear operator $T$ (or its matrix $A$) is **diagonalizable if and only if** the geometric multiplicity equals the algebraic multiplicity for every eigenvalue: $g_i = e_i$ for all $i = 1, \ldots, r$.

## Example: Non-Diagonalizable Matrix

Consider the matrix $A = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 2 \end{pmatrix}$.
The characteristic polynomial is $\chi(\lambda) = \det(A - \lambda I) = (1-\lambda)^2(2-\lambda) = 0$.
The eigenvalues are $\lambda_1 = 1$ with algebraic multiplicity $e_1 = 2$, and $\lambda_2 = 2$ with algebraic multiplicity $e_2 = 1$.
For $\lambda_2 = 2$, its geometric multiplicity $g_2 = 1$, which equals its algebraic multiplicity $e_2$.
For $\lambda_1 = 1$, we find the eigenspace $N_1 = \ker(A - I)$. Solving $(A-I)v=0$ for $v=(v_1, v_2, v_3)$ yields $v_2=0$ and $v_3=-v_1$.
Thus, $N_1 = \{(t, 0, -t) \mid t \in \mathbb{R}\}$, and its dimension, the geometric multiplicity $g_1 = \dim(N_1) = 1$.
Since $g_1 = 1 $<$ e_1 = 2$, the matrix $A$ is **not diagonalizable**.
(Exercise: Prove that eigenvectors corresponding to distinct eigenvalues are linearly independent.)

## Key Formulas

*   **Characteristic Polynomial**: $\chi(\lambda) = \det(A - \lambda I)$
*   **Eigenspace for $\lambda$**: $N_\lambda = \ker(T - \lambda I) = \{v \in V \mid T(v) = \lambda v\}$
*   **Geometric Multiplicity**: $g_\lambda = \dim(N_\lambda)$
*   **Algebraic Multiplicity**: $e_\lambda$, the exponent of $(\lambda - \lambda_i)$ in $\chi(\lambda)$
*   **Diagonalization Condition**: $T$ is diagonalizable $\iff g_\lambda = e_\lambda$ for all eigenvalues $\lambda$.

## Quick Summary

Diagonalization allows representing a linear operator using a simple diagonal matrix when an eigenbasis exists. This is possible if and only if the geometric multiplicity of each eigenvalue equals its algebraic multiplicity. While having $n$ distinct eigenvalues for an $n$-dimensional space guarantees diagonalizability, it is not a necessary condition. The eigenspace's dimension gives the geometric multiplicity, while the exponent in the characteristic polynomial gives the algebraic multiplicity.