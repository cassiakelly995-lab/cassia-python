import streamlit as st
import datetime

# --- CONFIGURAÇÃO DE ALTA PERFORMANCE (V8 GOD MODE) ---
st.set_page_config(page_title="Cássia Prompt V8 | Elite Edition", page_icon="💎", layout="wide")

# --- DESIGN CUSTOMIZADO (LUXO DIGITAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #ffffff; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; letter-spacing: 2px; }
    .stVideo { border: 4px solid #d4af37; border-radius: 15px; box-shadow: 0px 0px 25px rgba(212, 175, 55, 0.4); }
    .aula-card { background: rgba(212, 175, 55, 0.05); padding: 30px; border-radius: 15px; border-left: 10px solid #d4af37; margin-bottom: 25px; }
    div.stButton > button { width: 100%; background: linear-gradient(135deg, #d4af37 0%, #aa841e 100%); color: black !important; font-weight: bold; border-radius: 8px; padding: 15px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO ESTRATÉGICA ---
st.sidebar.markdown("<h1 style='font-size: 1.5rem;'>SYSTEM V8</h1>", unsafe_allow_html=True)
modulo = st.sidebar.radio("ACESSAR MÓDULO:", [
    "🏠 Welcome: A Revolução",
    "🧠 01. Mentalidade Exponencial",
    "⚡ 02. Engenharia de Prompt V8",
    "💼 03. Business High Performance",
    "🎬 04. Conteúdo Escalar 10X",
    "🎨 05. Autoridade Visual IA",
    "🎥 06. Deepfake & Avatares",
    "⚙️ 07. Arquitetura de Automação",
    "💰 08. Monetização & High-Ticket",
    "🎓 Graduation"
])

# --- FUNÇÃO DE VÍDEO SEGURO ---
def aula_video(url, titulo, descricao):
    st.title(titulo)
    st.video(url)
    st.markdown(f"""<div class='aula-card'>
    <h3>Guia da Aula</h3>
    <p>{descricao}</p>
    <a href='{url}' target='_blank'><button style='width:100%; background:#d4af37; color:black; font-weight:bold; padding:10px; border-radius:5px; border:none; cursor:pointer;'>🔓 ABRIR AULA EM NOVA ABA (CASO O PLAYER NÃO CARREGUE)</button></a>
    </div>""", unsafe_allow_html=True)

# --- MAPEAMENTO DE CONTEÚDO ---
if modulo == "🏠 Welcome: A Revolução":
    aula_video("https://www.youtube.com/watch?v=5V9X-CByhYw", "🛡️ BEM-VINDA À ELITE TECH", "Você não é mais aluna, você é a Comandante. O Cássia Prompt V8 é seu ecossistema de poder.")

elif modulo == "🧠 01. Mentalidade Exponencial":
    aula_video("https://www.youtube.com/watch?v=m7H09-l-H4U", "🚀 O Fim do Trabalho Manual", "Aprenda por que o papel morreu e como a IA vai gerir 90% das suas tarefas burocráticas.")

elif modulo == "⚡ 02. Engenharia de Prompt V8":
    aula_video("https://www.youtube.com/watch?v=jC4v5AS46Sg", "🧠 Engenharia de Prompt V8", "O segredo do God Mode: Persona + Contexto + Missão + Restrição. Ative o comando absoluto.")

elif modulo == "💼 03. Business High Performance":
    aula_video("https://www.youtube.com/watch?v=A_G3lO_AFeM", "💼 IA nos Negócios", "Análise de contratos, petições e relatórios em segundos. Tecnologia a serviço da justiça.")

elif modulo == "🎬 04. Conteúdo Escalar 10X":
    aula_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "🎬 Fábrica de Conteúdo", "Como criar 30 dias de autoridade digital em 15 minutos de comando estratégico.")

elif modulo == "🎨 05. Autoridade Visual IA":
    aula_video("https://www.youtube.com/watch?v=f-N9m1w0w_M", "🎨 Identidade de Poder", "Criação de imagens cinematográficas e profissionais para uma marca pessoal inesquecível.")

elif modulo == "🎥 06. Deepfake & Avatares":
    aula_video("https://www.youtube.com/watch?v=y7X6A8E19jM", "🎥 Cinematografia Digital", "Sua imagem clonada falando 50 idiomas. Ganhe escala global sem precisar gravar novos vídeos.")

elif modulo == "⚙️ 07. Arquitetura de Automação":
    aula_video("https://www.youtube.com/watch?v=K3SAnF_uT_k", "⚙️ Ecossistema Autônomo", "O robô trabalha, você lucra. Conectando IAs ao seu fluxo de trabalho diário.")

elif modulo == "💰 08. Monetização & High-Ticket":
    aula_video("https://www.youtube.com/watch?v=S_O58NfLshI", "💰 Monetização God Mode", "Como cobrar R$ 10.000+ por consultoria de IA e escalar seu conhecimento tecnológico.")

elif modulo == "🎓 Graduation":
    st.title("🎓 DIPLOMA DE EXCELÊNCIA V8")
    st.balloons()
    nome = st.text_input("NOME COMPLETO PARA O REGISTRO:")
    if st.button("EMITIR CERTIFICADO DE ELITE"):
        st.success(f"PARABÉNS, {nome.upper()}! VOCÊ É UMA ESPECIALISTA GOD MODE.")
