import streamlit as st
import pandas as pd
import plotly.express as px
import random

# --- CONFIGURAÇÃO V8 GOD MODE ---
st.set_page_config(page_title="V8 NEXUS | COMMAND CENTER", page_icon="🔱", layout="wide")

# --- DESIGN DE ELITE (ESTILO BLACK & GOLD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Syncopate:wght@700&display=swap');
    .stApp { background: #000; color: #fff; }
    .nexus-card { background: rgba(15, 15, 15, 0.9); border: 1px solid #d4af37; border-radius: 20px; padding: 30px; box-shadow: 0 0 40px rgba(212, 175, 55, 0.2); }
    h1 { font-family: 'Orbitron', sans-serif; color: #d4af37; text-align: center; letter-spacing: 10px; }
    .post-box { background: #111; border-left: 5px solid #d4af37; padding: 20px; border-radius: 10px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>V8 NEXUS</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='nexus-card'>", unsafe_allow_html=True)
    
    # INPUTS
    c1, c2, c3 = st.columns(3)
    with c1: nome = st.text_input("💎 NOME DO PROJETO", "Cássia V8")
    with c2: nicho = st.text_input("🎯 NICHO", "Direito de Elite")
    with c3: tom = st.selectbox("🎭 TOM DA VOZ", ["AGRESSIVO", "MAGNÉTICO", "TÉCNICO"])

    st.markdown("---")
    
    # RADAR INTERATIVO
    col_sl, col_gr = st.columns([1, 1])
    with col_sl:
        s1 = st.slider("COMUNICAÇÃO", 0, 10, 7)
        s2 = st.slider("AUTORIDADE", 0, 10, 5)
        s3 = st.slider("ESTRATÉGIA", 0, 10, 6)
        s4 = st.slider("VISUAL", 0, 10, 4)
    with col_gr:
        df = pd.DataFrame(dict(r=[s1, s2, s3, s4], theta=['Comunicação', 'Autoridade', 'Estratégia', 'Visual']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself', line_color='#d4af37')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#fff")
        st.plotly_chart(fig, use_container_width=True)

    if st.button("🔥 GERAR ECOSSISTEMA SUPREMO"):
        st.markdown("---")
        # GERADOR DE POST E ONDE POSTAR
        st.markdown("### 🎬 POST DE ELITE & CANAL ESTRATÉGICO")
        canais = ["REELS (Impacto)", "CARROSSEL (Educação)", "STORIES (Venda)"]
        canal = random.choice(canais)
        
        st.markdown(f"**ONDE POSTAR:** `{canal}`")
        st.markdown(f"""
        <div class='post-box'>
            <p><b>BIO SUGERIDA:</b> ⚖️ Especialista em {nicho} | 🏛️ Elevando seu padrão ao nível V8 | 👇 Agende aqui:</p>
            <p><b>LEGENDA:</b> O mercado de {nicho} não aceita amadores. Se você não é a autoridade, você é invisível. Chegou a hora de ativar o modo V8.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
