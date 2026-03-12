---
title: 'Supervised Learning: Linear & Logistic Regression'
lecture_number: 3
lecture_name: Linear & Logistic Regression Deep Dive
category: 'Module 2: Learning'
sidebar_label: Lecture 3
sidebar_position: 3
course: ES119
topic:
- Supervised Learning
- Linear Regression
- Logistic Regression
- Gradient Descent
- Feature Scaling
- PyTorch Basics
tags:
- supervised learning
- linear regression
- logistic regression
- gradient descent
- optimization
- feature scaling
- pytorch
- machine learning
- classification
- regression
summary: A concise overview of supervised learning techniques, focusing on the principles
  of linear and logistic regression, their optimization using gradient descent, the
  importance of feature scaling, and their implementation paradigms in scikit-learn
  and PyTorch.
math: true
---


## Introduction: Supervised Learning Recap

Supervised learning aims to **learn a function** ($f$) that maps input **features** ($\mathbf{X}$) to output **labels** ($\mathbf{Y}$).
The nature of the label defines the task:
*   **Regression:** $\mathbf{Y}$ is a continuous number (e.g., predicting house price).
*   **Classification:** $\mathbf{Y}$ is a discrete category (e.g., spam or not spam).

## Part 1: Linear Regression - Finding the Best Line

Linear Regression models a **linear relationship** between features and a continuous target variable.

### The Linear Model
For a single feature $x$:
$$ \hat{y} = w x + b $$
For multiple features $\mathbf{x} = [x_1, x_2, \dots, x_d]^T$:
$$ \hat{y} = \sum_{i=1}^{d} w_i x_i + b = \mathbf{w}^T \mathbf{x} + b $$
The bias term ($b$) can be absorbed into the weight vector $\mathbf{w}$ by augmenting the feature vector $\mathbf{x}$ with a constant '1': $\mathbf{x}_{aug} = [1, x_1, x_2, \dots, x_d]^T$, such that $\mathbf{w}_{aug} = [b, w_1, w_2, \dots, w_d]^T$. The prediction then becomes $\hat{y} = \mathbf{w}_{aug}^T \mathbf{x}_{aug}$.

### Interpreting Parameters
*   **Weight ($w_i$):** Represents the sensitivity; how much $\hat{y}$ changes for a unit increase in $x_i$, holding other features constant.
*   **Bias ($b$):** The baseline output when all features are zero.

## Part 2: Finding the Best Weights - The Optimization Problem

The goal is to find the optimal weights ($\mathbf{w}$) that **minimize the total error** between predicted values ($\hat{y}$) and actual values ($y$).

### Loss Function: Mean Squared Error (MSE)
The most common loss function for regression is MSE:
$$ J(\mathbf{w}) = MSE = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 $$
**Why MSE?**
*   Errors do not cancel out (due to squaring).
*   Penalizes larger errors more significantly.
*   Possesses desirable mathematical properties (differentiable and convex), simplifying optimization.

### Optimization Methods

1.  **Normal Equation:**
    *   **What it is:** A direct, closed-form mathematical solution for finding optimal $\mathbf{w}$.
    *   **Formula:** $\mathbf{w} = (X^T X)^{-1} X^T \mathbf{y}$ (where $X$ is the design matrix with a column of ones for bias).
    *   **Why it matters:** Provides an exact solution in a single step.
    *   **Limitations:** Requires matrix inversion ($O(d^3)$ computational complexity), which is impractical for datasets with many features ($d$).

2.  **Gradient Descent (GD):**
    *   **What it is:** An iterative optimization algorithm that updates $\mathbf{w}$ by taking small steps in the direction opposite to the gradient of the loss function.
    *   **Gradient:** A vector of partial derivatives, indicating the direction of the steepest increase in the loss function. To minimize, we move in the opposite direction.
    *   **Update Rule:** $\mathbf{w}_{new} = \mathbf{w}_{old} - \alpha \nabla_{\mathbf{w}} J(\mathbf{w})$
        *   $\alpha$ (Learning Rate): A crucial hyperparameter controlling the step size.
        *   $\nabla_{\mathbf{w}} J(\mathbf{w})$: The gradient of the loss function with respect to $\mathbf{w}$.
    *   **Why it matters:**
        *   Scalable to large datasets and numerous features.
        *   The fundamental optimization algorithm for neural networks and many complex models.
    *   **Learning Rate Importance:**
        *   Too small: Slow convergence.
        *   Just right: Efficient convergence.
        *   Too large: Overshoots the minimum, leading to divergence or unstable training.

## Part 3: Feature Scaling

### Why Scaling Matters
Features with vastly different numerical scales can lead to an inefficient and slow convergence of Gradient Descent. Larger-scale features can dominate the gradient calculations, causing the optimization path to zigzag.

### Common Scaling Methods
1.  **Standardization (Z-score normalization):** Transforms data to have a mean of 0 and a standard deviation of 1.
    $$ x' = \frac{x - \mu}{\sigma} $$
2.  **Min-Max Scaling:** Rescales data to a fixed range, typically $[0, 1]$.
    $$ x' = \frac{x - x_{min}}{x_{max} - x_{min}} $$

