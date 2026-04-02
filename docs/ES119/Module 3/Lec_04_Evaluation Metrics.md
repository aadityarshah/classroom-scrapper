---
title: Evaluation Metrics for AI Models
lecture_number: 4
lecture_name: Evaluation Metrics
category: Module 3
sidebar_label: Lecture 4
sidebar_position: 4
course: ES119 Principles of AI
topic:
- Machine Learning Evaluation
- Classification Metrics
- Confusion Matrix
- Precision and Recall
- F1 Score
- ROC Curve
- AUC
tags:
- AI
- Machine Learning
- Evaluation
- Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- ROC
- AUC
- Classification
summary: This lecture delves into the critical evaluation metrics for AI models, moving
  beyond simple accuracy to explore the nuances of performance using confusion matrices,
  precision, recall, F1 scores, and ROC curves with AUC for a comprehensive understanding
  of model effectiveness, especially in imbalanced datasets.
math: true
last_updated: "2 April 2026"
---


## Introduction: Why Evaluate?

After building and training an AI model, the paramount question is: "Does it actually work?" Before deployment in critical scenarios (e.g., healthcare, finance), we must rigorously grade its performance. This involves moving beyond superficial measures to deeply understand its strengths and weaknesses.

## The "Accuracy" Trap

The most intuitive metric, **Accuracy**, measures the proportion of correct predictions:

$$
\text{Accuracy} = \frac{\text{Total Correct Guesses}}{\text{Total Total Guesses}}
$$

While seemingly perfect, accuracy can be a deceptive metric, especially with **imbalanced datasets**.

### The Rare Disease Scenario

Consider an AI designed to detect a rare disease affecting 1 in 100 patients. A "lazy AI" that simply predicts "Everyone is Healthy" would achieve 99% accuracy (99 correct guesses, 1 wrong). Despite this high accuracy, the model is **100% useless** as it fails every single patient needing help. In such cases, accuracy is fundamentally misleading. This problem extends to fraud detection, cancer screening, and rainfall prediction, where the target event is infrequent.

## The Confusion Matrix: A Detailed View

To overcome the limitations of accuracy, we dissect an AI's predictions into four distinct categories using a **Confusion Matrix**. This $2 \times 2$ grid maps actual outcomes against predicted outcomes.

|                   | **Actually Yes (Positive)** | **Actually No (Negative)** |
| :---------------- | :-------------------------- | :------------------------- |
| **AI says Positive** | True Positive (TP)          | False Positive (FP)        |
| **AI says Negative** | False Negative (FN)         | True Negative (TN)         |

### Definitions of Confusion Matrix Components

*   **True Positives (TP):** The AI predicted Positive, and it was correct.
    *   *Example:* AI detected a fraudulent transaction, and it was actually fraud.
*   **True Negatives (TN):** The AI predicted Negative, and it was correct.
    *   *Example:* AI deemed a normal purchase safe, and it was.
*   **False Positives (FP):** The AI predicted Positive, but it was incorrect. This is a **Type I Error** or "False Alarm."
    *   *Example:* Your bank blocks your card for a regular shopping trip.
*   **False Negatives (FN):** The AI predicted Negative, but it was incorrect. This is a **Type II Error** or "Silent Miss."
    *   *Example:* A scammer steals money, and the AI fails to alert you.

### Not All Mistakes Are Equal

The relative severity of FP and FN errors varies significantly by application:

*   **Transaction Safety:** Avoiding FP (blocking legitimate users) is crucial. A false alarm is annoying.
*   **Medical Scans:** Avoiding FN (missing a tumor) is paramount. A false positive might lead to an extra, non-harmful test.

## Contextualizing Errors: Precision and Recall

Based on the relative costs of Type I and Type II errors, we prioritize different metrics.

### Precision: Quality Control

**Precision** answers: "Of all the cases the AI *claimed* were positive, how many actually were?" It measures the **trustworthiness** of positive predictions. High precision means fewer false alarms.

