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

# Function to run QED simulation
def run_qed():
    st.title("QED: Photon-Electron Scattering Simulation")

    # User input
    photon_input = st.slider("Photon Energy", 1, 5, 2)
    electron_input = st.slider("Electron Energy", 1, 10, 5)

    # Make prediction
    predicted_energy = model.predict(np.array([[electron_input, photon_input]]))

    st.write(f"Predicted Electron Energy After Scattering: {predicted_energy[0][0]:.2f} eV")

    # Plot results
    fig, ax = plt.subplots()
    ax.plot(photon_energy, scattered_data, label="Model Data")
    ax.scatter(photon_input, predicted_energy[0][0], color='red', label="Prediction", zorder=5)
    ax.set_xlabel("Photon Energy")
    ax.set_ylabel("Scattered Electron Energy")
    ax.legend()
    st.pyplot(fig)
