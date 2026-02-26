---
title: |
  Linear Independence & Dependence
lecture_number: 4
lecture_name: |
  Linear Independence & Dependence
category: |
  Linear Algebra
sidebar_label: |
  Lecture 4
sidebar_position: 4
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Linear Independence & Dependence
  2025-08-27
tags:
  - Linear Algebra
  - Vectors
  - Linear Independence
  - Basis
  - Dimension
summary: |
  This lecture introduces linear independence and dependence of vectors in $\mathbb{R}^n$, defines linear combinations, the zero vector, and explores how matrix rank relates to independence. It also covers standard basis vectors, spanning sets, bases for subspaces, and the unique concept of dimension.
math: true
---

# Linear Independence & Dependence

## Table of Contents
* Vectors in $\mathbb{R}^n$
* Linear Combinations
* Linear Independence and Dependence
* Rank and Linear Independence
* Standard Basis Vectors
* Spanning Sets
* Basis of a Vector Subspace
* Dimension of a Vector Subspace
* Key Formulas
* Quick Summary

## Vectors in $\mathbb{R}^n$
A vector in $\mathbb{R}^n$ is an $n$-tuple $v = (v_1, \dots, v_n)$ where $v_i \in \mathbb{R}$. $\mathbb{R}^n$ is closed under vector addition and scalar multiplication, forming a vector space. The zero vector is $\mathbf{0} = (0, 0, \dots, 0)$.

## Linear Combinations
**Definition:** A linear combination of vectors $v_1, \dots, v_m$ is a vector of the form $\lambda_1 v_1 + \dots + \lambda_m v_m$, where $\lambda_1, \dots, \lambda_m$ are real numbers (scalars).

## Linear Independence and Dependence
**Definition:** Vectors $v_1, \dots, v_m$ are **linearly independent (L.I.)** if the equation $\lambda_1 v_1 + \dots + \lambda_m v_m = \mathbf{0}$ implies that $\lambda_1 = \dots = \lambda_m = 0$. Otherwise, the vectors are **linearly dependent (L.D.)**. If vectors are L.D., at least one scalar $\lambda_i$ is non-zero, meaning one vector can be expressed as a linear combination of the others.

## Rank and Linear Independence
Vectors $v_1, \dots, v_m$ are linearly independent if and only if the homogeneous system of linear equations resulting from $\lambda_1 v_1 + \dots + \lambda_m v_m = \mathbf{0}$ has only the trivial solution. In matrix form $A\mathbf{\lambda} = \mathbf{0}$ (where columns of $A$ are $v_i$), this occurs if and only if $\text{rank}(A) = m$. There can be at most $n$ linearly independent vectors in $\mathbb{R}^n$.

## Standard Basis Vectors
In $\mathbb{R}^n$, the standard basis vectors are $e_1 = (1, 0, \dots, 0)$, $e_2 = (0, 1, \dots, 0)$, $\dots$, $e_n = (0, 0, \dots, 1)$. These vectors are linearly independent, and any vector $v = (a_1, \dots, a_n) \in \mathbb{R}^n$ can be uniquely written as a linear combination $v = a_1 e_1 + \dots + a_n e_n$.

## Spanning Sets
**Definition:** For a vector subspace $W$ of $\mathbb{R}^n$, a set of vectors $\{v_1, \dots, v_m\} \subseteq W$ is a **spanning set** of $W$ if every vector $v \in W$ can be expressed as a linear combination of $v_1, \dots, v_m$. The standard basis vectors $\{e_1, \dots, e_n\}$ form a spanning set for $\mathbb{R}^n$.

## Basis of a Vector Subspace
**Definition:** A subset $S$ of a vector subspace $W$ is called a **basis** of $W$ if $S$ is both linearly independent and spans $W$.
**Theorem:** Any two bases of a vector subspace of $\mathbb{R}^n$ have the same cardinality (the same number of elements).

## Dimension of a Vector Subspace
**Definition:** The **dimension** of a vector subspace is the cardinality (number of elements) of any of its bases. For example, $\mathbb{R}^3$ has dimension 3, and a subspace defined by $x+y+z=0$ in $\mathbb{R}^3$ has dimension 2.

## Key Formulas
*   **Linear Combination:** $L = \lambda_1 v_1 + \dots + \lambda_m v_m$
*   **Condition for Linear Independence:** $\lambda_1 v_1 + \dots + \lambda_m v_m = \mathbf{0} \implies \lambda_i = 0 \text{ for all } i$
*   **Matrix Rank for L.I.:** For vectors $v_1, \dots, v_m$ forming columns of matrix $A$, they are L.I. iff $\text{rank}(A) = m$.
*   **Standard Basis Vectors in $\mathbb{R}^n$:** $e_i$ (1 at $i$-th position, 0 elsewhere).

## Quick Summary
This lecture clarified linear independence and dependence, linking them to the trivial solution of homogeneous linear systems and the rank of a matrix. Key concepts include linear combinations, the zero vector, and the standard basis of $\mathbb{R}^n$. A basis was defined as a linearly independent spanning set for a vector subspace, and the unique cardinality of any basis for a given subspace was introduced as its dimension.