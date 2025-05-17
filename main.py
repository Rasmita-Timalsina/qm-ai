import streamlit as st
import importlib
import quantum_visualization  # Quantum visuals
import qed  # QED visualization
import qt_visual  # Quantum tunneling visualization
import qcd_visual1  # QCD visualization

# Force reload of modules to avoid caching issues
importlib.reload(quantum_visualization)
importlib.reload(qed)
importlib.reload(qt_visual)
importlib.reload(qcd_visual1)

# Sidebar Navigation
st.sidebar.title("🔬 Quantum Physics AI Visualizations")
page = st.sidebar.radio(
    "Choose a Simulation:",
    ["Quantum Phenomena", "QED Interaction", "Quantum Tunneling (QFT)", "QCD Simulation"]
)

# Debugging the page selection
st.write(f"Selected Page: {page}")

# Run Selected Simulation
if page == "Quantum Phenomena":
    st.write("Running Quantum Phenomena Visualization...")
    try:
        quantum_visualization.run_quantum_visuals()  # Calls function from quantum_visualization.py
    except Exception as e:
        st.error(f"Error running Quantum Phenomena: {e}")
elif page == "QED Interaction":
    st.write("Running QED Interaction...")
    try:
        qed.run_qed()  # Calls function from qed.py
    except Exception as e:
        st.error(f"Error running QED Interaction: {e}")
elif page == "Quantum Tunneling (QFT)":
    st.write("Running Quantum Tunneling (QFT)...")
    try:
        qt_visual.run_tunneling()  # Calls function from qt_visual.py
    except Exception as e:
        st.error(f"Error running Quantum Tunneling (QFT): {e}")
elif page == "QCD Simulation":
    st.write("Running QCD Simulation...")
    try:
        qcd_visual1.run_qcd()  # Calls function from qcd_visual1.py
    except Exception as e:
        st.error(f"Error running QCD Simulation: {e}")