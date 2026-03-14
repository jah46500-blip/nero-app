import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import time

# --- CONFIGURATION AVANCÉE ---
st.set_page_config(page_title="NERO OS - Advanced", page_icon="⚡", layout="centered")

# --- CUSTOM CSS (DARK MODE PREMIUM) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .stMetric { background-color: #1E2127; padding: 15px; border-radius: 8px; border: 1px solid #333; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    div[data-testid="stTabs"] button { font-weight: bold; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

# --- MÉMOIRE DE L'IA (ÉTAT DE SESSION) ---
if 'total_gain' not in st.session_state:
    st.session_state.total_gain = 20.80
if 'history' not in st.session_state:
    st.session_state.history = [] # Pour stocker la liste des ventes

# --- HEADER NERO OS ---
st.title("⚡ NERO OS | Edge Grid")
st.caption(f"📍 Node Actif : Quartier Eco-Lilas | Moteur DRL v2.1 | Brevet PCT/FR2026/0001")

# --- CRÉATION DES ONGLETS DE NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🤝 Marché P2P", "⚙️ NERO Box"])

# ==========================================
# ONGLET 1 : LE TABLEAU DE BORD PRINCIPAL
# ==========================================
with tab1:
    st.markdown("### Bilan Énergétique Temps Réel")
    c1, c2, c3 = st.columns(3)
    c1.metric("Prod. Solaire", "5.1 kW", "+12%")
    c2.metric("Conso. Foyer", "1.1 kW", "-5%")
    c3.metric("Stockage VE", "72%", "38 kWh")

    st.markdown("### 🧠 Modélisation des Flux (24h)")
    # Graphique avancé en aires croisées
    x = [f"{i}h" for i in range(24)]
    solar = [0,0,0,0,0,0, 1,4,7,9,10,10,9,7,4,1, 0,0,0,0,0,0,0,0]
    conso = [1,1,1,1,1,2, 3,2,1,1,1, 1, 1,1,2,4, 5,6,4,2,1,1,1,1]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=solar, fill='tozeroy', name="Solaire Produit", line=dict(color='#F5B041', width=3)))
    fig.add_trace(go.Scatter(x=x, y=conso, fill='tozeroy', name="Consommation", line=dict(color='#E74C3C', width=3)))
    
    fig.update_layout(
        height=320, margin=dict(l=0,r=0,t=10,b=0),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#FAFAFA"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='#333')
    )
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# ONGLET 2 : LE TRADING P2P (LA RENTABILITÉ)
# ==========================================
with tab2:
    st.markdown("### Bourse Énergétique Locale")
    st.metric("Gains P2P Cumulés", f"{st.session_state.total_gain:.2f} €", "Optimisé par IA")
    st.divider()

    if st.button("⚡ Lancer l'algorithme d'arbitrage P2P", use_container_width=True):
        with st.spinner("Deep Learning : Recherche du meilleur acheteur local..."):
            time.sleep(1.5)
            # Génération d'une vente aléatoire pour plus de réalisme
            gain = round(np.random.uniform(0.30, 0.80), 2)
            voisin = np.random.randint(10, 99)
            volume = round(np.random.uniform(1.0, 3.5), 1)
            
            # Mise à jour des données
            st.session_state.total_gain += gain
            st.session_state.history.insert(0, {
                "Heure": datetime.now().strftime("%H:%M:%S"), 
                "Acheteur": f"Voisin #{voisin}", 
                "Volume (kWh)": volume, 
                "Gain (€)": f"+{gain}"
            })
            
        st.success(f"Contrat intelligent exécuté ! +{gain}€ ajoutés.")
        st.balloons()

    # Affichage de l'historique si des ventes ont été faites
    if st.session_state.history:
        st.markdown("📜 **Historique (Blockchain Locale) :**")
        st.dataframe(pd.DataFrame(st.session_state.history), use_container_width=True, hide_index=True)

# ==========================================
# ONGLET 3 : LE HARDWARE (RÉASSURANCE VC)
# ==========================================
with tab3:
    st.markdown("### Télémétrie NERO Box")
    st.info("🟢 Communication avec le compteur Linky (Port TIC) : STABLE")
    
    c1, c2 = st.columns(2)
    c1.metric("CPU Temp (ESP32)", "42°C", "Normal")
    c2.metric("Latence Réseau", "12 ms", "Excellent")

    st.divider()
    st.warning("⚠️ Simulation de Crise Majeure")
    st.write("Démontrez la capacité de résilience du système aux investisseurs.")
    
    if st.button("🚨 Simuler Coupure Réseau National", type="primary", use_container_width=True):
        st.error("BLACKOUT DÉTECTÉ : Le réseau ENEDIS est tombé à 0V.")
        time.sleep(1)
        st.success("MODE ÎLOTAGE ACTIVÉ : La NERO Box a déconnecté la maison du réseau.")
        st.info("🔌 Le foyer est désormais alimenté à 100% par le V2H (Voiture) et le solaire. Autonomie vitale estimée : 48h.")
