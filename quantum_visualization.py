import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# ----------------- Helper Functions -----------------
def create_placeholder_image(color='lightblue', size=(100, 100)):
    """Create a simple placeholder image using PIL."""
    img = Image.new('RGB', size, color=color)
    return img

def add_image(ax, image, zoom=0.1, xy=(0.5, 0.5)):
    """Adds an image to the plot to help visualize the concept."""
    imagebox = OffsetImage(image, zoom=zoom)
    ab = AnnotationBbox(imagebox, xy, frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
    ax.add_artist(ab)

# ----------------- Quantum Visualizations -----------------
def plot_spinning_coin(state1_freq, state2_freq):
    x = np.linspace(0, 10, 1000)
    state1 = np.sin(2 * np.pi * state1_freq * x)  
    state2 = np.sin(2 * np.pi * state2_freq * x)  
    superposition = state1 + state2  

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, state1, label="Heads", linestyle='-', color='green', linewidth=2)
    ax.plot(x, state2, label="Tails", linestyle='--', color='red', linewidth=2)
    ax.plot(x, superposition, color='purple', label="Spinning Coin", linewidth=3, linestyle='-.')

    ax.set_title("Spinning Coin Example", fontsize=18)
    ax.set_xlabel("Time", fontsize=14)
    ax.set_ylabel("Amplitude", fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', color='gray', alpha=0.5)
    ax.set_facecolor('black')

    coin_image = create_placeholder_image(color='gold')
    add_image(ax, coin_image, zoom=0.1, xy=(0.8, 0.8))
    st.pyplot(fig)

def plot_instant_effect(distance, effect_strength):
    fig, ax = plt.subplots(figsize=(8, 6))
    particle1_x = 0.3 - distance / 2
    particle2_x = 0.7 + distance / 2
    color1 = plt.cm.Blues(effect_strength)
    color2 = plt.cm.Reds(effect_strength)

    circle1 = plt.Circle((particle1_x, 0.5), 0.1, color=color1, label="Particle 1")
    circle2 = plt.Circle((particle2_x, 0.5), 0.1, color=color2, label="Particle 2")
    ax.add_artist(circle1)
    ax.add_artist(circle2)

    ax.text(particle1_x, 0.5, "Particle 1", color="white", ha="center", va="center")
    ax.text(particle2_x, 0.5, "Particle 2", color="white", ha="center", va="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Instant Effect: Entangled Particles", fontsize=18)
    ax.legend(fontsize=12)

    entangled_image = create_placeholder_image(color='purple')
    add_image(ax, entangled_image, zoom=0.15, xy=(0.5, 0.5))
    st.pyplot(fig)

# ----------------- Example 3: Wave-Particle Duality -----------------
def plot_wave_particle_duality(wavelength):
    x = np.linspace(-10, 10, 1000)
    intensity = (np.sin(x / wavelength) / x) ** 2  

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, intensity, color='royalblue', label="Wave Pattern", linewidth=3)
    ax.set_title("Wave-Particle Duality", fontsize=18)
    ax.set_xlabel("Position", fontsize=14)
    ax.set_ylabel("Intensity", fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', color='gray', alpha=0.5)
    ax.set_facecolor('skyblue')

    wave_image = create_placeholder_image(color='aqua')
    add_image(ax, wave_image, zoom=0.1, xy=(0.8, 0.8))
    st.pyplot(fig)

# ----------------- Example 4: Quantum Uncertainty -----------------
def plot_uncertainty(position_uncertainty, momentum_uncertainty):
    x = np.linspace(-5, 5, 1000)
    position = np.exp(-x ** 2 / (2 * position_uncertainty ** 2))  
    momentum = np.exp(-x ** 2 / (2 * momentum_uncertainty ** 2))  

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, position, label="Position Uncertainty", color='orange', linewidth=3)
    ax.plot(x, momentum, label="Momentum Uncertainty", color='purple', linestyle='--', linewidth=2)
    ax.set_title("Quantum Uncertainty", fontsize=18)
    ax.set_xlabel("Variable")
    ax.set_ylabel("Probability Distribution")
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', color='gray', alpha=0.5)
    ax.set_facecolor('lightgray')

    uncertainty_image = create_placeholder_image(color='gray')
    add_image(ax, uncertainty_image, zoom=0.1, xy=(0.8, 0.8))
    st.pyplot(fig)

# ------------------ Main Function ------------------
def run_quantum_visuals():
    st.title("Quantum Phenomena Visualizations")

    # Spinning Coin Example (Superposition)
    st.header("Spinning Coin (Superposition)")
    state1_freq = st.slider("Frequency of Heads", min_value=1, max_value=10, value=2)
    state2_freq = st.slider("Frequency of Tails", min_value=1, max_value=10, value=4)
    plot_spinning_coin(state1_freq, state2_freq)

    # Instant Effect (Entanglement)
    st.header("Instant Effect (Entanglement)")
    distance = st.slider("Distance Between Particles", min_value=0.0, max_value=0.4, value=0.2)
    effect_strength = st.slider("Effect Strength", min_value=0.0, max_value=1.0, value=0.5)
    plot_instant_effect(distance, effect_strength)

    # Wave-Particle Duality
    st.header("Wave-Particle Duality")
    wavelength = st.slider("Wavelength", min_value=1, max_value=10, value=2)
    plot_wave_particle_duality(wavelength)

    # Quantum Uncertainty
    st.header("Quantum Uncertainty (Heisenberg Principle)")
    position_uncertainty = st.slider("Position Uncertainty", min_value=0.1, max_value=3.0, value=0.5)
    momentum_uncertainty = st.slider("Momentum Uncertainty", min_value=0.1, max_value=3.0, value=2.0)
    plot_uncertainty(position_uncertainty, momentum_uncertainty)
