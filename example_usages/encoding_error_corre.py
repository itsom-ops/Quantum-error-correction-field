
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import numpy as np

def create_surface_code_lattice(n):
    """
    Create a surface code lattice of size n x n.
    Args:
    - n (int): Size of the lattice (n x n).
    
    Returns:
    - QuantumCircuit: Quantum circuit with surface code lattice.
    """
    qc = QuantumCircuit(n*n, n*n)
   
    for i in range(n):
        for j in range(n):
           
            if (i + j) % 2 == 0:
                qc.h(i*n + j) 
            if i > 0:
                qc.cx((i-1)*n + j, i*n + j) 
            if j > 0:
                qc.cx(i*n + (j-1), i*n + j)  
    
    return qc

def simulate_surface_code(qc):
    """
    Simulate the surface code circuit and visualize results.
    Args:
    - qc (QuantumCircuit): Quantum circuit with surface code.
    
    Returns:
    - dict: Results of the simulation.
    """
    simulator = Aer.get_backend('qasm_simulator')
    compiled_circuit = qc.compile()
    result = execute(compiled_circuit, simulator, shots=1024).result()
    counts = result.get_counts(qc)
    
    return counts

def apply_error(qc, error_type, qubit_list):
    """
    Apply errors to the quantum circuit.
    Args:
    - qc (QuantumCircuit): Quantum circuit to apply errors.
    - error_type (str): Type of error ('bit-flip' or 'phase-flip').
    - qubit_list (list of int): List of qubits to apply errors.
    """
    if error_type == 'bit-flip':
        for qubit in qubit_list:
            qc.x(qubit)  
    elif error_type == 'phase-flip':
        for qubit in qubit_list:
            qc.z(qubit) 
def main():
   
    n = 5  
    qc = create_surface_code_lattice(n)
   
    counts_no_error = simulate_surface_code(qc)
    print("Counts without errors:", counts_no_error)
    
    
    error_qubits = [0, 1, 2]  
    apply_error(qc, 'bit-flip', error_qubits)
    counts_with_bit_flip = simulate_surface_code(qc)
    print("Counts with bit-flip errors:", counts_with_bit_flip)
    
    
    apply_error(qc, 'phase-flip', error_qubits)
    counts_with_phase_flip = simulate_surface_code(qc)
    print("Counts with phase-flip errors:", counts_with_phase_flip)
    
    
    plot_histogram([counts_no_error, counts_with_bit_flip, counts_with_phase_flip],
                   legend=['No Error', 'Bit-Flip Error', 'Phase-Flip Error'])

if __name__ == "__main__":
    main()
