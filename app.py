import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DE ALTA PATENTE ---
st.set_page_config(page_title="V8 COMMAND CENTER | ELITE EDITION", page_icon="🔱", layout="wide")

# --- DESIGN HUD MILITAR (BLACK & GOLD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Syncopate:wght@700&family=JetBrains+Mono:wght@300&display=swap');
    .stApp { background: #000; color: #fff; font-family: 'JetBrains Mono', monospace; }
    .v8-hud { background: rgba(10, 10, 10, 0.98); border: 2px solid #d4af37; border-radius: 0 40px 0 40px; padding: 40px; box-shadow: 0 0 80px rgba(212,175,55,0.15); margin: 10px; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37; letter-spacing: 3px; }
    .stButton>button { background: transparent; color: #d4af37; border: 1px solid #d4af37; font-family: 'Syncopate'; height: 50px; width: 100%; transition: 0.5s; font-weight: bold; }
    .stButton>button:hover { background: #d4af37; color: #000; box-shadow: 0 0 40px #d4af37; }
    .report-card { background: #0d0d0d; border-left: 5px solid #d4af37; padding: 20px; border-radius: 5px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h1>SYSTEM: V8_PROFESSIONAL_COMMAND</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#666;'>[ MODULE: CAREER_ARCHITECT_V.8.0 ]</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-hud'>", unsafe_allow_html=True)
    
    # INPUTS DE DADOS
    c1, c2, c3 = st.columns(3)
    with c1:
        nome = st.text_input("> NOME DO PROFISSIONAL:", "Dra. Franciane")
        experiencia = st.slider("> ANOS DE EXPERIÊNCIA:", 0, 20, 5)
    with c2:
        nicho = st.text_input("> NICHO DE ATUAÇÃO:", "Direito Imobiliário")
        especialidade = st.text_input("> MAIOR RESULTADO:", "Recuperação de Ativos")
    with c3:
        obj = st.selectbox("> OBJETIVO ATUAL:", ["ATRAIR CLIENTES", "PALESTRANTE", "ESCALA DIGITAL"])
        tom = st.selectbox("> TOM DE VOZ:", ["BRUTAL", "SOFISTICADO", "EXECUTIVO"])

    st.markdown("---")
    
    # ANALISADOR DE COMPETÊNCIA
    col_par, col_vis = st.columns([1, 1.2])
    with col_par:
        st.markdown("### [ SCANNER DE MERCADO ]")
        s1 = st.slider("AUTORIDADE PERCEBIDA", 0, 10, 5)
        s2 = st.slider("PODER DE CONVENCIMENTO", 0, 10, 5)
        s3 = st.slider("POSICIONAMENTO VISUAL", 0, 10, 5)
        s4 = st.slider("QUALIDADE TÉCNICA", 0, 10, 5)
    with col_vis:
        df = pd.DataFrame(dict(r=[s1, s2, s3, s4], theta=['Autoridade', 'Convencimento', 'Visual', 'Técnica']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself', line_color='#d4af37', fillcolor='rgba(212,175,55,0.2)')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color="#d4af37", polar=dict(bgcolor='rgba(0,0,0,0)'))
        st.plotly_chart(fig, use_container_width=True)

    if st.button("🔥 EXECUTAR ARQUITETURA DE CARREIRA"):
        st.markdown("---")
        
        # ABA DE RESULTADOS
        tab1, tab2, tab3 = st.tabs(["📲 BIOS PRONTAS", "📄 CURRÍCULO LINKEDIN", "📊 RELATÓRIO V8"])
        
        with tab1:
            st.markdown("### 🏹 BIOS MULTICHANNEL")
            st.subheader("Instagram")
            st.code(f"⚖️ {nicho}\n🏆 {especialidade}\n🚀 Estrategista de Elite | Protocolo V8\n📍 Atendendo em todo território nacional\n👇 Agende seu diagnóstico:")
            st.subheader("LinkedIn (Headline)")
            st.code(f"Especialista em {nicho} | {especialidade} | Consultoria Estratégica para {obj} | Protocolo V8")
            st.subheader("WhatsApp / Threads")
            st.code(f"🔥 {nome} | {nicho}\nElevando o padrão de {obj} no mercado.")

        with tab2:
            st.markdown("### 💼 RESUMO PROFISSIONAL (LINKEDIN)")
            resumo = f"""
            Com mais de {experiencia} anos de atuação em {nicho}, foco minha carreira em {especialidade}. 
            Minha metodologia une o rigor técnico à estratégia digital do Protocolo V8, garantindo que o posicionamento de mercado reflita a autoridade real.
            
            Atualmente focado em {obj}, busco conectar com parceiros e clientes que não aceitam a mediocridade. 
            Especialidades: {nicho}, {especialidade} e Gestão de Crise de Imagem.
            """
            st.info(resumo)
            st.markdown("**Sugestão de Experiência Profissional:**")
            st.write(f"• Implementação do Protocolo V8 em processos de {nicho}.")
            st.write(f"• Gestão de autoridade para {obj}.")

        with tab3:
            st.markdown("### 🚩 DIAGNÓSTICO SEVERO")
            avg = (s1+s2+s3+s4)/4
            if avg < 6:
                st.error(f"VEREDITO: SEU POSICIONAMENTO ESTÁ MATANDO SEU LUCRO. Sua nota de {avg} indica que você é visto como 'mais um'.")
            else:
                st.success(f"VEREDITO: ELITE EM CONSTRUÇÃO. Sua nota de {avg} permite escalar para High-Ticket imediatamente.")
            
            st.markdown("### 📈 PLANO DE ATAQUE")
            st.write("1. **Postagem:** Hoje você deve postar um vídeo sobre como o " + nicho + " está mudando.")
            st.write("2. **Conexão:** Envie seu currículo V8 para 5 potenciais parceiros hoje.")
    
    st.markdown("</div>", unsafe_allow_html=True)
