---
title: |
  Vector Subspaces and Row-Reduced Echelon Form
lecture_number: |
  2
lecture_name: |
  Vector Subspaces and Row-Reduced Echelon Form
category: |
  Linear Algebra
sidebar_label: |
  Lecture 2
sidebar_position: |
  2
course: |
  MA 103
topic: |
  Vector Subspaces and Row-Reduced Echelon Form
date: |
  20/08/2025
tags:
  - Linear Algebra
  - Vector Subspaces
  - Homogeneous Systems
  - Echelon Form
summary: |
  This lecture introduces homogeneous systems of linear equations, defines vector subspaces and their properties, explains affine spaces, and details the row-reduced echelon form of a matrix.
math: true
---
# Vector Subspaces and Row-Reduced Echelon Form

## Table of Contents
- Homogeneous Systems of Linear Equations
- Properties of Solutions to Homogeneous Systems
- Vector Subspaces
- Affine Spaces
- Properties of Vector Subspaces and Linear Equations
- Row-Reduced Echelon Form of a Matrix
- Key Formulas
- Quick Summary

## Homogeneous Systems of Linear Equations
A system of linear equations $E$ has a corresponding **homogeneous system** $E^0$ where all constant terms are set to zero. For $m$ equations and $n$ variables, $E^0$ is defined as:
$$
E^0: \begin{cases}
a_{11}x_1 + \dots + a_{1n}x_n = 0 \\
a_{21}x_1 + \dots + a_{2n}x_n = 0 \\
\vdots \\
a_{m1}x_1 + \dots + a_{mn}x_n = 0
\end{cases}
$$
A homogeneous system always possesses the trivial solution, which is the zero vector $(0,0,\dots,0)$.

## Properties of Solutions to Homogeneous Systems
Let $\beta = (\beta_1, \dots, \beta_n)$ and $\beta' = (\beta'_1, \dots, \beta'_n)$ be solutions to a homogeneous system $E^0$.
- **Additivity**: The sum $\beta + \beta' = (\beta_1+\beta'_1, \dots, \beta_n+\beta'_n)$ is also a solution of $E^0$.
- **Homogeneity**: For any scalar $\lambda \in \mathbb{R}$, the scalar multiple $\lambda\beta = (\lambda\beta_1, \dots, \lambda\beta_n)$ is also a solution of $E^0$.

## Vector Subspaces
**Definition**: A non-empty subset $S$ of $\mathbb{R}^n$ is a **vector subspace** if it satisfies both the additive and homogeneous properties.
- **Additive Property**: For any $\mathbf{u}, \mathbf{v} \in S$, their sum $\mathbf{u} + \mathbf{v}$ is in $S$.
- **Homogeneous Property**: For any scalar $\lambda \in \mathbb{R}$ and $\mathbf{u} \in S$, the scalar multiple $\lambda\mathbf{u}$ is in $S$.
The set $\mathbb{R}^n$ denotes the Cartesian product $\mathbb{R} \times \dots \times \mathbb{R}$ ($n$ times), where elements are $n$-tuples of real numbers. The solution set of any homogeneous system of linear equations constitutes a vector subspace of $\mathbb{R}^n$.

## Affine Spaces
The solution set of a non-homogeneous system of linear equations is generally not a vector subspace unless the system is homogeneous. Such solution sets are described as **affine spaces**, which are translates of vector subspaces by a particular solution.
For example, the equation $x_1 + x_2 + x_3 = 0$ defines a plane through the origin in $\mathbb{R}^3$ (a vector subspace), while $x_1 + x_2 + x_3 = 1$ defines a parallel plane shifted by a vector like $(1,0,0)$ (an affine space).

## Properties of Vector Subspaces and Linear Equations
- Every vector subspace of $\mathbb{R}^n$ must contain the origin $(0, \dots, 0)$, directly stemming from the homogeneity property ($0 \cdot \mathbf{v} = \mathbf{0}$ for any $\mathbf{v}$ in the subspace).
- Unlike homogeneous systems, a non-homogeneous system of linear equations may have no solution.
- An equation is classified as linear if and only if the solution set of its homogeneous counterpart forms a vector subspace. For instance, $\sin x = 1$ is not a linear equation because the solution set of $\sin x = 0$ is not a vector subspace of $\mathbb{R}$.

## Row-Reduced Echelon Form of a Matrix
An $r \times s$ matrix $A$ can be transformed into its **row-reduced echelon form (RREF)** using a sequence of elementary row operations. This form is characterized by the following conditions:
1. The first non-zero entry (called the leading entry or pivot) in each non-zero row is $1$.
2. Each leading $1$ is the only non-zero entry in its respective column.
3. All rows consisting entirely of zeros are placed at the bottom of the matrix.
4. For any two successive non-zero rows, the leading $1$ of the lower row appears to the right of the leading $1$ of the upper row.
Example of a matrix in RREF:
$$
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

## Key Formulas
- Homogeneous System: $a_{i1}x_1 + \dots + a_{in}x_n = 0$ for $i=1, \dots, m$.
- Vector Subspace Properties:
    - Additivity: $\mathbf{u}, \mathbf{v} \in S \implies \mathbf{u} + \mathbf{v} \in S$
    - Homogeneity: $\lambda \in \mathbb{R}, \mathbf{u} \in S \implies \lambda\mathbf{u} \in S$

## Quick Summary
This lecture covered homogeneous systems of linear equations, noting that their solutions form vector subspaces due to closure under addition and scalar multiplication. Non-homogeneous systems yield affine spaces, which are translated vector subspaces. All vector subspaces contain the origin. The row-reduced echelon form provides a unique, simplified representation of a matrix achieved through elementary row operations, characterized by leading $1$s and specific zero entries.