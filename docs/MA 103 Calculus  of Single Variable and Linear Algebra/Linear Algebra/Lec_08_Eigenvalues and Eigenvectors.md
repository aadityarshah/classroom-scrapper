---
title: |
  Eigenvalues and Eigenvectors
lecture_number: 8
lecture_name: |
  Eigenvalues and Eigenvectors
category: |
  Linear Algebra
sidebar_label: |
  Lecture 8
sidebar_position: 8
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Uncategorized
  2025-12-09
tags:
  - Math
  - Linear Algebra
  - Eigenvalues
  - Eigenvectors
  - Characteristic Polynomial
summary: |
  This lecture introduces linear operators, their kernel and image, and the Rank-Nullity Theorem. It then defines eigenvalues and eigenvectors, connecting their calculation to the characteristic polynomial and characteristic equation of a linear operator.
math: true
---

# Eigenvalues and Eigenvectors

## Table of Contents
* [Linear Operators and Related Definitions](#linear-operators-and-related-definitions)
* [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
* [Characteristic Polynomial and Equation](#characteristic-polynomial-and-equation)
* [Calculating Eigenvalues and Eigenvectors](#calculating-eigenvalues-and-eigenvectors)
* [Key Formulas](#key-formulas)
* [Quick Summary](#quick-summary)

## Linear Operators and Related Definitions
A **linear operator** $T: V \to V$ is a linear transformation on a finite-dimensional vector space $V$ over a field $F$ (typically $\mathbb{R}$ or $\mathbb{C}$), satisfying $T(v+w)=T(v)+T(w)$ and $T(\lambda v)=\lambda T(v)$ for all $v, w \in V, \lambda \in F$. The **kernel** (or null space) of $T$ is $\text{Ker}(T) = \{v \in V \mid T(v)=0\}$, and the **image** (or range) of $T$ is $\text{Im}(T) = \{T(v) \mid v \in V\}$. The **Rank-Nullity Theorem** states that for a finite-dimensional $V$, $\text{dim}(\text{Ker}(T)) + \text{dim}(\text{Im}(T)) = \text{dim}(V)$. Examples include the derivative operator, matrix transpose, zero operator, and identity operator.

## Eigenvalues and Eigenvectors
An element $\lambda \in F$ is an **eigenvalue** of a linear operator $T: V \to V$ if there exists a non-zero vector $v \in V$ such that $T(v) = \lambda v$. The vector $v$ is called an **eigenvector** corresponding to the eigenvalue $\lambda$. The set of all vectors $v$ satisfying $T(v) = \lambda v$ (including the zero vector) forms a subspace of $V$ called the **eigenspace** for $\lambda$, denoted $N_\lambda$. This is equivalent to finding $v \neq 0$ such that $(T-\lambda I)v = 0$, meaning $N_\lambda = \text{Ker}(T - \lambda I)$.

## Characteristic Polynomial and Equation
For a linear operator $T$ on an $n$-dimensional vector space $V$, choosing a basis $B$ allows $T$ to be represented by a matrix $[T]_B$. Finding eigenvalues and eigenvectors involves finding non-trivial solutions to $([T]_B - \lambda I)v = 0$. Such non-trivial solutions exist if and only if the matrix $[T]_B - \lambda I$ is singular, which means its rank is less than $n$. This is equivalent to $\text{det}([T]_B - \lambda I) = 0$. The expression $\text{det}([T]_B - \lambda I)$ is a polynomial in $\lambda$, known as the **characteristic polynomial** of $T$, denoted $\chi_T(\lambda)$. The equation $\chi_T(\lambda) = 0$ is called the **characteristic equation**. The roots of the characteristic equation are the eigenvalues of $T$, and the degree of $\chi_T(\lambda)$ is $n = \text{dim}(V)$, implying there are at most $n$ eigenvalues (counted with multiplicity).

## Calculating Eigenvalues and Eigenvectors
To find the eigenvalues of a linear operator $T$, one constructs its matrix representation $[T]_B$ with respect to a chosen basis $B$. Then, the eigenvalues $\lambda$ are found by solving the characteristic equation $\text{det}([T]_B - \lambda I) = 0$. Once an eigenvalue $\lambda$ is determined, its corresponding eigenvectors are found by solving the homogeneous linear system $([T]_B - \lambda I)v = 0$ for non-zero vectors $v$. The solutions form the eigenspace $N_\lambda$.

## Key Formulas
*   **Rank-Nullity Theorem**: $\text{dim}(\text{Ker}(T)) + \text{dim}(\text{Im}(T)) = \text{dim}(V)$
*   **Eigenvalue/Eigenvector Definition**: $T(v) = \lambda v$ (for $v \neq 0$)
*   **Eigenspace**: $N_\lambda = \{v \in V \mid T(v) = \lambda v\} = \text{Ker}(T - \lambda I)$
*   **Characteristic Equation**: $\text{det}([T]_B - \lambda I) = 0$

## Quick Summary
Linear operators map a vector space to itself. Their properties are described by the kernel (vectors mapped to zero) and image (range of the operator), linked by the Rank-Nullity Theorem. Eigenvalues are special scalars $\lambda$ that, when applied to a non-zero eigenvector $v$, yield the same result as the operator $T(v) = \lambda v$. These are found by solving the characteristic equation, $\text{det}([T]_B - \lambda I) = 0$, where $[T]_B$ is the matrix representation of $T$. For each eigenvalue, the corresponding eigenvectors form a subspace called the eigenspace.