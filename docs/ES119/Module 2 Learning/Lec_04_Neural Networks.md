---
title: Multi-Layer Perceptrons and the Paradigm Shift
lecture_number: 4
lecture_name: Multi-Layer Perceptrons
category: 'Module 2: Learning'
sidebar_label: Lecture 4
sidebar_position: 4
course: ES119 Principles of AI
last_updated: "16 March 2026"
topic:
- Neural Network Paradigms
- Perceptron Architecture
- Linear Separability
- Activation Functions
- Forward Propagation Vectorization
tags:
- Perceptron
- XOR Problem
- ReLU
- Sigmoid
- Matrix Calculus
summary: This lecture explores the fundamental shift from hand-crafted feature engineering to automated feature learning via Multi-Layer Perceptrons (MLPs), detailing the mathematics of artificial neurons and the vectorization of forward propagation.
math: true
---


## The Paradigm Shift in Machine Learning

Historically, machine learning involved a two-step process where experts designed "hand-crafted" features (e.g., counting horizontal lines or pixel intensity for digit recognition) which were then fed into a trainable classifier.

1.  **Traditional Machine Learning**: Input $\rightarrow$ **Hand-Crafted Feature Extractor** $\rightarrow$ **Trainable Classifier** $\rightarrow \hat{y}$.
2.  **Neural Network Paradigm**: Input $\rightarrow$ **Trainable Feature Learner (Hierarchical)** $\rightarrow$ **Trainable Classifier** $\rightarrow \hat{y}$.

In NNs, the model automatically learns **Low-Level Features** (edges, blobs) in early layers and composes them into **High-Level Features** (shapes, objects) in deeper layers. This entire pipeline is trainable end-to-end.

---

## The Artificial Perceptron

Developed by Rosenblatt in the 1960s (inspired by McCulloch & Pitts), the perceptron is the simplest form of an artificial neuron.

### Mathematical Definition
A perceptron takes multiple binary (or real) inputs $x_1, x_2, \dots, x_d$, applies weights $w_i$, adds a bias $b$, and passes the sum through a step function.

$$
\hat{y} = 
\begin{cases} 
0 & \text{if } \sum w_i x_i + b \leq 0 \\
1 & \text{if } \sum w_i x_i + b > 0 
\end{cases}
$$

### Components of a Neuron
1.  **Summation ($\Sigma$)**: The linear combination of inputs and weights plus bias: $z = \sum w_i x_i + b$.
2.  **Activation ($\int$ or $g$ )**: A non-linear function applied to $z$. For the original perceptron, this is the **Heaviside Step Function** (or sign function).

---

## Learning Logic Gates and Linear Separability

The perceptron can represent basic boolean logic.

| Gate | $x_1$ | $x_2$ | Output ($y$) | Possible Parameters |
| :--- | :--- | :--- | :--- | :--- |
| **AND** | $\{0,1\}$ | $\{0,1\}$ | $1$ only if both $1$ | $w_1=1, w_2=1, b=-1.5$ |
| **OR** | $\{0,1\}$ | $\{0,1\}$ | $1$ if either is $1$ | $w_1=1, w_2=1, b=-0.5$ |
| **NOT** | $\{x_1\}$ | - | $1-x_1$ | $w_1=-1, b=0.5$ |
| **NAND** | $\{0,1\}$ | $\{0,1\}$ | $\neg(x_1 \land x_2)$ | $w_1=-1, w_2=-1, b=1.5$ |

### Linear Separability
- **Linearly Separable**: Data points can be perfectly divided by a single hyperplane (e.g., AND, OR).
- **Non-Linearly Separable**: Data points cannot be separated by a single line (e.g., **XOR**).

#### The XOR Problem
A single perceptron **cannot** solve XOR because the decision boundary required is non-linear.
- **Solution 1**: Hand-craft non-linear features (e.g., $x_1 \bar{x}_2$ and $\bar{x}_1 x_2$).
- **Solution 2**: Use a Multi-Layer Perceptron (MLP) to learn these feature combinations automatically.

---

## Activation Functions

