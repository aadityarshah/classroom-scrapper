---
title: Data Foundation & ML Framework
lecture_number: 2
lecture_name: Data Foundation & ML Framework
category: 'Module 2: Learning'
sidebar_label: Lecture 2
sidebar_position: 2
course: ES119 Principles of AI
topic:
- Machine Learning Fundamentals
tags:
- Machine Learning
- ML Framework
- Data Foundation
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning
- Features
- Labels
- One-Hot Encoding
- Data Quality
- Train-Test Split
- Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- MCC
- Regression Metrics
- Scikit-learn
summary: This lecture lays the foundational concepts of Machine Learning, distinguishing it from traditional programming, exploring different learning paradigms (supervised, unsupervised, reinforcement), and detailing how data is represented, managed for quality, split for robust evaluation, and assessed using various metrics. It concludes with the universal scikit-learn API pattern.
math: true
---


# Data Foundation & ML Framework

## 1. The Machine Learning Mindset

Machine Learning offers a distinct programming paradigm compared to traditional methods.

### 1.1 ML vs. Traditional Programming

| Aspect               | Traditional Programming                               | Machine Learning                                   |
| :------------------- | :---------------------------------------------------- | :------------------------------------------------- |
| **Rule Generation**  | Human writes explicit rules.                          | Computer learns implicit rules from data.          |
| **Improvement**      | Does not inherently improve.                          | Improves with more data.                           |
| **Generalization**   | Prone to breaking on unforeseen edge cases.           | Generalizes patterns to new, unseen cases.         |

### 1.2 When to Use ML

ML is advantageous when:
*   **Rules are Complex:** Manual rule creation is infeasible (e.g., image recognition).
*   **Rules Evolve:** Patterns change over time (e.g., stock prediction).
*   **Rules are Unknown:** Underlying logic is not human-understandable (e.g., medical diagnosis).
*   **Data is Abundant:** Large datasets are available for pattern learning.

ML is not needed for simple, fixed rules (e.g., a calculator).

### 1.3 Formal Definition of Learning

According to Tom Mitchell, "A computer program is said to **learn** from **experience E** with respect to some class of **tasks T** and **performance measure P** if its performance at tasks in T, as measured by P, improves with experience E."

*   **Task (T):** The problem the ML model aims to solve.
*   **Experience (E):** The data (often labeled examples) the model trains on.
*   **Performance (P):** The metric used to quantify how well the model performs the task.

## 2. How Machines Learn: Three Paradigms

Machine learning models learn through different approaches:

### 2.1 Supervised Learning (Primary Focus)

*   **Concept:** Learning from labeled examples, akin to learning with a teacher.
*   **Mechanism:** Model is given input data ($\mathbf{X}$) and corresponding correct output labels ($\mathbf{y}$), learning a mapping function.
*   **Categories:**
    *   **Classification:** Predicts a discrete category or class (e.g., spam/not spam, cat/dog/bird).
    *   **Regression:** Predicts a continuous numerical value (e.g., house price, temperature).

### 2.2 Unsupervised Learning

*   **Concept:** Discovering hidden patterns or structures in unlabeled data. No explicit "correct answers" are provided.
*   **Mechanism:** Algorithms identify inherent groupings, dimensions, or anomalies.
*   **Examples:** Customer segmentation, anomaly detection, dimensionality reduction.

### 2.3 Reinforcement Learning (RL)

*   **Concept:** Learning through trial and error, by interacting with an environment and receiving rewards or penalties.
*   **Mechanism:** An agent performs actions, receives feedback (rewards), and learns a policy to maximize cumulative rewards over time.
*   **Examples:** Game-playing AI (e.g., AlphaGo), robotics, self-driving cars.

## 3. Representing Data: Features, Labels, and Notation

Data representation is fundamental for machine learning.

### 3.1 Features ($\mathbf{X}$) vs. Labels ($\mathbf{y}$)

*   **Features ($\mathbf{X}$):** The observable characteristics or attributes of the data; inputs to the model. Typically multiple columns.
*   **Label ($\mathbf{y}$):** The target variable or output we want to predict; the "answer." Usually a single column.

