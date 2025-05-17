import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Parameters for the simulation
barrier_height = 10  # Height of the potential barrier
barrier_width = 1    # Width of the potential barrier
x_min = 0
x_max = 10
x = np.linspace(x_min, x_max, 1000)

# Define the potential barrier
def potential(x):
    return np.piecewise(x, [x < 4, (x >= 4) & (x <= 5), x > 5], [0, barrier_height, 0])

# Define the wave function of the particle
def wave_function(x, energy, barrier_height):
    k1 = np.sqrt(2 * np.abs(energy))

    if energy < 0:
        k2 = np.sqrt(2 * np.abs(energy))
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

# Main visualization function
def run_tunneling():
    st.title("Quantum Tunneling Simulation: Particle and Potential Barrier Interaction")

    st.markdown("""
    ## 🌌 Quantum Field Theory (QFT)
    Quantum Field Theory (QFT) combines quantum mechanics with special relativity to explain how particles and forces interact. It’s the foundation of modern physics and helps us understand strange phenomena like quantum tunneling.

    ---
    ## 🚧 The Potential Barrier
    **What is it?** A potential barrier is like a hill that the particle must cross. If the particle’s energy is too low, it can’t go over it in classical physics.

    **In Quantum Mechanics:** The particle might *tunnel through* the hill instead of going over it.

    **🔴 Red Line in Graph:** Represents the barrier — high in the middle (between x = 4 and x = 5), zero elsewhere.

    ---
    ## 🌊 The Wave Function
    **What is it?** The wave function shows where the particle is likely to be. It’s not a single spot but a wave that spreads out.

    - **High energy:** The wave passes through and keeps oscillating.
    - **Low energy:** The wave shrinks inside the barrier but may reappear after — this is tunneling!

    **🔵 Blue Line in Graph:** Shows the particle’s wave function.

    ---
    ## ⚡ Energy Level and Bound States
    **Energy Level (Green Dashed Line):** Shows the particle’s energy.

    - **Above the barrier:** The particle moves freely.
    - **Below the barrier:** The particle is mostly trapped but may tunnel.

    ---
    ## ✨ Quantum Tunneling in Action
    Even with low energy, the particle’s wave can sneak through the barrier and appear on the other side.

    **Easy Analogy:** Imagine a ball trying to roll over a hill. In quantum physics, the ball doesn’t go over — it *disappears into the hill* and reappears on the other side.

    ---
    ## 🎛️ Interactive Slider
    Use the slider to change the particle’s energy and explore the behavior visually.

    ---
    ## 📌 Key Takeaways
    - Quantum tunneling lets particles cross barriers they shouldn’t be able to.
    - Wave functions show the spread and behavior of particles.
    - Energy levels determine whether the particle can pass or gets stuck.
    """)

    # User input
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
