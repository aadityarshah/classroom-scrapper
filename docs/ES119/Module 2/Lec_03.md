---
title: 'Supervised Learning Deep Dive: Linear & Logistic Regression'
lecture_number: 03
lecture_name: "Linear & Logistic Regression: Foundations of Supervised Learning"
category: 'Module 2: Learning'
sidebar_label: 'Lecture 3'
sidebar_position: 3
topic:
  - Linear Regression
  - Logistic Regression
  - Optimization Techniques
  - Feature Engineering
  - Model Implementation
tags:
  - Supervised Learning
  - Linear Regression
  - Logistic Regression
  - Machine Learning
  - Optimization
  - Gradient Descent
  - Normal Equation
  - MSE
  - Cross-Entropy
  - Sigmoid Function
  - Feature Scaling
  - Standardization
  - Min-Max Scaling
  - Feature Engineering
  - Basis Functions
  - Scikit-learn
  - PyTorch
summary: "This lecture provides a comprehensive deep dive into Linear and Logistic Regression, covering their theoretical foundations, optimization techniques (Normal Equation and Gradient Descent), the critical role of feature scaling, and how to extend models through feature engineering. We also bridge the gap between Scikit-learn's high-level abstractions and PyTorch's granular control for implementing these models, establishing the core training loop fundamental to deep learning."
math: true
---

# Learning Goals

By the end of this lecture, you will be able to:
1.  **Understand** how linear regression determines the "best fit" line for continuous predictions.
2.  **Learn** two primary methods for finding optimal model weights: the Normal Equation and Gradient Descent.
3.  **Apply** logistic regression for binary classification problems.
4.  **Connect** the concepts of `sklearn` models to the underlying mechanisms of `PyTorch` for neural networks.

# Recap: Supervised Learning

In supervised learning, we aim to learn a function that maps input features to output labels.

*   **Features ($\mathbf{X}$):** What we know about each example (independent variables).
*   **Labels ($y$):** What we want to predict (dependent variable).
*   **Goal:** Learn a function $f$ such that $f(\mathbf{X}) \approx y$.

The nature of the label $y$ dictates the type of task:
*   If $y$ is a **number** (e.g., house price), it's a **Regression** task.
*   If $y$ is a **category** (e.g., spam/not spam), it's a **Classification** task.

# Part 1: Linear Regression

## The Simplest Prediction Problem

Consider a scenario where a real estate agent needs to predict the price of a house based on its size.
We have historical data showing a clear linear relationship:
| Size (sqft) | Price (₹ lakhs) |
| :---------- | :-------------- |
| 1000        | 40              |
| 1500        | 60              |
| 2000        | 80              |
| 2500        | 100             |

The pattern reveals that every 500 sqft adds ₹20 lakhs. By simple interpolation, a 1750 sqft house would cost ₹70 lakhs. This intuitive process is essentially linear regression.

## The Equation of a Line

Linear regression models this relationship using the equation of a line:
$$ \hat{y} = w \cdot x + b $$
Where:
*   $x$: Input feature value (e.g., house size).
*   $\hat{y}$: Predicted output value (e.g., predicted price). The "hat" denotes a prediction.
*   $w$: Weight, representing the slope of the line.
*   $b$: Bias, representing the y-intercept.

In our example, $w = 0.04$ and $b = 0$. So, $\hat{y} = 0.04 \cdot x$.

## Interpreting Weights and Bias

The **weight $w$** quantifies the sensitivity of the output to changes in the input:
*   If $w = 0.04$, it means "For every 1 sqft increase, the price increases by ₹0.04 lakhs."
*   Equivalently, "For every 100 sqft increase, the price increases by ₹4 lakhs."
The weight essentially tells us *how much* the output changes for a unit change in the input.

The **bias $b$** represents the baseline value when all input features are zero.
*   If $b=0$, it implies a 0 sqft house costs ₹0.
*   In real-world scenarios, bias often captures irreducible baseline costs, such as land value, permits, or minimum construction costs. If $b=10$, even a tiny house would cost at least ₹10 lakhs.

## Multiple Features: The General Form