**Key Principle:** Good features are directly relevant to the label, while bad features (e.g., irrelevant IDs, noisy data) can confuse the model.

### 3.2 Mathematical Notation

Consistent notation is vital in ML literature:

*   $m$: Number of samples/data points.
*   $n$: Number of features.
*   $\mathbf{X}$: Feature matrix (all input data), with dimensions $m \times n$.
*   $\mathbf{y}$: Label vector (all output labels), with dimensions $m \times 1$.
*   $\mathbf{x}^{(i)}$: Features of the $i$-th sample (a row vector).
*   $y^{(i)}$: Label of the $i$-th sample (a scalar).

A dataset $\mathcal{D}$ is formally a collection of $m$ pairs: $\mathcal{D} = \{(\mathbf{x}^{(i)}, y^{(i)}) \text{ for } i=1, \dots, m\}$.

### 3.3 Encoding Categorical Features

Computers require numerical input. Categorical features (e.g., 'Red', 'Orange') must be encoded.

*   **One-Hot Encoding:** Creates a new binary (0 or 1) column for each unique category.
    *   **Logic:** For a feature 'Color' with categories 'Red', 'Orange', 'Yellow', it creates 'Color\_Red', 'Color\_Orange', 'Color\_Yellow'. If a sample is 'Orange', 'Color\_Orange' is 1, others are 0.
    *   **Why it matters:** Avoids implying an artificial ordinal relationship between categories (e.g., 'Orange' is not "between" 'Red' and 'Yellow'). Each category is treated as an independent state.

## 4. Data Quality: Garbage In, Garbage Out

The performance of an ML model is directly limited by the quality of its training data. No algorithm can compensate for fundamentally flawed data.

### 4.1 Common Data Quality Issues and Solutions

1.  **Missing Values:** Incomplete information.
    *   **Strategies:** Drop rows (if few missing), impute with mean/median (numerical), impute with mode (categorical), or use "Unknown" category.
2.  **Outliers:** Extreme values that can skew model training.
    *   **Strategies:** Remove if errors, cap at percentiles, or use models robust to outliers.
3.  **Imbalanced Classes:** One class significantly outnumbers others.
    *   **Problem:** Model may achieve high accuracy by simply predicting the majority class, failing to detect the minority class.
    *   **Strategies:** Collect more minority data, oversample minority, undersample majority, or use class weights during training.
4.  **Biased Data:** Data unrepresentative of the real world or reflecting societal biases.
    *   **Consequence:** Biased data leads to biased models, resulting in unfair or discriminatory predictions.
    *   **Mitigation:** Scrutinize data collection, perform bias detection, and apply fairness-aware algorithms.

## 5. Train/Test Split: The Most Important Concept

To ensure a model generalizes to new, unseen data, it must be evaluated on data it did not train on.

*   **Concept:** Divide the dataset into two distinct subsets:
    *   **Training Set:** Used to train the model.
    *   **Test Set:** Used to evaluate the model's performance on unseen data.
*   **Purpose:** Prevents **overfitting** (where the model memorizes the training data instead of learning general patterns). A high training accuracy but low test accuracy indicates overfitting.
*   **The Golden Rule:** **NEVER** use test data for any part of model training, selection, or hyperparameter tuning. This ensures an unbiased estimate of real-world performance.

## 6. Evaluation Metrics: How Do We Measure "Good"?

The choice of evaluation metric depends heavily on the problem and the costs associated with different types of errors.

### 6.1 Metrics for Classification

For binary classification, a **Confusion Matrix** summarizes prediction outcomes:

|               | Predicted: Positive | Predicted: Negative |
| :------------ | :------------------ | :------------------ |
| **Actual: Positive** | True Positive (TP)  | False Negative (FN) |
| **Actual: Negative** | False Positive (FP) | True Negative (TN)  |

1.  **Accuracy:** The proportion of correct predictions out of total predictions.
    $$ \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} $$
    *   **Limitation:** Can be misleading with imbalanced classes.