### Important Considerations
*   Always **fit the scaler on the training data only**, then use the *same fitted scaler* to transform both the training and test datasets. This prevents **data leakage** from the test set.
*   **When to Scale:** Essential for gradient descent-based algorithms (Linear/Logistic Regression, Neural Networks) and distance-based algorithms (K-Nearest Neighbors). Not necessary for tree-based models (Decision Trees, Random Forests) which are scale-invariant.

## Part 4: From sklearn to PyTorch - Building the Bridge

Both `sklearn` and `PyTorch` implement these concepts, but with different levels of abstraction and control.

### sklearn Paradigm
*   Provides high-level, production-ready implementations for standard machine learning algorithms.
*   Often uses highly optimized solvers (e.g., SVD for Linear Regression's Normal Equation equivalent) or optimized versions of Gradient Descent internally.
*   Simple and concise for common tasks.

### PyTorch Paradigm
*   A deep learning framework offering lower-level building blocks for defining models, loss functions, and optimizers.
*   Provides explicit control over the **5-step training loop**:
    1.  **Forward Pass:** Compute predictions (`model(X)`).
    2.  **Compute Loss:** Evaluate the chosen loss function (`criterion(y_pred, y)`).
    3.  **Zero Gradients:** Clear gradients from the previous iteration (`optimizer.zero_grad()`).
    4.  **Backward Pass:** Compute gradients of the loss with respect to model parameters (`loss.backward()`).
    5.  **Update Weights:** Adjust model parameters using the computed gradients and learning rate (`optimizer.step()`).
*   **Why it matters:** Foundation for designing and training complex neural networks, offers GPU acceleration and high customization.

## Part 5: Logistic Regression - From Numbers to Categories

Logistic Regression is a **classification algorithm** that uses a linear model combined with a **sigmoid function** to predict probabilities.

### The Sigmoid Function
Linear regression outputs values from $(-\infty, +\infty)$, which are unsuitable for probabilities. The sigmoid function "squashes" any real number into the range $(0, 1)$:
$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$
**Why it matters:** Converts a raw linear score ($z$) into a probability ($P \in (0,1)$).
*   Large positive $z \implies \sigma(z) \approx 1$
*   $z=0 \implies \sigma(z) = 0.5$
*   Large negative $z \implies \sigma(z) \approx 0$

### Logistic Regression Model
1.  **Linear Score:** Compute a linear combination of features: $z = \mathbf{w}^T \mathbf{x} + b$.
2.  **Probability:** Apply the sigmoid function to the score: $P(Y=1 | \mathbf{x}) = \sigma(z)$.
3.  **Decision Rule:** Classify as 1 if $P(Y=1 | \mathbf{x}) > \text{threshold}$ (commonly 0.5), otherwise classify as 0.

### Loss Function for Classification: Binary Cross-Entropy (BCE)
For binary classification, MSE is inappropriate. **Binary Cross-Entropy Loss** is used:
$$ L(\hat{y}, y) = - [y \log(\hat{y}) + (1-y) \log(1-\hat{y})] $$
**Why BCE?** It heavily penalizes confident wrong predictions, making it suitable for optimizing models that output probabilities.

## Part 6: Feature Engineering - Making Linear Models More Powerful

### The Limitation of Linear Models
Linear models inherently assume a linear relationship between features and the target. This limits their ability to capture **non-linear patterns**.

### Solution: Basis Functions (Feature Expansion)
The key idea is to transform the original input features into a higher-dimensional space using non-linear functions (e.g., polynomial terms, trigonometric functions).
*   Instead of $\hat{y} = w x + b$, use $\hat{y} = w_0 + w_1 x + w_2 x^2$.
*   The model remains **linear in its parameters** ($\mathbf{w}$), but becomes **non-linear with respect to the original input** ($x$).
*   This allows linear models (both regression and logistic) to fit curved patterns and non-linear decision boundaries.
*   **Example:** `PolynomialFeatures` in `sklearn` generates polynomial combinations of features.

## Quick Summary

*   **Supervised Learning:** Learning a function from features to labels (regression for numbers, classification for categories).
*   **Linear Regression:**
    *   Models `output = (weights * features) + bias`.
    *   Optimized by minimizing **Mean Squared Error (MSE)**.
    *   Solutions: **Normal Equation** (direct, for small datasets) or **Gradient Descent** (iterative, scalable, foundation of deep learning).
*   **Gradient Descent:** Iteratively updates weights by moving opposite to the gradient of the loss function, controlled by a **learning rate**.
*   **Feature Scaling:** Essential for gradient descent convergence to prevent features of different scales from dominating optimization. Methods include Standardization and Min-Max Scaling.
*   **PyTorch Training Loop:** The 5-step cycle (forward, loss, zero\_grad, backward, step) is universal for training neural networks.
*   **Logistic Regression:**
    *   A classification model.
    *   Applies a **Sigmoid function** to a linear score to produce probabilities (0-1).
    *   Optimized by minimizing **Binary Cross-Entropy Loss** for classification tasks.
*   **Basis Functions (Feature Engineering):** Allows linear models to learn non-linear patterns by transforming input features into a higher-dimensional, non-linear representation.
---