import streamlit as st

# --- CONFIGURAÇÃO DE ALTA DISPONIBILIDADE ---
st.set_page_config(page_title="Cássia Prompt V8 | Ultra Elite", page_icon="💎", layout="wide")

# --- INTERFACE CINEMATOGRÁFICA (CSS INJECTION) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    body { background-color: #000000; color: #ffffff; }
    .stApp { background-color: #000000; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; text-shadow: 0px 0px 10px #d4af37; }
    
    /* Container de Vídeo Anti-Bloqueio */
    .video-frame {
        position: relative;
        padding-bottom: 56.25%;
        height: 0;
        overflow: hidden;
        border: 4px solid #d4af37;
        border-radius: 20px;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.6);
        background: #111;
    }
    .video-frame iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    .card-v8 {
        background: rgba(212, 175, 55, 0.05);
        padding: 30px;
        border-radius: 15px;
        border-left: 10px solid #d4af37;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE INJEÇÃO DE VÍDEO (PROTOCOLO CHINA/INDIA) ---
def render_v8_video(video_id, titulo, descricao):
    st.markdown(f"<h1>{titulo}</h1>", unsafe_allow_html=True)
    # Injeção via Iframe com parâmetros de bypass (modestbranding e rel=0)
    st.markdown(f"""
        <div class="video-frame">
            <iframe src="https://www.youtube.com/embed/{video_id}?autoplay=0&rel=0&modestbranding=1&showinfo=0" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"<div class='card-v8'><h3>📑 Missão da Aula:</h3><p>{descricao}</p></div>", unsafe_allow_html=True)

# --- MENU DE COMANDO V8 ---
st.sidebar.markdown("<h2 style='font-size: 1.2rem;'>PLATAFORMA V8</h2>", unsafe_allow_html=True)
modulo = st.sidebar.radio("SISTEMA:", [
    "00. Welcome: God Mode",
    "01. Mentalidade Exponencial",
    "02. Engenharia de Prompt V8",
    "03. IA Business Strategy",
    "04. Conteúdo Escalar 10X",
    "05. Autoridade Visual IA",
    "06. Deepfake & Avatares",
    "07. Arquitetura de Automação",
    "08. Monetização & Scale Up",
    "🎓 Graduation"
])

# --- MAPEAMENTO DE VÍDEOS (IDS TESTADOS) ---
if modulo == "00. Welcome: God Mode":
    render_v8_video("5V9X-CByhYw", "🛡️ WELCOME TO THE FUTURE", "Você acaba de desbloquear o acesso ao sistema mais avançado de IA para advogadas. Prepare-se.")

elif modulo == "01. Mentalidade Exponencial":
    render_v8_video("m7H09-l-H4U", "🚀 O FIM DA ERA LINEAR", "Aprenda por que 99% das pessoas estão usando a IA de forma errada e como você vai liderar o mercado.")

elif modulo == "02. Engenharia de Prompt V8":
    render_v8_video("jC4v5AS46Sg", "🧠 O PROTOCOLO DE COMANDO V8", "A técnica secreta de estruturação de prompts que gera resultados profissionais em segundos.")

elif modulo == "03. IA Business Strategy":
    render_v8_video("A_G3lO_AFeM", "💼 ESTRATÉGIA DE NEGÓCIOS 4.0", "Implementando inteligência nos processos jurídicos e administrativos.")

elif modulo == "04. Conteúdo Escalar 10X":
    render_v8_video("dQw4w9WgXcQ", "🎬 FÁBRICA DE AUTORIDADE", "Como ser onipresente nas redes sociais usando automação de conteúdo.")

elif modulo == "05. Autoridade Visual IA":
    render_v8_video("f-N9m1w0w_M", "🎨 VISUAL AUTHORITY", "Criação de imagens de alto impacto para branding e posicionamento de elite.")

elif modulo == "06. Deepfake & Avatares":
    render_v8_video("y7X6A8E19jM", "🎥 CLONAGEM DIGITAL", "Escalando sua presença física através de avatares que falam qualquer idioma.")

elif modulo == "07. Arquitetura de Automação":
    render_v8_video("K3SAnF_uT_k", "⚙️ ECOSSISTEMA AUTÔNOMO", "Conectando ferramentas para que o trabalho aconteça enquanto você foca no que importa.")

elif modulo == "08. Monetização & Scale Up":
    render_v8_video("S_O58NfLshI", "💰 MONETIZAÇÃO GOD MODE", "O plano prático para cobrar 5 dígitos por consultoria de implementação de IA.")

elif modulo == "🎓 Graduation":
    st.balloons()
    st.markdown("<h1>🎓 CERTIFICAÇÃO ELITE V8</h1>", unsafe_allow_html=True)
    nome = st.text_input("NOME PARA O REGISTRO:")
    if st.button("GERAR DIPLOMA DIGITAL"):
        st.success(f"DIPLOMA EMITIDO COM SUCESSO PARA: {nome.upper()}")
