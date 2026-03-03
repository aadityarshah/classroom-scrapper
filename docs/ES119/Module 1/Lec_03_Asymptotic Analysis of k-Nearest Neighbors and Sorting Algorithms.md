---
title: Asymptotic Analysis of k-Nearest Neighbors and Sorting Algorithms
lecture_number: 3
lecture_name: Asymptotic Analysis of k-Nearest Neighbors and Sorting Algorithms
category: 'Module 1: Search and Planning'
sidebar_label: Lecture 3
sidebar_position: 3
course: 'ES119: Principles of AI'
topic:
- k-Nearest Neighbors
- Asymptotic Analysis
- Big-O Notation
- Sorting Algorithms
tags:
- k-NN
- Nearest Neighbor
- Asymptotic Complexity
- Big-O
- Sorting Algorithms
- Merge Sort
- Insertion Sort
- Time Complexity
- Space Complexity
- AI
summary: This lecture introduces the k-Nearest Neighbors algorithm, delves into its
  computational complexity using asymptotic analysis, and compares the efficiency
  of different sorting algorithms like Insertion Sort and Merge Sort. We explore the
  significance of Big-O notation for understanding algorithmic scalability and discuss
  practical considerations and enhancements for k-NN, including adaptive and condensed
  variants.
math: true
---


# Introduction to k-Nearest Neighbors (k-NN)

The $k$-Nearest Neighbors ($k$-NN) algorithm is a non-parametric, instance-based learning algorithm used for classification and regression. It's a lazy learner, meaning it does not construct a general internal model during training; instead, it memorizes the training dataset.

## 1. The k-NN Algorithm Steps

Consider a dataset of $n$ training points, $\{(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)\}$, where each $x_i$ is a $d$-dimensional feature vector and $y_i$ is its corresponding label. For instance, in our example:
-   $x_i$: A feature vector, typically $(x_{i1}, x_{i2})$ representing $(\text{size}_i, \text{avgR}_i)$.
-   $y_i$: A label, such as $\{J, M\}$ (Jamun, Mango).

To classify a new test point $t = (t_1, t_2, \dots, t_d)$:

1.  **Calculate Distances:** Compute the distance between $t$ and every training point $x_i$ in the dataset. A common choice is the Euclidean distance:
    $$d_i = ||x_i - t||_2 = \sqrt{\sum_{j=1}^{d} (x_{ij} - t_j)^2}$$
    For 2D data, this simplifies to:
    $$d_i = \sqrt{(x_{i1} - t_1)^2 + (x_{i2} - t_2)^2}$$

2.  **Find $k$ Smallest Distances:** Identify the $k$ training points that have the smallest distances to the test point $t$.

3.  **Assign Label:** Assign the label to the test point $t$ based on the majority class among its $k$ nearest neighbors. In regression tasks, this might involve averaging the values of the $k$ neighbors.

## 2. General Complexity Analysis for k-NN

Let's analyze the computational resources (time and space) required by the $k$-NN algorithm.

### 2.1 Data Representation
Assume the training data $X$ is an $n \times d$ matrix, where $n$ is the number of training instances and $d$ is the dimensionality of each instance:
$$X = \begin{pmatrix} x_1^\top \\ x_2^\top \\ \vdots \\ x_n^\top \end{pmatrix}$$
Each $x_i$ is a $d$-dimensional vector.

### 2.2 Time Complexity of Distance Calculation (Step 1)
For each training point $x_i$, calculating the Euclidean distance to the test point $t$ involves:
-   $d$ subtractions.
-   $d$ squarings.
-   $d-1$ additions.
-   1 square root (often optimized away if only comparing distances).
This is approximately $\mathcal{O}(d)$ operations per training point.
Since there are $n$ training points, the total time for Step 1 is $\mathcal{O}(nd)$.

### 2.3 Time Complexity of Finding $k$ Smallest Distances (Step 2)

Given a list of $n$ distances $d_1, d_2, \dots, d_n$, we need to find the $k$ smallest ones.

#### 2.3.1 Approach 1: Iterative Search
One naive approach is to repeatedly search for the smallest element $k$ times.
-   First search: Find the smallest element in $n$ steps ($\mathcal{O}(n)$).
-   Second search: Find the next smallest in $n-1$ steps (after removing the first smallest) ($\mathcal{O}(n)$).
-   Repeat $k$ times.
The total time complexity for this approach is $\mathcal{O}(nk)$.

#### 2.3.2 Approach 2: Sorting
Another approach is to sort all $n$ distances and then pick the first $k$ elements.

**Insertion Sort:**
-   **Mechanism:** Builds the final sorted array (or list) one item at a time. It iterates through the input elements and inserts each element into its correct position in the already sorted part of the array.
-   **Complexity:**
    -   Best Case: $\mathcal{O}(n)$ (when the array is already sorted).
    -   Worst Case: $\mathcal{O}(n^2)$ (when the array is sorted in reverse order).
    -   Average Case: $\mathcal{O}(n^2)$.
