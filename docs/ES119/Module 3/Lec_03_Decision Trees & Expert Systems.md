---
title: 'Decision Trees & Expert Systems: From Rules to Learning'
lecture_number: 3
lecture_name: Decision Trees & Expert Systems
category: Module 3
sidebar_label: Lecture 3
sidebar_position: 3
course: ES119 Principles of AI
topic:
- Decision Trees
- Expert Systems
- Information Theory
- Machine Learning Basics
tags:
- AI
- Decision Trees
- Machine Learning
- Entropy
- Information Gain
- Expert Systems
- Supervised Learning
math: true
summary: This lecture explores the evolution from rule-based Expert Systems to data-driven
  Decision Trees. We delve into the limitations of hard-coded logic, introduce Decision
  Trees as a 'white box' AI solution, and detail the mathematical principles of Entropy
  and Information Gain used to build them. Key concepts include recursive splitting,
  the problem of overfitting, and pruning techniques.
last_updated: "2 April 2026"
---


# Decision Trees & Expert Systems

## From Probability to Decision

In previous modules, we focused on calculating probabilities using tools like Bayes Nets. The next critical step in AI is to translate these probabilities into firm, actionable decisions (e.g., Yes/No, A/B/C). This lecture explores the evolution of AI decision-making, from manually crafted expert systems to data-driven decision trees.

## The Era of Expert Systems (1980s)

**Expert Systems** represented an early approach to AI, based on manually encoding human expert knowledge into a system.

*   **Approach:** Human experts (e.g., doctors) collaborated with programmers to translate their domain-specific logic into code.
*   **Knowledge Engineering:** The process of acquiring, representing, and organizing expert knowledge.
*   **Structure:** Typically relied on vast databases of `IF/THEN` rules. For instance, `IF Fever $>$ 100 AND Cough THEN Flu = 80%`.
*   **Domains:** Effective for narrow, structured problems (e.g., MYCIN for blood infections, credit scoring).

### Limitations: The "Exception Trap" and Complexity Wall

Real-world logic is rarely straightforward; exceptions abound.

*   **The Exception Trap:** Every rule seems to have a "but...". An initial rule like `IF Raining THEN Wear_Coat` quickly expands to `IF Raining AND Temp $<$ 70Â°F THEN Wear_Coat`, and then to further exceptions.
*   **Hard-coding Paradox:** To achieve true intelligence with expert systems, an infinite number of rules would be required to cover every possible context. This led to:
    *   **Brittleness:** Changing one rule to fix an exception often broke others due to unforeseen interactions.
    *   **Complexity Wall:** The system's logic became unmanageably complex, making maintenance and scaling impossible.

## The Data-Driven Pivot: Machine Learning

The solution to the expert system bottleneck was a paradigm shift: stop manually encoding rules and let machines discover patterns directly from data.

*   **Expert Systems (Old):** Human $\rightarrow$ Manual Rules $\rightarrow$ AI
*   **Machine Learning (New):** Data $\rightarrow$ Algorithm $\rightarrow$ Generated Rules

In this new paradigm, the computer "writes" the logic by observing evidence in historical data, moving from "hand-crafted logic" to "statistical learning."

## Decision Trees: Visualizing Generated Rules

A **Decision Tree** is a supervised learning algorithm that maps features (attributes) to a target value (class/decision). It stores the generated rules in an intuitive, tree-like structure.

*   **Root Node:** The initial question or attribute used to split the data.
*   **Branches:** Represent the possible outcomes or values of a question, leading to subsequent nodes or leaves.
*   **Leaf Nodes:** The final outcome or decision, representing a "pure" class.

**Key Advantage:** Decision Trees offer a clear **path of reasoning** (**"White Box" AI**). If an AI makes a decision, one can trace back through the branches to understand exactly why.

### How Decision Trees Solve the Bottleneck

*   **Automatic Exception Handling:** If patterns like "Rain + 100Â°F" exist in the data, the algorithm automatically creates a split for it, rather than requiring manual rule updates.
*   **Mathematical Rigor:** Decisions on splitting are based on quantifiable metrics (Entropy, Information Gain), removing human guesswork.
*   **Scalability:** Relatively easy to process a large number of features and examples.

## The Decision Tree Algorithm: Playing "20 Questions"

The core idea behind building a Decision Tree is analogous to the game "20 Questions": identify a sequence of questions that efficiently narrows down possibilities to reach a correct answer.

*   **Goal:** Organize data into homogeneous groups (or "piles") by asking a series of Yes/No (or multi-valued) questions.
*   **Rule:** Achieve the classification using the fewest questions possible.
*   **Machine's Goal:** Find questions that create the "purest" piles possible, minimizing ambiguity in each resulting subgroup.