When the output depends on more than one feature (e.g., size, number of bedrooms, bathrooms), the linear equation expands:
$$ \hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_d x_d + b $$
This can be expressed more compactly in **vector form**:
$$ \hat{y} = \mathbf{w}^{\top} \mathbf{x} + b = \langle \mathbf{w}, \mathbf{x} \rangle + b $$
Where:
*   $\mathbf{x}$ is a vector of input features: $\mathbf{x} = [x_1, x_2, \dots, x_d]^{\top}$.
*   $\mathbf{w}$ is a vector of learned weights: $\mathbf{w} = [w_1, w_2, \dots, w_d]^{\top}$.
*   $\mathbf{w}^{\top} \mathbf{x}$ (or $\langle \mathbf{w}, \mathbf{x} \rangle$) denotes the **dot product** (sum of element-wise products).

## Notation: Absorbing Bias into $\theta$

For mathematical elegance and simplified matrix operations, it's common to absorb the bias $b$ into the weight vector $\mathbf{w}$. We introduce an augmented feature $\mathbf{x}_{\text{aug}}$ by adding a constant '1' to the input vector and combine $\mathbf{w}$ and $b$ into a single parameter vector $\boldsymbol{\theta}$.

Original form: $\hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_d x_d + b$

Augmented form:
1.  Augment the input feature vector $\mathbf{x}$ to $\mathbf{x}_{\text{aug}} = [1, x_1, x_2, \dots, x_d]^{\top}$.
2.  Define the combined parameter vector $\boldsymbol{\theta} = [b, w_1, w_2, \dots, w_d]^{\top}$.

Now, the prediction equation becomes a simple dot product:
$$ \hat{y} = \theta_0 \cdot 1 + \theta_1 x_1 + \theta_2 x_2 + \dots + \theta_d x_d = \boldsymbol{\theta}^{\top} \mathbf{x}_{\text{aug}} $$
Going forward, we will use $\mathbf{x}$ to refer to the augmented input and $\boldsymbol{\theta}$ to represent the combined weights and bias. So, $\hat{y} = \boldsymbol{\theta}^{\top} \mathbf{x}$.

## Interpreting Multiple Weights

Each weight $\theta_j$ (or $w_j$) in a multiple-feature model represents the **independent contribution** of its corresponding feature $x_j$ to the predicted output, assuming other features are held constant.

Example: If a trained model yields `coef_ = [0.03, 5.0, 8.0]` (for size, bedrooms, bathrooms) and `intercept_ = -10`:
*   Size weight (0.03): "+100 sqft $\rightarrow$ +₹3 lakhs"
*   Bedroom weight (5.0): "+1 bedroom $\rightarrow$ +₹5 lakhs"
*   Bathroom weight (8.0): "+1 bathroom $\rightarrow$ +₹8 lakhs"

# Part 2: Finding the Best Weights: The Optimization Problem

## The Goal: Minimize Errors (Loss Functions)

Real-world data is noisy; points rarely fall perfectly on a line. Our goal is to find the line (or hyperplane in higher dimensions) that *best fits* the data. This means minimizing the difference between our predictions ($\hat{y}$) and the actual values ($y$). This difference is called the **residual** or **error**:
$$ \text{Residual}_i = y_i - \hat{y}_i $$
To find the "best" line, we need a way to quantify the total error across all data points. This is done using a **loss function** (or **cost function**).

### Why Squared Errors?

A common and mathematically convenient choice for regression loss is the **Sum of Squared Errors (SSE)**:
$$ \text{SSE} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
Squaring the errors serves several purposes:
*   **Prevents cancellation:** Positive and negative errors do not cancel each other out, ensuring all errors contribute positively to the total loss.
*   **Penalizes large errors more:** Larger errors are penalized disproportionately more than smaller errors (e.g., an error of 10 costs $10^2 = 100$, not 10). This encourages the model to reduce significant deviations.
*   **Nice mathematical properties:** The SSE function is **differentiable** and **convex**, which is crucial for optimization algorithms. A convex function has a single global minimum, making it easier to find.

### Mean Squared Error (MSE)

More commonly, we use the **Mean Squared Error (MSE)**, which is the average of the squared errors:
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
This is our primary **Loss Function** or **Cost Function** for linear regression.
Substituting $\hat{y}_i = \boldsymbol{\theta}^{\top} \mathbf{x}_i$ (using the absorbed bias notation), the loss function becomes:
$$ \mathcal{L}(\boldsymbol{\theta}) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \boldsymbol{\theta}^{\top} \mathbf{x}_i)^2 $$
Our ultimate goal is to find the parameter vector $\boldsymbol{\theta}$ that minimizes this loss function $\mathcal{L}(\boldsymbol{\theta})$.

