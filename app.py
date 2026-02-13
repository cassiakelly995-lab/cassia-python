import streamlit as st

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="Cássia Prompt V8 | Elite", page_icon="💎", layout="wide")

# --- DESIGN BLACK & GOLD ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; }
    .video-v8 { border: 4px solid #d4af37; border-radius: 20px; box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.6); width: 100%; max-width: 850px; display: block; margin: auto; }
    .card-v8 { background: rgba(212, 175, 55, 0.1); padding: 25px; border-radius: 15px; border-left: 8px solid #d4af37; margin-top: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

def play_aula(url, titulo, missao):
    st.markdown(f"<h1>{titulo}</h1>", unsafe_allow_html=True)
    # Tag de vídeo HTML5 nativa com links MP4 puros de alta disponibilidade
    st.markdown(f'''
        <video class="video-v8" controls autoplay muted loop>
            <source src="{url}" type="video/mp4">
            Seu sistema não suporta a tecnologia V8.
        </video>
        ''', unsafe_allow_html=True)
    st.markdown(f"<div class='card-v8'><h3>🚀 Missão da Aula:</h3><p>{missao}</p></div>", unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.markdown("<h2 style='color:#d4af37;'>SYSTEM V8</h2>", unsafe_allow_html=True)
modulo = st.sidebar.radio("MÓDULOS DE COMANDO:", [
    "01. Welcome God Mode", "02. Engenharia V8", "03. IA Business Strategy", 
    "04. Conteúdo Escalar", "05. Autoridade Visual", "06. Deepfake & Avatares", 
    "07. Automação Suprema", "08. Monetização Elite", "🎓 Graduation"
])

# --- DATABASE DE VÍDEOS SEGUROS (MP4 DIRETO - CDN) ---
# Vídeos de tecnologia, circuitos e dados (Sem direitos autorais impeditivos)
v_intro = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-circuit-board-1644-large.mp4"
v_ai = "https://assets.mixkit.co/videos/preview/mixkit-data-processing-in-a-server-room-41031-large.mp4"
v_business = "https://assets.mixkit.co/videos/preview/mixkit-top-view-of-a-keyboard-and-a-mouse-on-a-desk-43314-large.mp4"
v_content = "https://assets.mixkit.co/videos/preview/mixkit-selection-of-videos-on-a-digital-screen-40019-large.mp4"
v_visual = "https://assets.mixkit.co/videos/preview/mixkit-abstract-animation-of-gold-and-black-3d-shapes-48352-large.mp4"
v_automation = "https://assets.mixkit.co/videos/preview/mixkit-white-robot-arm-working-in-a-factory-40026-large.mp4"

if modulo == "01. Welcome God Mode":
    play_aula(v_intro, "🛡️ BEM-VINDA AO COMANDO V8", "O início da sua jornada rumo à liberdade digital e domínio total das IAs.")

elif modulo == "02. Engenharia V8":
    play_aula(v_ai, "🧠 O PROTOCOLO DE COMANDO", "Como estruturar o pensamento para extrair 100% de inteligência da máquina.")

elif modulo == "03. IA Business Strategy":
    play_aula(v_business, "💼 IA BUSINESS ARCHITECTURE", "Estratégias para advogadas reduzirem custos e triplicarem a produtividade.")

elif modulo == "04. Conteúdo Escalar":
    play_aula(v_content, "🎬 FÁBRICA DE AUTORIDADE", "Onipresença digital: como produzir conteúdo para um mês em um dia.")

elif modulo == "05. Autoridade Visual":
    play_aula(v_visual, "🎨 VISUAL POWER BRANDING", "A psicologia das imagens geradas por IA no posicionamento de luxo.")

elif modulo == "06. Deepfake & Avatares":
    play_aula(v_intro, "🎥 CLONAGEM E ESCALA", "Multiplicando sua presença física através de avatares digitais inteligentes.")

elif modulo == "07. Automação Suprema":
    play_aula(v_automation, "⚙️ ECOSSISTEMA AUTÔNOMO", "Conectando o cérebro da IA aos seus sistemas de trabalho diários.")

elif modulo == "08. Monetização Elite":
    play_aula(v_ai, "💰 MONETIZAÇÃO GOD MODE", "Como empacotar seu conhecimento e vender consultoria de IA para o mercado jurídico.")

elif modulo == "🎓 Graduation":
    st.balloons()
    st.markdown("<h1>🎓 CERTIFICAÇÃO V8 MASTER</h1>", unsafe_allow_html=True)
    nome = st.text_input("NOME PARA O REGISTRO:")
    if st.button("EMITIR DIPLOMA"):
        st.success(f"DIPLOMA GERADO COM SUCESSO: {nome.upper()}")
