---
title: |
  Inner Product Spaces
lecture_number: 10
lecture_name: |
  Inner Product Spaces
category: |
  Linear Algebra
sidebar_label: |
  Lecture 10
sidebar_position: 10
course: |
  MA 103 Calculus of Single Variable and Linear Algebra
topic: |
  Inner Product Spaces
date: |
  22/10/2025
tags:
  - Math
  - Linear Algebra
  - Inner Product Spaces
summary: |
  This lecture introduces Inner Product Spaces, defining an inner product and its essential properties. Key concepts such as the norm of a vector, orthogonality, and orthonormal sets are established. The fundamental Cauchy-Schwarz and Triangle Inequalities are also presented.
math: true
---

# Inner Product Spaces

## Table of Contents
* [Inner Product Space Definition](#inner-product-space-definition)
* [Properties of Inner Product Spaces](#properties-of-inner-product-spaces)
* [Norm Definition and Properties](#norm-definition-and-properties)
* [Cauchy-Schwarz Inequality](#cauchy-schwarz-inequality)
* [Triangle Inequality](#triangle-inequality)
* [Orthogonality](#orthogonality)
* [Independent Definition of Norm](#independent-definition-of-norm)

## Inner Product Space Definition
An **Inner Product Space** $(V, \langle \cdot, \cdot \rangle)$ is a vector space $V$ over a field $\mathbb{F}$ ($\mathbb{R}$ or $\mathbb{C}$) equipped with an **inner product**, a function $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{F}$ that satisfies the following axioms for all $x, y, z \in V$ and $c \in \mathbb{F}$:
1.  **Additivity in the first argument:** $\langle x+y, z \rangle = \langle x,z \rangle + \langle y,z \rangle$.
2.  **Homogeneity in the first argument:** $\langle cx, y \rangle = c \langle x,y \rangle$.
3.  **Conjugate symmetry:** $\langle x,y \rangle = \overline{\langle y,x \rangle}$. (For $\mathbb{F}=\mathbb{R}$, this simplifies to $\langle x,y \rangle = \langle y,x \rangle$.)
4.  **Positive-definiteness:** $\langle x,x \rangle \ge 0$, and $\langle x,x \rangle = 0$ if and only if $x=0$.
Common examples include the usual dot product in $\mathbb{R}^n$, the complex dot product in $\mathbb{C}^n$, the integral of products for continuous functions $C[0,1]$, and $\text{tr}(B^*A)$ for matrices $M_n(\mathbb{F})$.

## Properties of Inner Product Spaces
**Theorem:** If $V$ is an Inner Product Space over $\mathbb{F}$, then for all $x, y, z \in V$ and $c \in \mathbb{F}$, the following properties hold:
1.  $\langle x, y+z \rangle = \langle x,y \rangle + \langle x,z \rangle$
2.  $\langle x, cy \rangle = \bar{c} \langle x,y \rangle$
3.  $\langle x, 0 \rangle = \langle 0, x \rangle = 0$
4.  If $\langle x,y \rangle = \langle x,z \rangle$ for all $x \in V$, then $y=z$.

## Norm Definition and Properties
The **norm** (or length) of a vector $x \in V$ in an Inner Product Space is defined as $||x|| = \sqrt{\langle x,x \rangle}$. From this definition, the following properties are derived:
1.  $||cx|| = |c| ||x||$ for any scalar $c \in \mathbb{F}$.
2.  $||x|| = 0$ if and only if $x=0$. (Note that $||x|| > 0$ if $x \ne 0$).

## Cauchy-Schwarz Inequality
**Theorem (Cauchy-Schwarz Inequality):** For any vectors $x, y$ in an Inner Product Space $V$, the absolute value of their inner product is less than or equal to the product of their norms:
$$|\langle x,y \rangle| \le ||x|| \cdot ||y||$$

## Triangle Inequality
**Theorem (Triangle Inequality):** For any vectors $x, y$ in an Inner Product Space $V$, the norm of their sum is less than or equal to the sum of their norms:
$$||x+y|| \le ||x|| + ||y||$$

## Orthogonality
1.  **Orthogonal Vectors:** Two vectors $x, y \in V$ are **orthogonal** if their inner product is zero: $\langle x,y \rangle = 0$.
2.  **Orthogonal Set:** A set $S \subseteq V$ is an **orthogonal set** of vectors if every distinct pair of vectors in $S$ is orthogonal: $\langle x,y \rangle = 0$ for all $x,y \in S$ with $x \ne y$.
3.  **Orthonormal Set:** An **orthonormal set** $S \subseteq V$ is an orthogonal set where every vector in $S$ has a norm of 1: $||x||=1$ for all $x \in S$.

## Independent Definition of Norm
A **norm** can also be independently defined as a function $||\cdot||: V \to \mathbb{F}$ (where $\mathbb{F}$ is $\mathbb{R}$ or $\mathbb{C}$) satisfying the following axioms for all $x, y \in V$ and $c \in \mathbb{F}$:
1.  **Positive-definiteness:** $||x|| \ge 0$, and $||x|| = 0$ if and only if $x=0$.
2.  **Absolute homogeneity:** $||cx|| = |c| ||x||$.
3.  **Triangle inequality:** $||x+y|| \le ||x|| + ||y||$.

## Key Formulas
*   **Inner Product Axioms:**
    1.  $\langle x+y, z \rangle = \langle x,z \rangle + \langle y,z \rangle$
    2.  $\langle cx, y \rangle = c \langle x,y \rangle$
    3.  $\langle x,y \rangle = \overline{\langle y,x \rangle}$
    4.  $\langle x,x \rangle \ge 0$ and $\langle x,x \rangle = 0 \iff x=0$
*   **Derived Inner Product Properties:**
    1.  $\langle x, y+z \rangle = \langle x,y \rangle + \langle x,z \rangle$
    2.  $\langle x, cy \rangle = \bar{c} \langle x,y \rangle$
    3.  $\langle x, 0 \rangle = \langle 0, x \rangle = 0$
*   **Norm Definition:** $||x|| = \sqrt{\langle x,x \rangle}$
*   **Derived Norm Properties:**
    1.  $||cx|| = |c| ||x||$
    2.  $||x|| = 0 \iff x=0$
*   **Cauchy-Schwarz Inequality:** $|\langle x,y \rangle| \le ||x|| \cdot ||y||$
*   **Triangle Inequality:** $||x+y|| \le ||x|| + ||y||$
*   **Orthogonality Condition:** $\langle x,y \rangle = 0$
*   **Independent Norm Axioms:**
    1.  $||x|| \ge 0$ and $||x|| = 0 \iff x=0$
    2.  $||cx|| = |c| ||x||$
    3.  $||x+y|| \le ||x|| + ||y||$

## Quick Summary
Inner Product Spaces extend the concept of dot product, allowing for notions of length (norm) and angle (orthogonality) in abstract vector spaces. An inner product satisfies linearity, conjugate symmetry, and positive-definiteness. The norm is derived from the inner product, giving rise to fundamental relationships like the Cauchy-Schwarz and Triangle Inequalities. Vectors are orthogonal if their inner product is zero, and an orthonormal set consists of orthogonal vectors with unit norm. A norm can also be defined independently, adhering to positive-definiteness, absolute homogeneity, and the triangle inequality.