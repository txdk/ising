import numpy as np
import matplotlib.pyplot as plt

# Setup class for 2D Ising model
class ising2D:
    def __init__(self, N, beta, coupling_const, state):
        self.N = N # Lattice size
        self.beta = beta # Inverse temperature
        self.coupling_const = coupling_const # Coupling strength of adjacent spin sites
        self.state = state # Lattice configuration

    # Setup periodic boundary conditions on lattice
    def setup_BCs(self):
        next_indx = np.concatenate((np.arange(1,self.N),np.array([0])))
        return next_indx

    # Plot the current spin configuration
    def plot_state(self):
        plt.imshow(self.state, vmin = -1, vmax = 1)
        plt.show()

    # Compute energy of current lattice configuration
    def compute_Hamiltonian(self):
        # Initialise cumulative variable to 0
        H = 0
        
        # Impose periodicity of lattice
        next_indx = self.setup_BCs()
        
        # Sum contributions over the lattice
        for i in range(self.N):
            for j in range(self.N):
                H += self.state[i, j]*(self.state[next_indx[i], j] + self.state[i, next_indx[j]])
        return -self.coupling_const*H

    # Flip the spin of the i,j lattice site based on the Metropolis-Hastings algorithm
    def flip_spin(self, H_current, i, j):
        # Impose periodicity of lattice
        next_indx = self.setup_BCs()

        # Compute difference in energy if the i,j spin is flipped
        deltaH = 2*self.coupling_const*self.state[i,j]*(self.state[i-1,j] + self.state[i,j-1] + self.state[next_indx[i], j] + self.state[i, next_indx[j]])

        # Compute probability of flipping the spin
        if deltaH > 0:
            prob = np.exp(-self.beta*deltaH)
        else:
            prob = 1.0

        # Accept or reject modification to state
        if np.random.random() <= prob:
            # Flip spin of i,j lattice site
            self.state[i, j] = -self.state[i, j]
            H_current += deltaH

        return self, H_current

    # Apply Metropolis-Hastings algorithm for flipping the spin of each lattice site
    def sweep_lattice(self, H_state):    
        for i in range(self.N):
            for j in range(self.N):
                self, H_state = self.flip_spin(H_state, i ,j)
        return self, H_state

    # Sweep the lattice a number of times
    def do_sweeps(self, H_state, numSweeps):
        for k in range(numSweeps):
            self, H_state = self.sweep_lattice(H_state)
        return self, H_state

    # Compute magnetisation of a given configuration
    def compute_magnetisation(self):
        return np.abs(np.mean(self.state))
