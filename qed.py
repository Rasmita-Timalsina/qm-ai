import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# 💡 Physics: Compton Scattering Formula
def compton_scattering(electron_energy, photon_energy):
    scattered_energy = electron_energy / (1 + (electron_energy * photon_energy) / 1000)
    return scattered_energy

# 🧠 Define and compile the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

# 🧪 Generate training data
electron_energy = np.linspace(1, 10, 100)
photon_energy = np.linspace(1, 5, 100)
scattered_data = np.array([compton_scattering(e, p) for e, p in zip(electron_energy, photon_energy)])

# 🚀 Main Function to Run the Streamlit App
def run_qed():
    st.title("Compton: Photon-Electron Scattering")

    st.markdown("""
    ### 🧲 QED

    **What Happens?**  
    When a photon hits an electron, the photon transfers energy to it. This causes the electron to scatter.  
    This is known as **Compton scattering**.

    **AI's Role:**  
    We trained a simple neural network to learn how an electron's energy changes after a photon collision.

    🔧 **How to Use:**
    - Adjust the photon and electron energy sliders.
    - The AI will predict the new energy after scattering.
    - You’ll see how closely the AI prediction matches actual physics.

    """)

    # 🎛️ User Input
    photon_input = st.slider("🔦 Photon Energy (eV)", 1, 5, 2)
    electron_input = st.slider("🧮 Electron Energy (eV)", 1, 10, 5)

    # 🤖 AI Prediction
    predicted_energy = model.predict(np.array([[electron_input, photon_input]]), verbose=0)

    st.success(f"🔮 Predicted Electron Energy After Scattering: **{predicted_energy[0][0]:.2f} eV**")

    # 📊 Visualization
    fig, ax = plt.subplots()
    ax.plot(photon_energy, scattered_data, label="Actual Compton Scattering", linewidth=2)
    ax.scatter(photon_input, predicted_energy[0][0], color='red', label="AI Prediction", zorder=5, s=100)
    ax.set_xlabel("Photon Energy (eV)")
    ax.set_ylabel("Scattered Electron Energy (eV)")
    ax.set_title("Compton Scattering: AI vs Physics")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)

    st.pyplot(fig)
