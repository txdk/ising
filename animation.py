# An animation to visualise the Ising spin model in a 2D lattice

from ising import ising2D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fixing RNG seed for reproducibility
np.random.seed(19680801)

# Setup simulation parameters
N = 50 # Lattice size
beta = 10 # Inverse temperature
coupling_const = 0.1 # Coupling strength of adjacent spin sites
# state = np.ones((N, N))
state = 2*np.random.randint(2, size = (N, N)) - np.ones((N, N))
numSweeps = 500 # Number of lattice sweeps to display in animation

# Preallocate array to store states of lattice
state_array = np.ones((N,N,numSweeps+1))

# Input the parameters into our model
simulation = ising2D(N, beta, coupling_const, state)

# Function to produce the image in each frame
def update_image(num, state_array, image):
    image.set_data(state_array[:, :, num])
    return image

# Compute states
iSweep = 0 # Initialise loop counter to 0
state_array[:, :, 0] = state
H = simulation.compute_Hamiltonian()
for i in range(numSweeps):
    iSweep += 1 # Increment counter
    print("%i of %i computations done." % (iSweep, numSweeps), end = '\r')
    simulation, H = simulation.sweep_lattice(H)
    state_array[:, :, iSweep] = simulation.state

print('Done!\n')
print('Building animation...\n')

# Setup figure to display animation
fig = plt.figure()
ax = fig.add_subplot()
image = ax.imshow(simulation.state, vmin = -1, vmax = 1)

# Create animation object
animation = FuncAnimation(fig, update_image, numSweeps + 1, fargs = (state_array, image), interval = 100)

# Display animation
plt.show()
