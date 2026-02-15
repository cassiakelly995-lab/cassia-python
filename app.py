import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="V8 Social Auditor", page_icon="🛡️", layout="wide")

# --- BANCO DE DADOS ---
Base = declarative_base()
class Auditoria(Base):
    __tablename__ = 'v8_audits'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    rede = Column(String)
    score = Column(Float)
    status = Column(String)

engine = create_engine('sqlite:///v8_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# --- ESTILO V8 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000; color: #fff; }
    h1, h2 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; }
    .report-card { background: #111; padding: 25px; border-left: 8px solid #d4af37; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE ---
st.title("🛡️ V8 SOCIAL COMPETENCE")
st.subheader("SISTEMA DE ANÁLISE CRÍTICA")

with st.sidebar:
    st.header("CADASTRO")
    nome_perfil = st.text_input("Perfil")
    rede_sel = st.selectbox("Rede", ["Instagram", "LinkedIn", "TikTok", "OUTROS"])
    rede = st.text_input("Qual rede?") if rede_sel == "OUTROS" else rede_sel
    nicho = st.text_input("Nicho")

st.markdown("### ⚡ AVALIAÇÃO (0-10)")
c1, c2 = st.columns(2)
with c1:
    s1 = st.slider("Comunicação", 0, 10, 5)
    s2 = st.slider("Autoridade", 0, 10, 5)
with c2:
    s3 = st.slider("Posicionamento", 0, 10, 5)
    s4 = st.slider("Técnica", 0, 10, 5)

if st.button("EXECUTAR AUDITORIA SEVERA"):
    avg = (s1 + s2 + s3 + s4) / 4
    status = "FRACO" if avg < 5 else "INCONSISTENTE" if avg < 7 else "ELITE"
    
    st.markdown(f"<div class='report-card'><h2>RESULTADO: {status}</h2>", unsafe_allow_html=True)
    st.metric("Score V8", f"{avg:.2f}")
    
    if avg < 6:
        st.error("🛑 FALHA CRÍTICA DETECTADA: Desempenho abaixo do padrão V8.")
    
    # Salvar no Banco
    session = Session()
    session.add(Auditoria(nome=nome_perfil, rede=rede, score=avg, status=status))
    session.commit()
    session.close()
    st.toast("Relatório Salvo com Sucesso.")
