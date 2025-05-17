import streamlit as st
import matplotlib.pyplot as plt

# 🎯 Main function to run QCD interaction visualization
def run_qcd():
    st.title(" 🧬 Quark-Gluon Interaction")

    st.markdown("""
    ### Explains the strong force — the force that holds atomic nuclei together.

    **How it works:**  
    - Quarks are fundamental particles with color charges: red, green, or blue.  
    - Gluons mediate the strong force and are exchanged between **quarks of different colors**.  
    - If the quark colors are the same, they **don’t interact** via gluon exchange.

    **🔧 Try it out:**  
    Select two quark colors below and see if they interact by exchanging a gluon.
    """)

    # 🎨 Quark color options
    quark_colors = ['red', 'green', 'blue']

    # 🧪 User selections
    col1, col2 = st.columns(2)
    with col1:
        quark1_color = st.selectbox("🎨 Select Quark 1 Color", quark_colors)
    with col2:
        quark2_color = st.selectbox("🎨 Select Quark 2 Color", quark_colors)

    # ❌ No interaction if colors are the same
    if quark1_color == quark2_color:
        st.warning("⚠️ Quarks with the same color cannot exchange gluons. Please select different colors.")
        return

    # ✅ Valid interaction
    gluon = f"Gluon ({quark1_color}-{quark2_color})"
    st.success(f"💥 Quark Interaction via: **{gluon}**")

    # 🎯 Plot visualization
    fig, ax = plt.subplots()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)

    # Quarks as colored circles
    ax.add_patch(plt.Circle((-2.5, 0), 1, color=quark1_color, label="Quark 1"))
    ax.text(-2.5, -1.5, f"Quark 1 ({quark1_color})", ha='center', fontsize=10)

    ax.add_patch(plt.Circle((2.5, 0), 1, color=quark2_color, label="Quark 2"))
    ax.text(2.5, -1.5, f"Quark 2 ({quark2_color})", ha='center', fontsize=10)

    # Gluon exchange arrow
    ax.arrow(-1.5, 0, 3, 0, head_width=0.3, head_length=0.5, fc='black', ec='black', linewidth=2)
    ax.text(0, 0.5, gluon, ha='center', fontsize=12, fontweight='bold')

    ax.set_title("Quark-Gluon Interaction", fontsize=14)
    ax.axis('off')  # Remove axes for clean look
    st.pyplot(fig)
