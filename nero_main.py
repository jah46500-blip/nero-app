
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time  # Indispensable pour l'animation de recherche de l'IA

# --- CONFIGURATION SMARTPHONE ---
st.set_page_config(page_title="NERO Energy", page_icon="⚡", layout="centered")

# Custom CSS pour un look "Premium Tech"
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_stdio=True)

# --- INITIALISATION DE LA MÉMOIRE (Pour le profit cumulé) ---
if 'total_gain' not in st.session_state:
    st.session_state.total_gain = 20.80  # Le chiffre de départ de ta capture d'écran

# --- EN-TÊTE ---
st.title("⚡ NERO Intelligence")
st.write(f"📅 **{datetime.now().strftime('%d %B %Y')}** | Quartier : *Eco-Lilas*")

# --- MODES DE PILOTAGE ---
mode = st.select_slider(
    "Mode de gestion IA",
    options=["💰 Cash-Out", "🌿 Éco-Pilote", "🛡️ Sérénité"],
    value="🌿 Éco-Pilote"
)

st.divider()

# --- STATS TEMPS RÉEL ---
col1, col2 = st.columns(2)
with col1:
    st.metric("Production Solaire", "5.10 kW", "+12% ☀️")
    # Le compteur de gains se met à jour dynamiquement !
    st.metric("Gains NERO (Mois)", f"{st.session_state.total_gain:.2f} €", "+8.20 €")
with col2:
    st.metric("Conso. Maison", "1.16 kW", "-5% ✅")
    st.metric("Autonomie", "94%", "Optimale")

# --- VISU BATTERIE ---
st.write("### 🔋 État du Stockage (Maison + VE)")
bat_val = st.progress(72)
st.caption("72% - 38 kWh disponibles (Capacité totale 52 kWh)")

# --- LE COEUR DE L'INVENTION : LE GRAPH PRÉDICTIF ---
st.write("### 🧠 Prévisions IA (24h)")
x = np.arange(24)
prices = [0.15, 0.15, 0.15, 0.15, 0.15, 0.22, 0.28, 0.28, 0.20, 0.15, 0.15, 0.15, 0.12, 0.12, 0.12, 0.15, 0.18, 0.25, 0.30, 0.30, 0.25, 0.20, 0.15, 0.15]
solar = [0, 0, 0, 0, 0, 1, 3, 6, 8, 9, 10, 9, 8, 6, 4, 2, 0.5, 0, 0, 0, 0, 0, 0, 0]

fig = go.Figure()
fig.add_trace(
