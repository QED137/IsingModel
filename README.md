# IsingModel
This project implements a 2D Ising model simulation using the **Metropolis-Hastings algorithm** in Python
# 2D Ising Model Simulation with Metropolis Algorithm

This project implements a 2D Ising model simulation using the **Metropolis-Hastings algorithm** in Python. The Ising model is a simple representation of ferromagnetism in statistical mechanics. In this implementation, spins are placed on a two-dimensional lattice, where each spin can be either +1 or -1, and the model can simulate the effects of both nearest-neighbor interactions and an external magnetic field.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [Code Structure](#code-structure)
- [Simulation Parameters](#simulation-parameters)
- [Results and Visualization](#results-and-visualization)
- [Future Work](#future-work)
- [License](#license)

## Overview

The Ising model is a mathematical model of ferromagnetism in statistical mechanics. It consists of discrete variables (spins) that represent magnetic dipole moments of atomic spins that can be in one of two states: +1 (spin up) or -1 (spin down). 

In this implementation, we simulate a 2D grid of spins and compute the energy and magnetization of the system using the **Metropolis algorithm**. The simulation considers interactions between nearest neighbors and can include an external magnetic field.

# 2D Ising Model: Simulation and Analysis

The 2D Ising model is a fundamental model in statistical mechanics and computational physics. It represents a system of interacting spins (magnetic moments) on a lattice and is used to study phase transitions, magnetism, and critical phenomena. The spins can take values of \(S_{i,j} = +1\) (spin-up) or \(S_{i,j} = -1\) (spin-down), and their interactions are described by the Hamiltonian, \(H(S)\), which sums the energy contributions from nearest-neighbor interactions between spins. This project will involve simulating the Ising model using the Metropolis-Hastings algorithm and studying its thermodynamic properties through numerical experiments.

## Problem Outline:

### Hamiltonian of the Ising Model:
\[
H(S) = -J \sum_{\langle \mu \nu \rangle} S_\mu S_\nu
\]

Where \(J\) is the coupling constant, \(\langle \mu \nu \rangle\) refers to a summation over neighboring spin pairs, and \(S_\mu\) represents the spin at lattice site \(\mu\).
- If \(J > 0\), the system is ferromagnetic (spins prefer alignment).
- If \(J < 0\), the system is antiferromagnetic (spins prefer anti-alignment).

### Boltzmann Weight for Canonical Ensemble:
The probability weight of a given spin configuration \(S\) is determined by the Boltzmann factor:
\[
w(S) = \frac{e^{-H(S)/(k_B T)}}{Z}
\]
Where \(Z\) is the partition function and \(T\) is the temperature.

### Physical Quantities of Interest:
- **Energy per spin:**
\[
E = \sum_S w(S) H(S)
\]
- **Magnetization per spin:**
\[
M = \sum_S w(S) \left( \sum_\mu S_\mu \right)
\]

### Simulation Method:
The **Metropolis-Hastings algorithm** is used to update the spin configuration. A single spin flip is proposed at each lattice site, and the change in energy is evaluated. The transition probability is governed by the Metropolis ratio:
\[
\frac{w(S')}{w(S)} = e^{-[H(S') - H(S)] / (k_B T)}
\]

For a single spin flip, this simplifies to:
\[
\frac{w(S')}{w(S)} = e^{-2J S_{i,j} [S_{i+1,j} + S_{i-1,j} + S_{i,j+1} + S_{i,j-1}] / (k_B T)}
\]

### Tasks:
- **Simulate** a 16x16 Ising lattice with periodic boundary conditions.
- **Compute and plot** energy and magnetization per spin for various values of the coupling constant \(J\).
- **Extend** the model by including an external magnetic field \(B\).


## Features

- **2D Lattice**: Simulates spins on a \(n \times n\) lattice.
- **Periodic Boundary Conditions**: Implemented for spins at the edges of the lattice.
- **Metropolis Algorithm**: Used for updating the spins based on a probabilistic acceptance rule.
- **External Magnetic Field**: Allows the simulation to account for the effect of an external magnetic field on the spins.
- **Energy and Magnetization**: Tracks the energy and magnetization per spin over time.
- **Visualization**: Generates plots of energy and magnetization per spin over iterations.

## Dependencies

Make sure you have the following Python packages installed:

```bash
numpy
matplotlib
```
# How to Run
```bash
git clone repository
cd repo_directory
python isingwithmagnetic.py
```
## Code Structure
isingwithmagnetic.py: The main script containing the 2D Ising model simulation with an external magnetic field. It includes:
  -Initialization of the lattice.
  - Implementation of the Metropolis-Hastings algorithm.
  - Calculation of energy and magnetization.
  - Visualization of results using matplotlib.

## Key Functions:
   - initialize_lattice(n): Initializes the lattice with random spins of +1 or -1.
   - metropolis_ising_with_field(lattice, J, B, kBT, n_steps): Runs the Metropolis algorithm for a given number of steps, considering both nearest-neighbor interactions and an external magnetic field.
   - calculate_energy_with_field(lattice, J, B): Computes the energy of the system, including the contribution of the external magnetic field.
## Simulation Parameters
   - Lattice Size (n): The number of spins in each dimension of the square lattice (e.g., 16x16).
   - Interaction Strength (J): Strength of the interaction between neighboring spins.
   - External Magnetic Field (B): Strength of the external magnetic field.
   - Temperature (kBT): Temperature of the system in natural units.
   - Number of Steps (n_steps): The number of iterations for the Metropolis algorithm.
### Example of adjusting parameters in the script:
```bash
n = 16           # Lattice size (n x n)
J = 0.3          # Interaction strength
B = 0.5          # Magnetic field strength
kBT = 1.0        # Temperature
n_steps = 500    # Number of Metropolis steps
```

LICENSE @MIT

## Future Work

### Possible extensions of this project include:
   - Simulating the Ising model in 3D.
   - Investigating phase transitions as the temperature varies.
   - Parallelizing the code to speed up simulations for larger lattice sizes.
   - Exploring the Ising model in the presence of different types of external fields (e.g., varying fields over time).
