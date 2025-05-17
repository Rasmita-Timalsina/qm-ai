def run_quantum_visuals():
    st.title("🔬 Quantum Phenomena Visualizations")
    st.markdown("""
    Welcome!  
    Explore foundational quantum concepts through interactive visualizations powered by Python and Streamlit.

    Use the sliders below to adjust parameters and see how these fascinating quantum effects behave in real time.  
    Enjoy your quantum journey! 🚀
    """)

    st.markdown("---")

    # Project Info (short and clear)
    st.markdown("""
    **About this Project:**  
    This interactive tool demonstrates key quantum phenomena—such as superposition, entanglement, wave-particle duality, and uncertainty—using simple analogies and real-time visualizations.  
    The goal is to make complex quantum mechanics accessible and engaging for learners of all levels.
    """)

    st.markdown("---")

    # Spinning Coin (Superposition)
    st.header("Spinning Coin (Superposition)")
    st.markdown("""
    In quantum mechanics, particles can exist in multiple states at once, like a coin spinning in the air — it's both heads and tails until it lands.

    **Visualization:**  
    The graph shows two states (Heads and Tails), each oscillating at different frequencies.  
    The superposition (combined state) is a mix of both, represented by the purple line.

    **Simple Explanation:**  
    Imagine a spinning coin. Instead of being just heads or tails, the coin is in both states at the same time — this is quantum superposition.

    **Interactive Element:**  
    Sliders let you adjust the frequency of heads and tails to see how the superposition changes.
    """)
    state1_freq = st.slider("Frequency of Heads", min_value=1, max_value=10, value=2)
    st.caption("ℹ️ Controls the oscillation frequency of the 'Heads' state wave.")

    state2_freq = st.slider("Frequency of Tails", min_value=1, max_value=10, value=4)
    st.caption("ℹ️ Controls the oscillation frequency of the 'Tails' state wave.")

    plot_spinning_coin(state1_freq, state2_freq)

    st.markdown("---")

    # Instant Effect (Quantum Entanglement)
    st.header("Instant Effect (Quantum Entanglement)")
    st.markdown("""
    When two particles are entangled, changes to one affect the other instantly, regardless of distance.

    **Visualization:**  
    Two particles represented as circles interact instantly even when separated.

    **Simple Explanation:**  
    Think of a magical connection where if you change one particle, the other changes too immediately, no matter how far apart they are.

    **Interactive Element:**  
    Use sliders to adjust the distance between particles and the strength of their entanglement.
    """)
    distance = st.slider("Distance Between Particles", min_value=0.0, max_value=0.4, value=0.2)
    st.caption("ℹ️ Controls the horizontal distance between entangled particles.")

    effect_strength = st.slider("Effect Strength", min_value=0.0, max_value=1.0, value=0.5)
    st.caption("ℹ️ Controls how strongly the particles influence each other.")

    plot_instant_effect(distance, effect_strength)

    st.markdown("---")

    # Wave-Particle Duality
    st.header("Wave-Particle Duality")
    st.markdown("""
    Particles like photons behave as both waves and particles.

    **Visualization:**  
    A wave intensity graph shows the particle's wave-like behavior changing with wavelength.

    **Simple Explanation:**  
    Particles can act like waves, spreading out and interfering, not just tiny balls.

    **Interactive Element:**  
    Adjust the wavelength slider to see how the wave pattern changes.
    """)
    wavelength = st.slider("Wavelength", min_value=1, max_value=10, value=2)
    st.caption("ℹ️ Controls the wavelength of the particle's wave behavior.")

    plot_wave_particle_duality(wavelength)

    st.markdown("---")

    # Quantum Uncertainty (Heisenberg Principle)
    st.header("Quantum Uncertainty (Heisenberg Principle)")
    st.markdown("""
    You cannot know both the exact position and momentum of a particle simultaneously.

    **Visualization:**  
    Probability distributions show uncertainty in position and momentum.

    **Simple Explanation:**  
    Trying to pinpoint a particle's position makes its momentum fuzzy, and vice versa.

    **Interactive Element:**  
    Adjust sliders to change uncertainty levels in position and momentum.
    """)
    position_uncertainty = st.slider("Position Uncertainty", min_value=0.1, max_value=3.0, value=0.5)
    st.caption("ℹ️ Controls the spread of the position probability distribution.")

    momentum_uncertainty = st.slider("Momentum Uncertainty", min_value=0.1, max_value=3.0, value=2.0)
    st.caption("ℹ️ Controls the spread of the momentum probability distribution.")

    plot_uncertainty(position_uncertainty, momentum_uncertainty)
