import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="V8 God Mode | Auditoria Inteligente", page_icon="🛡️", layout="wide")

# --- ESTILO VISUAL IMPACTANTE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;700&display=swap');
    .stApp { background-color: #050505; color: #fff; font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; text-transform: uppercase; letter-spacing: 2px; }
    .stSlider [data-baseweb="slider"] { margin-bottom: 25px; }
    .report-card { background: linear-gradient(145deg, #111, #000); padding: 30px; border: 1px solid #d4af37; border-radius: 20px; box-shadow: 0 10px 30px rgba(212,175,55,0.2); margin: 20px 0; }
    .bio-box { background: #1a1a1a; padding: 20px; border-radius: 10px; border-left: 5px solid #d4af37; font-style: italic; color: #aaa; margin: 10px 0; }
    .status-badge { padding: 5px 15px; border-radius: 50px; font-weight: bold; text-transform: uppercase; font-size: 0.8em; }
    .fail { background: #ff4b4b; color: white; }
    .elite { background: #d4af37; color: black; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h1>🛡️ V8 SOCIAL AUDITOR - ELITE EDITION</h1>", unsafe_allow_html=True)

# --- ENTRADA DE DADOS ---
with st.sidebar:
    st.markdown("### 🛠️ CONFIGURAÇÃO DO ALVO")
    nome = st.text_input("NOME DO PERFIL", placeholder="Ex: Dra. Ana Paula")
    plataforma = st.selectbox("PLATAFORMA", ["Instagram", "LinkedIn", "TikTok", "YouTube", "OUTROS"])
    if plataforma == "OUTROS":
        plataforma = st.text_input("QUAL?")
    nicho = st.text_input("NICHO / ESPECIALIDADE", placeholder="Ex: Direito Civil")
    obj = st.selectbox("OBJETIVO", ["Venda de Consultoria", "Autoridade Acadêmica", "Escala de Curso", "Atração de Clientes"])

# --- SISTEMA DE PONTUAÇÃO ---
col1, col2 = st.columns(2)
with col1:
    s_comm = st.slider("🗣️ COMUNICAÇÃO", 0, 10, 5)
    s_auth = st.slider("🏛️ AUTORIDADE", 0, 10, 5)
    s_clar = st.slider("💡 CLAREZA", 0, 10, 5)
with col2:
    s_pos = st.slider("🎯 POSICIONAMENTO", 0, 10, 5)
    s_tech = st.slider("⚙️ TÉCNICA/ESTÉTICA", 0, 10, 5)
    s_cons = st.slider("⏳ CONSISTÊNCIA", 0, 10, 5)

# --- LÓGICA DE INTELIGÊNCIA V8 ---
if st.button("🔥 EXECUTAR ANÁLISE E GERAR ESTRATÉGIA"):
    avg = (s_comm + s_auth + s_clar + s_pos + s_tech + s_cons) / 6
    
    # Classificação
    status = "ELITE" if avg >= 8.5 else "PROMISSOR" if avg >= 6 else "INCONSISTENTE"
    badge_class = "elite" if status == "ELITE" else "fail"

    st.markdown(f"<div class='report-card'>", unsafe_allow_html=True)
    st.markdown(f"<h2>DIAGNÓSTICO: <span class='status-badge {badge_class}'>{status}</span></h2>", unsafe_allow_html=True)
    st.metric("SCORE DE MATURIDADE V8", f"{avg:.2f}")

    # --- GERADOR DE BIO INTELIGENTE ---
    st.markdown("### 📝 NOVA BIO SUGERIDA (COPIAR/COLAR)")
    bio = f"⚖️ {nicho}\n📍 Especialista em {obj}\n🚀 Transformando complexidade em solução.\n👇 Agende sua consulta aqui:"
    st.markdown(f"<div class='bio-box'>{bio}</div>", unsafe_allow_html=True)

    # --- PLANO DE ATAQUE CRÍTICO ---
    st.markdown("### ⚡ PLANO DE ATAQUE (PRÓXIMOS 7 DIAS)")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**PARA O FEED (AUTORIDADE):**")
        if s_auth < 7:
            st.write("1. Post de 'Bastidores de um caso real' (borrando dados).")
            st.write("2. Carrossel: '3 erros que seu advogado não te conta'.")
        else:
            st.write("1. Artigo de opinião sobre nova lei.")
            st.write("2. Vídeo de Lifestyle de alto padrão + Insight jurídico.")

    with col_b:
        st.markdown("**PARA OS STORIES (CONEXÃO):**")
        st.write("1. Box de perguntas: 'Dúvida do dia'.")
        st.write("2. Narrativa: 'Por que eu escolhi o " + nicho + "'.")

    # --- RELATÓRIO TÉCNICO ---
    st.markdown("### 📊 LACUNAS DETECTADAS")
    scores = {"Comunicação": s_comm, "Autoridade": s_auth, "Clareza": s_clar, "Posicionamento": s_pos, "Técnica": s_tech, "Consistência": s_cons}
    for k, v in scores.items():
        if v < 6:
            st.warning(f"🚨 **{k.upper()}**: Nota {v}. Você está perdendo dinheiro por falta de clareza nesta área.")
        
    st.markdown("</div>", unsafe_allow_html=True)
    st.success("✅ Relatório V8 Gerado com Sucesso. Comande o mercado!")
