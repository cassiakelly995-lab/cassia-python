import streamlit as st

# --- CONFIGURAÇÃO SUPREMA ---
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
    st.markdown(f'<video class="video-v8" controls autoplay muted loop><source src="{url}" type="video/mp4"></video>', unsafe_allow_html=True)
    st.markdown(f"<div class='card-v8'><h3>🚀 Missão:</h3><p>{missao}</p></div>", unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.markdown("<h2 style='color:#d4af37;'>SYSTEM V8</h2>", unsafe_allow_html=True)
modulo = st.sidebar.radio("MÓDULOS:", [
    "01. Boas-vindas", "02. Engenharia V8", "03. IA Business", "04. Conteúdo 10X",
    "05. Visual Power", "06. Avatares", "07. Automação", "08. Monetização", "🎓 Graduation"
])

# --- LINKS DAS AULAS (Substitua pelos seus links MP4 diretos) ---
links = {
    "01": "LINK_DA_SUA_AULA_01.mp4",
    "02": "LINK_DA_SUA_AULA_02.mp4",
    "03": "LINK_DA_SUA_AULA_03.mp4",
    "04": "LINK_DA_SUA_AULA_04.mp4",
    "05": "LINK_DA_SUA_AULA_05.mp4",
    "06": "LINK_DA_SUA_AULA_06.mp4",
    "07": "LINK_DA_SUA_AULA_07.mp4",
    "08": "LINK_DA_SUA_AULA_08.mp4"
}

if modulo == "01. Boas-vindas":
    play_aula(links["01"], "🛡️ BEM-VINDA AO COMANDO V8", "Início da jornada de transformação digital jurídica.")
elif modulo == "02. Engenharia V8":
    play_aula(links["02"], "🧠 O PROTOCOLO DE COMANDO", "Domine a engenharia de prompt avançada.")
elif modulo == "03. IA Business":
    play_aula(links["03"], "💼 NEGÓCIOS DE ALTA PERFORMANCE", "IA na estrutura jurídica e redução de custos.")
elif modulo == "04. Conteúdo 10X":
    play_aula(links["04"], "🎬 FÁBRICA DE AUTORIDADE", "Produção escalar de conteúdo estratégico.")
elif modulo == "05. Visual Power":
    play_aula(links["05"], "🎨 VISUAL POWER BRANDING", "Identidade visual de autoridade com IA.")
elif modulo == "06. Avatares":
    play_aula(links["06"], "🎥 CLONAGEM E ESCALA", "Sua presença digital multiplicada por avatares.")
elif modulo == "07. Automação":
    play_aula(links["07"], "⚙️ ECOSSISTEMA AUTÔNOMO", "Processos que rodam sem sua intervenção.")
elif modulo == "08. Monetização":
    play_aula(links["08"], "💰 MONETIZAÇÃO ELITE", "Como cobrar caro por consultoria de IA.")
elif modulo == "🎓 Graduation":
    st.balloons()
    st.markdown("<h1>🎓 CERTIFICAÇÃO V8 MASTER</h1>", unsafe_allow_html=True)
    nome = st.text_input("NOME PARA O REGISTRO:")
    if st.button("EMITIR DIPLOMA"):
        st.success(f"DIPLOMA GERADO: {nome.upper()}")
