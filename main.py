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
        "Quantum Phenomena",
        "QED Interaction",
        "Quantum Tunneling (QFT)",
        "QCD Simulation"
    ]
)

# Main page header based on selection and run the corresponding module
if page == "Quantum Phenomena":
    st.header("⚛️ Quantum Phenomena")
    try:
        quantum_visualization.run_quantum_visuals()
    except Exception as e:
        st.error(f"Error running Quantum Phenomena: {e}")

elif page == "QED Interaction":
    st.header("🔆 Quantum Electrodynamics (QED) Interaction")
    try:
        qed.run_qed()
    except Exception as e:
        st.error(f"Error running QED Interaction: {e}")

elif page == "Quantum Tunneling (QFT)":
    st.header("🌀 Quantum Tunneling (Quantum Field Theory)")
    try:
        qt_visual.run_tunneling()
    except Exception as e:
        st.error(f"Error running Quantum Tunneling (QFT): {e}")

elif page == "QCD Simulation":
    st.header("🧬 Quantum Chromodynamics (QCD) Simulation")
    try:
        qcd_visual1.run_qcd()
    except Exception as e:
        st.error(f"Error running QCD Simulation: {e}")