$$
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
$$

*   **Use Case (Spam Filter):** If an important email (e.g., bank OTP) goes to spam (FP), it's a disaster. If a marketing ad reaches the inbox (FN), it's merely annoying. Here, we prioritize **high precision** to ensure that anything labeled "spam" is genuinely spam.

### Recall: The Dragnet

**Recall** (also known as **Sensitivity**) answers: "Of all the *actual* positive cases, how many did the AI successfully find?" It measures the **completeness** of positive identification. High recall means fewer missed actual positives.

$$
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
$$

*   **Use Case (Life-Saving AI):** If a sick patient is sent home (FN), it's fatal. If a healthy person gets an extra test (FP), it's less critical. Here, we prioritize **high recall** to catch every single case of the disease.

### The Precision-Recall Trade-off

Often, increasing precision leads to decreasing recall, and vice-versa. Making an AI stricter to avoid false alarms (higher precision) may cause it to miss more actual positive cases (lower recall). This is the "see-saw" effect.

### F1 Score: The Balancing Act

The **F1 Score** is the harmonic mean of Precision and Recall. It provides a single metric that punishes models with extreme imbalances between precision and recall, thus favoring models that perform well on both.

$$
\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

**Example Calculation (Medical Results: 100 Patients)**
Given: TP = 8, FP = 2, FN = 2, TN = 88.

*   **Accuracy:** $(8 + 88) / (8 + 2 + 2 + 88) = 96/100 = 96\%$
*   **Precision:** $8 / (8 + 2) = 8/10 = 0.8 = 80\%$
*   **Recall:** $8 / (8 + 2) = 8/10 = 0.8 = 80\%$
*   **F1 Score:** $2 \times (0.8 \times 0.8) / (0.8 + 0.8) = 2 \times 0.64 / 1.6 = 1.28 / 1.6 = 0.8 = 80\%$

In this example, despite 96% accuracy, 1 in 5 positive results are false alarms (80% precision), highlighting the need for more nuanced metrics.

## Beyond Binary Outcomes: Thresholds and Probabilities

Most AI models output a **probability score** (a value between 0 and 1) rather than a direct "Yes" or "No." For example, "There is a 0.72 chance this transaction is fraud." To translate these probabilities into discrete predictions, we must choose a **Threshold ($k$)**.

*   If an AI's score is $\ge k$, predict "Positive".
*   If an AI's score is $< k$, predict "Negative".

The choice of $k$ significantly impacts Precision and Recall:
*   **High Threshold (e.g., $k=0.9$):** "Only alert if you are 90% sure." This leads to high precision (fewer FPs), but many false negatives (FNs).
*   **Low Threshold (e.g., $k=0.1$):** "Alert if there is even a 10% chance." This leads to high recall (fewer FNs), but many false positives (FPs).

### Score Distributions

The "skill" of an AI lies in its ability to separate the probability scores of positive and negative classes.
*   **Perfect Separation:** If there's a clear "gap" between the scores of positive and negative instances, a single threshold can achieve 100% success with zero mistakes.
*   **Real-World Overlap:** In practice, score distributions often overlap. This overlap forces a trade-off: catching more true positives will inevitably lead to flagging more false positives.

## The Receiver Operating Characteristic (ROC) Curve

To evaluate a model's performance across *all possible thresholds*, we use the **Receiver Operating Characteristic (ROC) curve**. It graphically illustrates the trade-off between:

*   **Y-axis: True Positive Rate (TPR)**, also known as **Sensitivity** or **Recall**.
    $$
    \text{TPR} = \frac{\text{TP}}{\text{TP} + \text{FN}}
    $$
    (How sensitive is the AI to finding the positive cases?)

*   **X-axis: False Positive Rate (FPR)**.
    $$
    \text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}
    $$
    FPR is related to **Specificity** (the ability to correctly identify negatives): $\text{FPR} = 1 - \text{Specificity}$.
    (How specific is the AI about only flagging the truly sick?)