-   **Space:** $\mathcal{O}(1)$ (sorts in place).

**Merge Sort:**
-   **Mechanism:** A divide-and-conquer algorithm. It recursively divides the array into halves until it has single-element arrays (which are sorted by definition), and then merges those halves back together in sorted order.
-   **Complexity:**
    -   Best Case: $\mathcal{O}(n \log n)$.
    -   Worst Case: $\mathcal{O}(n \log n)$.
    -   Average Case: $\mathcal{O}(n \log n)$.
-   **Space:** $\mathcal{O}(n)$ (due to temporary arrays used during merging).

#### 2.3.3 Comparison of Sorting Algorithms
Let's compare the growth of $n^2$ (Insertion Sort) and $n \log_2 n$ (Merge Sort) for increasing input size $n$:

| $n$     | $n^2$         | $n \log_2 n$ |
| :------ | :------------ | :----------- |
| 10      | 100           | 33           |
| 50      | 2,500         | 282          |
| 100     | 10,000        | 664          |
| 500     | 250,000       | 4,483        |
| 1,000   | 1,000,000     | 9,966        |
| 10,000  | 100,000,000   | 132,877      |

This table clearly illustrates that $n \log_2 n$ grows significantly slower than $n^2$ for larger $n$.

### 2.4 Why Algorithmic Efficiency over Absolute Time?
When comparing algorithms, we focus on the number of "steps" or operations rather than absolute execution time. This is because:
-   **System Differences:** Actual execution time can vary drastically based on hardware, operating system, programming language, compiler, and other concurrent processes.
-   **Algorithmic Efficiency:** The number of steps directly reflects the algorithm's inherent efficiency, independent of the underlying system.

While a slower algorithm might appear faster for small input sizes due to constant factors or better hardware, the algorithm with better asymptotic complexity will eventually outperform it as the input size $n$ grows. This emphasizes the importance of understanding how algorithms scale.

### 2.5 Overall Time Complexity of k-NN
Combining the steps:

-   Distance calculation: $\mathcal{O}(nd)$.
-   Finding $k$ smallest distances:
    -   Using iterative search: $\mathcal{O}(nk)$.
    -   Using efficient sorting (e.g., Merge Sort): $\mathcal{O}(n \log n)$.
    -   Using a min-heap or selection algorithm (e.g., Quickselect) can find the $k$-th smallest element and thus the $k$ smallest elements in $\mathcal{O}(n)$ time on average. If $k$ elements are extracted from a min-heap, it's $\mathcal{O}(n + k \log k)$.

So, the total time complexity for $k$-NN depends on how Step 2 is implemented:
1.  **Iterative Search for $k$ smallest:** $\mathcal{O}(nd + nk + k) \equiv \mathcal{O}(nd + nk)$.
2.  **Sorting all distances (e.g., Merge Sort):** $\mathcal{O}(nd + n \log n + k) \equiv \mathcal{O}(nd + n \log n)$.
3.  **Using Quickselect/Min-Heap for $k$ smallest:** $\mathcal{O}(nd + n)$. (assuming $k \log k$ is dominated by $n$ or $k$ is small).

Typically, $k \ll n$.
If $k$ is small constant, $nk$ becomes $n$, so $\mathcal{O}(nd + n)$.
If $d$ is also small constant, the dominant term becomes $n$.

### 2.6 Space Complexity of k-NN
The $k$-NN algorithm is instance-based, meaning it needs to store all training data to make predictions.
-   Storing the $n \times d$ training matrix $X$: $\mathcal{O}(nd)$.
-   Storing distances: $\mathcal{O}(n)$.
The dominant space complexity is $\mathcal{O}(nd)$.

## 3. Asymptotic Notation: Big-O

Asymptotic notation provides a way to describe the limiting behavior of functions, particularly the growth rate of an algorithm's running time or space requirements as the input size grows.

### 3.1 Definition of Big-O Notation
A function $f(n)$ is said to be $\mathcal{O}(g(n))$ (read as "Big-O of $g(n)$") if there exist positive constants $c$ and $n_0$ such that:
$$f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0$$
This means that for sufficiently large input sizes ($n \ge n_0$), the growth rate of $f(n)$ is bounded above by some constant multiple of $g(n)$. In other words, $g(n)$ is an asymptotic upper bound for $f(n)$. It implies that $g(n)$ is "not more efficient" (or potentially less efficient or equally efficient) than $f(n)$ in terms of growth rate.

### 3.2 Examples
Let's apply the definition to common scenarios:

