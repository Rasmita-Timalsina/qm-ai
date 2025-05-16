import streamlit as st
import matplotlib.pyplot as plt

def run_qcd():
    st.title("Quantum Chromodynamics (QCD): Quark-Gluon Interaction")

    # Quark colors
    quark_colors = ['red', 'green', 'blue']
    
    # User input for quark colors
    quark1_color = st.selectbox("Select color for Quark 1", quark_colors)
    quark2_color = st.selectbox("Select color for Quark 2", quark_colors)
    
    # If both quarks have the same color, inform the user
    if quark1_color == quark2_color:
        st.write("The selected quark colors cannot exchange gluons.")
        st.write("Please select different colors for the quarks.")
        return
    
    # Simulate gluon exchange and plot interaction
    gluon = f"Gluon ({quark1_color}-{quark2_color})"
    st.write(f"Exchanged gluon color: {gluon}")

    fig, ax = plt.subplots()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.add_patch(plt.Circle((-2, 0), 1, color=quark1_color, label="Quark 1"))
    ax.add_patch(plt.Circle((2, 0), 1, color=quark2_color, label="Quark 2"))
    ax.arrow(-2, 0, 4, 0, head_width=0.5, head_length=1, fc='black', ec='black')

    ax.set_title("Quark-Gluon Interaction (QCD)")
    ax.legend()
    ax.grid(True, linestyle='--', color='gray', alpha=0.5)
    
    st.pyplot(fig)