## Two Ways to Find Optimal Weights

There are two primary approaches to find the optimal weights that minimize the loss function:

1.  **Normal Equation:** A direct, analytical formula. Suitable for small datasets.
2.  **Gradient Descent:** An iterative, step-by-step optimization algorithm. Essential for large datasets and neural networks.

## Quick Review: Derivatives and Gradients

Before diving into optimization, a quick recap of calculus concepts:

*   **Derivative ($\frac{df}{dx}$):** For a single-variable function $f(x)$, the derivative measures the instantaneous rate of change of $f$ with respect to $x$.
    *   Example: If $f(x) = x^2$, then $\frac{df}{dx} = 2x$.

*   **Partial Derivative ($\frac{\partial f}{\partial x}$):** For a multi-variable function $f(x, y, \dots)$, a partial derivative measures the rate of change of $f$ with respect to one variable, assuming all other variables are held constant.
    *   Example: If $f(x, y) = x^2 + y^2$, then $\frac{\partial f}{\partial x} = 2x$ and $\frac{\partial f}{\partial y} = 2y$.

*   **Gradient ($\nabla f$):** For a multi-variable function $f$, the gradient is a vector containing all its partial derivatives. It points in the direction of the **steepest increase** of the function.
    *   Example: For $f(x, y) = x^2 + y^2$, the gradient is $\nabla f = \left[ \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right] = [2x, 2y]$.
    *   At point $(1, 2)$, $\nabla f = [2, 4]$. This means moving in the $+x$ direction increases $f$ at rate 2, and moving in the $+y$ direction increases $f$ at rate 4.
    *   **Key Insight:** To minimize a function, we must move in the **opposite direction** of its gradient (i.e., downhill). Setting the gradient to zero ($\nabla f = \mathbf{0}$) helps us find local minima (or maxima/saddle points).

## Normal Equation

The Normal Equation provides a direct, closed-form solution for the optimal parameter vector $\boldsymbol{\theta}$ that minimizes the MSE loss function. By setting the gradient of the MSE loss function with respect to $\boldsymbol{\theta}$ to zero ($\nabla \mathcal{L}(\boldsymbol{\theta}) = \mathbf{0}$) and solving for $\boldsymbol{\theta}$, we arrive at:
$$ \hat{\boldsymbol{\theta}} = (\mathbf{X}^{\top} \mathbf{X})^{-1} \mathbf{X}^{\top} \mathbf{y} $$
Where:
*   $\mathbf{X}$ is the design matrix (each row is an augmented feature vector $\mathbf{x}_i$, each column is a feature).
*   $\mathbf{y}$ is the vector of actual target values.

**Limitation:** The Normal Equation requires computing the inverse of the matrix $\mathbf{X}^{\top} \mathbf{X}$. Matrix inversion has a computational complexity of $O(d^3)$, where $d$ is the number of features. For datasets with millions of features, this becomes prohibitively slow.

## Gradient Descent: The Algorithm

Gradient Descent is an iterative optimization algorithm that finds the minimum of a function by repeatedly taking small steps in the direction opposite to the gradient.

The core idea:
1.  Start with a random initial set of parameters $\boldsymbol{\theta}$.
2.  Compute the gradient of the loss function $\mathcal{L}(\boldsymbol{\theta})$ with respect to the current $\boldsymbol{\theta}$. This tells us the steepest uphill direction.
3.  Update $\boldsymbol{\theta}$ by taking a small step in the **opposite direction** of the gradient.
4.  Repeat steps 2 and 3 until the parameters converge to a minimum, or a maximum number of iterations (epochs) is reached.

The **update rule** for Gradient Descent is:
$$ \boldsymbol{\theta}_{\text{new}} = \boldsymbol{\theta}_{\text{old}} - \eta \cdot \nabla_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}_{\text{old}}) $$
Where:
*   $\boldsymbol{\theta}_{\text{new}}$: The updated parameter vector.
*   $\boldsymbol{\theta}_{\text{old}}$: The current parameter vector.
*   $\eta$ (eta): The **learning rate**, a hyperparameter that controls the size of each step.
*   $\nabla_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}_{\text{old}})$: The gradient of the loss function with respect to $\boldsymbol{\theta}$ at the current parameters. This vector points towards steepest increase.
*   $-\nabla_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}_{\text{old}})$: Points towards the steepest decrease.

