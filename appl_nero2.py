import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time 

st.set_page_config(page_title="NERO Energy", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_stdio=True)

if 'total_gain' not in st.session_state:
    st.session_state.total_gain = 20.80

st.title("⚡ NERO Intelligence")
st.write(f"📅 **{datetime.now().strftime('%d %B %Y')}** | Quartier : *Eco-Lilas*")

mode = st.select_slider(
    "Mode de gestion IA",
    options=["💰 Cash-Out", "🌿 Éco-Pilote", "🛡️ Sérénité"],
    value="🌿 Éco-Pilote"
)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.metric("Production Solaire", "5.10 kW", "+12% ☀️")
    st.metric("Gains NERO (Mois)", f"{st.session_state.total_gain:.2f} €", "+8.20 €")
with col2:
    st.metric("Conso. Maison", "1.16 kW", "-5% ✅")
    st.metric("Autonomie", "94%", "Optimale")

st.write("### 🔋 État du Stockage (Maison + VE)")
bat_val = st.progress(72)
st.caption("72% - 38 kWh disponibles (Capacité totale 52 kWh)")

st.write("### 🧠 Prévisions IA (24h)")
x = np.arange(24)
prices = [0.15, 0.15, 0.15, 0.15, 0.15, 0.22, 0.28, 0.28, 0.20, 0.15, 0.15, 0.15, 0.12, 0.12, 0.12, 0.15, 0.18, 0.25, 0.30, 0.30, 0.25, 0.20, 0.15, 0.15]
solar = [0, 0, 0, 0, 0, 1, 3, 6, 8, 9, 10, 9, 8, 6, 4, 2, 0.5, 0, 0, 0, 0, 0, 0, 0]

# --- PARTIE CORRIGÉE POUR LE BUG ---
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=x, y=prices, name="Prix Réseau (€)", line=dict(color='firebrick', width=2, dash='dot'))
)

fig.add_trace(
    go.Bar(x=x, y=solar, name="Prod. Solaire (kW)", marker_color='orange', opacity=0.6)
)

fig.update_layout(height=300, margin=dict(l=0, r=0, t=20, b=0), legend=dict(orientation="h", yanchor="bottom", y=1.02))
st.plotly_chart(fig, use_container_width=True)
# ------------------------------------

st.write("### 🤝 Marché Local (P2P)")
if st.button("🚀 Simuler une vente au voisin"):
    with st.status("Négociation Smart Grid en cours...", expanded=True) as status:
        st.write("🔍 Scan des besoins du quartier...")
        time.sleep(1.5) 
        st.write("🤝 Voisin #42 détecté (Besoin : 2.5kWh pour VE)")
        st.write("💰 Prix négocié : 0.18€/kWh (vs 0.10€ rachat réseau)")
        
        gain_transaction = 2.5 * 0.18
        st.session_state.total_gain += gain_transaction
        
        status.update(label=f"Vente terminée ! Gain : +{gain_transaction:.2f}€", state="complete", expanded=False)
    
    st.balloons()
    st.success(f"📈 Transaction réussie ! Le profit mensuel est passé à {st.session_state.total_gain:.2f} €")

with st.expander("⚠️ Rapports de Résilience (Stress Test)"):
    st.warning("Simuler un Blackout réseau")
    if st.button("Activer Mode Îlotage"):
        st.error("RÉSEAU COUPÉ : NERO maintient l'alimentation via la batterie.")
        st.info("Priorité : Frigo, Wi-Fi, Alarme. Autonomie restante : 18h20.")

st.divider()
st.caption("NERO v1.0 - Protégé par Brevet PCT/FR2026/0001")
