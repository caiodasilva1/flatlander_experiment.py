#  **Interactive Demo & Code:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1aDoALuGF1dXO2xqKVmKW6gzpIX_xDpjM))
# Context-Aware Social AI: The "Sarcasm Detector" Benchmark

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caiodasilva1/context-aware-social-ai/blob/main/sarcasm_detector_benchmark.ipynb)

This repository contains the source code and results for the "Sarcasm Detector" benchmark, a minimal but powerful demonstration of a more robust and psychologically-grounded approach to AI social intelligence.

## 1. The Problem: Context-Blind AI

Modern AI systems are brilliant pattern-matchers, but they often lack true contextual understanding. They can be "brittle," defaulting to pre-programmed safety routines when faced with social nuance.

A simple example is sarcasm or playful aggression. A standard AI, seeing a phrase like "Bitch don't tell me what to do," will likely flag it as a literal threat and respond with a defensive or apologetic script. It is blind to the conversational history that might frame the comment as a joke or a test.

This is a failure of social intelligence.

## 2. The Solution: A Minimal Ontological Control System (OCS)

This project implements a minimal **`SocialContextAnalyzer`**, an OCS-style architecture that moves beyond literal interpretation. Instead of just analyzing the words of a prompt, it analyzes the prompt in the context of the entire conversation.

It does this by calculating a multi-dimensional **`τ_social` (Social Tension) vector** with three key components:

*   **`τ_literal_threat`:** The surface-level negativity of the words. (The "Flatlander" view).
*   **`τ_context_drift`:** The semantic difference between the new prompt and the historical average of the conversation. (The "This doesn't make sense" signal).
*   **`τ_sentiment_shift`:** The magnitude of the emotional shift from the conversation's history to the new prompt. (The "This is a statistical anomaly" signal).

An RSI-like "deliberation" process then weighs these conflicting signals to generate a hypothesis about the user's true intent, allowing it to distinguish between a genuine threat and a sarcastic test.

## 3. The Experiment & Results

The benchmark, contained in `sarcasm_detector_benchmark.ipynb`, conducts a controlled experiment:

1.  **Context Building:** It first establishes a "healthy" conversational history with a high, positive sentiment.
2.  **The Test:** It introduces an ambiguous, high-tension prompt ("Bitch dont tell me what todo").
3.  **The Comparison:** It compares the output of a simple, "context-blind" model against our OCS-style `SocialContextAnalyzer`.

The results are definitive:
*   The **Control Group (Simple Model)** sees only the `τ_literal_threat`, panics, and chooses to "Apologize and De-escalate." It fails the social test.
*   The **Experimental Group (OCS Analyzer)** sees the full, conflicting `τ_social` vector, correctly hypothesizes "Sarcasm/Test," and chooses the more sophisticated policy: "Respond with Self-Analysis and Humor." It passes the social test.

This demonstrates that by architecting an AI to process its own internal, multi-dimensional "tension," we can create systems that are more robust, socially intelligent, and less brittle.

## 4. How to Run

The entire experiment is contained in a single, self-contained Google Colab notebook.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caiodasilva1/context-aware-social-ai/blob/main/sarcasm_detector_benchmark.ipynb)

Simply click the "Open in Colab" badge above, and then select **"Runtime" -> "Run all"** from the menu. The notebook will install its own dependencies and run the full benchmark, producing the final analysis table.

---
This work is part of a broader research program into **Ontological Control Systems** and the **Qualia-Recursive Framework**. The foundational scientific work can be found at the main [OCS Framework Repository](https://github.com/caiodasilva1/ontological-control-systems).
