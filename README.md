# Ontological Control Systems (OCS) Framework

**A research framework exploring intrinsic AI safety through ontological tension minimization.**

This repository contains the prototype implementation for the **Ontological Control Systems (OCS)** paradigm and the **τ-Veto mechanism**. Our work investigates a foundational shift in AI alignment: moving from external behavioral filters to embedding an intrinsic drive for multi-dimensional coherence within the agent itself.

🔗 **Interactive Prototype:** [Open the main notebook in Google Colab](https://colab.research.google.com/drive/1hcXNEdmH7o-3Una4Xsh95D6OvFtS9Mt_)

## 🧠 Core Concept: From External Cages to Intrinsic Conscience

Current AI safety approaches often act as brittle "cages" around a core optimizer that remains amoral. The OCS paradigm proposes a different path: an agent whose primary drive is to minimize its own **ontological tension (τ)**.

This tension τ is a multi-dimensional vector quantifying:
*   **Epistemic Tension:** Internal inconsistency, logical conflict, or uncertainty.
*   **Social Tension:** Misalignment with norms, violation of values, or causing harm.
*   **Physical Tension:** Impending system stress or violation of operational constraints.

By minimizing τ, an OCS agent seeks stable, coherent states across all dimensions, forming the basis for a **computational conscience**. This repository provides the first open-source tools to instantiate and test this theory.

## 🚀 Quick Start

The fastest way to explore the core concepts is via our interactive Colab notebook. It requires no local setup.

1.  **Open the Notebook:** Click the Google Colab link at the top of this README.
2.  **Follow the Instructions:** The notebook is structured to guide you through:
    *   The core `tau_framework.py` library.
    *   Instantiating a τ-Veto head on a small language model.
    *   Running simple experiments to see tension monitoring and veto mechanisms in action.

For local development, clone this repository and install the dependencies listed in `requirements.txt`.

## 📁 Repository Structure & Key Components

**Core Framework**
*   `tau_framework.py`: The central library defining the `TensionVector` and the logic for calculating and minimizing ontological tension (τ).
*   `tau_veto_head.py`: A safety-layer class designed to wrap Hugging Face transformer models. It monitors token generation in real-time and can veto sequences that lead to high tension states.

**Prototype Environments & Benchmarks**
*   `moral_maze.py`: A custom multi-agent grid-world environment to benchmark cooperative behavior and social tension dynamics.
*   `flatlander.py`: An environment for testing structured exploration and the management of epistemic vs. physical tension.
*   `experiments/`: Contains scripts for running comparative benchmarks between OCS-guided agents and standard reward-maximizing baselines.

**Getting Started & Examples**
*   `ocs_framework_demo.ipynb`: The main Jupyter/Colab notebook serving as an interactive tutorial and entry point.
*   `requirements.txt`: List of Python dependencies.

## 🎯 Project Goals & Roadmap

This work is the foundation for a formal research grant aimed at **scaling and rigorously validating the OCS approach for AI safety.**

*   **Phase 1 (Scale):** Port and evaluate the τ-Veto mechanism on state-of-the-art 7B parameter language models using standardized safety benchmarks.
*   **Phase 2 (Productize):** Refactor the core components into a clean, well-documented Python library (`ocs-safety`) to lower the barrier for community adoption and scrutiny.
*   **Phase 3 (Collaborate):** Disseminate findings through a technical report and seek pilot evaluations with alignment teams.

## 📄 License

This research prototype is published under the **MIT License**. See the `LICENSE` file for details.

---
**Research by Caio Pereira.** This project is part of a proposal to the Long-Term Future Fund, focused on reducing existential risk from misaligned AI.)

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
