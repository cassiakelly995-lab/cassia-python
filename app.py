import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DE ALTA PATENTE ---
st.set_page_config(page_title="V8 OMNIPOTENCE", page_icon="🔱", layout="wide")

# --- DESIGN HUD CYBER-LUXURY (PRETO & OURO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@400;700&display=swap');
    
    .stApp { background: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    
    .v8-panel {
        background: rgba(10, 10, 10, 0.95);
        border: 2px solid #d4af37;
        padding: 40px;
        border-radius: 0 50px 0 50px;
        box-shadow: 0 0 100px rgba(212, 175, 55, 0.2);
    }

    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37; letter-spacing: 5px; }
    
    .stButton>button {
        background: linear-gradient(90deg, #8a6d1d, #d4af37);
        color: #000; font-family: 'Orbitron'; font-weight: 900;
        height: 70px; width: 100%; border-radius: 5px; border: none;
        font-size: 1.2rem; transition: 0.5s;
    }
    .stButton>button:hover { box-shadow: 0 0 60px #d4af37; transform: translateY(-5px); }

    .network-card {
        background: #0a0a0a; border-left: 5px solid #d4af37;
        padding: 20px; margin-bottom: 20px; border-radius: 10px;
    }
    
    .stTextArea textarea { background: #111 !important; color: #d4af37 !important; border: 1px solid #333 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE INTELIGÊNCIA V8 ---
st.markdown("<h1>V8 OMNIPOTENCE SYSTEM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666;'>[ STATUS: MAXIMUM POWER | OPERATOR: CÁSSIA ]</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-panel'>", unsafe_allow_html=True)
    
    # MATRIZ DE ENTRADA INTERATIVA
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("💎 NOME DO OPERADOR:", "Cássia Kelly")
        nicho = st.text_input("🎯 NICHO DE DOMÍNIO:", "Estrategista Digital")
        xp = st.text_input("⏳ TEMPO DE MERCADO:", "10 Anos")
    with col2:
        metodo = st.text_input("🔥 MÉTODO PRÓPRIO:", "Protocolo V8")
        target = st.text_input("🚀 ALVO (PÚBLICO-ALVO):", "Empresários High-Ticket")
        objetivo = st.selectbox("🎯 OBJETIVO DA PRESENÇA:", ["DOMÍNIO DE MERCADO", "VENDA DE HIGH-TICKET", "AUTORIDADE MÁXIMA"])

    st.markdown("---")
    
    # SCANNER DE STATUS (RADAR)
    col_l, col_r = st.columns([1, 1.2])
    with col_l:
        st.markdown("### [ 🧠 SCANNER DE ATRIBUTOS ]")
        s1 = st.slider("AUTORIDADE PERCEBIDA", 0, 10, 5)
        s2 = st.slider("PODER DE COMUNICAÇÃO", 0, 10, 5)
        s3 = st.slider("DESIGN ESTRATÉGICO", 0, 10, 5)
        s4 = st.slider("ESCALABILIDADE", 0, 10, 5)
    with col_r:
        df = pd.DataFrame(dict(r=[s1, s2, s3, s4], theta=['Autoridade', 'Comunicação', 'Design', 'Escala']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself', line_color='#d4af37', fillcolor='rgba(212,175,55,0.2)')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#d4af37", polar=dict(bgcolor='rgba(0,0,0,0)'))
        st.plotly_chart(fig, use_container_width=True)

    if st.button("🔥 EXECUTAR ARQUITETURA OMNICHANNEL"):
        st.markdown("---")
        st.markdown("### 📊 DOSSIÊ FINAL: PERFIL DE ELITE MONTADO")
        
        # INTERFACE DE RESULTADO MULTI-REDES
        tabs = st.tabs(["📸 INSTAGRAM", "💼 LINKEDIN", "👥 FACEBOOK", "📜 CURRÍCULO V8"])
        
        with tabs[0]:
            st.markdown("<div class='network-card'>", unsafe_allow_html=True)
            st.subheader("Arquitetura Instagram")
            st.text_input("Nome do Usuário (Sugerido):", f"@{nome.lower().replace(' ', '')}_v8")
            st.text_area("BIO (Otimizada):", f"⚖️ {nicho}\n🏆 {xp} | Criadora do {metodo}\n💎 Elevando {target} ao Nível Elite.\n👇 Aplique para a Consultoria:", height=120)
            st.info("**ESTRATÉGIA DE DESTAQUES:** 1. Método V8 | 2. Resultados | 3. Comece Aqui")
            st.markdown("</div>", unsafe_allow_html=True)

        with tabs[1]:
            st.markdown("<div class='network-card'>", unsafe_allow_html=True)
            st.subheader("Arquitetura LinkedIn")
            st.text_input("Título Profissional (Headline):", f"{nicho} | Especialista em {metodo} | Focada em Gerar Escala para {target}")
            st.text_area("RESUMO 'SOBRE' (Copy de Alto Valor):", f"Estrategista com {xp} de experiência. Utilizo o {metodo} para transformar a presença digital de {target} em máquinas de lucro. Especialidades: {nicho} e Posicionamento de Luxo.", height=200)
            st.markdown("</div>", unsafe_allow_html=True)

        with tabs[2]:
            st.markdown("<div class='network-card'>", unsafe_allow_html=True)
            st.subheader("Arquitetura Facebook (Fanpage)")
            st.text_input("Categoria:", "Consultoria de Negócios")
            st.text_area("Informações Adicionais (About):", f"Página oficial de {nome}. Focada em disseminar a cultura do {metodo} e elevar o nível de {nicho} no mercado atual.", height=100)
            st.markdown("</div>", unsafe_allow_html=True)

        with tabs[3]:
            st.markdown("<div class='network-card'>", unsafe_allow_html=True)
            st.subheader("Dossiê de Carreira")
            cv = f"Dossiê Profissional: {nome}\nStatus: {objetivo}\nMetodologia: {metodo}\n\nO mercado de {nicho} exige o nível V8. Este currículo reflete a autoridade de quem domina {target}."
            st.text_area("CURRÍCULO EDITÁVEL:", cv, height=200)
            st.download_button("📥 BAIXAR DOSSIÊ", cv, file_name="v8_dossie.txt")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
