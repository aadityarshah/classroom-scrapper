---
title: |
  Gram-Schmidt Orthogonalization and Least Squares Approximation
lecture_number: 11
lecture_name: |
  Gram-Schmidt Orthogonalization and Least Squares Approximation
category: |
  Linear Algebra
sidebar_label: |
  Lecture 11
sidebar_position: 11
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Gram-Schmidt Orthogonalization, Orthogonal Complement, Least Square Approximation, Adjoint
  24/10/2025
tags:
  - Linear Algebra
  - Orthogonalization
  - Gram-Schmidt
  - Least Squares
  - Adjoint Operator
  - Inner Product Space
summary: |
  This lecture introduces the Gram-Schmidt orthogonalization process to construct an orthonormal basis, defines the orthogonal complement of a set, and details the method of Least Squares Approximation for finding the best linear fit to a data set, including the concept of an adjoint operator.
math: true
---

# Gram-Schmidt Orthogonalization and Least Squares Approximation

## Table of Contents
- Gram-Schmidt Orthogonalization
- Orthogonal Complement
- Least Square Approximation
- Adjoint Operator
- Key Formulas
- Quick Summary

## Gram-Schmidt Orthogonalization

The Gram-Schmidt (G-S) process is a method to obtain an orthonormal basis from any basis of a finite-dimensional Inner Product Space (IPS).

**Theorem (Orthogonal Set Basis)**: If $V$ is an IPS and $S = \{v_1, \dots, v_k\}$ is an orthogonal set with $v_i \neq 0$ for all $i$, then for any $y \in \text{Span}(S)$,
$$ y = \sum_{i=1}^k \frac{\langle y, v_i \rangle}{\|v_i\|^2} v_i $$
If $S$ is orthonormal, then $y = \sum_{i=1}^k \langle y, v_i \rangle v_i$.
An orthogonal set of non-zero vectors is linearly independent.

**Theorem (Gram-Schmidt Process)**: Let $V$ be an IPS, and $S = \{w_1, \dots, w_n\}$ be a linearly independent set of $V$. Define $S' = \{v_1, \dots, v_n\}$ as:
$$ v_1 = w_1 $$
$$ v_k = w_k - \sum_{j=1}^{k-1} \frac{\langle w_k, v_j \rangle}{\|v_j\|^2} v_j \quad \text{for } 2 \le k \le n $$
Then $S'$ is an orthogonal set of nonzero vectors, and $\text{Span}(S') = \text{Span}(S)$. If $S$ is a basis for $V$, the G-S method yields an orthonormal basis $S'$ for $V$ by normalizing the $v_k$ vectors.

## Orthogonal Complement

**Definition**: For a subset $S$ of an IPS $V$, its orthogonal complement $S^\perp$ is defined as:
$$ S^\perp = \{x \in V \mid \langle x, y \rangle = 0 \text{ for all } y \in S\} $$

**Theorem (Orthogonal Decomposition)**: Let $W$ be a finite-dimensional subspace of an IPS $V$. For any $y \in V$, there exist unique vectors $u \in W$ and $z \in W^\perp$ such that $y = u + z$.
Furthermore, if $\{v_1, \dots, v_k\}$ is an orthonormal basis (ONB) of $W$, then
$$ u = \sum_{i=1}^k \langle y, v_i \rangle v_i $$
The vector $u$ is the unique vector in $W$ that is closest to $y$, meaning $\|y - x\| \ge \|y - u\|$ for all $x \in W$, and equality holds if and only if $x=u$.

## Least Square Approximation

Given a data set $\{(t_1, y_1), \dots, (t_m, y_m)\}$, where $y_i$ is the observed value at time $t_i$. If there is an essential linear relationship ($y = ct + d$), the goal is to find $c$ and $d$ such that the error $E = \sum_{i=1}^m (y_i - ct_i - d)^2$ is minimized. This line is called the least squares line.

This problem can be formulated in matrix form: Let
$$ A = \begin{pmatrix} t_1 & 1 \\ \vdots & \vdots \\ t_m & 1 \end{pmatrix}, \quad x = \begin{pmatrix} c \\ d \end{pmatrix}, \quad y = \begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} $$
Then $E = \|y - Ax\|^2$. The problem is to find $x_0 \in \mathbb{F}^n$ such that $E$ is minimized, i.e., $\|y - Ax_0\| \le \|y - Ax\|$ for all $x \in \mathbb{F}^n$.

## Adjoint Operator

**Definition**: For an $m \times n$ matrix $A \in \text{IM}_{m,n}(\mathbb{F})$, its adjoint $A^*$ is defined as $A^* = (\overline{A_{ji}})^t = (\overline{A})^t$.
For a linear operator $T: V \to V$ in an IPS $V$, its adjoint $T^*: V \to V$ is a unique linear operator such that $\langle T(x), y \rangle = \langle x, T^*(y) \rangle$ for all $x, y \in V$. The matrix representation of $T^*$ with respect to an orthonormal basis $\mathcal{B}$ is $[T^*]_\mathcal{B} = ([T]_\mathcal{B})^*$.

**Theorem (Least Squares Solution)**: Let $A \in \text{IM}_{m,n}(\mathbb{F})$ and $y \in \mathbb{F}^m$. There exists $x_0 \in \mathbb{F}^n$ such that $(A^*A)x_0 = A^*y$ (Normal Equations), and $\|Ax_0 - y\| \le \|Ax - y\|$ for all $x \in \mathbb{F}^n$.
Furthermore, if $\text{rank}(A) = n$, then $A^*A$ is invertible, and the unique solution is $x_0 = (A^*A)^{-1}A^*y$. This relies on the fact that $\text{rank}(A^*A) = \text{rank}(A)$.

## Key Formulas

- **Gram-Schmidt process**: $v_k = w_k - \sum_{j=1}^{k-1} \frac{\langle w_k, v_j \rangle}{\|v_j\|^2} v_j$
- **Orthogonal complement**: $S^\perp = \{x \in V \mid \langle x, y \rangle = 0 \text{ for all } y \in S\}$
- **Orthogonal decomposition**: $y = u + z$ where $u = \sum_{i=1}^k \langle y, v_i \rangle v_i \in W$ and $z \in W^\perp$.
- **Least squares error**: $E = \|y - Ax\|^2$
- **Normal equations**: $(A^*A)x_0 = A^*y$
- **Least squares solution (if rank(A)=n)**: $x_0 = (A^*A)^{-1}A^*y$
- **Adjoint operator property**: $\langle T(x), y \rangle = \langle x, T^*(y) \rangle$

## Quick Summary

This lecture covered crucial methods for working with Inner Product Spaces and linear data fitting. The Gram-Schmidt process provides a systematic way to convert any basis into an orthonormal one. We defined the orthogonal complement and explored the unique decomposition of vectors into components within a subspace and its complement, with the closest vector property. Finally, we introduced the least squares approximation method to find the best linear fit for data, derived its solution using the normal equations, and defined the adjoint operator in both matrix and abstract linear operator contexts.