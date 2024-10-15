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