### Visualizing the ROC Curve

A model's "skill" is evident in how much its ROC curve "bows" towards the top-left corner of the graph. The further it bows, the better it is at catching more positives while making fewer mistakes.

### Random Guessing Baseline

A purely random guessing model always produces a diagonal line from (0,0) to (1,1) on the ROC curve. This is because its hit rate (TPR) equals its error rate (FPR) regardless of how often it guesses "Positive." For example, guessing "Positive" 50% of the time yields (0.5, 0.5).

### Interpreting ROC Corners

*   **Point (0,0):** Achieved by setting a very high threshold (e.g., $k=1.0$). The AI predicts "Negative" for everyone. This results in **0 FPR** (no false alarms) and **0 TPR** (no true positives caught).
*   **Point (1,1):** Achieved by setting a very low threshold (e.g., $k=0.0$). The AI predicts "Positive" for everyone. This results in **1.0 FPR** (maximum false alarms) and **1.0 TPR** (perfect recall, caught everyone).

### ROC for Perfect Separation vs. Overlap

*   **Perfect Separation:** An AI with perfectly separated score distributions can achieve the "perfect point" (0,1) on the ROC curve, meaning 100% TPR and 0% FPR at an optimal threshold. The curve shoots straight up to (0,1) and then straight across to (1,1).
*   **Overlapping Scores:** When scores overlap, the ROC curve bows away from (0,1). Every increase in TPR will be accompanied by an increase in FPR, illustrating the inherent trade-off.

## Area Under the Curve (AUC)

The **Area Under the (ROC) Curve (AUC)** is a single scalar value that quantifies the overall performance of a classification model. It represents the probability that the model ranks a randomly chosen positive instance higher than a randomly chosen negative instance.

### Interpreting the AUC Score

*   **AUC = 1.0:** Perfect model (perfect separation).
*   **AUC = 0.8 - 0.9:** Excellent model.
*   **AUC = 0.5:** Random guessing (diagonal line).
*   **AUC $<$ 0.5:** Worse than random guessing (model likely miscalibrated or inverted).

### Why use AUC instead of Accuracy?

1.  **Threshold Independent:** AUC measures the model's inherent ability to separate classes, irrespective of the chosen classification threshold.
2.  **Imbalance Robust:** Unlike accuracy, AUC is not fooled by imbalanced datasets. It evaluates how well the model distinguishes between positive and negative classes across all possible thresholds, making it a robust metric for scenarios like the rare disease problem.

AUC tells you: "Is this model actually capable of distinguishing between these two groups?"

### Engineering the "Elbow"

The ROC curve also helps in selecting an optimal threshold for specific application needs. We can identify an "elbow" point on the curve that balances TPR and FPR according to the problem's costs:

*   **Medical AI:** We might want to move "up" the curve to maximize TPR, even if it slightly increases FPR, prioritizing catching all true positives.
*   **Spam Filter:** We might want to move "left" on the curve to minimize FPR, even if it slightly lowers TPR, prioritizing trustworthy positive predictions.

## Quick Summary

*   **Accuracy:** Use only for balanced, low-stakes data. Easily misled by class imbalance.
*   **Confusion Matrix:** Breaks down predictions into TP, TN, FP, FN for detailed analysis.
*   **Precision:** Use when False Positives (false alarms) are costly (e.g., spam filter).
*   **Recall:** Use when False Negatives (silent misses) are fatal (e.g., medical diagnosis).
*   **F1 Score:** Use to balance Precision and Recall for a single optimal threshold, especially on imbalanced datasets.
*   **ROC Curve (TPR vs. FPR):** Visualizes the model's performance across all possible thresholds, showing the trade-off.
*   **AUC (Area Under ROC Curve):** A single metric (0.5 to 1.0) to measure the overall discriminative power of the model, robust to threshold choice and class imbalance.

In AI engineering, a model is only as good as the metric used to judge it. Always **measure what matters, not just what is easy.**

