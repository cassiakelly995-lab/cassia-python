import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DE ÚLTIMA POTÊNCIA ---
st.set_page_config(page_title="V8 COMMAND | OMNIPOTENCE", page_icon="🔱", layout="wide")

# --- DESIGN HUD BLACK & GOLD ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@400&display=swap');
    .stApp { background: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    .v8-card { background: rgba(10, 10, 10, 0.95); border: 2px solid #d4af37; border-radius: 0 50px 0 50px; padding: 40px; box-shadow: 0 0 80px rgba(212,175,55,0.15); margin-bottom: 25px; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37; letter-spacing: 2px; }
    .stButton>button { background: #d4af37; color: #000; font-family: 'Orbitron'; font-weight: 900; border-radius: 0; height: 60px; width: 100%; border: none; transition: 0.5s; }
    .stButton>button:hover { box-shadow: 0 0 50px #d4af37; transform: scale(1.01); }
    .metric-box { background: #111; border: 1px solid #333; padding: 20px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>V8 GOD MODE: OMNIPOTENCE</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-card'>", unsafe_allow_html=True)
    
    # INPUTS ESTRATÉGICOS
    c1, c2, c3 = st.columns(3)
    with c1:
        nome = st.text_input("💎 NOME DO ALVO:", "Cliente VIP")
        nicho = st.text_input("🎯 ÁREA/NICHO:", "Estrategista")
    with c2:
        ticket = st.number_input("💰 TICKET MÉDIO (R$):", 1000, 50000, 5000)
        perda_est = st.slider("📉 QUANTO DEIXA DE VENDER/MÊS (%):", 0, 100, 40)
    with c3:
        concorrente = st.text_input("⚔️ NOME DO CONCORRENTE:", "Maior Player")
        obj = st.selectbox("🚀 OBJETIVO:", ["DOMÍNIO DE MERCADO", "ESCALA HIGH-TICKET", "REPOSICIONAMENTO LUXO"])

    st.markdown("---")

    # RADAR COMPARATIVO
    st.markdown("### [ 🧠 DOSSIÊ COMPARATIVO: VOCÊ VS CONCORRENTE ]")
    col_l, col_r = st.columns([1, 1.2])
    
    with col_l:
        st.markdown("**SUAS NOTAS:**")
        s1 = st.slider("AUTORIDADE ", 0, 10, 5)
        s2 = st.slider("CONVERSÃO ", 0, 10, 5)
        s3 = st.slider("ESTÉTICA ", 0, 10, 5)
        st.markdown("**NOTAS CONCORRENTE:**")
        c1_n = st.slider("AUTORIDADE CONC.", 0, 10, 8)
        c2_n = st.slider("CONVERSÃO CONC.", 0, 10, 7)
        c3_n = st.slider("ESTÉTICA CONC.", 0, 10, 9)

    with col_r:
        categories = ['Autoridade', 'Conversão', 'Estética']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[s1, s2, s3], theta=categories, fill='toself', name=nome, line_color='#d4af37'))
        fig.add_trace(go.Scatterpolar(r=[c1_n, c2_n, c3_n], theta=categories, fill='toself', name=concorrente, line_color='#555'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), paper_bgcolor='rgba(0,0,0,0)', font_color="#d4af37", plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

    if st.button("🔥 EXECUTAR PROTOCOLO OMNIPOTENCE"):
        st.markdown("---")
        
        # CALCULADORA DE IMPACTO FINANCEIRO
        st.markdown("### 💸 IMPACTO FINANCEIRO DA MEDIOCRIDADE")
        perda_anual = (ticket * (perda_est / 100)) * 12
        st.markdown(f"<div class='metric-box'><h2 style='color:#ff4b4b;'>PERDA ESTIMADA ANUAL: R$ {perda_anual:,.2f}</h2><p>Este é o custo de não aplicar o Protocolo V8.</p></div>", unsafe_allow_html=True)

        # ABAS DE ENTREGA
        tab1, tab2, tab3 = st.tabs(["🖋️ BIOS & HEADLINES", "📄 CURRÍCULO DE ELITE", "📱 FUNIL DE STORIES"])
        
        with tab1:
            st.markdown("<p style='color:#d4af37;'>[ EDITÁVEL ]</p>", unsafe_allow_html=True)
            st.text_area("INSTAGRAM", f"💎 {nicho}\n🚀 Mentorada pelo Protocolo V8\n🏆 Especialista em {obj}\n👇 Sua escala começa aqui:", height=100)
            st.text_area("LINKEDIN", f"Estrategista de Negócios em {nicho} | Especialista em {obj} | Foco em High-Ticket", height=70)

        with tab2:
            st.text_area("RESUMO EXECUTIVO (EDITÁVEL)", f"Profissional com foco em {nicho}. Através do Protocolo V8, implemento metodologias de elite para {obj}. Especialidade em gerar faturamento e autoridade inquestionável.", height=200)

        with tab3:
            st.markdown("### 🎬 FUNIL DE 3 DIAS")
            st.warning("**DIA 1 (CONSCIÊNCIA):** Mostre o erro comum do mercado de " + nicho + ".")
            st.info("**DIA 2 (AUTORIDADE):** Apresente o resultado do Protocolo V8.")
            st.success("**DIA 3 (CONVERSÃO):** Chamada direta para o WhatsApp/Direct.")

    st.markdown("</div>", unsafe_allow_html=True)
