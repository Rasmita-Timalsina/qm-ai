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

    ax.set_title("Spinning Coin Example", fontsize=18, fontweight='bold')
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

    ax.text(particle1_x, 0.5, "Particle 1", color="white", ha="center", va="center", fontweight='bold')
    ax.text(particle2_x, 0.5, "Particle 2", color="white", ha="center", va="center", fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Instant Effect: Entangled Particles", fontsize=18, fontweight='bold')
    ax.legend(fontsize=12)

    entangled_image = create_placeholder_image(color='purple')
    add_image(ax, entangled_image, zoom=0.15, xy=(0.5, 0.5))
    st.pyplot(fig)

def plot_wave_particle_duality(wavelength):
    x = np.linspace(-10, 10, 1000)
    intensity = (np.sin(x / wavelength) / x) ** 2  

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, intensity, color='royalblue', label="Wave Pattern", linewidth=3)
    ax.set_title("Wave-Particle Duality", fontsize=18, fontweight='bold')
    ax.set_xlabel("Position", fontsize=14)
    ax.set_ylabel("Intensity", fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', color='gray', alpha=0.5)
    ax.set_facecolor('skyblue')

    wave_image = create_placeholder_image(color='aqua')
    add_image(ax, wave_image, zoom=0.1, xy=(0.8, 0.8))
    st.pyplot(fig)

def plot_uncertainty(position_uncertainty, momentum_uncertainty):
    x = np.linspace(-5, 5, 1000)
    position = np.exp(-x ** 2 / (2 * position_uncertainty ** 2))  
    momentum = np.exp(-x ** 2 / (2 * momentum_uncertainty ** 2))  

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, position, label="Position Uncertainty", color='orange', linewidth=3)
    ax.plot(x, momentum, label="Momentum Uncertainty", color='purple', linestyle='--', linewidth=2)
    ax.set_title("Quantum Uncertainty", fontsize=18, fontweight='bold')
    ax.set_xlabel("Variable", fontsize=14)
    ax.set_ylabel("Probability Distribution", fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', color='gray', alpha=0.5)
    ax.set_facecolor('lightgray')

    uncertainty_image = create_placeholder_image(color='gray')
    add_image(ax, uncertainty_image, zoom=0.1, xy=(0.8, 0.8))
    st.pyplot(fig)

# ------------------ Main Function ------------------
def run_quantum_visuals():
    st.title("Quantum Phenomena Visualizations")
    st.markdown("""
    <div style="font-family: 'Arial'; font-size:18px; line-height:1.6; max-width:800px;">
    <h2>Introduction to Quantum Phenomena</h2>
    <p><strong>Title:</strong> Understanding Quantum Phenomena through Visualization</p>
    <p><strong>Overview:</strong><br>
    This project aims to visualize key quantum phenomena using interactive plots and graphs. These visualizations help make complex quantum concepts more accessible and understandable.</p>
    </div>
    """, unsafe_allow_html=True)

    st.header("Spinning Coin (Superposition)")
    st.markdown("""
    <div style="font-family: 'Georgia'; font-size:16px; max-width:700px;">
    <p><strong>Title:</strong> Superposition: The Spinning Coin</p>
    <p><strong>Key Concept:</strong> <em>Superposition</em> – In quantum mechanics, particles can exist in multiple states simultaneously, like a coin spinning in the air — both heads and tails until it lands.</p>
    <p><strong>Visualization:</strong> The graph shows two states (Heads and Tails), oscillating at different frequencies. The superposition (combined state) is the purple line.</p>
    <p><strong>Simple Explanation:</strong> Imagine a spinning coin. Instead of being just heads or tails, it is in both states at once — this is quantum superposition.</p>
    <p><strong>Interactive Element:</strong> Use the sliders below to adjust frequencies of heads and tails and observe the changes in superposition.</p>
    </div>
    """, unsafe_allow_html=True)
    state1_freq = st.slider("Frequency of Heads", min_value=1, max_value=10, value=2, help="Adjust the frequency for the Heads state.")
    state2_freq = st.slider("Frequency of Tails", min_value=1, max_value=10, value=4, help="Adjust the frequency for the Tails state.")
    plot_spinning_coin(state1_freq, state2_freq)

    st.header("Instant Effect (Entanglement)")
    st.markdown("""
    <div style="font-family: 'Georgia'; font-size:16px; max-width:700px;">
    <p><strong>Title:</strong> Entanglement: Instant Communication Between Particles</p>
    <p><strong>Key Concept:</strong> <em>Quantum Entanglement</em> – When two particles are entangled, changes to one instantaneously affect the other, no matter the distance.</p>
    <p><strong>Visualization:</strong> Two particles are displayed (circles) with colors representing their states, illustrating entanglement effects.</p>
    <p><strong>Simple Explanation:</strong> Think of two particles linked such that altering one instantly affects the other, as if communicating across space.</p>
    <p><strong>Interactive Element:</strong> Adjust the distance and strength of entanglement using sliders below.</p>
    </div>
    """, unsafe_allow_html=True)
    distance = st.slider("Distance Between Particles", min_value=0.0, max_value=0.4, value=0.2, step=0.01, help="Control how far apart the particles are.")
    effect_strength = st.slider("Effect Strength", min_value=0.0, max_value=1.0, value=0.5, step=0.01, help="Control the strength of the entanglement effect.")
    plot_instant_effect(distance, effect_strength)

    st.header("Wave-Particle Duality")
    st.markdown("""
    <div style="font-family: 'Georgia'; font-size:16px; max-width:700px;">
    <p><strong>Title:</strong> Wave-Particle Duality: The Nature of Light and Matter</p>
    <p><strong>Key Concept:</strong> <em>Wave-Particle Duality</em> – Particles such as electrons or photons exhibit properties of both particles and waves.</p>
    <p><strong>Visualization:</strong> The plot depicts the intensity of the wave pattern across space, showing wave-like behavior of particles.</p>
    <p><strong>Simple Explanation:</strong> Like ocean waves, particles can interfere and display wave characteristics depending on observation.</p>
    <p><strong>Interactive Element:</strong> Adjust the wavelength below to see how the wave pattern changes.</p>
    </div>
    """, unsafe_allow_html=True)
    wavelength = st.slider("Wavelength", min_value=1, max_value=10, value=2, help="Modify the wavelength of the particle wave.")
    plot_wave_particle_duality(wavelength)

    st.header("Quantum Uncertainty (Heisenberg Principle)")
    st.markdown("""
    <div style="font-family: 'Georgia'; font-size:16px; max-width:700px;">
    <p><strong>Title:</strong> Uncertainty: The Heisenberg Principle</p>
    <p><strong>Key Concept:</strong> <em>Heisenberg Uncertainty Principle</em> – It is impossible to simultaneously know the exact position and momentum of a particle.</p>
    <p><strong>Visualization:</strong> The plot shows two curves representing uncertainty distributions for position and momentum.</p>
    <p><strong>Simple Explanation:</strong> The more precisely you know a particle’s position, the less precisely you know its momentum, and vice versa.</p>
    <p><strong>Interactive Element:</strong> Adjust uncertainties in position and momentum using the sliders below.</p>
    </div>
    """, unsafe_allow_html=True)
    position_uncertainty = st.slider("Position Uncertainty", min_value=0.1, max_value=3.0, value=0.5, step=0.05, help="Adjust uncertainty in particle position.")
    momentum_uncertainty = st
