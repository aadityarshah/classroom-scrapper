---
title: Set Theory Fundamentals
lecture_number: 1
lecture_name: Introduction to Set Theory and Operations
category: Probability Theory
sidebar_label: Lecture 1
sidebar_position: 1
course: "ES 114 Probability, Statistics and Data Visualisation"
last_updated: "23 March 2026"
topic:
- Set Theory
- Basic Definitions
- Set Operations
- Probability Foundations
tags:
- sets
- elements
- subset
- empty set
- universal set
- union
- intersection
- complement
- set difference
- disjoint sets
- partition
- commutative law
- associative law
- distributive law
- De Morgan's Law
math: true
summary: 'This lecture provides a comprehensive introduction to set theory, a fundamental
  building block for probability. We define sets, elements, and explore various types
  like finite, countable, and uncountable sets, alongside open and closed intervals.
  Key concepts such as subsets, empty sets, and universal sets are established. The
  lecture then dives into essential set operations: union, intersection, complement,
  and set difference, concluding with definitions of disjoint sets and partitions.
  Finally, we review the fundamental laws governing set operations, including commutative,
  associative, distributive, and De Morgan''s laws.'
---


In the realm of probability and stochastic processes, a solid understanding of set theory is absolutely fundamental. Sets provide the language and framework for defining sample spaces, events, and relationships between them. This lecture lays the groundwork by introducing core concepts of set theory and their associated operations.

## 1. Sets and Elements

### Definition of a Set
A **set** is a well-defined collection of distinct objects. These objects are referred to as **elements** or **members** of the set.
We typically denote a set with a capital letter, e.g., $A$, and its elements are enclosed in curly braces.
For example, $A = \{\xi_1, \xi_2, \dots, \xi_n\}$ represents a set where $\xi_i$ is the $i$-th element.

### Set Membership
The relationships between an element and a set are denoted as follows:
*   $\xi \in A$: An object $\xi$ is an element of set $A$.
*   $\xi \notin A$: An object $\xi$ is not an element of set $A$.

### Types of Sets
Sets can be categorized based on the number and nature of their elements:
*   **Finite Set**: A set containing a limited or fixed number of elements.
    *   Example: $A = \{0, 1\}$.
*   **Countable Set**: A set whose elements can be put into a one-to-one correspondence with the set of natural numbers $\mathbb{N} = \{1, 2, 3, \dots\}$. This includes finite sets and infinite sets that can be "counted" (enumerated).
    *   Example: $A = \{2, 4, 6, 8, \dots\}$ (the set of positive even integers).
*   **Uncountable Set**: A set whose elements cannot be put into a one-to-one correspondence with the natural numbers. These sets are "larger" than countable sets.
    *   Example: $A = \{x \mid 0 < x < 1\}$ (the set of real numbers between 0 and 1).

### Open and Closed Intervals
For sets of real numbers, intervals are commonly used:
*   **Open Interval**: $(a, b) = \{x \mid a < x < b\}$. This set includes all real numbers strictly between $a$ and $b$, but does not include $a$ or $b$.
*   **Closed Interval**: $[a, b] = \{x \mid a \le x \le b\}$. This set includes all real numbers between $a$ and $b$, including $a$ and $b$.

### Sets of Functions
Elements of a set are not limited to numbers; they can be any type of object, including functions. For instance, one could define a set of all straight lines or a set of all periodic cosine functions.

## 2. Subsets

### Definition of a Subset
A set $B$ is a **subset** of $A$, denoted $B \subseteq A$, if every element of $B$ is also an element of $A$. In other words, for any $\xi \in B$, it must also be true that $\xi \in A$.

### Proper and Improper Subsets
*   **Proper Subset**: If $B \subseteq A$ and $B \ne A$, then $B$ is a **proper subset** of $A$, denoted $B \subset A$. This means $A$ contains at least one element not found in $B$.
    *   Example: If $A = \{1, 2, 3, 4, 5, 6\}$ and $B = \{1, 2\}$, then $B$ is a proper subset of $A$.