2.  **Precision:** "When the model predicts positive, how often is it correct?"
    $$ \text{Precision} = \frac{TP}{TP + FP} $$
    *   **Prioritize when:** False positives are costly (e.g., spam filter - avoid marking legitimate emails as spam).
3.  **Recall (Sensitivity):** "Of all actual positives, how many did the model correctly identify?"
    $$ \text{Recall} = \frac{TP}{TP + FN} $$
    *   **Prioritize when:** False negatives are costly (e.g., cancer screening - avoid missing actual cancer cases).
4.  **F1 Score:** The harmonic mean of Precision and Recall. It provides a balanced measure, high only when both Precision and Recall are high.
    $$ F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} $$
    *   **Trade-off:** Precision and Recall often have an inverse relationship; increasing one may decrease the other. The F1 score helps identify a balanced model.
5.  **Matthews Correlation Coefficient (MCC):** A robust metric that works well with imbalanced classes, ranging from -1 (worst) to +1 (best), and 0 (random).
    $$ \text{MCC} = \frac{TP \times TN - FP \times FN}{\sqrt{(TP + FP)(TP + FN)(TN + FP)(TN + FN)}} $$

### 6.2 Multi-Class Classification Metrics

*   A multi-class confusion matrix shows errors between specific classes (e.g., confusing '4' with '9').
*   **Multi-Class F1 Score:**
    *   **Macro F1:** Averages F1 scores calculated independently for each class.
    *   **Weighted F1:** Averages F1 scores by considering the number of samples in each class.
    *   **Micro F1:** Calculates global TP, TN, FP, FN and then computes F1.

### 6.3 Metrics for Regression

For predicting continuous numbers, metrics quantify the magnitude of error:

1.  **Mean Absolute Error (MAE):** Average of the absolute differences between predicted and actual values.
    $$ \text{MAE} = \frac{1}{m} \sum_{i=1}^{m} |y_i - \hat{y}_i| $$
    *   **Intuition:** Average magnitude of errors.
2.  **Mean Squared Error (MSE):** Average of the squared differences. Penalizes larger errors more heavily.
    $$ \text{MSE} = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2 $$
3.  **Root Mean Squared Error (RMSE):** The square root of MSE, putting the error back into the same units as the target variable.
    $$ \text{RMSE} = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2} $$

## 7. The Scikit-learn (sklearn) Pattern

The `scikit-learn` library in Python provides a consistent, universal API for most ML models.

### 7.1 The Universal 4-Step Pattern

All `sklearn` models follow this structure:

1.  **Create Model Instance:**
    ```python
    model = SomeModel(parameters)
    ```
2.  **Train (Fit) Model:** Train the model using the training features and labels.
    ```python
    model.fit(X_train, y_train)
    ```
3.  **Predict:** Generate predictions on new, unseen data (typically the test set).
    ```python
    predictions = model.predict(X_test)
    ```
4.  **Evaluate:** Assess the model's performance using relevant metrics.
    ```python
    score = model.score(X_test, y_test) # Or use sklearn.metrics functions
    ```

This consistency means once you learn this pattern, you can easily swap between different models (e.g., `DecisionTreeClassifier`, `LinearRegression`) by changing only the first line.

## Quick Summary

Machine Learning is a paradigm where computers **learn rules from data** (experience $E$) to perform **tasks $T$** and improve **performance $P$**. Key learning types include **supervised** (from labeled data for classification or regression), unsupervised (finding patterns in unlabeled data), and reinforcement (learning via rewards). Data is structured as **features ($\mathbf{X}$)** and **labels ($\mathbf{y}$)**, with categorical data often requiring **one-hot encoding**. **Data quality** (addressing missing values, outliers, imbalance, bias) is paramount. Models must be evaluated on **unseen data** using a **train/test split** to prevent overfitting. Evaluation metrics like **Accuracy, Precision, Recall, F1 Score, and MCC** are used for classification, with **MAE, MSE, and RMSE** for regression, chosen based on problem context. The **scikit-learn API** provides a standardized `create -> fit -> predict -> evaluate` workflow for all models.