**Gradient for MSE:** For the Mean Squared Error, the gradient with respect to $\boldsymbol{\theta}$ is:
$$ \nabla_{\boldsymbol{\theta}} \mathcal{L} = \frac{2}{n} \mathbf{X}^{\top} (\mathbf{X}\boldsymbol{\theta} - \mathbf{y}) = -\frac{2}{n} \mathbf{X}^{\top} (\mathbf{y} - \hat{\mathbf{y}}) $$
This intuitively means that the update for each parameter is proportional to the error multiplied by the corresponding feature value. Big error + big feature = big update.

### Learning Rate: The Key Hyperparameter

The **learning rate ($\eta$)** is crucial for the performance of Gradient Descent. It dictates how large each step is:
*   **Too Small ($\eta = 0.0001$):** Converges very slowly, requiring many iterations to reach the minimum.
*   **Just Right ($\eta = 0.01$ or $0.1$):** Makes good progress and converges efficiently to the minimum.
*   **Too Large ($\eta = 1.0$):** Overshoots the minimum, can oscillate wildly, or even diverge, never reaching the optimum.

**How to choose a learning rate:**
*   Start with common values like $0.001$ or $0.01$.
*   If the loss doesn't decrease, try a smaller learning rate.
*   If the loss "explodes" (becomes `NaN`), try a much smaller learning rate.

### Why Gradient Descent Matters

| Feature              | Normal Equation                       | Gradient Descent                          |
| :------------------- | :------------------------------------ | :---------------------------------------- |
| Computation          | One-shot, direct formula              | Iterative process                         |
| Solution             | Exact solution (for linear models)    | Approximate (but close enough)            |
| Complexity           | $O(d^3)$                              | $O(d)$ per iteration                      |
| Model applicability | Only for linear models                | Works for ANY differentiable model        |

**Key takeaway:** Gradient Descent is the **foundation of neural network training**. Its iterative nature allows it to scale to millions of parameters and handle non-linear models where direct solutions are impossible.

# Part 3: Feature Scaling

## The Scaling Problem and Why It Helps

Different features in a dataset often have vastly different scales. For example:
| Feature      | Range               | Scale     |
| :----------- | :------------------ | :-------- |
| House size   | 500 - 5000 sqft     | ~1000s    |
| Bedrooms     | 1 - 6               | ~1s       |
| Age          | 0 - 100 years       | ~10s      |

**Problem:** Large-scale features tend to **dominate** gradient descent updates. The loss function's contours become elongated ellipses rather than circles, causing gradient descent to "zigzag" inefficiently, slowing down convergence.

**Without scaling:**
*   Weights for large-valued features need tiny updates.
*   Weights for small-valued features need large updates.
*   Gradient descent zigzags inefficiently, taking longer to converge.

**With scaling:**
*   All features contribute equally to the gradient updates.
*   Gradient descent converges faster and more directly.
*   Training becomes more stable.

**Currency Analogy:** Imagine training with mixed currencies (e.g., millions of rupees vs. single digits of rooms). The model might incorrectly perceive the features with larger numerical values as inherently more important. Scaling brings all features to a "standard currency."

## Common Scaling Methods

Two widely used scaling methods are:

1.  **Standardization (Z-score normalization):**
    *   Formula: $x' = \frac{x - \mu}{\sigma}$
    *   Result: Mean = 0, Standard Deviation = 1.
    *   Most common approach, useful when feature distributions are Gaussian or when outliers are not a major concern.

2.  **Min-Max Scaling:**
    *   Formula: $x' = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}$
    *   Result: Range [0, 1].
    *   Useful when you need features bounded within a specific range (e.g., for neural network activation functions that operate on inputs between 0 and 1).

Both are implemented in `sklearn.preprocessing`: `StandardScaler` and `MinMaxScaler`.

## Practical Considerations for Scaling

