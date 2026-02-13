import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURAÇÃO DE ALTA TECNOLOGIA ---
st.set_page_config(page_title="Cássia Prompt V8 - God Mode", page_icon="💎", layout="wide")

# --- DESIGN CUSTOMIZADO (LUXO DIGITAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #E0E0E0; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; letter-spacing: 2px; text-align: center; }
    
    .stVideo { border: 2px solid #d4af37; border-radius: 15px; box-shadow: 0px 0px 15px #d4af37; }
    
    /* Botão Estilo Tesla */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #d4af37 0%, #aa841e 100%);
        color: black !important;
        font-weight: bold;
        border: none;
        padding: 15px;
        border-radius: 8px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
st.sidebar.markdown("<h1 style='font-size: 1.2rem;'>CÁSSIA PROMPT V8</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")

modulo = st.sidebar.selectbox("ESCOLHA A AULA:", [
    "00. Início: Welcome Experience",
    "01. Mentalidade Exponencial",
    "02. Engenharia V8 God Mode",
    "03. IA Business Strategy",
    "04. Conteúdo Escalar 10X",
    "05. Autoridade Visual (IA)",
    "06. Deepfake & Avatares",
    "07. Arquitetura de Automação",
    "08. Monetização & High-Ticket",
    "🎓 Graduation Certificado"
])

# --- FUNÇÃO PARA EXIBIR VÍDEO ---
def exibir_video(url):
    st.video(url)

# --- CONTEÚDO DOS MÓDULOS ---

if modulo == "00. Início: Welcome Experience":
    st.title("🛡️ BEM-VINDA À ELITE DA TECNOLOGIA")
    st.markdown("### Assista ao vídeo de boas-vindas abaixo:")
    exibir_video("https://www.youtube.com/watch?v=5V9X-CByhYw")
    st.info("Este é o seu primeiro passo para dominar a IA com a Metodologia V8.")

elif modulo == "01. Mentalidade Exponencial":
    st.title("🚀 Módulo 1: O Fim da Era Linear")
    exibir_video("https://www.youtube.com/watch?v=m7H09-l-H4U")
    st.markdown("Nesta aula, exploramos por que a produtividade humana mudou para sempre.")

elif modulo == "02. Engenharia V8 God Mode":
    st.title("🧠 Módulo 2: O Protocolo V8")
    exibir_video("https://www.youtube.com/watch?v=0_fN_7P11i8")
    st.markdown("Aprenda a fórmula secreta de comando que as faculdades não ensinam.")

elif modulo == "03. IA Business Strategy":
    st.title("💼 Módulo 3: Estratégia de Negócios")
    exibir_video("https://www.youtube.com/watch?v=A_G3lO_AFeM")
    st.markdown("Como transformar a IA no seu funcionário mais produtivo e barato.")

elif modulo == "04. Conteúdo Escalar 10X":
    st.title("🎬 Módulo 4: Fábrica de Conteúdo")
    exibir_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.markdown("Domine a criação de postagens, roteiros e blogs em segundos.")

elif modulo == "05. Autoridade Visual (IA)":
    st.title("🎨 Módulo 5: Imagem e Poder")
    exibir_video("https://www.youtube.com/watch?v=f-N9m1w0w_M")
    st.markdown("Como criar fotos e artes que transmitem autoridade imediata.")

elif modulo == "06. Deepfake & Avatares":
    st.title("🎥 Módulo 6: Cinematografia Digital")
    exibir_video("https://www.youtube.com/watch?v=y7X6A8E19jM")
    st.markdown("Clonagem de voz e avatares digitais que falam por você.")

elif modulo == "07. Arquitetura de Automação":
    st.title("⚙️ Módulo 7: Ecossistema Autônomo")
    exibir_video("https://www.youtube.com/watch?v=K3SAnF_uT_k")
    st.markdown("Conectando ferramentas para trabalhar no piloto automático.")

elif modulo == "08. Monetização & High-Ticket":
    st.title("💰 Módulo 8: Lucro Real com IA")
    exibir_video("https://www.youtube.com/watch?v=S_O58NfLshI")
    st.markdown("O guia definitivo para vender consultoria e serviços de IA.")

elif modulo == "🎓 Graduation Certificado":
    st.title("🎓 DIPLOMA DE EXCELÊNCIA")
    st.markdown("Digite seu nome abaixo para gerar seu certificado oficial.")
    nome = st.text_input("NOME DO ALUNO:")
    if st.button("GERAR CERTIFICADO"):
        st.balloons()
        st.success(f"Parabéns {nome}! Você é agora uma Especialista V8.")
