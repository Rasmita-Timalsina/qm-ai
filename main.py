import streamlit as st
import importlib
import quantum_visualization  # Quantum visuals
import qed  # QED visualization
import qt_visual  # Quantum tunneling visualization
import qcd_visual1  # QCD visualization

# Force reload modules to avoid caching issues
importlib.reload(quantum_visualization)
importlib.reload(qed)
importlib.reload(qt_visual)
importlib.reload(qcd_visual1)

# Sidebar Navigation with Title
st.sidebar.title("Artificial Intelligence Assisted Visualization of Quantum Phenomena")
page = st.sidebar.radio(
    "Choose a Simulation:",
    [
        "Home",
        "Quantum Phenomena",
        "QED Interaction",
        "Quantum Tunneling (QFT)",
        "QCD Simulation"
    ]
)

# Home page content
if page == "Home":
    st.title("🧠 AI-Powered Visualization of Quantum Phenomena")
    st.markdown("""
    Welcome !

    Interactive visualizations enabled by AI-driven techniques illuminate fundamental quantum phenomena, making complex ideas easier to explore and understand in this project conducted for the graduate course *‘The Art & Science of AI’* at **CUA**.

    ---
    ### 🔬 Mentioned Visuals

    – **Superposition:** A spinning coin being both heads and tails.  
    – **Entanglement:** Instant communication between distant particles.  
    – **Wave-Particle Duality:** Particles shifting between waves and particles.  
    – **Uncertainty:** Knowing position affects the uncertainty of momentum.  
    – **Tunneling:** A ball passing through a wall instead of bouncing.  
    – **Compton Scattering:** Light hitting an electron and scattering it.  
    – **Quarks & Gluons:** Quarks exchanging gluons to stay together.

    ---
    **Developed by:** Rasmita Timalsina  
    **Affiliation:** The Catholic University of America  
    **Contact:** timalsina@cua.edu
    """)

# Quantum Phenomena
elif page == "Quantum Phenomena":
    st.header("⚛️ Quantum Phenomena")
    try:
        quantum_visualization.run_quantum_visuals()
    except Exception as e:
        st.error(f"Error running Quantum Phenomena: {e}")

# QED Interaction
elif page == "QED Interaction":
    st.header("🔆 Quantum Electrodynamics (QED) Interaction")
    try:
        qed.run_qed()
    except Exception as e:
        st.error(f"Error running QED Interaction: {e}")

# Quantum Tunneling (QFT)
elif page == "Quantum Tunneling (QFT)":
    st.header("🌀 Quantum Tunneling (Quantum Field Theory)")
    try:
        qt_visual.run_tunneling()
    except Exception as e:
        st.error(f"Error running Quantum Tunneling (QFT): {e}")

# QCD Simulation
elif page == "QCD Simulation":
    st.header("🧬 Quantum Chromodynamics (QCD) Simulation")
    try:
        qcd_visual1.run_qcd()
    except Exception as e:
        st.error(f"Error running QCD Simulation: {e}")
