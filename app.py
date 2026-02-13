import streamlit as st
from fpdf import FPDF
import datetime

st.set_page_config(page_title="Cássia Prompt V8 - Premium", page_icon="💎", layout="wide")

# Estética Black & Gold
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stSelectbox label, .stHeader, h1, h2, h3 { color: #d4af37 !important; }
    div.stButton > button:first-child { background-color: #d4af37; color: black; border-radius: 8px; font-weight: bold; }
    .stExpander { background-color: #1a1a1a; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.write("Comandante: **Cássia Kelly**")

modulo = st.sidebar.selectbox("ESCOLHA O MÓDULO:", [
    "🏠 Boas-vindas",
    "🧠 Módulo 1: O Cérebro da IA (Prompts)",
    "💼 Módulo 2: IA na Carreira e Negócios",
    "🎨 Módulo 3: Criação de Imagens e Identidade",
    "🎬 Módulo 4: Vídeos e Avatares com IA",
    "⚙️ Módulo 5: Automações e Robôs",
    "🎓 Gerar Certificado Final"
])

if modulo == "🏠 Boas-vindas":
    st.title("Seja bem-vindo ao Futuro!")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Exemplo de onde você pode por seus vídeos
    st.markdown("Neste curso, você vai dominar a ferramenta que está mudando o mundo.")

elif modulo == "🧠 Módulo 1: O Cérebro da IA (Prompts)":
    st.title("🧠 Engenharia de Prompt Reversa")
    with st.expander("Aula 1.1: O Comandante"):
        st.write("Aqui você aprende a dar ordens complexas...")
    with st.expander("Aula 1.2: Estrutura de Prompt de Ouro"):
        st.write("A fórmula secreta: Persona + Contexto + Ação + Restrição.")
    
    # Exemplo de Botão de PDF
    st.info("📚 Material de Apoio")
    st.markdown("*(Para PDF, suba o arquivo no GitHub e me peça o link!)*")

elif modulo == "🎓 Gerar Certificado Final":
    st.title("🎓 Sua Conquista Profissional")
    nome = st.text_input("Nome completo:")
    if st.button("Emitir Diploma"):
        # (Código do PDF que você já testou e funcionou)
        st.success("Certificado Gerado!")
