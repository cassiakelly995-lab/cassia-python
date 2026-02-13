import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="Cássia Prompt V8 - Elite IA", page_icon="💎", layout="wide")

# --- DESIGN PREMIUM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #000000; color: #FFFFFF; }
    .stVideo { border: 3px solid #d4af37; border-radius: 15px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; }
    div.stButton > button { width: 100%; background: #d4af37; color: black; font-weight: bold; border-radius: 10px; }
    .card { background: #111; padding: 20px; border-radius: 10px; border-left: 5px solid #d4af37; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
st.sidebar.title("💎 CÁSSIA PROMPT V8")
modulo = st.sidebar.selectbox("ESCOLHA SUA JORNADA:", [
    "01. Boas-vindas & Mentalidade",
    "02. Engenharia V8 God Mode",
    "03. IA para Negócios Reais",
    "04. Conteúdo Infinito 10X",
    "05. Identidade Visual de Poder",
    "06. Vídeos e Avatares IA",
    "07. Automação de Processos",
    "08. O Futuro e Monetização",
    "🎓 Certificação Final"
])

# --- CONTEÚDO ---
if modulo == "01. Boas-vindas & Mentalidade":
    st.title("🚀 Boas-vindas à Revolução V8")
    st.video("https://www.youtube.com/watch?v=5V9X-CByhYw")
    st.markdown('<div class="card"><h3>Atividade 01</h3>Imagine que a IA é um estagiário gênios. Liste 3 tarefas chatas que você nunca mais quer fazer na vida.</div>', unsafe_allow_html=True)

elif modulo == "02. Engenharia V8 God Mode":
    st.title("🧠 O Protocolo V8 de Comandos")
    st.video("https://www.youtube.com/watch?v=0_fN_7P11i8")
    st.markdown("""
    ### A Fórmula Secreta:
    **[PERSONA] + [CONTEXTO] + [TAREFA] + [FORMATO]**
    * **Atividade:** Escreva seu primeiro prompt V8 abaixo.
    """)
    st.text_area("Digite seu comando aqui:")

elif modulo == "03. IA para Negócios Reais":
    st.title("💼 IA no Mundo dos Negócios")
    st.video("https://www.youtube.com/watch?v=m7H09-l-H4U")
    st.markdown('<div class="card">Como economizar 20 horas por semana usando automação de emails e documentos.</div>', unsafe_allow_html=True)

elif modulo == "04. Conteúdo Infinito 10X":
    st.title("🎬 Criando Conteúdo em Massa")
    st.video("https://www.youtube.com/watch?v=A_G3lO_AFeM")
    st.write("Aprenda a criar 1 mês de conteúdo em apenas 15 minutos.")

elif modulo == "05. Identidade Visual de Poder":
    st.title("🎨 Visual de Autoridade")
    st.video("https://www.youtube.com/watch?v=f-N9m1w0w_M")
    st.write("Crie imagens cinematográficas para suas redes sociais sem gastar 1 real.")

elif modulo == "06. Vídeos e Avatares IA":
    st.title("🎥 Avatares Digitais")
    st.video("https://www.youtube.com/watch?v=y7X6A8E19jM")
    st.write("Sua imagem e voz clonadas para trabalhar 24h por você.")

elif modulo == "07. Automação de Processos":
    st.title("⚙️ O Robô que Trabalha")
    st.video("https://www.youtube.com/watch?v=K3SAnF_uT_k")
    st.write("Conectando ferramentas para criar fluxos de trabalho automáticos.")

elif modulo == "08. O Futuro e Monetização":
    st.title("💰 Como Ganhar Dinheiro com IA")
    st.video("https://www.youtube.com/watch?v=S_O58NfLshI")
    st.markdown('<div class="card">Venda consultoria de IA por R$ 5.000 ou mais por cliente.</div>', unsafe_allow_html=True)

elif modulo == "🎓 Certificação Final":
    st.title("🎓 Diploma de Elite")
    nome = st.text_input("NOME PARA O CERTIFICADO:")
    if st.button("GERAR MEU CERTIFICADO"):
        st.balloons()
        st.success(f"Parabéns, {nome}! Você concluiu o curso de tecnologia mais completo do mercado.")
