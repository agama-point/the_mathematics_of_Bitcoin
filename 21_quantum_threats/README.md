# the_mathematics_of_Bitcoin

## 21) Quantum Threats

---

### 🚀 Fast Classical Factorization Demo

This simple Python script factorizes large integers **classically** in about 2 seconds, proving that for currently relevant numbers, traditional methods are still dominant.

```
N = 261980999226229
Prime factors:
15538213
16860433
Factorization time: 2.635 s
```

### 📊 The Current State of Factorization

While quantum computing (QC) is making steady progress, **quantum supremacy** in factorization is not an immediate threat.

The largest number successfully factored on a real, general-purpose quantum device in 2023 was:

$$\text{N} = 261,980,999,226,229 \text{ (a 48-bit number)}$$



### ⚛️ The Quantum Algorithm Used in the 2023 Experiment

The 2023 record of factoring the 48-bit number was **not** achieved using the full, revolutionary **Shor's Algorithm**.

Instead, the problem was solved using the **Quantum Approximate Optimization Algorithm (QAOA)**. This method is a **hybrid algorithm** that:

1.  Translates the factorization problem into a **lattice-ordering problem**.
2.  Solves the resulting optimization problem using the QAOA approach, combining quantum and classical steps.

**Conclusion:** For now, your machine's classic CPU is perfectly safe (and much faster) at breaking numbers in this range!


---

### 🚀 Classical Factorization vs. Quantum Limits

This Python script demonstrates that for small, 48-bit numbers, a classic CPU is still significantly faster and more practical than current state-of-the-art quantum computers.

| Feature | Classic Python Script (Your PC) | Quantum Factorization (2023 Record) |
| :--- | :--- | :--- |
| **Factored Number** | Millions/Billions (in $\approx 2 \text{s}$) | $261,980,999,226,229$ (48-bit) |
| **Algorithm Used** | Trial Division, Pollard's Rho, etc. | **QAOA** (Quantum Approximate Optimization Algorithm) |
| **Hardware** | Standard CPU | 10-Qubit Superconducting Processor |
| **Total Time** | **Seconds** | **Hours to Days** (dominated by classical preparation) |
| **Dominant Phase** | Direct Calculation | Classical Problem Reduction (Lattice Methods) |

### ⚛️ Deeper Dive: The Hybrid Approach and Time Complexity

The 2023 record, while technically impressive, was achieved using a **hybrid** quantum-classical method, not the direct, high-threat **Shor's Algorithm**.

The process involved significant pre-processing:

| Phase | Description | Estimated Time Range |
| :--- | :--- | :--- |
| **Classical Preparation** | Converting the factorization into a lattice optimization problem (CVP) and extensively reducing its size. | **Hours to Days** (Requires high-performance classical resources) |
| **Quantum Computation** | Repeatedly running the QAOA circuit to solve the final, small optimization step. | **Seconds to Minutes** (The actual circuit execution time) |
| **Evaluation** | Measuring, post-processing, and verifying the result. | **Seconds** |

**Conclusion:** The threat of full-scale **quantum supremacy** to current encryption (like RSA) remains in the future, as Shor's Algorithm requires thousands of stable qubits, which are not yet available. For now, the classical computer wins!

---

## Reported Quantum Gate Fidelities (Recent Years)

The table below summarizes **experimentally reported gate fidelities** achieved in recent years.  
Values focus mainly on **two-qubit gate fidelity**, which is the critical metric for entanglement and scalable quantum computation. Single-qubit fidelities are included where explicitly notable.

| Year | Organization / Lab | Qubit Technology | Metric | Reported Fidelity |
|-----:|--------------------|------------------|--------|-------------------|
| 2019 | Google (Sycamore) | Superconducting | Two-qubit gate fidelity | ~99.38% |
| 2021 | USTC (China) | Superconducting | Two-qubit XEB fidelity | ~99.9% |
| 2024 | IQM Quantum Computers | Superconducting | CZ two-qubit gate fidelity | ~99.9% |
| 2024 | Quantinuum (Helios) | Trapped ions | Single-qubit gate fidelity | ~99.9975% |
| 2025 | MIT (Fluxonium qubits) | Superconducting | Single-qubit gate fidelity | ~99.998% |
| 2025 | Rigetti Computing | Superconducting | Two-qubit gate fidelity | ~99.5% |
| 2025 | IonQ | Trapped ions | Two-qubit gate fidelity | ~99.99% |

### Notes
- **Two-qubit gate fidelity** is the dominant bottleneck for large-scale quantum computation.
- **Single-qubit fidelities** are typically higher and already exceed 99.99% on multiple platforms.
- Reported values depend on benchmarking methods (e.g. RB, XEB) and are not always directly comparable.
- Even fidelities above 99.9% lead to rapid reliability loss when many entangled qubits are involved, motivating **quantum error correction**.

This data provides realistic bounds for probabilistic models where total correctness scales as \( p^N \).


