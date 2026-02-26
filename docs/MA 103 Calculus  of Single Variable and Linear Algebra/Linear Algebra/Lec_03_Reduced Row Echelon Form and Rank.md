---
title: |
  MA 103: Reduced Row Echelon Form and Rank
lecture_number: 3
lecture_name: |
  Reduced Row Echelon Form and Rank
category: |
  Linear Algebra
sidebar_label: |
  Lecture 3
sidebar_position: 3
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Reduced Row Echelon Form and Rank
  2025-08-22
tags:
  - Linear Algebra
  - Matrices
  - Row Operations
  - Echelon Form
  - Rank
  - Systems of Linear Equations
summary: |
  Key concepts of Reduced Row Echelon Form (RREF), matrix rank, and the condition for non-trivial solutions to homogeneous linear systems.
math: true
---

# MA 103: Reduced Row Echelon Form and Rank

## Table of Contents
- Row Echelon Form (REF) Overview
- Reduced Row Echelon Form (RREF)
- Rank of a Matrix
- Homogeneous Systems of Linear Equations

## Row Echelon Form (REF) Overview
A matrix is in Row Echelon Form (REF) if it satisfies three conditions:
1. All non-zero rows are above any rows of all zeros.
2. The leading entry (pivot) of each non-zero row is 1.
3. Each leading 1 is in a column to the right of the leading 1 of the row above it.
REF for a given matrix is generally not unique, as different sequences of row operations can lead to different REF matrices.

## Reduced Row Echelon Form (RREF)
**Definition:** A matrix is in Reduced Row Echelon Form (RREF) if it satisfies the conditions for REF, and additionally:
4. Each column containing a leading 1 has zeros in all other positions.
The RREF of any given matrix is unique.

## Rank of a Matrix
**Definition:** For an $m \times n$ matrix $A$ with real entries, its **rank**, denoted as $\text{rank}(A)$, is defined as the number of non-zero rows in any row echelon form of $A$.
It is a fundamental property that the row rank (number of non-zero rows in REF) equals the column rank (maximum number of linearly independent column vectors), and both are equal to the rank of the matrix.

## Homogeneous Systems of Linear Equations
Consider the system of linear equations $A \cdot x = b$, where $A \in \mathbb{M}_{m \times n}(\mathbb{R})$, $x \in \mathbb{M}_{n \times 1}(\mathbb{R})$, and $b \in \mathbb{M}_{m \times 1}(\mathbb{R})$.
For the homogeneous case, where $b = 0$, the system is $A \cdot x = 0$.

**Theorem:** The homogeneous system $A \cdot x = 0$ has at least one non-zero solution in $\mathbb{R}^n$ if and only if $\text{rank}(A) $<$ n$.
This theorem establishes a crucial link between the rank of the coefficient matrix and the existence of non-trivial solutions.
- If $\text{rank}(A) $<$ n$, the columns of $A$ are linearly dependent, implying a non-zero solution $x$.
- If $A \cdot x = 0$ has a non-zero solution, the column vectors of $A$ are linearly dependent, which means $\text{rank}(A) $<$ n$.

## Key Formulas
- Homogeneous linear system: $A \cdot x = 0$
- Condition for non-zero solution: $\text{rank}(A) $<$ n$
- Column vector linear combination for $A \cdot x = 0$: $x_1 C_1 + x_2 C_2 + \dots + x_n C_n = 0$, where $C_i$ are column vectors of $A$.

## Quick Summary
Reduced Row Echelon Form (RREF) is a unique, standardized form of a matrix, characterized by leading 1s with zeros elsewhere in their columns. The rank of a matrix is the number of non-zero rows in its REF, a unique scalar value indicating the dimensionality of the vector space spanned by its rows or columns. A homogeneous system of linear equations $A \cdot x = 0$ possesses at least one non-zero solution if and only if the rank of matrix $A$ is less than the number of its columns ($n$).