**Crucial Rule: Fit on Train, Transform Both!**
When scaling data, it's paramount to prevent **data leakage**. This means the statistics (mean, standard deviation for standardization; min, max for min-max scaling) used for scaling **must only be computed from the training data**.

*   **Correct Way:**
    1.  Initialize a `scaler` object (e.g., `StandardScaler()`).
    2.  `scaler.fit(X_train)`: Compute the scaling parameters (mean/std, min/max) *only* from the training set.
    3.  `X_train_scaled = scaler.transform(X_train)`: Apply the scaling to the training set.
    4.  `X_test_scaled = scaler.transform(X_test)`: Apply the *same* scaling (using parameters learned from `X_train`) to the test set.

*   **Wrong Way (Data Leakage!):**
    *   `scaler.fit_transform(X_all)`: Fitting the scaler on the entire dataset (training + test) or just on the test set. This leaks information from the test set into the training process, leading to overly optimistic performance estimates.

## When to Scale?

Not all machine learning algorithms require feature scaling. Here's a general guide:

| Algorithm                 | Needs Scaling? | Why                                    |
| :------------------------ | :------------- | :------------------------------------- |
| Linear/Logistic Regression | Yes            | Gradient descent (faster convergence)  |
| Neural Networks           | Yes            | Gradient descent (faster convergence)  |
| Decision Trees            | No             | Split-based, scale-invariant           |
| K-Nearest Neighbors       | Yes            | Distance-based                         |
| Random Forest             | No             | Tree-based                             |

Algorithms that use distance metrics (like KNN, SVMs with RBF kernel) or iterative optimization (like gradient descent for linear models, neural networks) generally benefit significantly from feature scaling. Tree-based models are scale-invariant.

# Part 4: Practical Implementation with sklearn and PyTorch

This section demonstrates how to implement Linear Regression and sets the stage for understanding the core PyTorch training loop.

## Linear Regression in sklearn

Scikit-learn (`sklearn`) provides high-level abstractions for machine learning models.
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Our data
X = np.array([[1000], [1500], [2000], [2500]]) # House sizes
y = np.array([40, 60, 80, 100])               # House prices

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Understanding what sklearn learned
print(f"Weight (w): {model.coef_[0]:.4f}")    # Output: 0.0400
print(f"Intercept (b): {model.intercept_:.1f}") # Output: 0.0

# Now predict!
prediction = model.predict([[1750]])
print(f"Prediction for 1750 sqft: {prediction[0]:.1f} (₹ lakhs)") # Output: 70.0 (₹70 lakhs)
```
`sklearn` internally solves this using techniques like Singular Value Decomposition (SVD), which is related to the Normal Equation, providing a direct, non-iterative solution.

## Linear Regression in PyTorch

PyTorch offers a more granular control over the model, loss, and optimization process, which is essential for building and training neural networks.
```python
import torch
import torch.nn as nn
import torch.optim as optim

# Data as tensors
X = torch.tensor([[1000.], [1500.], [2000.], [2500.]])
y = torch.tensor([[40.], [60.], [80.], [100.]])

# Normalize for stable training (important for PyTorch/GD)
X_norm = X / 1000.0 # Scale input feature to a smaller range

# Linear model: y = wx + b (nn.Linear takes 1 input, 1 output)
model = nn.Linear(1, 1)

# Loss function and optimizer
criterion = nn.MSELoss() # Mean Squared Error
optimizer = optim.SGD(model.parameters(), lr=0.1) # Stochastic Gradient Descent

# Training loop
for epoch in range(100): # 100 iterations
    # 1. Forward pass: compute predictions
    y_pred = model(X_norm)

    # 2. Compute loss
    loss = criterion(y_pred, y)

    # 3. Clear gradients from previous iteration
    optimizer.zero_grad()

    # 4. Compute gradients (backward pass)
    loss.backward()

    # 5. Update weights
    optimizer.step()

