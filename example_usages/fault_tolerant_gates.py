

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
                qc.cx(i*n + j, (i+1)%n*n + j) s

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
                qc.cz(i*n + j, (i+1)%n*n + j) 

def simulate_surface_code(qc):
    """
    Simulate the surface code circuit and visualize results.
    Args:
    - qc (QuantumCircuit): Quantum circuit with surface code.
    
    Returns:
    - dict: Results of the simulation.
    """
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    
    return counts

def main():
    n = 5  
    qc = create_surface_code_lattice(n)
    
   
    apply_logical_x_gate(qc, n)
    counts_logical_x = simulate_surface_code(qc)
    print("Counts after applying logical X gate:", counts_logical_x)
    
    
    apply_logical_z_gate(qc, n)
    counts_logical_z = simulate_surface_code(qc)
    print("Counts after applying logical Z gate:", counts_logical_z)
    
    
    plot_histogram([counts_logical_x, counts_logical_z],
                   legend=['Logical X Gate', 'Logical Z Gate'])

if __name__ == "__main__":
    main()

