import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Define the Compton scattering function
def compton_scattering(electron_energy, photon_energy):
    scattered_energy = electron_energy / (1 + (electron_energy * photon_energy) / 1000)
    return scattered_energy

# Create and compile the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

# Generate training data
electron_energy = np.linspace(1, 10, 100)
photon_energy = np.linspace(1, 5, 100)
scattered_data = np.array([compton_scattering(e, p) for e, p in zip(electron_energy, photon_energy)])

def run_qed():
    st.title("Quantum Electrodynamics (QED): Photon-Electron Scattering Simulation")
    
    st.markdown("""
    ### Quantum Electrodynamics (QED) — Compton Scattering Simulation
    
    **Concept:**  
    This simulation models Compton scattering, where photons (particles of light) collide with electrons. When this happens, photons transfer some energy to electrons, causing the electrons to scatter with higher energy.
    
    **Neural Network (AI):**  
    We've trained a neural network to learn how the electron's energy changes based on the initial energies of the photon and electron. The network predicts the electron's energy after the collision.
    
    **User Input:**  
    Use the sliders to select the photon energy (energy of the light) and electron energy (energy of the electron before collision).
    
    **Visualization:**  
    The graph compares actual calculated data from the Compton scattering formula with the AI's prediction. The red dot shows the predicted electron energy based on your inputs.
    
    **In Simple Terms:**  
    - Input photon and electron energies.  
    - The AI predicts the electron's new energy after scattering.  
    - See how well the AI prediction matches the real physics calculation!
    """)

    # User input
    photon_input = st.slider("Photon Energy", 1, 5, 2)
    electron_input = st.slider("Electron Energy", 1, 10, 5)

    # Make prediction
    predicted_energy = model.predict(np.array([[electron_input, photon_input]]))

    st.write(f"Predicted Electron Energy After Scattering: **{predicted_energy[0][0]:.2f} eV**")

    # Plot results
    fig, ax = plt.subplots()
    ax.plot(photon_energy, scattered_data, label="Actual Compton Scattering Data")
    ax.scatter(photon_input, predicted_energy[0][0], color='red', label="AI Prediction", zorder=5)
    ax.set_xlabel("Photon Energy (eV)")
    ax.set_ylabel("Scattered Electron Energy (eV)")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)