# After training:
# model.weight and model.bias will be close to 0.04 * 1000 (since X_norm was X/1000) and 0.
# The `model.weight` for the normalized input will be approximately 40.0
# because y = w_actual * x_actual + b_actual
# y = w_norm * x_norm + b_norm
# w_actual = w_norm / 1000
# So w_norm = w_actual * 1000 = 0.04 * 1000 = 40
print(f"Trained weight: {model.weight.item():.4f}") # Output: ~40.0
print(f"Trained bias: {model.bias.item():.4f}")   # Output: ~0.0
```
Note: Since `X_norm` was used, the learned weight corresponds to `X_norm`. To get the `w` for `X` (original unscaled input), you would divide the PyTorch weight by 1000. So `40.0 / 1000 = 0.04`.

## The PyTorch Training Loop

The 5-step training cycle demonstrated above is a fundamental pattern in PyTorch and deep learning:

| Step | Code                       | What it does                       |
| :--- | :------------------------- | :--------------------------------- |
| 1    | `y_pred = model(X)`        | **Forward pass:** Compute predictions |
| 2    | `loss = criterion(y_pred, y)` | **Measure error:** Calculate loss  |
| 3    | `optimizer.zero_grad()`    | **Clear old gradients:** Reset gradients to zero for fresh computation |
| 4    | `loss.backward()`          | **Compute new gradients:** Perform backpropagation |
| 5    | `optimizer.step()`         | **Update $\boldsymbol{\theta}$:** Adjust parameters using gradients and learning rate |

**Crucial Insight:** This exact loop works for ANY neural network, from simple linear regression to complex models like GPT! Understanding this loop is central to deep learning.

## Comparing sklearn vs PyTorch

| Aspect        | sklearn                       | PyTorch                           |
| :------------ | :---------------------------- | :-------------------------------- |
| Simplicity    | 2 lines of code               | 10+ lines                         |
| Method        | Closed-form (SVD) for Linear  | Gradient Descent (iterative)      |
| Customization | Limited                       | Full control                      |
| Neural nets   | Basic only (e.g., MLPClassifier) | Full support for complex architectures |
| GPU support   | No (typically CPU)            | Yes! (essential for deep learning) |

**Recommendation:** Start with `sklearn` for quick prototyping and simpler models. Move to `PyTorch` when you need more power, customization, GPU acceleration, or are building deep neural networks.

# Part 5: Logistic Regression: From Numbers to Categories

## The Classification Problem

Linear regression is suitable for predicting continuous numerical values. However, for predicting categories (e.g., spam/not spam, disease/no disease), we need a different approach.

Consider building a spam filter:
| Email | Exclamation Marks | Has "FREE" | Is Spam? |
| :---- | :---------------- | :--------- | :------- |
| 1     | 5                 | Yes        | Spam     |
| 2     | 0                 | No         | Not Spam |
| 3     | 3                 | Yes        | Spam     |
| 4     | 1                 | No         | Not Spam |

The output "Is Spam?" is a category, not a number.

## Why Linear Regression Fails for Classification

If we try to use linear regression to predict a binary outcome (e.g., 0 for "Not Spam", 1 for "Spam"):
$$ \text{Spam Score} = \theta_1 \cdot \text{Exclamations} + \theta_2 \cdot \text{HasFREE} + \theta_0 $$
The problem is that a linear model can output *any* number from $-\infty$ to $+\infty$.
*   A "Spam Score" of -2.5, 0.3, 1.5, or 147 doesn't directly translate to a probability or a clear category.
*   We need an output that is bounded between 0 and 1, representing a probability.

## The Sigmoid Function

The **sigmoid function** (also known as the logistic function) solves this problem by squashing any real number into the range (0, 1).
$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$
Where:
*   $z$ is the output of a linear model ($\boldsymbol{\theta}^{\top} \mathbf{x}$).
*   $\sigma(z)$ is the predicted probability.

The sigmoid function has an characteristic **S-curve** shape:
*   **Very negative $z$:** $\sigma(z) \approx 0$
*   **$z$ near 0:** $\sigma(z) \approx 0.5$ (this is the **decision boundary**)
*   **Very positive $z$:** $\sigma(z) \approx 1$

**Key Insight:** The sigmoid function converts any raw linear score ($z$) into a probability ($P \in [0, 1]$).

## The Logistic Regression Model

Logistic Regression is a two-step process:
1.  **Linear Step:** Compute a linear score $z$ from the input features, just like linear regression.
    $$ z = \boldsymbol{\theta}^{\top} \mathbf{x} = \theta_0 + \theta_1 x_1 + \dots + \theta_d x_d $$
2.  **Sigmoid Step:** Convert this linear score $z$ into a probability $P$.
    $$ P(\text{class=1} | \mathbf{x}) = \sigma(z) = \frac{1}{1 + e^{-z}} $$
This probability $P(\text{class=1} | \mathbf{x})$ is the model's estimate that the input $\mathbf{x}$ belongs to class 1 (e.g., "Spam").

## The Decision Rule

Once we have a probability $P(\text{class=1} | \mathbf{x})$, we need a decision rule to classify.
*   Typically, if $P(\text{class=1} | \mathbf{x}) > 0.5$, predict Class 1.
*   If $P(\text{class=1} | \mathbf{x}) \le 0.5$, predict Class 0.

The threshold of 0.5 corresponds to $z=0$. So, the decision boundary is defined by $\boldsymbol{\theta}^{\top} \mathbf{x} = 0$.

**Threshold Tuning:** The 0.5 threshold can be adjusted based on the specific application's needs:
*   **Lower threshold (e.g., $>$0.3):** Catches more positives (e.g., more spam), but might increase false positives (false alarms).
*   **Higher threshold (e.g., $>$0.7):** Fewer false positives (fewer false alarms), but might miss some true positives.

## Logistic Regression in sklearn

`sklearn` simplifies logistic regression as well:
```python
import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample data: [exclamations, has_FREE (1=yes, 0=no)]
X = np.array([[5, 1], [0, 0], [3, 1], [1, 0]])
# Labels: [1=spam, 0=not spam]
y = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

