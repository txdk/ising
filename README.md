# Ising

A collection of Python scripts for the simulation of the Ising spin model for a 2D lattice, based on Markov Chain Monte Carlo (MCMC) techniques.

## Installation

Requires Python 3.9.12, as well as the NumPy and MatPlotLib libraries.

To use, simply clone the repository to a local directory.

    $ git clone https://github.com/txdk/ising.git
    
## Usage

The core functionality is contained in `ising.py`, which provides most of the functions required to simulate the Ising model.

Example usage is shown in:
1. `main.py` - Computes the magnetisation of the system for various (inverse) temperature values.
2. `animation.py` - Creates an animation to visualise how the specified initial lattice state iteratively evolves to its equilibrium state.
