# A script to compute the magnetisation of a 2D lattice of spins for various temperatures.

from ising import ising2D
import numpy as np
import matplotlib.pyplot as plt

# Define initial variables
N = 50 # Lattice size
nBeta = 20 # Number of beta values considered
beta_values = np.linspace(0.01, 10, nBeta) # Inverse temperature
coupling_const = 0.1 # Coupling strength of adjacent spin sites
state = np.ones((N,N)) # Initial state of system
numSweeps = 1000 # Number of lattice sweeps to equilibriate system
nBetween = 2000 # Number of sweeps between each sample of the magnetisation
nSamples = 20 # Number of magnetisation values computed for an ensemble average

# Initialise random number generator
np.random.default_rng()

# Preallocate array to store magnetisation expectation values
M_values = np.array([])
iSample = 0

# Loop over beta values
for beta in beta_values:
    iSample += 1
    print("Computing magnetisation for %i of %i temperatures." % (iSample, nBeta), end = '\r')
    
    # Input the parameters into our model
    experiment = ising2D(N, beta, coupling_const, state)

    # Compute initial energy
    H_state = experiment.compute_Hamiltonian()

    # Do initial sweep to obtain equilibrium state of system
    experiment, H_state = experiment.do_sweeps(H_state, numSweeps)

    # Compute ensemble average of magnetisation
    M = 0.0
    for i in range(nSamples):
        experiment, H_state = experiment.do_sweeps(H_state, nBetween)
        M += experiment.compute_magnetisation()
    M = float(M)/float(nSamples)
    M_values = np.append(M_values, [M])

print('Done!\n')

# Plot magnetisation vs temperature (beta)
fontSize = 18
plt.plot(beta_values, M_values, '--', color='red')
plt.xlabel('Inverse temperature', fontsize = fontSize)
plt.ylabel('Magnetisation', fontsize = fontSize)
plt.show()