# Predict class for a new email: 4 exclamations, has_FREE
print(f"Predicted class: {model.predict([[4, 1]])[0]}") # Output: 1 (Spam)

# Predict probabilities for the new email
proba = model.predict_proba([[4, 1]])
print(f"Predicted probabilities: P(not spam)={proba[0, 0]:.2f}, P(spam)={proba[0, 1]:.2f}")
# Output: P(not spam)=0.12, P(spam)=0.88
```

## Logistic Regression in PyTorch

In PyTorch, Logistic Regression is essentially a linear layer followed by a sigmoid activation function.
```python
import torch
import torch.nn as nn
import torch.optim as optim

# Model Definition
class LogisticRegression(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1) # Linear layer for z = WX + b
        self.sigmoid = nn.Sigmoid()         # Sigmoid activation for probability

    def forward(self, x):
        return self.sigmoid(self.linear(x))

# Sample Data (as tensors)
X = torch.tensor([[5., 1.], [0., 0.], [3., 1.], [1., 0.]])
y = torch.tensor([[1.], [0.], [1.], [0.]])

model = LogisticRegression(input_dim=2)

# Loss Function: Binary Cross-Entropy
criterion = nn.BCELoss() # Binary Cross-Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Training loop (same 5-step loop as Linear Regression)
for epoch in range(100):
    y_pred = model(X)
    loss = criterion(y_pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# After training, you can get predictions and probabilities
```

## Why Cross-Entropy Loss?

For classification problems, Mean Squared Error (MSE) is generally not suitable because:
*   It assumes outputs are continuous and normally distributed.
*   It doesn't penalize confident wrong predictions severely enough, especially for probabilities.

For binary classification with logistic regression, we use **Binary Cross-Entropy (BCE) Loss**:
$$ \mathcal{L}_{\text{BCE}} = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)] $$
Where:
*   $y_i$ is the true label (0 or 1).
*   $\hat{y}_i$ is the predicted probability (between 0 and 1).

**Key Insight:** Cross-Entropy loss penalizes **confident wrong predictions very severely!**
*   **If $y_i=1$:** The term $(1 - y_i) \log(1 - \hat{y}_i)$ becomes zero. The loss is $-\log(\hat{y}_i)$.
    *   If $\hat{y}_i \approx 1$ (correct & confident), $-\log(\hat{y}_i) \approx 0$ (low loss).
    *   If $\hat{y}_i \approx 0$ (wrong & confident), $-\log(\hat{y}_i) \approx \infty$ (very high loss!).
*   **If $y_i=0$:** The term $y_i \log(\hat{y}_i)$ becomes zero. The loss is $-\log(1 - \hat{y}_i)$.
    *   If $\hat{y}_i \approx 0$ (correct & confident), $-\log(1 - \hat{y}_i) \approx 0$ (low loss).
    *   If $\hat{y}_i \approx 1$ (wrong & confident), $-\log(1 - \hat{y}_i) \approx \infty$ (very high loss!).

This property makes BCE loss highly effective for training classification models.

# Part 6: Feature Engineering: Making Linear Models More Powerful

## The Limitation of Linear Models

Linear models, by definition, can only capture linear relationships between features and targets.
**Problem:** What if the relationship isn't linear?
Example: Ice cream sales vs. temperature. Sales typically increase with temperature but then might plateau or even decrease at extremely high temperatures. A straight line (Degree 1) would lead to **underfitting**. A quadratic curve (Degree 2) might fit much better.

## Basis Functions: The Key Idea

To allow linear models to capture non-linear patterns, we can transform the input features using **basis functions**. The model remains *linear in its parameters* ($\boldsymbol{\theta}$), but becomes *non-linear in the original input features* ($\mathbf{x}$).

Instead of: $\hat{y} = \theta_0 + \theta_1 x$
Use: $\hat{y} = \theta_0 + \theta_1 x + \theta_2 x^2$

Here, we've added $x^2$ as a new feature. The model is still a linear combination of its features ($1, x, x^2$), but now it can fit a quadratic curve.

Common examples of basis-expanded features:
*   Polynomial: $[1, x, x^2]$ or $[1, x, x^2, x^3]$
*   Trigonometric: $[1, \sin(x), \cos(x)]$
*   Radial Basis Functions (RBFs)

## Feature Expansion Visualized

By adding $x^2$ as a feature, we transform the original 1D feature space into a 2D feature space ($x, x^2$). In this new space, the relationship might appear linear, allowing our linear model to fit it effectively. This provides the model with more "raw material" to work with.

## Polynomial Features in sklearn

`sklearn.preprocessing.PolynomialFeatures` makes feature expansion easy:
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[15], [20], [25], [30], [35]]) # Temperature
y = np.array([15, 10, 20, 55, 120])           # Ice cream sales

poly = PolynomialFeatures(degree=2) # Transform x -$>$ [1, x, x^2]
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y) # Now it can fit curves!
# The model learns weights for 1 (bias), x, and x^2.
```

## Works for Classification Too!

The same idea applies to logistic regression. By using polynomial features (or other basis functions), logistic regression can learn non-linear decision boundaries.
```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
# ... (data setup)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LogisticRegression()
model.fit(X_poly, y) # Now decision boundary can be curved!
```
**Key Insight:** Basis functions allow linear models to learn complex, non-linear patterns by implicitly transforming the input space into a higher-dimensional space where the relationship becomes linear.

# Conclusion: The Big Picture and Key Takeaways

## Quick Summary

| Concept                  | Key Takeaway                                         |
| :----------------------- | :--------------------------------------------------- |
| **Linear Regression**    | Fits a line to predict continuous values: $\hat{y} = \boldsymbol{\theta}^{\top} \mathbf{x}$ |
| **Loss Function**        | Measures how "wrong" our model's predictions are (e.g., MSE for regression, Cross-Entropy for classification) |
| **Gradient Descent**     | Iterative algorithm to find optimal parameters: $\boldsymbol{\theta}_{\text{new}} = \boldsymbol{\theta}_{\text{old}} - \eta \cdot \nabla_{\boldsymbol{\theta}} \mathcal{L}$ |
| **Logistic Regression**  | Classifies by converting linear scores to probabilities using the Sigmoid function |
| **Cross-Entropy Loss**   | The preferred loss for classification, severely penalizing confident wrong predictions |
| **Feature Scaling**      | Standardizes features to improve gradient descent convergence and stability |
| **Feature Engineering**  | Transforms inputs (e.g., via basis functions) to enable linear models to learn non-linear patterns |
| **sklearn vs PyTorch**   | `sklearn` for ease-of-use, `PyTorch` for control, deep learning, and GPU acceleration |
| **PyTorch Training Loop** | The 5-step forward-loss-zero_grad-backward-step cycle is universal for deep learning |

You now understand the fundamental building blocks of supervised learning and model optimization! The training loop you learned today is the *same* loop used to train large-scale models like GPT-4, demonstrating the universality of these core principles.

**Next:** Model Selection & Evaluation — How do we know if our model is good, and how do we choose between different models?