### Evaluating Question Quality

A "good" question reduces the "messiness" or "impurity" of the data more effectively.

*   **Useless Question:** No progress; all items remain in one mixed pile.
*   **Confusing Question:** Some progress, but piles remain mixed.
*   **Perfect Question:** Creates perfectly pure piles.

## Measuring Messiness: Entropy

To objectively score questions, we need a "messiness meter." In computer science, this is **Entropy**.

*   **Entropy (H):** A measure of the impurity, disorder, or uncertainty in a set of data.
    *   $H = 0.0$: Perfectly pure (certainty). All items belong to one class.
    *   $H = 1.0$: Perfectly split 50/50 (maximum chaos/uncertainty for a binary classification).

### Shannon Entropy Equation

For a set of data with different classes (or outcomes), the Entropy $H$ is calculated as:
$$H = - \sum_{i=1}^{c} P(x_i) \log_2 P(x_i)$$
Where:
*   $c$ is the number of unique classes.
*   $P(x_i)$ is the proportion (percentage) of items belonging to class $x_i$ in the current pile.

**Example:**
If a pile has 10 Red and 10 Blue items:
$P(\text{Red}) = \frac{10}{20} = 0.5$
$P(\text{Blue}) = \frac{10}{20} = 0.5$
$H = - (0.5 \log_2 0.5 + 0.5 \log_2 0.5)$
$H = - (0.5 \times -1 + 0.5 \times -1)$
$H = - (-0.5 - 0.5) = - (-1) = 1.0$ (Perfectly Messy)

If a pile has 20 Red and 0 Blue items:
$P(\text{Red}) = 1.0$
$P(\text{Blue}) = 0.0$
$H = - (1.0 \log_2 1.0 + 0.0 \log_2 0.0)$
$H = - (1.0 \times 0 + 0)$ (Note: $0 \log_2 0$ is typically treated as 0 in this context)
$H = 0.0$ (Perfectly Pure)

## Information Gain: The "Improvement" Score

**Information Gain (IG)** quantifies how much a question reduces the entropy (messiness) of a dataset. It measures the "improvement" after a split. The goal is to maximize Information Gain at each step.

$$IG = \text{Entropy}(\text{Parent}) - \text{Weighted Average Entropy}(\text{Children})$$

Where:
*   $\text{Entropy}(\text{Parent})$: The entropy of the data before the split.
*   $\text{Weighted Average Entropy}(\text{Children})$: The sum of the entropy of each child node, weighted by the proportion of data that goes into that child node.

**Why "Weighted"?** A split typically creates child nodes of different sizes. Multiplying each child's entropy by its size relative to the parent ensures that the gain reflects the overall reduction in messiness across the entire dataset.
$$ \text{Weighted Avg Entropy} = \sum_{j=1}^{k} \left( \frac{\text{Items in Child}_j}{\text{Total Items}} \times \text{Entropy}(\text{Child}_j) \right) $$

*   **Higher Gain:** Indicates a "cleaner" split, moving significantly towards pure piles.
*   **Zero Gain:** No improvement; the piles remain just as messy as before.

## The Recursive Algorithm for Building a Decision Tree

Decision trees are built iteratively and recursively using the following steps:

1.  **Calculate Information Gain:** For every available attribute (column) in the current dataset, calculate its Information Gain if it were used to split the data.
2.  **Pick the Best Split:** Select the attribute with the highest Information Gain. This attribute becomes the current node (either root or an internal node).
3.  **Split the Data:** Divide the dataset into subsets based on the values of the chosen attribute. Each subset corresponds to a branch from the node.
4.  **Repeat (Recursion):** For each new subset (child node), repeat steps 1-3. Continue this process until:
    *   The entropy of a subset is $0$ (perfectly pure). This subset becomes a **leaf node**.
    *   No more attributes are available to split on.
    *   Pre-defined stopping criteria (pruning rules) are met.

### Example Walkthrough (Condensed)

Let's use a simplified "Play Tennis?" dataset (10 days, 5 Yes, 5 No outcomes).

**Starting State:** 5 Yes, 5 No.
*   **Initial Entropy (Parent):**
    $P(\text{Yes}) = 5/10 = 0.5$
    $P(\text{No}) = 5/10 = 0.5$
    $H = -(0.5 \log_2 0.5 + 0.5 \log_2 0.5) = 1.0$ (Perfectly messy)

**Step 1: Calculate IG for potential root splits (attributes: Outlook, Humidity, Wind).**

