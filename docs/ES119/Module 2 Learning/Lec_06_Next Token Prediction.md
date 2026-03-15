---
title: Next Token Prediction
lecture_number: 6
lecture_name: Next Token Prediction
category: Module 2 Learning
sidebar_label: Lecture 6
sidebar_position: 6
course: ES119 Principles of AI
topic:
- Natural Language Processing
- Generative Models
- Character-level Language Models
- Neural Networks
tags:
- Next Token Prediction
- NLP
- Generative AI
- Character Embeddings
- MLP
- Cross-Entropy
- Sampling
- Andrej Karpathy
summary: This lecture introduces the foundational concept of next token prediction,
  a core mechanism behind modern large language models. We explore character-level
  prediction as a classification task, delve into the critical role of learnable character
  embeddings, and detail a simple Multi-Layer Perceptron (MLP) based architecture
  for training and generating sequences through probabilistic sampling. The concepts
  are illustrated with a practical example of generating Indian names, emphasizing
  the iterative nature of sequence generation.
math: true
---


# Next Token Prediction: Foundations of Generative Language Models

Welcome to Lecture 6. Today, we delve into one of the most fundamental concepts underpinning modern generative AI: **Next Token Prediction**. This mechanism, often operating at the character or subword level, is the core engine for models like ChatGPT, allowing them to produce coherent and contextually relevant text. Our discussion draws inspiration from foundational works, including Andrej Karpathy's "Neural Networks: Zero to Hero" series, which provides excellent insights into building these systems from first principles.

## The Problem Formulation: Character-Level Prediction

At its heart, next token prediction, especially at the character level, can be framed as a **classification task**. Given a sequence of preceding characters (the "context"), the model's goal is to predict the most probable *next* character.

Consider the prompt "app\_". The task is to determine what character is most likely to follow "app". The model doesn't just guess one character; it outputs a **probability distribution** over all possible characters in its vocabulary. For instance:

| Character (c) | Probability P(c) |
| :------------ | :--------------- |
| a             | 0.01             |
| b             | ...              |
| ...           | ...              |
| p             | 0.4              |
| ...           | ...              |
| z             | ...              |
| - (end token) | ...              |

In this example, 'p' might have a probability of 0.4, indicating it's a strong candidate for the next character.

## Case Study: Generating Indian Names

To make this concrete, let's consider a specific problem: **generating plausible Indian names**.

Our dataset would consist of a list of Indian names, such as:
*   aabid
*   aadesha
*   ...
*   zeel

To simplify the problem, we establish a few assumptions:
1.  **Limited Vocabulary:** We only consider 26 lowercase English characters (a-z).
2.  **End-of-Sequence Token:** A special character, often denoted as '-', indicates the end of a name. This allows the model to know when to stop generating.
3.  **Length Constraints:** For this specific task, we might impose a length constraint, e.g., $4 < \text{length} < 10$.

## Creating Training Data

For training, we transform our list of names into `(input_context, next_character)` pairs. We define a fixed "context window" (e.g., 3 characters) that the model considers.

Let's take the name "aabid" and a context window of 3 characters:
*   Initial state (empty context): `---` predicts `a`
*   Context: `--a` predicts `a`
*   Context: `-aa` predicts `b`
*   Context: `aab` predicts `i`
*   Context: `abi` predicts `d`
*   Context: `bid` predicts `-` (end token)

Each of these `(context, next_character)` pairs forms a training example for our classification task.

## The Crucial Role of Character Embeddings

A key idea in modern NLP is **representation learning**. Instead of treating characters as discrete, arbitrary symbols, we learn a **vector representation (embedding)** for each character.
The intuition is that "similar" characters (e.g., phonetically or contextually similar) should have vector representations that are "closer" in a multi-dimensional space.

This concept extends from Word2Vec, where semantic relationships are captured through vector arithmetic. For example:
$$ \text{vector}(\text{KING}) - \text{vector}(\text{MAN}) + \text{vector}(\text{WOMAN}) \approx \text{vector}(\text{QUEEN}) $$
Similarly, at a character level, 'a' and 'e' might be closer in embedding space than 'a' and 'z' if they frequently appear in similar contexts or have similar phonetic properties within our dataset.

### The Embedding Matrix

We implement this by having an **embedding matrix** or lookup table. This table maps each unique character in our vocabulary to a fixed-dimensional vector. If we have 27 characters (a-z, plus the end token '-') and we choose a `k`-dimensional embedding, our matrix would be $27 \times k$.

