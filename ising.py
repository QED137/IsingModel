import numpy as np
import matplotlib.pyplot as plt

# Metropolis-Hastings algorithm for 2D Ising model
def metropolis_ising(lattice, J, kBT, n_steps):
    n = lattice.shape[0]
    energies = []
    magnetizations = []

    # Calculate the initial energy and magnetization
    energy = calculate_energy(lattice, J)
    magnetization = np.sum(lattice)
    
    for step in range(n_steps):
        # Loop through the lattice and flip spins
        for _ in range(n**2):
            i = np.random.randint(0, n)
            j = np.random.randint(0, n)

            # Calculate the change in energy if we flip the spin at (i, j)
            delta_E = 2 * J * lattice[i, j] * (
                lattice[(i+1) % n, j] +
                lattice[(i-1) % n, j] +
                lattice[i, (j+1) % n] +
                lattice[i, (j-1) % n]
            )
            if delta_E < 0 or np.random.rand() < np.exp(-delta_E / kBT):
                lattice[i, j] *= -1
                energy += delta_E
                magnetization += 2 * lattice[i, j]
        
        # Track energy and magnetization per spin
        energies.append(energy / (n**2))
        magnetizations.append(magnetization / (n**2))

    return np.array(energies), np.array(magnetizations)

def calculate_energy(lattice, J):
    n = lattice.shape[0]
    energy = 0
    for i in range(n):
        for j in range(n):
            spin = lattice[i, j]
            # Sum over nearest neighbors
            neighbors = lattice[(i+1) % n, j] + lattice[(i-1) % n, j] + lattice[i, (j+1) % n] + lattice[i, (j-1) % n]
            energy += -J * spin * neighbors
    return energy / 2  # Each bond is counted twice

def initialize_lattice(n):
    return np.random.choice([-1, 1], size=(n, n))

# Simulation parameters
n = 16
J = 0.3
kBT = 1.0
n_steps = 500

# Initialize lattice and run the Metropolis algorithm
lattice = initialize_lattice(n)
energies, magnetizations = metropolis_ising(lattice, J, kBT, n_steps)

# Plot the energy and magnetization per spin over iterations
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(energies)
plt.title('Energy per Spin vs Iterations')
plt.xlabel('Iterations')
plt.ylabel('Energy per Spin')

plt.subplot(1, 2, 2)
plt.plot(magnetizations)
plt.title('Magnetization per Spin vs Iterations')
plt.xlabel('Iterations')
plt.ylabel('Magnetization per Spin')

plt.tight_layout()
plt.show()
