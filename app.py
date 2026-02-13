import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURAÇÃO DE ALTO PADRÃO ---
st.set_page_config(page_title="Cássia Prompt V8 - Elite", page_icon="💎", layout="wide")

# --- ESTÉTICA PREMIUM (BLACK & GOLD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #000000; color: #FFFFFF; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-weight: 700; }
    .stVideo { border: 3px solid #d4af37; border-radius: 15px; box-shadow: 0px 0px 20px rgba(212,175,55,0.4); }
    .card-aula { background: #111; padding: 25px; border-radius: 15px; border-left: 8px solid #d4af37; margin-bottom: 25px; }
    div.stButton > button { width: 100%; background: linear-gradient(45deg, #d4af37, #f4d03f); color: black !important; font-weight: bold; height: 50px; border-radius: 10px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.markdown("<h1 style='text-align: center;'>💎 CÁSSIA PROMPT</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>V8 God Mode Edition</p>", unsafe_allow_html=True)

modulo = st.sidebar.selectbox("ESCOLHA O MÓDULO:", [
    "00. Welcome Experience",
    "01. Mentalidade Exponencial",
    "02. Engenharia de Prompt V8",
    "03. IA para Negócios",
    "04. Conteúdo Escalar 10X",
    "05. Autoridade Visual",
    "06. Vídeos e Avatares",
    "07. Automação de Processos",
    "08. Monetização e Escala",
    "🎓 Certificação Final"
])

# --- CONTEÚDO DOS MÓDULOS ---

if modulo == "00. Welcome Experience":
    st.title("🛡️ BEM-VINDA À FRONTEIRA DA TECNOLOGIA")
    st.video("https://www.youtube.com/watch?v=A_G3lO_AFeM") # Vídeo Institucional IA
    st.markdown('<div class="card-aula"><h3>Boas-vindas, Comandante!</h3>Este é o início da sua jornada. Aqui você deixa de ser usuária para se tornar Mestra da Inteligência Artificial. Assista ao vídeo acima para entender o poder do que você tem em mãos.</div>', unsafe_allow_html=True)

elif modulo == "01. Mentalidade Exponencial":
    st.title("🚀 Módulo 1: O Fim do Trabalho Linear")
    st.video("https://www.youtube.com/watch?v=m7H09-l-H4U")
    st.markdown('<div class="card-aula">Nesta aula, quebramos as crenças limitantes. A IA não é uma ferramenta de pesquisa, é um motor de execução que economiza 90% do seu tempo de escritório.</div>', unsafe_allow_html=True)

elif modulo == "02. Engenharia de Prompt V8":
    st.title("🧠 Módulo 2: O Protocolo God Mode V8")
    st.video("https://www.youtube.com/watch?v=0_fN_7P11i8")
    st.markdown('<div class="card-aula"><b>Método V8:</b><br>1. Persona de Elite<br>2. Contexto Cirúrgico<br>3. Objetivo Atômico<br>4. Restrição de Saída.</div>', unsafe_allow_html=True)
    st.text_area("Desafio Prático: Escreva um comando V8 aqui:")

elif modulo == "03. IA para Negócios":
    st.title("💼 Módulo 3: Business Strategy")
    st.video("https://www.youtube.com/watch?v=K3SAnF_uT_k")
    st.write("Aprenda a analisar contratos, criar planos de negócios e otimizar o atendimento ao cliente.")

elif modulo == "04. Conteúdo Escalar 10X":
    st.title("🎬 Módulo 4: Fábrica de Conteúdo")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.write("Como gerar 30 dias de posts estratégicos em 15 minutos de comando.")

elif modulo == "05. Autoridade Visual":
    st.title("🎨 Módulo 5: Identidade de Poder")
    st.video("https://www.youtube.com/watch?v=f-N9m1w0w_M")
    st.write("Fotos profissionais e artes cinematográficas usando apenas texto.")

elif modulo == "06. Vídeos e Avatares":
    st.title("🎥 Módulo 6: Clonagem Digital")
    st.video("https://www.youtube.com/watch?v=y7X6A8E19jM")
    st.write("Sua voz e imagem trabalhando 24h por dia através de avatares de IA.")

elif modulo == "07. Automação de Processos":
    st.title("⚙️ Módulo 7: Robôs de Trabalho")
    st.video("https://www.youtube.com/watch?v=0_fN_7P11i8")
    st.write("Conectando ferramentas para que o trabalho aconteça sem a sua intervenção.")

elif modulo == "08. Monetização e Escala":
    st.title("💰 Módulo 8: Lucro Real com IA")
    st.video("https://www.youtube.com/watch?v=S_O58NfLshI")
    st.markdown('<div class="card-aula">Como cobrar caro por consultoria de IA e criar produtos digitais que vendem no automático.</div>', unsafe_allow_html=True)

elif modulo == "🎓 Certificação Final":
    st.title("🎓 DIPLOMA DE EXCELÊNCIA")
    nome = st.text_input("NOME COMPLETO DO FORMANDO:")
    if st.button("GERAR CERTIFICADO"):
        st.balloons()
        st.success(f"Parabéns, {nome}! Você é oficialmente uma Especialista Cássia Prompt V8.")
