import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Parameters for the simulation
barrier_height = 10  # Height of the potential barrier
barrier_width = 1  # Width of the potential barrier
x_min = 0  # Minimum x-axis position
x_max = 10  # Maximum x-axis position
x = np.linspace(x_min, x_max, 1000)  # x values for plotting

# Define the potential barrier (step-like function)
def potential(x):
    return np.piecewise(x, [x < 4, (x >= 4) & (x <= 5), x > 5], [0, barrier_height, 0])

# Define the wave function of the particle
def wave_function(x, energy, barrier_height):
    k1 = np.sqrt(2 * np.abs(energy))  # Wave number outside the barrier (free particle)
    
    if energy < 0:
        k2 = np.sqrt(2 * np.abs(energy))  # Decay inside the barrier (imaginary wave number)
        psi_inside = np.exp(-k2 * (x - 4))  
        return np.piecewise(x, 
                            [x < 4, (x >= 4) & (x <= 5), x > 5],
                            [lambda x: np.exp(k2 * (x - 4)),  
                             lambda x: np.exp(-k2 * (x - 4)),  
                             lambda x: np.exp(k2 * (x - 5))])  
    elif energy > barrier_height:
        k2 = np.sqrt(2 * (energy - barrier_height))  
        return np.piecewise(x, 
                            [x < 4, (x >= 4) & (x <= 5), x > 5],
                            [lambda x: np.sin(k1 * x),  
                             lambda x: np.sin(k2 * (x - 4)),  
                             lambda x: np.sin(k1 * (x - 5))])  
    else:
        k2 = np.sqrt(2 * (barrier_height - energy))  
        return np.piecewise(x, 
                            [x < 4, (x >= 4) & (x <= 5), x > 5],
                            [lambda x: np.sin(k1 * x),  
                             lambda x: np.exp(-k2 * (x - 4)),  
                             lambda x: np.sin(k1 * (x - 5))])  

# Function to run Quantum Tunneling visualization in `main.py`
def run_tunneling():
    st.title("Quantum Tunneling and Bound States")

    # User input for energy level
    energy = st.slider("Select Particle Energy (eV)", min_value=-5, max_value=15, value=5)

    # Plot potential, wave function, and energy level
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, potential(x), label="Potential Barrier (V)", color="red", linewidth=3)
    ax.plot(x, wave_function(x, energy, barrier_height), label="Wave Function (Ψ)", color="blue", linewidth=2)
    ax.axhline(y=energy, color="green", linestyle="--", label="Particle Energy (E)")

    ax.set_title("Quantum Tunneling and Bound State: Particle Interaction with Potential Barrier")
    ax.set_xlabel("Position (x)")
    ax.set_ylabel("Energy / Wave Function Amplitude")
    ax.legend(loc="upper right")
    ax.grid(True)

    st.pyplot(fig)
