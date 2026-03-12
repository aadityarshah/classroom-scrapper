---
title: Autograd
lecture_number: 5
lecture_name: Automatic Differentiation (Autograd)
category: 'Module 2: Learning'
sidebar_label: Lecture 5
sidebar_position: 5
course: ES119
topic:
- Automatic Differentiation
- Backpropagation
- Computational Graphs
tags:
- Autograd
- Automatic Differentiation
- Backpropagation
- Gradients
- Deep Learning
- Machine Learning
- Optimization
summary: A concise overview of Automatic Differentiation (Autograd), its mechanism
  using computational graphs and the chain rule for efficient gradient computation,
  and why it's superior to finite differences in machine learning.
math: true
---


# Automatic Differentiation (Autograd)

## What is Autograd?

Autograd, or Automatic Differentiation (AD), is a set of techniques used to compute derivatives of functions numerically. It's distinct from symbolic differentiation (which produces an explicit formula) and numerical differentiation (like finite differences). Autograd is fundamental for optimizing complex functions, especially in machine learning and deep learning, by efficiently and accurately calculating gradients.

## What Autograd Is Not

### Finite Differences

Numerical differentiation methods approximate derivatives by evaluating the function at perturbed points.

*   **One-Sided Difference**:
    $$ \frac{\partial f}{\partial x_i} \approx \frac{f(x_1, \dots, x_i+h, \dots, x_N) - f(x_1, \dots, x_i, \dots, x_N)}{h} $$
*   **Two-Sided (Central) Difference**:
    $$ \frac{\partial f}{\partial x_i} \approx \frac{f(x_1, \dots, x_i+h, \dots, x_N) - f(x_1, \dots, x_i-h, \dots, x_N)}{2h} $$

### Challenges with Finite Differences

1.  **Computational Expense**: For a function $f: \mathbb{R}^N \to \mathbb{R}$, computing all partial derivatives using finite differences requires $O(N)$ forward passes, which is infeasible for high-dimensional inputs (e.g., neural network weights).
2.  **Numerical Instability**: Prone to floating-point errors (round-off error for small $h$, truncation error for large $h$).

## Computational Graphs

Autograd leverages computational graphs to represent mathematical expressions.

*   **Nodes**: Represent operations (e.g., addition, multiplication, exponentiation, trigonometric functions).
*   **Edges**: Represent variables or tensors, showing data dependencies between operations.

A complex function is decomposed into a sequence of elementary operations. The forward pass evaluates the function by traversing the graph from inputs to output, storing intermediate values.

## Backpropagation through Computational Graphs

Backpropagation is the application of the chain rule in reverse-mode automatic differentiation. It efficiently computes gradients by traversing the computational graph backward from the output to the inputs.

### Core Logic: The Chain Rule

For a function $J$ composed of intermediate functions, say $J = g(z)$ where $z = f(x, y)$, the gradients of $J$ with respect to $x$ and $y$ are:

*   $ \frac{\partial J}{\partial x} = \frac{\partial J}{\partial z} \cdot \frac{\partial z}{\partial x} $
*   $ \frac{\partial J}{\partial y} = \frac{\partial J}{\partial z} \cdot \frac{\partial z}{\partial y} $

This is broken down into two parts at each node:

1.  **Upstream Gradient**: $ \frac{\partial J}{\partial z} $ (the gradient of the final output $J$ with respect to the output of the current operation $z$). This comes "from upstream" (later in the graph).
2.  **Local Gradient**: $ \frac{\partial z}{\partial x} $ or $ \frac{\partial z}{\partial y} $ (the derivative of the current operation's output $z$ with respect to its inputs $x$ or $y$). These are known for all elementary operations.

### Downstream Gradient Calculation

The gradient with respect to a node's input (its "downstream" gradient) is the product of the upstream gradient and the local gradient.

$$ \text{Downstream Gradient} = \text{Upstream Gradient} \times \text{Local Gradient} $$

This process is repeated iteratively backward through the graph until gradients for all input variables are computed.

## How Autograd Works

1.  **Forward Pass**: The computation performs the usual forward evaluation of the function. During this process, the computational graph is built, and all intermediate values and the local gradients for each elementary operation are recorded.
2.  **Backward Pass (Backpropagation)**: Starting from the final output (which has an initial upstream gradient of 1 with respect to itself), the algorithm traverses the graph backward. At each node, it takes the incoming (upstream) gradient, multiplies it by the local gradient of that node's operation with respect to its inputs, and passes these new gradients further backward to the preceding nodes. If a node has multiple outgoing paths, its upstream gradient is the sum of the gradients from all paths that lead to the final output.

Autograd libraries (like PyTorch Autograd, TensorFlow Autodiff) implement this by automatically creating the computational graph and performing the backward pass. They typically have a predefined set of elementary operations and their analytical derivatives.

## Why it Matters

Autograd is crucial for modern machine learning because it provides:

*   **Efficiency**: Computes all gradients in $O(1)$ forward and $O(1)$ backward passes (relative to the operations in the graph), regardless of the number of input variables $N$. This is vastly more efficient than finite differences for high-dimensional models.
*   **Accuracy**: Computes exact analytical gradients, avoiding the numerical errors inherent in finite differences.
*   **Flexibility**: Automatically handles complex, nested, and conditional computations, as long as they are composed of differentiable elementary operations.

This efficiency and accuracy are vital for training large-scale models using gradient-based optimization algorithms (e.g., Stochastic Gradient Descent, Adam).

## Quick Summary

Autograd is a powerful technique for computing exact gradients of complex functions efficiently by decomposing them into a computational graph of elementary operations. It performs a forward pass to build the graph and store intermediate values and local gradients, followed by a backward pass (backpropagation) that iteratively applies the chain rule using upstream and local gradients. This approach overcomes the computational cost and numerical instability of finite differences, making it indispensable for training machine learning models.