# surface_code_fault_tolerant_gates.py

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import numpy as np

def create_surface_code_lattice(n):
    """
    Create a surface code lattice of size n x n.
    Args:
    - n (int): Size of the lattice (n x n).
    
    Returns:
    - QuantumCircuit: Quantum circuit with surface code lattice.
    """
    qc = QuantumCircuit(n*n)
    # Encode logical qubits into surface code lattice
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                qc.h(i*n + j)
            if i > 0:
                qc.cx((i-1)*n + j, i*n + j)
            if j > 0:
                qc.cx(i*n + (j-1), i*n + j)
    
    return qc

def apply_logical_x_gate(qc, n):
    """
    Apply a logical X gate to the surface code lattice.
    Args:
    - qc (QuantumCircuit): Quantum circuit with surface code.
    - n (int): Size of the lattice (n x n).
    """
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                qc.cx(i*n + j, (i+1)%n*n + j)  # Apply logical X gate using CNOTs

def apply_logical_z_gate(qc, n):
    """
    Apply a logical Z gate to the surface code lattice.
    Args:
    - qc (QuantumCircuit): Quantum circuit with surface code.
    - n (int): Size of the lattice (n x n).
    """
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                qc.cz(i*n + j, (i+1)%n*n + j)  # Apply logical Z gate using CZs

def simulate_surface_code(qc):
    """
    Simulate the surface code circuit and visualize results.
    Args:
    - qc (QuantumCircuit): Quantum circuit with
