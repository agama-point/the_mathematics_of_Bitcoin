# the_mathematics_of_Bitcoin

## 20) quantum computer

### Quantum Computing Experiments

Check out the repository here: [Quantum Computing Experiments](https://github.com/octopusengine/quantum_computing)

This repository focuses on **basic operations with qubits**, which can be tested and explored using **quantum simulators**. Our work in this area has been ongoing **since 2023**, providing practical examples and experiments for anyone interested in learning or experimenting with quantum computing.


We aim to provide a hands-on approach for beginners and enthusiasts to understand **superposition, entanglement, and basic quantum gates** without requiring access to real quantum hardware.


```python
from qiskit import QuantumCircuit
    
qc = QuantumCircuit(2, 2)
qc.h(0)     # Hadamard
qc.cx(0, 1) # CNOT
qc.measure([0, 1], [0, 1])

# Returns a circuit putting  
# 2 qubits in the Bell state.
print("[ bc ] bell circuit")
print(qc)
```

---

