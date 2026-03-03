---
title: k-NN Asymptotic Analysis
lecture_number: 2
lecture_name: k-NN Asymptotic Analysis
category: 'Module 1: Search and Planning'
sidebar_label: Lecture 2
sidebar_position: 2
course: "ES119: Principles of AI"
topic:
  - k-Nearest Neighbors
  - Asymptotic Analysis
  - Classification
  - Algorithm Complexity
  - Sorting Algorithms
tags:
  - Machine Learning
  - AI
  - kNN
  - Complexity Analysis
  - Data Structures
  - Algorithms
  - Classification
summary: This lecture delves into the k-Nearest Neighbors (k-NN) classification algorithm, focusing on its theoretical underpinnings and asymptotic analysis. We analyze the time and space complexity of k-NN, examine the role of sorting algorithms in its efficiency, and discuss key practical drawbacks.
math: true
---

## k-Nearest Neighbors (k-NN) Asymptotic Analysis

The k-Nearest Neighbors (k-NN) algorithm is a non-parametric, instance-based learning algorithm used for classification and regression. In this lecture, we primarily focus on its application to classification and a thorough analysis of its computational efficiency.

### 1. Introduction to k-NN Classification

The core idea of k-NN is to classify a new data point based on the labels of its $k$ closest neighbors in the training dataset.

#### 1.1 Feature Representation
Consider a classification task, such as distinguishing between "Jamun" and "Mango" fruits. Raw image data (e.g., RGB pixel values) must be converted into meaningful features. For simplicity, we can use high-level features like:
-   **Size:** The measured dimension (e.g., length in cm).
-   **Average R-value:** The average red color component across the image.

For instance, Jamuns might have an average R-value $\approx 192$, while Mangoes might have $\approx 246$. These features define a 2D space where each fruit is a data point.

#### 1.2 The k-NN Algorithm Steps
Let's formalize the k-NN classification algorithm for a test point $t$:

1.  **Training Points:** We are given a set of $n$ training points, $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$.
    *   Each feature vector $x_i$ is $d$-dimensional. For our fruit example, $x_i = (\text{size}_i, \text{avgR}_i)$, so $d=2$.
    *   Each $y_i$ is the corresponding class label. For our example, $y_i \in \{\text{Jamun}, \text{Mango}\}$.

2.  **For a new test point $t$**: We want to predict its label. The test point $t$ is also a $d$-dimensional feature vector.

3.  **Calculate Distances:** Find the distance $d_i$ between the test point $t$ and each training point $x_i$. A common choice is the Euclidean distance ($L_2$ norm):
    $$d_i = ||x_i - t||_2 = \sqrt{\sum_{j=1}^d (x_{ij} - t_j)^2}$$
    For our 2D example ($d=2$):
    $$d_i = \sqrt{(x_{i1} - t_1)^2 + (x_{i2} - t_2)^2}$$

4.  **Find $k$ Smallest Distances:** Identify the $k$ training points that have the smallest distances to the test point $t$. Let these be $x_{(1)}, x_{(2)}, \dots, x_{(k)}$ with corresponding labels $y_{(1)}, y_{(2)}, \dots, y_{(k)}$.

5.  **Assign Label:** Assign the label to the test point $t$ based on the majority class among the $k$ nearest neighbors.
    $$y_t = \text{mode}(y_{(1)}, y_{(2)}, \dots, y_{(k)})$$

### 2. Asymptotic Analysis of k-NN

Understanding the computational complexity of k-NN is crucial, especially for large datasets or high-dimensional data.

#### 2.1 Training Time Complexity
The training phase of k-NN is extremely fast. It merely involves storing the training data points and their labels. There is no explicit model building or parameter learning.
*   **Training Time: $\mathcal{O}(1)$** (or more precisely, $\mathcal{O}(nd)$ to store the data if $n$ points and $d$ dimensions are considered part of the "training" operation).

#### 2.2 Testing Time Complexity
The testing phase is where the computational cost lies. For each new test point, we must perform the following:

