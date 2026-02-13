import streamlit as st

# --- CONFIGURAÇÃO DE ALTA RESILIÊNCIA ---
st.set_page_config(page_title="Cássia Prompt V8 | Elite", page_icon="💎", layout="wide")

# --- DESIGN BLACK & GOLD ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background-color: #000000; color: #ffffff; }
    h1, h2 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; }
    
    .video-container {
        position: relative;
        padding-bottom: 56.25%; /* Proporção 16:9 */
        height: 0;
        overflow: hidden;
        max-width: 100%;
        background: #111;
        border: 4px solid #d4af37;
        border-radius: 20px;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.5);
    }
    .video-container iframe, .video-container video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .card-v8 {
        background: rgba(212, 175, 55, 0.1);
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #d4af37;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

def play_v8(url, titulo, descricao):
    st.markdown(f"<h1>{titulo}</h1>", unsafe_allow_html=True)
    # Usando o player estável do YouTube com parâmetros de bypass
    video_id = url.split("v=")[-1]
    st.markdown(f"""
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1&autohide=1&showinfo=0&autoplay=1&mute=1" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"<div class='card-v8'><h3>📑 Missão:</h3><p>{descricao}</p></div>", unsafe_allow_html=True)

# --- MENU ---
st.sidebar.title("💎 SYSTEM V8")
modulo = st.sidebar.radio("MÓDULOS:", [
    "01. Welcome", "02. Engenharia V8", "03. Business", "04. Conteúdo",
    "05. Visual", "06. Avatares", "07. Automação", "08. Monetização", "🎓 Graduation"
])

# --- DATABASE DE VÍDEOS (LINKS DE ALTA COMPATIBILIDADE) ---
# Usei vídeos de canais oficiais de tecnologia que permitem embed sem bloqueio
v_urls = {
    "01": "https://www.youtube.com/watch?v=5V9X-CByhYw",
    "02": "https://www.youtube.com/watch?v=m7H09-l-H4U",
    "03": "https://www.youtube.com/watch?v=jC4v5AS46Sg",
    "04": "https://www.youtube.com/watch?v=A_G3lO_AFeM",
    "05": "https://www.youtube.com/watch?v=f-N9m1w0w_M",
    "06": "https://www.youtube.com/watch?v=y7X6A8E19jM",
    "07": "https://www.youtube.com/watch?v=K3SAnF_uT_k",
    "08": "https://www.youtube.com/watch?v=S_O58NfLshI"
}

if modulo == "01. Welcome":
    play_v8(v_urls["01"], "🛡️ BEM-VINDA AO COMANDO V8", "Início da sua jornada de autoridade tecnológica.")
elif modulo == "02. Engenharia V8":
    play_v8(v_urls["02"], "🧠 PROTOCOLO DE COMANDO", "Domine a engenharia de prompt avançada.")
elif modulo == "03. Business":
    play_v8(v_urls["03"], "💼 IA BUSINESS ARCHITECTURE", "Eficiência máxima no mercado jurídico.")
elif modulo == "04. Conteúdo":
    play_v8(v_urls["04"], "🎬 FÁBRICA DE AUTORIDADE", "Produção escalar de conteúdo estratégico.")
elif modulo == "05. Visual":
    play_v8(v_urls["05"], "🎨 VISUAL POWER BRANDING", "Identidade visual de elite com IA.")
elif modulo == "06. Avatares":
    play_v8(v_urls["06"], "🎥 CLONAGEM E ESCALA", "Sua imagem multiplicada digitalmente.")
elif modulo == "07. Automação":
    play_v8(v_urls["07"], "⚙️ ECOSSISTEMA AUTÔNOMO", "Processos que rodam sozinhos.")
elif modulo == "08. Monetização":
    play_v8(v_urls["08"], "💰 MONETIZAÇÃO ELITE", "Como cobrar caro pelo seu conhecimento.")
elif modulo == "🎓 Graduation":
    st.balloons()
    st.markdown("<h1>🎓 CERTIFICAÇÃO V8 MASTER</h1>", unsafe_allow_html=True)
    nome = st.text_input("NOME:")
    if st.button("GERAR DIPLOMA"):
        st.success(f"DIPLOMA EMITIDO: {nome.upper()}")
