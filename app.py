import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DE PODER MÁXIMO ---
st.set_page_config(page_title="V8 COMMAND | ULTIMATE POTENTIAL", page_icon="⚡", layout="wide")

# --- DESIGN CYBER-LUXURY (HUD MILITAR EVOLUÍDO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Syncopate:wght@700&family=JetBrains+Mono:wght@400&display=swap');
    
    .stApp { background: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    
    .v8-container {
        background: linear-gradient(145deg, #0a0a0a, #111);
        border: 2px solid #d4af37;
        padding: 40px;
        box-shadow: 0 0 100px rgba(212, 175, 55, 0.2);
        border-radius: 0 60px 0 60px;
    }

    h1 { font-family: 'Orbitron', sans-serif; font-weight: 900; background: linear-gradient(90deg, #d4af37, #fff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3em !important; }
    
    .stTextArea textarea, .stTextInput input {
        background: #111 !important; color: #d4af37 !important; border: 1px solid #333 !important; font-family: 'JetBrains Mono', monospace;
    }

    .stButton>button {
        background: #d4af37; color: #000; font-family: 'Syncopate'; font-weight: bold; border-radius: 0; height: 70px; font-size: 1.2em; border: none; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 50px #d4af37; }
    
    .editor-label { color: #d4af37; font-family: 'Orbitron'; font-size: 0.8em; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE DE CONSTRUÇÃO ---
st.markdown("<h1>V8 GOD MODE: ULTIMATE</h1>", unsafe_allow_html=True)
st.markdown("<p style='letter-spacing:5px; color:#555;'>[ SYSTEM STATUS: UNLIMITED POWER | OPERATOR: CÁSSIA ]</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-container'>", unsafe_allow_html=True)
    
    # INPUTS GLOBAIS
    c1, c2, c3 = st.columns(3)
    with c1:
        nome = st.text_input("💎 NOME DO ALVO:", "Cássia")
        nicho = st.text_input("🎯 ÁREA DE ATUAÇÃO:", "Estrategista Digital")
    with c2:
        especialidade = st.text_input("🔥 MAIOR DIFERENCIAL:", "Método V8 de Escala")
        xp = st.number_input("⏳ ANOS DE MERCADO:", 0, 30, 10)
    with c3:
        target = st.text_input("🚀 PÚBLICO-ALVO:", "Empresários High-Ticket")
        vibe = st.selectbox("🎭 IDENTIDADE VISUAL:", ["TECH-NOIR", "LUXO MINIMALISTA", "POWERFUL GOLD"])

    st.markdown("---")

    # SCANNER DE COMPETÊNCIA
    col_sl, col_rad = st.columns([1, 1])
    with col_sl:
        st.markdown("### [ 🧠 SCANNER DE ATRIBUTOS ]")
        a1 = st.slider("AUTORIDADE", 0, 10, 8)
        a2 = st.slider("PODER DE CÓPIA", 0, 10, 7)
        a3 = st.slider("DESIGN ESTRATÉGICO", 0, 10, 6)
        a4 = st.slider("ESCALABILIDADE", 0, 10, 5)
    with col_rad:
        df = pd.DataFrame(dict(r=[a1, a2, a3, a4], theta=['Autoridade', 'Copy', 'Design', 'Escala']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself', line_color='#d4af37', fillcolor='rgba(212,175,55,0.2)')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#d4af37", polar=dict(bgcolor='rgba(0,0,0,0)'))
        st.plotly_chart(fig, use_container_width=True)

    if st.button("🔥 ATIVAR MATRIZ DE CRIAÇÃO EXTRAORDINÁRIA"):
        st.markdown("---")
        
        # ÁREA DE EDIÇÃO REAL (Onde a mágica acontece)
        st.markdown("### 🛠️ ESTÚDIO DE EDIÇÃO (MODIFIQUE COMO QUISER)")
        
        ed1, ed2 = st.columns(2)
        
        with ed1:
            st.markdown("<p class='editor-label'>[ ARQUIVO: BIOS_OMNICHANNEL ]</p>", unsafe_allow_html=True)
            bio1 = st.text_area("INSTAGRAM (Bio Magnética)", f"🚀 {nicho} | {especialidade}\n💎 Transformando {target} em Autoridade\n⚡ Criadora do Protocolo V8\n👇 Aplique para a Elite:", height=120)
            bio2 = st.text_area("LINKEDIN (Headline de Poder)", f"{nicho} Especialista em {especialidade} | Focada em Gerar Escala para {target} | Mentorada pelo Método V8", height=100)
            bio3 = st.text_area("THREADS / WHATSAPP (Direto)", f"🔥 {nome} | {especialidade}\nConstruindo o futuro de {nicho}.", height=80)

        with ed2:
            st.markdown("<p class='editor-label'>[ ARQUIVO: CURRICULUM_ELITE_LINKEDIN ]</p>", unsafe_allow_html=True)
            curriculo = st.text_area("RESUMO 'SOBRE' EDITÁVEL", 
                f"Estrategista com {xp} anos de campo em {nicho}. \n\nEspecializada em {especialidade}, minha trajetória é marcada pela entrega de resultados extraordinários para {target}. Através do Protocolo V8, implemento sistemas de alta conversão e autoridade inquestionável. \n\nNão busco clientes, seleciono parceiros de negócios que desejam a última potência do digital.", height=340)

        # RELATÓRIO DE IMPACTO
        st.markdown("### 📊 RELATÓRIO DE POTENCIAL V8")
        st.success(f"O sistema detectou um potencial de escala de {(a1+a2+a3+a4)*2.5}%.")
        st.write(f"**Veredito:** O projeto {nome} está pronto para dominar o nicho de {nicho}. Use as bios acima para unificar sua marca hoje.")
        
    st.markdown("</div>", unsafe_allow_html=True)
