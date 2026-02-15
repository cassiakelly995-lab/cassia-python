import streamlit as st
import pandas as pd
import plotly.express as px

# --- SETUP V8 GENESIS ---
st.set_page_config(page_title="V8 GENESIS | ULTIMATE", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    .stApp { background: #000; color: #d4af37; font-family: 'Courier New', monospace; }
    .v8-box { border: 2px solid #d4af37; padding: 30px; border-radius: 20px; background: rgba(10,10,10,0.9); box-shadow: 0 0 50px rgba(212,175,55,0.2); }
    h1 { text-align: center; letter-spacing: 5px; font-family: 'Orbitron', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>🔱 V8 GENESIS: FORJA DE ELITE</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-box'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        nome = st.text_input("💎 NOME DO OPERADOR:", "Cássia")
        nicho = st.text_input("🎯 ÁREA DE DOMÍNIO:", "Estrategista")
    with c2:
        poder = st.text_input("🔥 DIFERENCIAL:", "Método V8")
        objetivo = st.text_input("🚀 ALVO:", "High-Ticket")

    st.markdown("---")
    
    # Radar Interativo
    s1 = st.slider("AUTORIDADE", 0, 10, 8)
    s2 = st.slider("ESTRATÉGIA", 0, 10, 7)
    s3 = st.slider("VISUAL", 0, 10, 6)
    
    df = pd.DataFrame(dict(r=[s1, s2, s3], theta=['Autoridade', 'Estratégia', 'Visual']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself', line_color='#d4af37', fillcolor='rgba(212,175,55,0.2)')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#d4af37", polar=dict(bgcolor='rgba(0,0,0,0)'))
    st.plotly_chart(fig, use_container_width=True)

    if st.button("🔥 GERAR PERFIL INVENCÍVEL"):
        tab1, tab2 = st.tabs(["📌 BIOS OMNICHANNEL", "📄 CURRÍCULO EDITÁVEL"])
        with tab1:
            st.text_area("INSTAGRAM:", f"🚀 {nicho}\n💎 Especialista em {poder}\n⚡ Elevando {objetivo} ao topo.\n👇 Link:", height=100)
        with tab2:
            st.text_area("RESUMO EXECUTIVO:", f"Operador: {nome}\nEstrategista focado em {nicho}.\nUtilizando o {poder} para dominar o mercado de {objetivo}.", height=150)
    st.markdown("</div>", unsafe_allow_html=True)