1.  **Calculate $n$ distances (Step 3):**
    *   For a $d$-dimensional feature vector, calculating one Euclidean distance requires $d$ subtractions, $d$ squares, $(d-1)$ additions, and one square root. This is $\mathcal{O}(d)$ operations.
    *   Since we do this for all $n$ training points, the total complexity for this step is $\mathcal{O}(nd)$.

2.  **Find $k$ smallest distances (Step 4):** This is the most critical part for efficiency.
    *   **Naive Approach:** Iteratively search for the smallest distance, remove it, and repeat $k$ times. Each linear search takes $\mathcal{O}(n)$ time. Repeating $k$ times yields a complexity of $\mathcal{O}(nk)$.
    *   **Sorting Approach:** Sort all $n$ distances and then pick the first $k$ elements. If using an efficient comparison-based sorting algorithm like Merge Sort, this takes $\mathcal{O}(n \log n)$ time.

3.  **Assign label based on majority (Step 5):**
    *   Counting the majority class among $k$ neighbors involves iterating through $k$ labels and maintaining counts. This takes $\mathcal{O}(k)$ time.

Combining these steps, the total testing time complexity depends heavily on how Step 4 is implemented:
*   **With naive $k$ searches:** $\mathcal{O}(nd + nk + k) = \mathcal{O}(nd + nk)$.
*   **With sorting all distances (e.g., Merge Sort):** $\mathcal{O}(nd + n \log n + k) = \mathcal{O}(nd + n \log n)$.

Since $k \ll n$ is usually true, and $n \log n$ is generally much smaller than $nk$ for large $n$, sorting all distances is usually more efficient than $k$ linear searches. Furthermore, specialized algorithms like Quickselect can find the $k$-th smallest element in average $\mathcal{O}(n)$ time, leading to an average case testing complexity of $\mathcal{O}(nd + n)$.

#### 2.3 Space Complexity
The k-NN algorithm is an "eager" learner in terms of storage but a "lazy" learner in terms of computation at training time. All training data must be stored for prediction.
*   **Storing Training Data:** We need to store $n$ data points, each $d$-dimensional, along with their labels. This requires $\mathcal{O}(nd)$ space.
*   **Storing Distances:** During testing, we may need to store all $n$ calculated distances (and their corresponding indices/labels) to find the $k$ smallest. This requires $\mathcal{O}(n)$ additional space.
*   **Total Space Complexity:** $\mathcal{O}(nd + n) = \mathcal{O}(nd)$.

### 3. Sorting Algorithms in k-NN (Step 4 Detailed)

To find the $k$ smallest distances efficiently, sorting algorithms are key. Let's compare two common ones:

#### 3.1 Insertion Sort
*   **Concept:** Builds the final sorted array (or list) one item at a time. It iterates through the input elements and inserts each element into its correct position in the already sorted part of the array.
*   **Example (for $n$ numbers):** Given $[8,3,5,2,9]$
    *   Start with $[8]$ (sorted part)
    *   Insert $3$: $[3,8]$
    *   Insert $5$: $[3,5,8]$
    *   Insert $2$: $[2,3,5,8]$
    *   Insert $9$: $[2,3,5,8,9]$
*   **Time Complexity:**
    *   **Best Case:** $\mathcal{O}(n)$ (when the array is already sorted).
    *   **Worst Case:** $\mathcal{O}(n^2)$ (when the array is sorted in reverse). This involves roughly $1 + 2 + \dots + (n-1) \approx n^2/2$ comparisons/swaps.
*   **Space Complexity:** $\mathcal{O}(1)$ auxiliary space (sorts in place).

#### 3.2 Merge Sort
*   **Concept:** A divide-and-conquer algorithm. It recursively divides the array into halves until it has single-element arrays (which are inherently sorted), then repeatedly merges the sorted sub-arrays to produce new sorted sub-arrays until there is only one sorted array remaining.
*   **Example (for $n$ numbers):** Given $[8,3,5,2,9,1]$
    *   Divide: $[8,3,5]$ and $[2,9,1]$
    *   ... (recursive division) ...
    *   Merge: $[3,5,8]$ and $[1,2,9]$
    *   Merge: $[1,2,3,5,8,9]$
*   **Time Complexity:**
    *   **Best Case:** $\mathcal{O}(n \log n)$.
    *   **Worst Case:** $\mathcal{O}(n \log n)$. (Consistently efficient).
