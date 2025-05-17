import streamlit as st
import matplotlib.pyplot as plt

def run_qcd():
    st.title("🧲 Quark-Gluon Interaction (QCD Simulation)")

    st.markdown("""
    Quantum Chromodynamics (QCD) explains the **strong force** — the force that holds atomic nuclei together.

    - **Quarks** have color charges: red, green, or blue.  
    - **Gluons** are the force carriers exchanged between quarks of *different* colors.  
    - Quarks with the *same* color do **not** interact via gluons.

    🔧 **Try it out:** Choose colors for two quarks and see if they interact!
    """)

    # Quark color options
    quark_colors = ['red', 'green', 'blue']

    # User inputs
    col1, col2 = st.columns(2)
    with col1:
        quark1_color = st.selectbox("Select Quark 1 Color", quark_colors)
    with col2:
        quark2_color = st.selectbox("Select Quark 2 Color", quark_colors)

    if quark1_color == quark2_color:
        st.warning("⚠️ Quarks with the same color cannot exchange gluons. Please select different colors.")
        return

    gluon = f"Gluon ({quark1_color}-{quark2_color})"
    st.success(f"💥 Gluon exchanged: **{gluon}**")

    # Visualization
    fig, ax = plt.subplots()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)

    ax.add_patch(plt.Circle((-2.5, 0), 1, color=quark1_color))
    ax.text(-2.5, -1.5, f"Quark 1 ({quark1_color})", ha='center', fontsize=10)

    ax.add_patch(plt.Circle((2.5, 0), 1, color=quark2_color))
    ax.text(2.5, -1.5, f"Quark 2 ({quark2_color})", ha='center', fontsize=10)

    ax.arrow(-1.5, 0, 3, 0, head_width=0.3, head_length=0.5, fc='black', ec='black', linewidth=2)
    ax.text(0, 0.5, gluon, ha='center', fontsize=12, fontweight='bold')

    ax.set_title("Quark-Gluon Interaction", fontsize=14)
    ax.axis('off')

    st.pyplot(fig)
