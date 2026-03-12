import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="NERO Smart Dashboard", page_icon="⚡", layout="centered")

st.title("⚡ NERO : Votre Hub Énergétique")
st.subheader("Optimisation IA en temps réel")

# --- SIDEBAR (PARAMÈTRES) ---
st.sidebar.header("Paramètres du Mode")
mode = st.sidebar.selectbox(
    "Choisir le mode", ["🌿 Éco-Pilote", "🛡️ Sérénité", "💰 Cash-Out"]
)

# --- SIMULATION DE DONNÉES EN DIRECT ---
col1, col2, col3 = st.columns(3)

# Simulation de valeurs
sol_prod = round(np.random.uniform(3.0, 5.5), 2)
house_cons = round(np.random.uniform(1.0, 2.5), 2)
profit = round(np.random.uniform(12.50, 45.00), 2)

with col1:
    st.metric("Production Solaire", f"{sol_prod} kW", "+12%")
with col2:
    st.metric("Consommation", f"{house_cons} kW", "-5%")
with col3:
    st.metric("Gains NERO (Mois)", f"{profit} €", "+8.20 €")

# --- VISUEL DU FLUX (Progress Bar pour la batterie) ---
st.write("---")
bat_level = st.slider("Niveau de batterie (Maison + VE)", 0, 100, 68)
st.progress(bat_level / 100)
st.caption(f"Batterie à {bat_level}% - Autonomie estimée : 14h")

# --- GRAPHIQUE DE L'IA ---
st.write("### 📈 Prédiction de charge (Prochaines 24h)")
chart_data = pd.DataFrame(
    np.random.randn(24, 2), columns=["Production Estimée", "Prix du Réseau (€)"]
)
st.line_chart(chart_data)

# --- BOUTON D'ACTION POUR LE PITCH ---
if st.button("Simuler une vente au voisinage"):
    with st.spinner("Négociation du meilleur prix P2P..."):
        time.sleep(2)
        st.success("Succès ! 2.5 kWh vendus au Voisin #42 à 0.18€/kWh (Gain : 0.45€)")
        st.balloons()

st.write("---")
st.info(
    f"💡 NERO a activé le mode {mode}. Votre chauffe-eau a été décalé à 14h pour profiter du pic solaire."
)
