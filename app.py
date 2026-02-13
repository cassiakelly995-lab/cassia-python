import streamlit as st

# --- CONFIGURAÇÃO DE ELITE (BYPASS TOTAL) ---
st.set_page_config(page_title="Cássia Prompt V8 | Elite", page_icon="💎", layout="wide")

# --- DESIGN ULTRA-MODERNO (BLACK & GOLD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #000; color: #fff; }
    .main { background-color: #000; }
    h1, h2 { color: #d4af37 !important; text-align: center; font-weight: 700; text-transform: uppercase; }
    
    /* Container de Vídeo com Tecnologia de Auto-Ajuste */
    .video-wrapper {
        position: relative;
        padding-bottom: 56.25%; /* 16:9 */
        height: 0;
        border: 3px solid #d4af37;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0px 0px 25px rgba(212, 175, 55, 0.5);
    }
    .video-wrapper iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .card-info {
        background: #111;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #d4af37;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÃO DE RENDERIZAÇÃO DE ELITE ---
def play_v8(url_video, titulo, texto):
    st.markdown(f"<h1>{titulo}</h1>", unsafe_allow_html=True)
    # Usando Iframe direto para garantir compatibilidade total
    st.markdown(f"""
        <div class="video-wrapper">
            <iframe src="{url_video}" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"<div class='card-info'><h3>📖 Conteúdo Estratégico</h3><p>{texto}</p></div>", unsafe_allow_html=True)

# --- MENU LATERAL DE COMANDO ---
st.sidebar.title("💎 CÁSSIA V8")
modulo = st.sidebar.radio("ACESSAR MÓDULO:", [
    "01. Welcome Experience",
    "02. Engenharia de Prompt V8",
    "03. IA Business Architecture",
    "04. Conteúdo Escalar 10X",
    "05. Autoridade Visual IA",
    "06. Deepfake & Avatares",
    "07. Automação de Processos",
    "08. Monetização & Scale",
    "🎓 Graduation"
])

# --- MAPEAMENTO DE VÍDEOS (LINKS DE ALTA DISPONIBILIDADE) ---
if modulo == "01. Welcome Experience":
    play_v8("https://player.vimeo.com/video/253982136", "🛡️ BEM-VINDA À ELITE TECH", "Este é o início da sua transformação. Aqui, você assume o controle das máquinas.")

elif modulo == "02. Engenharia de Prompt V8":
    play_v8("https://player.vimeo.com/video/110594344", "🧠 PROTOCOLO V8 GOD MODE", "Aprenda a estruturar comandos que nenhuma faculdade ensina. Persona + Contexto + Missão.")

elif modulo == "03. IA Business Architecture":
    play_v8("https://player.vimeo.com/video/110594344", "💼 ESTRATÉGIA DE NEGÓCIOS", "Implemente processos que rodam sozinhos e economizam 40 horas por mês.")

elif modulo == "04. Conteúdo Escalar 10X":
    play_v8("https://player.vimeo.com/video/253982136", "🎬 FÁBRICA DE AUTORIDADE", "Como criar autoridade digital infinita usando inteligência gerativa.")

elif modulo == "05. Autoridade Visual IA":
    play_v8("https://player.vimeo.com/video/110594344", "🎨 IDENTIDADE VISUAL", "Domine as ferramentas de criação de imagens que transmitem poder e confiança.")

elif modulo == "06. Deepfake & Avatares":
    play_v8("https://player.vimeo.com/video/253982136", "🎥 CLONAGEM DIGITAL", "Sua presença física escala sem que você precise estar na frente da câmera.")

elif modulo == "07. Automação de Processos":
    play_v8("https://player.vimeo.com/video/110594344", "⚙️ ECOSSISTEMA AUTÔNOMO", "Conecte todas as ferramentas e deixe os robôs trabalharem enquanto você dorme.")

elif modulo == "08. Monetização & Scale":
    play_v8("https://player.vimeo.com/video/253982136", "💰 MONETIZAÇÃO V8", "O plano de ação para cobrar caro por consultoria de implementação de IA.")

elif modulo == "🎓 Graduation":
    st.balloons()
    st.markdown("<h1>🎓 CERTIFICAÇÃO ELITE V8</h1>", unsafe_allow_html=True)
    nome = st.text_input("NOME PARA O CERTIFICADO:")
    if st.button("EMITIR DIPLOMA"):
        st.success(f"PARABÉNS, {nome.upper()}! VOCÊ É UMA ESPECIALISTA MASTER V8.")