-   If $f(n) = n^2 + 1000$ and $g(n) = n^2$: Is $f(n) = \mathcal{O}(n^2)$? Yes, for $c=2$ and $n_0=1000$, $n^2 + 1000 \le 2n^2$ for $n \ge 1000$. So, $f(n) = \mathcal{O}(n^2)$.
-   If $f(n) = 100n^2$ and $g(n) = n^2$: Is $f(n) = \mathcal{O}(n^2)$? Yes, for $c=100$ and $n_0=1$, $100n^2 \le 100n^2$ for $n \ge 1$. So, $f(n) = \mathcal{O}(n^2)$.
-   If $f(n) = 100n^2 + 1000$ and $g(n) = n^2$: Is $f(n) = \mathcal{O}(n^2)$? Yes, for $c=101$ and $n_0=1000$, $100n^2 + 1000 \le 101n^2$ for $n \ge 1000$. So, $f(n) = \mathcal{O}(n^2)$. (Lower-order terms and constant factors are dropped).
-   If $f(n) = n^2 + n$ and $g(n) = n^2$: Is $f(n) = \mathcal{O}(n^2)$? Yes, for $c=2$ and $n_0=1$, $n^2 + n \le 2n^2$ for $n \ge 1$. So, $f(n) = \mathcal{O}(n^2)$.
-   If $f(n) = n^2$ and $g(n) = n \log n$: Is $f(n) = \mathcal{O}(n \log n)$? No, because $n^2$ grows faster than $n \log n$.
-   If $f(n) = n^3 + 20n + 1$ and $g(n) = n^2$: Is $f(n) = \mathcal{O}(n^2)$? No, because $n^3$ grows faster than $n^2$.
-   If $f(n) = n^3 + 20n + 1$ and $g(n) = n^4$: Is $f(n) = \mathcal{O}(n^4)$? Yes, for $c=1$ and $n_0 \approx 20$, $n^3 + 20n + 1 \le n^4$ for $n \ge \text{some } n_0$. Here $n^4$ provides a valid upper bound.

The Big-O notation focuses on the term that grows fastest as $n$ approaches infinity, disregarding constant coefficients and lower-order terms.

## 4. Practical Considerations and Enhancements for k-NN

### 4.1 Choosing $k$
The choice of $k$ is crucial and impacts the algorithm's performance:
-   **Small $k$:** Makes the model sensitive to noise and outliers (low bias, high variance). It captures local structure well but can overfit.
-   **Large $k$:** Smooths out the decision boundary, reducing the impact of noise but potentially overlooking fine-grained local patterns (high bias, low variance). It can lead to underfitting.
-   **Class Imbalance:** In imbalanced datasets, a large $k$ might lead to the majority class dominating predictions, even for points closer to the minority class.
-   **Local Structure:** The optimal $k$ often reflects the underlying density and distribution of data points.

### 4.2 Other Drawbacks
-   **Feature Scaling:** Different features (e.g., 'size' vs. 'avgR') often have different scales. Distance metrics are sensitive to these scales, meaning features with larger ranges can disproportionately influence the distance calculation. **Normalization or standardization of features is critical.**
-   **High Test Time and Storage Requirements:** As seen in the complexity analysis, $k$-NN requires significant computational time ($\mathcal{O}(nd)$ or $\mathcal{O}(nd + n \log n)$) and storage ($\mathcal{O}(nd)$) for large $n$ and $d$. This makes it computationally expensive for large datasets, particularly during inference, and susceptible to the "Curse of Dimensionality."

### 4.3 Adaptive k-NN
Instead of using a fixed $k$ for all test points, adaptive $k$-NN chooses a specific $k(x)$ for each new test point $x$.
-   One approach is to select $k(x)$ based on the number of points within a certain $\epsilon$-radius around $x$.
-   Another approach could be to choose $k(x)$ to maximize a "confidence" score for the prediction. This allows for local adaptation of the neighborhood size.

### 4.4 Condensed k-NN
Condensed $k$-NN aims to reduce the memory footprint and potentially the inference time by finding a smaller, representative subset of the training data.
The general idea:
1.  Start with an empty condensed set $C$.
2.  Iterate through the original training set $T$.
3.  For each point $x$ in $T$:
    a.  Apply the $k$-NN algorithm using only the points currently in $C$ to predict $x$'s label.
    b.  If the prediction for $x$ is incorrect, add $x$ to $C$.
4.  Repeat until no more points are added to $C$ in an iteration, or a stopping criterion is met.
5.  Finally, during test time, use only the condensed set $C$ for predictions.

This method helps prune redundant training instances, making the model more efficient while striving to maintain predictive performance.

---

## Quick Summary

This lecture covered the k-Nearest Neighbors (k-NN) algorithm, detailing its step-by-step process for classification based on distance metrics and majority voting. We then performed a thorough complexity analysis, distinguishing between the $\mathcal{O}(nd)$ cost for distance calculations and various costs for finding the $k$ nearest neighbors ($\mathcal{O}(nk)$ for iterative search, $\mathcal{O}(n \log n)$ for sorting-based methods). The lecture emphasized the critical role of **Big-O notation** in evaluating algorithmic scalability by providing an asymptotic upper bound on growth rates, highlighting why it's preferred over absolute time measurements. Finally, we discussed practical challenges of k-NN, such as **feature scaling** and high computational demands, and introduced **adaptive k-NN** and **condensed k-NN** as strategies to address these limitations.