Example for `k=2` dimensions:
| Char | Dim 1 | Dim 2 | ... | Dim k |
| :--- | :---- | :---- | :-- | :---- |
| a    | 0.1   | 0.3   | ... | ...   |
| b    | -0.1  | 0.1   | ... | ...   |
| ...  | ...   | ...   | ... | ...   |
| z    | ...   | ...   | ... | ...   |
| -    | ...   | ...   | ... | ...   |

Crucially, the values in this embedding matrix are **learnable parameters**. They are not fixed manually but are optimized during the training process to best serve the next token prediction task.

## Overall Model Architecture

Let's break down the architecture of our character-level next token predictor:

1.  ### Embedding Lookup
    Given an input context, say `a b i` (each character represented by its numerical index), we perform a lookup in the embedding matrix. Each character `c` maps to its corresponding `k`-dimensional vector $\mathbf{v}_c$.
    E.g., `a` -$>$ $\mathbf{v}_a$, `b` -$>$ $\mathbf{v}_b$, `i` -$>$ $\mathbf{v}_i$.

2.  ### Concatenation of Embeddings
    The individual `k`-dimensional embeddings of the context characters are concatenated to form a single, long feature vector. If the context window is `N` characters and each embedding is `k`-dimensional, the resulting feature vector will be `N * k` dimensions.
    For `a b i` with `k=2`: $[\mathbf{v}_a, \mathbf{v}_b, \mathbf{v}_i] = [0.1, 0.3, -0.1, 0.1, 0.6, 0.4]$

3.  ### Multi-Layer Perceptron (MLP)
    This concatenated feature vector is then fed into a standard Multi-Layer Perceptron (MLP). The MLP consists of one or more hidden layers, each typically followed by a non-linear activation function (e.g., ReLU).
    The final layer of the MLP is an output layer with `V` neurons, where `V` is the size of our character vocabulary (27 in our example). A softmax activation function is applied to the output layer to produce a probability distribution over all possible next characters.
    $$ \text{softmax}(\mathbf{z})_j = \frac{e^{z_j}}{\sum_{c=1}^{V} e^{z_c}} $$

4.  ### Training with Cross-Entropy Loss
    The model is trained to minimize the **cross-entropy loss** between the predicted probability distribution and the true next character (represented as a one-hot vector). Cross-entropy loss is suitable for multi-class classification problems.
    $$ L(\mathbf{y}, \hat{\mathbf{y}}) = - \sum_{j=1}^{V} y_j \log(\hat{y}_j) $$
    where $\mathbf{y}$ is the true one-hot vector and $\hat{\mathbf{y}}$ is the predicted probability distribution.

    During backpropagation, this loss is used to update:
    *   The **weights and biases of the MLP layers**.
    *   The **values in the character embedding matrix**. This is how the character embeddings become meaningful and learn to capture semantic similarity.

## Generating New Sequences (Sampling)

Once the model is trained, we can use it to generate new names or sequences:

1.  **Initial Context:** Start with an empty context (e.g., `---`).
2.  **Predict Probabilities:** Feed the current context into the trained model to get a probability distribution $P(c)$ for the next character.
3.  **Sample the Next Character:** Instead of simply picking the character with the highest probability (greedy approach), we **sample** from this distribution. This introduces stochasticity and diversity, preventing the model from always generating the exact same sequence. If 'p' has 40% chance and 'q' has 30% chance, we might sometimes pick 'q' even if 'p' is more likely.
4.  **Append and Repeat:** Append the sampled character to the current sequence. Shift the context window (discarding the oldest character and adding the new one). Repeat steps 2 and 3.
5.  **Termination:** Continue until the end-of-sequence token ('-') is sampled or a maximum length is reached.

This iterative sampling process allows the model to explore different paths in the "generation tree," creating novel sequences that reflect the patterns learned from the training data. For example, starting with `aab`, the model might sample `a` (leading to `aaba`), or `i` (leading to `aabi`), each path further branching based on subsequent sampled characters.

## Quick Summary

Next token prediction forms the bedrock of modern generative language models. By framing it as a classification task, we leverage neural networks to learn both contextual patterns and meaningful character embeddings. The architecture involves looking up embeddings for context characters, concatenating them, passing them through an MLP, and training with cross-entropy loss. Crucially, the generation process utilizes probabilistic sampling to produce diverse and creative output sequences.