---
title: |
  Linear Transformations: Kernel, Image, Rank-Nullity Theorem
lecture_number: 6
lecture_name: |
  Linear Transformations: Kernel, Image, Rank-Nullity Theorem
category: |
  Linear Algebra
sidebar_label: |
  Lecture 6
sidebar_position: 6
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Linear Algebra
date: |
  2025-03-09
tags:
  - Linear Algebra
  - Linear Transformations
  - Kernel
  - Image
  - Rank-Nullity Theorem
summary: |
  Explore linear transformations, their matrix representations, and fundamental subspaces like kernel and image. Define rank and nullity, culminating in the Rank-Nullity Theorem.
math: true
---

# Linear Transformations: Kernel, Image, Rank-Nullity Theorem

## Table of Contents
- Linear Transformations and Matrix Representation
- Kernel of a Linear Transformation
- Image of a Linear Transformation
- Nullity and Rank
- Rank-Nullity Theorem

## Linear Transformations and Matrix Representation
A function $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$ is a **linear transformation**. Given the standard basis $B = \{e_1, \ldots, e_n\}$ of $\mathbb{R}^n$, the matrix representation of $T$ with respect to $B$, denoted $[T]_B$, is an $m \times n$ matrix whose columns are the images of the basis vectors under $T$: $[T]_B = [T(e_1) \ T(e_2) \ \ldots \ T(e_n)]$. For any vector $x \in \mathbb{R}^n$, $T(x)$ can be computed as $[T]_B x$.

## Kernel of a Linear Transformation
**Definition:** The **kernel** of a linear transformation $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$, denoted $\text{ker}(T)$, is the set of all vectors $x \in \mathbb{R}^n$ such that $T(x) = 0$.
The kernel is a vector subspace of $\mathbb{R}^n$, corresponding to the solution space of the homogeneous linear system $[T]_B x = 0$.

## Image of a Linear Transformation
**Definition:** The **image** of a linear transformation $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$, denoted $\text{im}(T)$, is the set of all vectors $y \in \mathbb{R}^m$ such that $y = T(x)$ for some $x \in \mathbb{R}^n$.
The image is a vector subspace of $\mathbb{R}^m$ and is spanned by the images of the standard basis vectors, i.e., $\text{im}(T) = \text{span}\{T(e_1), \ldots, T(e_n)\}$.

## Nullity and Rank
**Definition:** The **nullity** of a linear transformation $T$, denoted $\text{nullity}(T)$, is the dimension of its kernel: $\text{nullity}(T) = \text{dim}(\text{ker}(T))$.
**Definition:** The **rank** of a linear transformation $T$, denoted $\text{rank}(T)$, is the dimension of its image: $\text{rank}(T) = \text{dim}(\text{im}(T))$.
The rank of $T$ is equal to the rank of its matrix representation $[T]_B$.

## Rank-Nullity Theorem
**Theorem (Rank-Nullity Theorem):** For a linear transformation $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$, the sum of its rank and nullity equals the dimension of its domain.
$$ \text{rank}(T) + \text{nullity}(T) = n $$

## Key Formulas
- **Matrix Representation:** $[T]_B = [T(e_1) \ T(e_2) \ \ldots \ T(e_n)]$
- **Kernel Definition:** $\text{ker}(T) = \{x \in \mathbb{R}^n \mid T(x) = 0\}$
- **Image Definition:** $\text{im}(T) = \{T(x) \mid x \in \mathbb{R}^n\}$
- **Nullity:** $\text{nullity}(T) = \text{dim}(\text{ker}(T))$
- **Rank:** $\text{rank}(T) = \text{dim}(\text{im}(T))$
- **Rank-Nullity Theorem:** $\text{rank}(T) + \text{nullity}(T) = n$

## Quick Summary
Linear transformations $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$ can be represented by an $m \times n$ matrix $[T]_B$. The **kernel** is the subspace of vectors mapped to zero, and its dimension is the **nullity**. The **image** is the subspace of all possible outputs, and its dimension is the **rank**. The **Rank-Nullity Theorem** states that for any linear transformation, $\text{rank}(T) + \text{nullity}(T) = n$, where $n$ is the dimension of the domain.