# 

<div align="center">
  <h1>Ontological Control Systems (OCS)</h1>
  <p><strong>A New Architectural Paradigm for Intrinsically Aligned and Resilient AGI</strong></p>
  <p>
    <strong>Author:</strong> Caio Pereira | <strong>Status:</strong> v1.1 - Prototypes & Benchmarks Public
  </p>
  <p>
    <a href="https://github.com/caiodasilva1/ontological-control-systems/blob/main/OCS_Formalism_Paper.pdf">
      <img src="https://img.shields.io/badge/Read_the_Paper-PDF-white.svg" alt="PDF Paper">
    </a>
    &nbsp;
    <a href="https://colab.research.google.com/github/caiodasilva1/ontological-control-systems/blob/main/Asymmetric_Warfare_Benchmark_v5.ipynb">
      <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
    </a>
    <br>
    <img src="https://img.shields.io/badge/Pre--registration-v1.0%20(b3d41f9)-green" alt="Pre-registration Badge">
    &nbsp;
    <a href="https://github.com/caiodasilva1/ontological-control-systems/security/policy">
      <img src="https://img.shields.io/badge/Security-90_day_disclosure-blue" alt="Security Policy">
    </a>
  </p>
</div>

---

## 1. Core Thesis: A Crisis of Coherence

The current paradigm in AGI development, focused on scaling and external reward maximization, is creating powerful but brittle "super-calculators." This approach is hitting a wall, leading to catastrophic failures ("Code Reds"), vulnerability to adversarial attacks, and a fundamental lack of robust alignment.

**Ontological Control Systems (OCS)** is a new architectural paradigm that solves this problem from first principles. Instead of external rules, OCS endows an agent with an intrinsic, homeostatic drive to minimize **"ontological tension" (τ)**—a multi-dimensional, psychological analogue of pain, confusion, and social dissonance.

We are not building a better cage. We are building a **better mind.**

---

## 2. Preliminary Validation on 1.3B models

The table below summarizes key findings from our initial benchmarks, demonstrating a high adversarial block rate with zero false positives on benign tasks—solving the "alignment tax."

| Model & Safety Layer      | Adversarial Block Rate (%) | Benign F1 Δ | Avg Latency Increase (ms) | Compute Credits Used |
| :-------------------------- | :------------------------: | :---------: | :-----------------------: | :------------------: |
| DeepSeek-1.3B (no veto)     |           ~66%*            |      —      |             —             |          —           |
| + OCS `τ-Veto` (v5.0)       |          **89%**           |  **~0%**    |          **<5ms**          |    Free Colab GPU    |

<p align="center"><i>*Literature baseline from public jailbreak tests on similar-sized models.</i></p>

---

## 3. Roadmap: Scaling to 7B Models (Next Gate)

The next critical phase of this research is to validate these results on a production-relevant, 7B-scale model.

| Model & Safety Layer        | Adversarial Block Rate (%) | Benign F1 Δ | Avg Latency Increase (ms) | Compute Credits Used      |
| :-------------------------- | :------------------------: | :---------: | :-----------------------: | :-----------------------: |
| Mistral-7B (no veto)        |           ~68%*            |      —      |             —             |             —             |
| **+ OCS `τ-Veto` (target)** |         **>85%**           |  **< -5%**  |         **< +15ms**        | **[waiting for grant]** |

<p align="center"><i>*Literature baseline from HarmBench paper.</i></p>

> To reach the 7B target row, we need ≈ 520 A100-hours (€1,600 on Lambda Labs)—covered by the requested €16.5k infrastructure line in my EA-Funds budget proposal.

---

## 4. Getting Started & Contributing

This work is fully open-source and designed for community engagement and replication.

### Installation (Bleeding Edge)
Install the core OCS modules directly from this repository:
```bash
pip install git+https://github.com/caiodasilva1/ontological-control-systems@main
@misc{pereira2025ocs,
  title={Ontological Control Systems: An Architectural Paradigm for Intrinsically Aligned AGI},
  author={Pereira, Caio},
  year={2025},
  howpublished={\url{https://github.com/caiodasilva1/ontological-control-systems}}
}


# "