To use Gradient Descent (Backpropagation), we need **differentiable** non-linearities, as the step function's derivative is zero almost everywhere.

### Standard Activations
1.  **Sigmoid**: $g(z) = \frac{1}{1 + e^{-z}}$
    - Output range: $(0, 1)$.
    - Useful for probabilistic estimates.
2.  **Tanh**: $g(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$
    - Output range: $(-1, 1)$.
    - Useful if data is transformed to have mean $\approx 0$.
3.  **ReLU (Rectified Linear Unit)**: $g(z) = \max(0, z)$
    - **Game Changer**: Default choice for modern deep networks.
    - Resolves vanishing gradient issues for $z > 0$.
4.  **Leaky ReLU**: $g(z) = \max(\alpha z, z)$ where $\alpha \to 0$.
    - Ensures the neuron "learns" even for $z < 0$.

---

## Multi-Layer Perceptron (MLP) Architecture

An MLP consists of an **Input Layer** (Layer 0), one or more **Hidden Layers**, and an **Output Layer**.

### Notation
- $L$: Total number of layers.
- $N^{[l]}$: Number of units (nodes) in layer $l$.
- $a^{[l]}$: Activation vector of layer $l$ (where $a^{[0]} = x$).
- $W^{[l]}$: Weight matrix for layer $l$.
- $b^{[l]}$: Bias vector for layer $l$.

### Layerwise Computation (Vectorized)
For a specific layer $l$, the linear combination $z^{[l]}$ and activation $a^{[l]}$ are calculated as:
- $$z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}$$
- $$a^{[l]} = g(z^{[l]})$$

### Matrix Dimensions
To ensure valid matrix multiplication:
- $a^{[l]} \in \mathbb{R}^{N^{[l]} \times 1}$
- $W^{[l]} \in \mathbb{R}^{N^{[l]} \times N^{[l-1]}}$
- $b^{[l]} \in \mathbb{R}^{N^{[l]} \times 1}$

---

## Numerical Example: XOR with MLP and ReLU

Consider an MLP with 2 input units, 2 hidden units, and 1 output unit using ReLU.

**Weights/Biases for Layer 1:**
$$W^{[1]} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}, \quad b^{[1]} = \begin{bmatrix} 0 \\ -1 \end{bmatrix}$$
**Weights/Biases for Layer 2:**
$$W^{[2]} = \begin{bmatrix} 1 & -2 \end{bmatrix}, \quad b^{[2]} = [0]$$

**Case $x = [0, 0]^T$:**
1. $z^{[1]} = W^{[1]}a^{[0]} + b^{[1]} = \begin{bmatrix} 0 \\ -1 \end{bmatrix}$
2. $a^{[1]} = \text{ReLU}(z^{[1]}) = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$
3. $z^{[2]} = W^{[2]}a^{[1]} + b^{[2]} = 0 \implies \hat{y} = 0$. (Correct)

**Case $x = [0, 1]^T$:**
1. $z^{[1]} = \begin{bmatrix} 1 & 1\\ 1 & 1 \end{bmatrix} \begin{bmatrix} 0 \\ 1 \end{bmatrix} + \begin{bmatrix} 0 \\ -1 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$
2. $a^{[1]} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$
3. $z^{[2]} = [1, -2] \begin{bmatrix} 1 \\ 0 \end{bmatrix} + 0 = 1 \implies \hat{y} = 1$. (Correct)

---

## Quick Summary
- **Paradigm Shift**: Moved from hand-crafted feature engineering to hierarchical, automated feature learning.
- **The Neuron**: Computes a weighted sum of inputs plus bias, followed by a non-linear activation.
- **Linear Separability**: Single perceptrons can solve AND/OR/NAND but fail on XOR.
- **Activation Functions**: ReLU is the modern default; Sigmoid/Tanh are used for specific probabilistic or centered data needs.
- **Vectorization**: Forward propagation is expressed as $a^{[l]} = g(W^{[l]}a^{[l-1]} + b^{[l]})$, where $W^{[l]}$ has shape $(N^{[l]} \times N^{[l-1]})$.