1.  **Outlook:**
    *   Sunny (3 items: 3 No, 0 Yes) $\rightarrow H=0$
    *   Rain (7 items: 2 No, 5 Yes) $\rightarrow P(\text{No})=2/7, P(\text{Yes})=5/7 \rightarrow H \approx 0.86$
    *   Weighted Avg Entropy = $(3/10 \times 0) + (7/10 \times 0.86) \approx 0.60$
    *   $IG(\text{Outlook}) = 1.0 - 0.60 = 0.40$

2.  **Wind:**
    *   Weak (6 items: 3 No, 3 Yes) $\rightarrow H=1.0$
    *   Strong (4 items: 2 No, 2 Yes) $\rightarrow H=1.0$
    *   Weighted Avg Entropy = $(6/10 \times 1.0) + (4/10 \times 1.0) = 1.0$
    *   $IG(\text{Wind}) = 1.0 - 1.0 = 0.0$ (Useless!)

3.  **Humidity:**
    *   High (4 items: 4 No, 0 Yes) $\rightarrow H=0$
    *   Normal (6 items: 1 No, 5 Yes) $\rightarrow P(\text{No})=1/6, P(\text{Yes})=5/6 \rightarrow H \approx 0.65$
    *   Weighted Avg Entropy = $(4/10 \times 0) + (6/10 \times 0.65) \approx 0.39$
    *   $IG(\text{Humidity}) = 1.0 - 0.39 = 0.61$ (**Winner!**)

**Step 2: First Split (Root Node: Humidity)**
Humidity has the highest Information Gain (0.61), so it becomes the root node.
*   `Humidity = High` branch: Leads to a `NO` decision (pure, $H=0$). This becomes a leaf node.
*   `Humidity = Normal` branch: Leads to a mixed pile (5 Yes, 1 No, $H \approx 0.65$). We recurse here.

**Step 3: Recursive Split on "Normal Humidity" Pile (remaining attributes: Outlook, Wind)**
Now, we only consider the 6 days where Humidity is Normal (5 Yes, 1 No).

1.  **Outlook (for Normal Humidity data):**
    *   Sunny (1 item: 1 No, 0 Yes) $\rightarrow H=0$ (pure)
    *   Rain (5 items: 0 No, 5 Yes) $\rightarrow H=0$ (pure)
    *   Outlook creates two perfectly pure groups.
    *   $IG(\text{Outlook for Normal Humidity}) = 0.65 - ((1/6 \times 0) + (5/6 \times 0)) = 0.65$ (**Winner!**)

**Step 4: Final Decision Tree**
The tree is now fully developed, with all leaf nodes being pure.

```text
Humidity?
|-- High (4 Days): NO (Leaf)
`-- Normal (6 Days)
    `-- Outlook?
        |-- Sunny (1 Day): NO (Leaf)
        `-- Rain (5 Days): YES (Leaf)
```

## The Danger of Overfitting & Engineering Fixes

A Decision Tree can perfectly memorize training data if allowed to grow indefinitely, asking a question for every single data point. This leads to **overfitting**.

*   **Overfitting:** The model performs exceptionally well on the training data but fails to generalize to new, unseen real-world data because it has learned noise and specific patterns rather than the underlying trends.

### Pruning Techniques

To prevent overfitting, engineers "prune" the tree, forcing it to stop growing early.

*   **Max Depth:** Limit the maximum number of questions (levels) in the tree. E.g., "Stop after 5 questions."
*   **Min Samples (per leaf/split):** Specify the minimum number of data points required to split a node or for a node to be considered a leaf. E.g., "Stop if a pile has fewer than 10 items."

Pruning simplifies the tree, making it more robust and improving its generalization performance.

## The "White Box" Advantage of Decision Trees

Decision Trees are highly valued for their interpretability.

*   **Interpretability:** Unlike "black box" models (e.g., complex Neural Networks), the exact logic of every prediction made by a Decision Tree can be easily traced and understood by humans.
*   **Human-Readable Logic:** The tree directly translates into a set of simple `IF-THEN` rules.
    *   `IF (Humidity is Normal) AND (Outlook is Rain) THEN Play Tennis.`
    *   `IF (Humidity is High) THEN Don't Play.`
*   **Auditability & Trust:** This transparency is critical in high-stakes fields like medicine, finance, and law, where understanding *why* a decision was made is as important as the decision itself. It allows for auditing the AI's reasoning and building trust in its outputs.

## Quick Summary

Decision Trees represent a powerful shift from brittle, human-coded Expert Systems to robust, data-driven Machine Learning. They use **Entropy** to quantify data impurity and **Information Gain** to determine the best splitting questions, recursively building an interpretable, rule-based model. While intuitive, they are prone to **overfitting**, which is mitigated by **pruning techniques** like `max_depth` and `min_samples`. Their "white box" nature, offering clear, auditable decision paths, makes them indispensable in many applications.


