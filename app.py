import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- CONFIGURAÇÃO DE ELITE V8 ---
st.set_page_config(page_title="V8 Social Competence | Auditoria", page_icon="💎", layout="wide")

# --- BANCO DE DADOS (SQLite) ---
Base = declarative_base()
class ProfileV8(Base):
    __tablename__ = 'profiles_v8'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform = Column(String)
    followers = Column(Integer)
    niche = Column(String)
    diagnosis = Column(Text)
    score_final = Column(Float)

engine = create_engine('sqlite:///v8_competence.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# --- ESTÉTICA DO SISTEMA ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000; color: #fff; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; }
    .stButton>button { background: linear-gradient(135deg, #d4af37, #aa841e); color: black; font-weight: bold; width: 100%; border: none; }
    .report-card { background: #111; padding: 20px; border-left: 8px solid #d4af37; border-radius: 10px; margin: 15px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE DE COMANDO ---
st.title("🛡️ V8 SOCIAL COMPETENCE ANALYZER")
st.subheader("Auditoria Crítica e Severa de Maturidade Digital")

with st.sidebar:
    st.header("📌 Cadastro de Perfil")
    name = st.text_input("Nome do Perfil")
    platform_options = ["Instagram", "LinkedIn", "TikTok", "YouTube", "Twitter", "Facebook", "OUTROS"]
    platform_sel = st.selectbox("Plataforma Principal", platform_options)
    
    # Campo "OUTROS" obrigatório conforme protocolo
    platform = st.text_input("Especifique a rede (Obrigatório para 'OUTROS')") if platform_sel == "OUTROS" else platform_sel
    
    followers = st.number_input("Volume de Seguidores", min_value=0)
    niche = st.text_input("Nicho de Atuação")
    freq = st.selectbox("Frequência de Postagem", ["Nula", "Inconsistente", "3x/Semana", "Diária"])
    objective = st.text_area("Objetivo Estratégico")

st.markdown("### ⚡ Teste Estruturado de Competência (0 a 10)")
c1, c2, c3, c4 = st.columns(4)
with c1:
    s_comm = st.slider("Comunicação", 0, 10, 5)
    s_auth = st.slider("Autoridade", 0, 10, 5)
with c2:
    s_clarity = st.slider("Clareza", 0, 10, 5)
    s_pos = st.slider("Posicionamento", 0, 10, 5)
with c3:
    s_strat = st.slider("Estratégia", 0, 10, 5)
    s_tech = st.slider("Técnica", 0, 10, 5)
with c4:
    s_eng = st.slider("Engajamento", 0, 10, 5)
    s_consist = st.slider("Consistência", 0, 10, 5)

# --- MOTOR DE ANÁLISE CRÍTICA ---
if st.button("EXECUTAR PROTOCOLO DE AUDITORIA V8"):
    scores = [s_comm, s_auth, s_clarity, s_pos, s_strat, s_tech, s_eng, s_consist]
    avg = sum(scores) / len(scores)
    
    # Identificação de Lacunas (Notas abaixo de 6)
    lacunas = []
    labels = ["Comunicação", "Autoridade", "Clareza", "Posicionamento", "Estratégia", "Técnica", "Engajamento", "Consistência"]
    for i, s in enumerate(scores):
        if s < 6: lacunas.append(labels[i])

    # Classificação Severa
    if avg < 4: status = "FRACO"
    elif avg < 6: status = "INCONSISTENTE"
    elif avg < 8: status = "PROMISSOR"
    elif avg < 9.5: status = "ESTRATÉGICO"
    else: status = "AUTORIDADE CONSOLIDADA"

    st.markdown("---")
    st.markdown(f"<div class='report-card'><h2>CLASSIFICAÇÃO: {status}</h2>", unsafe_allow_html=True)
    st.metric("Score de Maturidade Digital", f"{avg:.2f}")

    st.markdown("### 🛑 Diagnóstico Técnico e Severo")
    if lacunas:
        st.error(f"FALHA ESTRUTURAL: Lacunas críticas detectadas em: {', '.join(lacunas).upper()}.")
    
    # Mensagens de impacto baseadas na média
    if avg < 6:
        st.warning("Diagnóstico: Perfil operando em regime de amadorismo. Risco alto de estagnação e perda de autoridade no mercado jurídico.")
    else:
        st.success("Diagnóstico: Estrutura funcional, mas requer refinamento técnico para atingir o nível God Mode.")

    st.markdown("### 🛠️ Plano de Melhoria Automático")
    for item in lacunas:
        st.info(f"Ação Corretiva [{item}]: Aplicar protocolo de reforço técnico imediatamente para mitigar a inconsistência.")
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Gravação no Banco de Dados
    session = Session()
    new_profile = ProfileV8(
        name=name, platform=platform, followers=followers, 
        niche=niche, diagnosis=status, score_final=avg
    )
    session.add(new_profile)
    session.commit()
    session.close()
    st.toast("Dados arquivados no banco de dados SQLite.")