*   **Space Complexity:** $\mathcal{O}(n)$ auxiliary space (for merging sub-arrays).

#### 3.3 Comparing Sorting Efficiencies
The table and plot clearly demonstrate that $n \log n$ (Merge Sort) scales much better than $n^2$ (Insertion Sort worst case) for larger input sizes $n$. While Insertion Sort might be faster for very small $n$ due to smaller constant factors, its quadratic growth makes it impractical for large datasets.

| $n$    | $n^2$        | $n \log_2 n$ |
| :----- | :----------- | :----------- |
| 10     | 100          | 33           |
| 50     | 2,500        | 282          |
| 100    | 10,000       | 664          |
| 500    | 250,000      | 4,483        |
| 1,000  | 1,000,000    | 9,966        |
| 10,000 | 100,000,000  | 132,877      |

**Why do we use "steps" (algorithmic efficiency) and not "time" for comparison?**
Actual execution time is influenced by many factors (CPU speed, memory access, programming language, compiler optimizations, system load). Algorithmic efficiency, expressed using Big-O notation, provides a machine-independent measure of how an algorithm's resource usage (time/space) grows with the input size. It focuses on the dominant term, ignoring constant factors and lower-order terms, which are often swallowed by system differences. For large datasets, the asymptotic behavior is what truly dictates performance.

### 4. Overall k-NN Analysis Revisited

Considering the $n \times d$ feature matrix $X$:

*   **Total Time Complexity (per query/test point):**
    *   Without optimized $k$-selection (naive $k$ linear searches): $\mathcal{O}(nd + nk)$.
    *   With efficient sorting (e.g., Merge Sort to sort all distances): $\mathcal{O}(nd + n \log n)$.
    *   With Quickselect (average case for finding $k$ smallest): $\mathcal{O}(nd + n)$.
    *   Typically, $k \ll n$, so sorting or Quickselect is preferred for large $n$.

*   **Total Space Complexity:** $\mathcal{O}(nd)$ (to store the entire training dataset).

### 5. Drawbacks of k-NN

Despite its simplicity and interpretability, k-NN has several practical drawbacks:

1.  **Choice of $k$:**
    *   **Too small $k$:** The model becomes highly sensitive to noise and outliers in the data, leading to a high variance and potentially overfitting.
    *   **Too large $k$:** The model's decision boundaries become overly smoothed, potentially blurring the distinctions between classes and leading to high bias and underfitting. The optimal $k$ often needs to be determined via cross-validation.

2.  **Feature Scaling Sensitivity:** Features with larger scales (e.g., "size" in cm) can disproportionately influence the distance calculation compared to features with smaller scales (e.g., "avgR" from 0-255). This requires **feature scaling** (e.g., standardization or normalization) as a crucial preprocessing step.

3.  **High Test Time and Storage Requirements:**
    *   **Lazy Learning:** The model does not learn a fixed function during training; instead, it memorizes the entire training dataset. This leads to **high storage costs** ($\mathcal{O}(nd)$).
    *   **Prediction Cost:** For every new test point, the algorithm must compare it against *all* training points. This results in **high computational cost during prediction** ($\mathcal{O}(nd)$ or $\mathcal{O}(nd + n \log n)$), especially problematic for large $n$ or high $d$. This makes k-NN unsuitable for real-time applications with large datasets. The curse of dimensionality exacerbates this problem.

## Quick Summary

k-Nearest Neighbors (k-NN) is a simple, instance-based classification algorithm. Its **training phase is $\mathcal{O}(1)$** (just storing data), making it a "lazy" learner. However, its **testing phase is computationally intensive**, requiring distance calculations to all $n$ training points for each test query. The total time complexity per test point is typically **$\mathcal{O}(nd + n \log n)$** (if sorting all distances) or **$\mathcal{O}(nd + n)$** (with Quickselect), where $n$ is the number of training points and $d$ is the dimensionality of features. The **space complexity is $\mathcal{O}(nd)$** as the entire training dataset must be stored. Key drawbacks include the sensitivity to the choice of $k$, the need for feature scaling, and high computational/storage costs during prediction, particularly in high-dimensional spaces or with large datasets.