*   **Improper Subset**: If $B \subseteq A$ and $B = A$, then $B$ is an **improper subset** of $A$. In this case, the sets are identical.
    *   Example: If $A = \{1, 2, 3\}$ and $B = \{1, 2, 3\}$, then $B$ is an improper subset of $A$.

### Theorem: Equality of Sets
**Theorem**: If $A \subseteq B$ and $B \subseteq A$, then $A = B$.
**Proof Sketch**: Assume, for the sake of contradiction, that $A \ne B$. If $A \subseteq B$ and $B \subseteq A$, but $A \ne B$, it would imply that there is an element in $A$ not in $B$, or an element in $B$ not in $A$.
1.  If there exists an $x \in A$ such that $x \notin B$, this contradicts the condition $A \subseteq B$.
2.  If there exists an $x \in B$ such that $x \notin A$, this contradicts the condition $B \subseteq A$.
Since both scenarios lead to a contradiction, the initial assumption that $A \ne B$ must be false. Therefore, $A = B$.

## 3. Empty and Universal Sets

### Empty Set
*   **Definition**: The **empty set**, denoted $\emptyset$ or $ \{\} $, is a unique set that contains no elements.
*   **Property**: The empty set is a subset of every set. That is, for any set $A$, $\emptyset \subseteq A$.

### Universal Set
*   **Definition**: The **universal set**, denoted $\Omega$ (or $S$ for sample space in probability), is the set containing all possible elements relevant to a particular context or problem.
*   **Property**: Every set $A$ under consideration in that context is a subset of the universal set, i.e., $A \subseteq \Omega$. The universal set is also a subset of itself.

## 4. Set Operations: Union

### Finite Union
*   **Definition**: The **union** of two sets $A$ and $B$, denoted $A \cup B$, is the set containing all elements that are in $A$ **or** in $B$ (or both).
    $$ A \cup B = \{\xi \mid \xi \in A \text{ or } \xi \in B\} $$
*   **Example 1**: If $A = \{1, 2, 3, 4\}$ and $B = \{1, 5, 6\}$, then $A \cup B = \{1, 2, 3, 4, 5, 6\}$.
*   **Example 2**: If $A = \{t \mid 3 < t < 4\}$ and $B = \{t \mid t \ge 3.5\}$, then $A \cup B = \{t \mid t > 3\}$.

### Infinite Union
*   **Definition**: The **infinite union** of a sequence of sets $A_1, A_2, \dots, A_n, \dots$ is denoted $\bigcup_{n=1}^\infty A_n$. An element $x$ belongs to this union if $x$ is in at least one of the sets $A_n$.
    $$ \bigcup_{n=1}^\infty A_n = \{x \mid \exists n \in \mathbb{N}, x \in A_n \} $$
*   **Example**: Consider the sequence of sets $A_n = [0, 1 - 1/n]$ for $n \in \mathbb{N}$.
    *   $A_1 = [0, 0]$
    *   $A_2 = [0, 0.5]$
    *   $A_3 = [0, 2/3]$
    *   As $n \to \infty$, the upper bound $1 - 1/n$ approaches $1$. The union accumulates all points up to, but not including, $1$.
    *   Thus, $\bigcup_{n=1}^\infty A_n = [0, 1)$.

## 5. Set Operations: Intersection

### Finite Intersection
*   **Definition**: The **intersection** of two sets $A$ and $B$, denoted $A \cap B$, is the set containing all elements that are in $A$ **and** in $B$.
    $$ A \cap B = \{\xi \mid \xi \in A \text{ and } \xi \in B\} $$
*   **Example 1**: If $A = \{1, 2, 3, 4\}$ and $B = \{1, 5, 6\}$, then $A \cap B = \{1\}$.
*   **Example 2**: If $A = \{t \mid 3 < t < 4\}$ and $B = \{t \mid t \ge 3.5\}$, then $A \cap B = \{t \mid 3.5 \le t < 4\}$.

### Infinite Intersection
*   **Definition**: The **infinite intersection** of a sequence of sets $A_1, A_2, \dots, A_n, \dots$ is denoted $\bigcap_{n=1}^\infty A_n$. An element $x$ belongs to this intersection if $x$ is in **all** of the sets $A_n$.
    $$ \bigcap_{n=1}^\infty A_n = \{x \mid \forall n \in \mathbb{N}, x \in A_n \} $$
