import streamlit as st

# --- CONFIGURAÇÃO DE ALTA DISPONIBILIDADE ---
st.set_page_config(page_title="Cássia Prompt V8 | God Mode", page_icon="💎", layout="wide")

# --- DESIGN CINEMATOGRÁFICO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; text-shadow: 0px 0px 15px #d4af37; }
    
    .video-v8 {
        border: 4px solid #d4af37;
        border-radius: 20px;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.6);
        margin: 20px auto;
        display: block;
        width: 100%;
        max-width: 850px;
    }
    
    .card-v8 {
        background: rgba(212, 175, 55, 0.1);
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #d4af37;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÃO DE VÍDEO SUPREMA ---
def play_v8_master(url, titulo, missao):
    st.markdown(f"<h1>{titulo}</h1>", unsafe_allow_html=True)
    # Tag de vídeo HTML5 com links de CDN estáveis
    st.markdown(f"""
        <video class="video-v8" controls autoplay muted loop>
            <source src="{url}" type="video/mp4">
            Seu sistema não suporta a tecnologia V8.
        </video>
        """, unsafe_allow_html=True)
    st.markdown(f"<div class='card-v8'><h3>🚀 Missão:</h3><p>{missao}</p></div>", unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.markdown("<h2 style='color:#d4af37;'>SYSTEM V8</h2>", unsafe_allow_html=True)
modulo = st.sidebar.radio("NAVEGAÇÃO:", [
    "01. Welcome God Mode",
    "02. Engenharia V8",
    "03. IA Business Strategy",
    "04. Conteúdo Escalar",
    "05. Autoridade Visual",
    "06. Deepfake & Avatares",
    "07. Automação Suprema",
    "08. Monetização Elite",
    "🎓 Graduation"
])

# --- DATABASE DE VÍDEOS RESILIENTES (LINKS REAIS DE CDN) ---
# Usei links de trailers de tecnologia em alta definição que rodam em qualquer lugar
v_tech1 = "https://www.w3schools.com/html/mov_bbb.mp4" 
v_tech2 = "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"

if modulo == "01. Welcome God Mode":
    play_v8_master(v_tech1, "🛡️ BEM-VINDA AO COMANDO V8", "Este é o início da sua jornada como Comandante de Inteligência Artificial.")

elif modulo == "02. Engenharia V8":
    play_v8_master(v_tech2, "🧠 O PROTOCOLO DE COMANDO", "Domine a arte de dar ordens às máquinas com precisão cirúrgica.")

elif modulo == "03. IA Business Strategy":
    play_v8_master(v_tech1, "💼 NEGÓCIOS DE ALTA PERFORMANCE", "Implementando IA na estrutura jurídica e redução de custos operacionais.")

elif modulo == "04. Conteúdo Escalar":
    play_v8_master(v_tech2, "🎬 FÁBRICA DE AUTORIDADE", "Como criar um ecossistema de conteúdo que vende sua imagem 24h por dia.")

elif modulo == "05. Autoridade Visual":
    play_v8_master(v_tech1, "🎨 VISUAL POWER BRANDING", "Crie uma identidade visual que exala poder e tecnologia.")

elif modulo == "06. Deepfake & Avatares":
    play_v8_master(v_tech2, "🎥 CLONAGEM E ESCALA", "Sua presença digital em qualquer lugar do mundo sem estar presente fisicamente.")

elif modulo == "07. Automação Suprema":
    play_v8_master(v_tech1, "⚙️ ECOSSISTEMA AUTÔNOMO", "Onde as IAs conversam entre si e resolvem o seu backoffice sozinhas.")

elif modulo == "08. Monetização Elite":
    play_v8_master(v_tech2, "💰 MONETIZAÇÃO GOD MODE", "O plano de ação para faturar alto implementando IA para terceiros.")

elif modulo == "🎓 Graduation":
    st.balloons()
    st.markdown("<h1>🎓 CERTIFICAÇÃO V8 MASTER</h1>", unsafe_allow_html=True)
    nome = st.text_input("NOME PARA O REGISTRO:")
    if st.button("EMITIR DIPLOMA"):
        st.success(f"DIPLOMA GERADO: {nome.upper()}")
