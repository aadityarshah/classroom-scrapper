---
title: |
  Matrix Representation, Basis Change, and Vector Spaces
lecture_number: 7
lecture_name: |
  Matrix Representations, Basis Change, and Vector Space Axioms
category: |
  Linear Algebra
sidebar_label: |
  Lecture 7
sidebar_position: 7
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Uncategorized
  10/9/2025
tags:
  - Math
  - Linear Algebra
  - Vector Spaces
  - Basis Change
  - Linear Transformations
  - Matrix Representation
summary: |
  This lecture introduces the matrix representation of linear transformations between vector spaces with respect to chosen bases, defines the concept of a basis change matrix and its role in transforming coordinate vectors, and formally establishes the axioms that define a vector space over a field, distinguishing between finite and infinite dimensional spaces.
math: true
---

# Matrix Representation, Basis Change, and Vector Spaces

## Table of Contents
*   Matrix Representation of Linear Transformations
*   The Basis Change Matrix
*   Coordinate Representation of Vectors
*   Vector Spaces
*   Finite vs. Infinite Dimensional Vector Spaces
*   Key Formulas
*   Quick Summary

## Matrix Representation of Linear Transformations
For a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$, let $B_1$ be a basis for $\mathbb{R}^n$ and $B_2$ be a basis for $\mathbb{R}^m$. We can represent $T$ by a matrix $[T]_{B_1}^{B_2}$, whose columns are the coordinate vectors of the images of the basis vectors from $B_1$ with respect to the basis $B_2$.

## The Basis Change Matrix
The basis change matrix, denoted $S_{B \to C}$, transforms coordinate representations of a vector from basis $B$ to basis $C$. It is constructed such that its columns are the coordinate vectors of the basis vectors from $B$ with respect to basis $C$. This matrix enables conversion between different coordinate systems for the same vector space.

## Coordinate Representation of Vectors
Given a finite-dimensional vector space $V$ with a basis $B = \{b_1, \dots, b_n\}$, any vector $v \in V$ can be uniquely expressed as a linear combination $v = \alpha_1 b_1 + \dots + \alpha_n b_n$. The coordinate vector of $v$ with respect to $B$ is $[v]_B = (\alpha_1, \dots, \alpha_n)^T$.

## Vector Spaces
A **Vector Space** $V$ over a field $F$ is a non-empty set equipped with two operations: vector addition ($+$) and scalar multiplication ($\cdot$). Vector addition makes $(V, +)$ an abelian group, satisfying closure, associativity, identity (zero vector $0$), inverse (for every $v$, there is $-v$), and commutativity. Scalar multiplication (where $\lambda \in F, v \in V \implies \lambda \cdot v \in V$) must satisfy four additional axioms: (1) $1 \cdot v = v$, (2) $(\lambda + \lambda') \cdot v = \lambda \cdot v + \lambda' \cdot v$, (3) $\lambda \cdot (v + w) = \lambda \cdot v + \lambda \cdot w$, and (4) $(\lambda \mu) \cdot v = \lambda \cdot (\mu \cdot v)$.

## Finite vs. Infinite Dimensional Vector Spaces
A vector space is **finite-dimensional** if it has a basis consisting of a finite number of vectors; otherwise, it is **infinite-dimensional**. Examples include $\mathbb{R}^2$ and $M_2(\mathbb{R})$ (the space of $2 \times 2$ matrices with real entries) as finite-dimensional vector spaces. In contrast, $C[0,1]$ (the space of continuous functions on the interval $[0,1]$) is an infinite-dimensional vector space because it contains an infinite linearly independent subset, such as the set of polynomials $\{1, x, x^2, \dots, x^n, \dots\}$.

## Key Formulas
*   **Coordinate Transformation**: $[v]_C^T = S_{B \to C} [v]_B^T$
*   **Basis Change Matrix Construction**: For $B = \{b_1, \dots, b_n\}$, $S_{B \to C} = ([b_1]_C^T \ [b_2]_C^T \ \dots \ [b_n]_C^T)$
*   **Inverse Basis Change Matrix**: $S_{C \to B} = (S_{B \to C})^{-1}$

## Quick Summary
Linear transformations can be represented by matrices relative to chosen bases. The basis change matrix facilitates conversion between different coordinate representations of a vector. A vector space is a fundamental algebraic structure defined by an abelian group under addition and scalar multiplication satisfying specific distributive and associative axioms. Vector spaces can be classified as finite-dimensional if they possess a finite basis or infinite-dimensional otherwise.