*   **Example**: Consider the sequence of sets $A_n = [0, 1 + 1/n]$ for $n \in \mathbb{N}$.
    *   $A_1 = [0, 2]$
    *   $A_2 = [0, 1.5]$
    *   $A_3 = [0, 4/3]$
    *   As $n \to \infty$, the upper bound $1 + 1/n$ approaches $1$. The intersection must contain only elements that are common to *all* these sets. The common interval shrinks to include only elements from $0$ up to $1$.
    *   Thus, $\bigcap_{n=1}^\infty A_n = [0, 1]$.

## 6. Set Operations: Complement and Difference

### Complement
*   **Definition**: The **complement** of a set $A$, denoted $A^c$ or $A'$, is the set of all elements in the universal set $\Omega$ that are not in $A$.
    $$ A^c = \{\xi \mid \xi \in \Omega \text{ and } \xi \notin A\} $$
*   **Example**: Let $\Omega = \{\text{integers}\}$ and $A = \{\text{even integers}\}$. Then $A^c = \{\text{odd integers}\}$.

### Set Difference
*   **Definition**: The **difference** of set $A$ and set $B$, denoted $A \setminus B$ or $A - B$, is the set of all elements that are in $A$ but not in $B$.
    $$ A \setminus B = \{\xi \mid \xi \in A \text{ and } \xi \notin B\} $$
*   It can also be expressed in terms of intersection and complement: $A \setminus B = A \cap B^c$.

## 7. Disjoint Sets and Partitions

### Disjoint Sets
*   **Definition**: Two sets $A$ and $B$ are said to be **disjoint** (or mutually exclusive) if their intersection is the empty set, i.e., $A \cap B = \emptyset$. They share no common elements.
*   **For a collection of sets**: A collection of sets $\{A_1, A_2, \dots, A_n\}$ is said to be disjoint (or mutually exclusive) if $A_i \cap A_j = \emptyset$ for all $i \ne j$.

### Partition
*   **Definition**: A collection of sets $\{A_1, A_2, \dots, A_n\}$ forms a **partition** of the universal set $\Omega$ if it satisfies two conditions:
    1.  **Non-overlap (Disjoint)**: The sets are mutually exclusive, meaning $A_i \cap A_j = \emptyset$ for all $i \ne j$.
    2.  **Decomposition (Completeness)**: The union of all sets equals the universal set, meaning $A_1 \cup A_2 \cup \dots \cup A_n = \Omega$.

## 8. Laws of Set Operations

These fundamental laws govern how set operations interact and are crucial for simplifying and manipulating set expressions.

### Commutative Laws
The order of sets in union or intersection does not affect the result.
*   $A \cap B = B \cap A$
*   $A \cup B = B \cup A$

### Associative Laws
For three sets, the grouping of sets in union or intersection does not affect the result.
*   $A \cup (B \cup C) = (A \cup B) \cup C$
*   $A \cap (B \cap C) = (A \cap B) \cap C$

### Distributive Laws
These laws describe how union and intersection distribute over each other.
*   $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
*   $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

### De Morgan's Laws
These laws relate complements of unions and intersections, providing a way to transform one into the other.
*   $(A \cap B)^c = A^c \cup B^c$ (The complement of an intersection is the union of the complements)
*   $(A \cup B)^c = A^c \cap B^c$ (The complement of a union is the intersection of the complements)

## Quick Summary

This lecture provided a foundational introduction to set theory, a prerequisite for understanding probability. We defined what a set is, distinguished between finite, countable, and uncountable sets, and clarified set membership. Key concepts included subsets (proper and improper), the empty set, and the universal set. We then thoroughly explored fundamental set operations: union (finite and infinite), intersection (finite and infinite), complement, and set difference. Finally, we defined disjoint sets and partitions, concluding with a review of essential set operation laws, namely commutative, associative, distributive, and De Morgan's laws. These principles form the bedrock for constructing more complex probabilistic models.
