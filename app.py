import streamlit as st

# --- CONFIGURAÇÃO DE ALTO IMPACTO ---
st.set_page_config(page_title="Cássia Prompt V8 | Ultra Elite", page_icon="💎", layout="wide")

# --- ESTÉTICA TECNOLÓGICA AVANÇADA ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;600&display=swap');
    
    .main { background-color: #000000; color: #ffffff; }
    h1, h2 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; letter-spacing: 3px; }
    
    /* Moldura de Vídeo Ultra-Resiliente */
    .video-container {
        border: 4px solid #d4af37;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.5);
        background: #111;
        margin: 20px auto;
        max-width: 900px;
    }
    
    .card-v8 {
        background: rgba(212, 175, 55, 0.07);
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #d4af37;
        margin-top: 20px;
        font-family: 'Inter', sans-serif;
    }
    
    /* Botão de Comando */
    div.stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #f4d03f 100%);
        color: #000 !important;
        font-weight: bold;
        border-radius: 10px;
        padding: 15px;
        border: none;
        width: 100%;
        font-family: 'Orbitron', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE VÍDEO NATIVO (BYPASS TOTAL) ---
def render_aula(url, titulo, missao):
    st.markdown(f"<h1>{titulo}</h1>", unsafe_allow_html=True)
    # Usando tag de vídeo nativa HTML5 para evitar bloqueios de terceiros
    st.markdown(f"""
        <div class="video-container">
            <video width="100%" height="auto" controls autoplay muted loop>
                <source src="{url}" type="video/mp4">
                Seu navegador não suporta vídeos de alta tecnologia.
            </video>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"<div class='card-v8'><h3>🚀 Missão da Aula:</h3><p>{missao}</p></div>", unsafe_allow_html=True)

# --- PAINEL DE COMANDO ---
st.sidebar.markdown("<h1 style='font-size: 1.5rem;'>SYSTEM V8</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")
modulo = st.sidebar.radio("NAVEGAÇÃO:", [
    "01. Welcome: A Nova Era",
    "02. Engenharia V8 God Mode",
    "03. IA Business Architecture",
    "04. Conteúdo Escalar 10X",
    "05. Autoridade Visual IA",
    "06. Deepfake & Avatares",
    "07. Automação de Processos",
    "08. Monetização & Scale",
    "🎓 Certificação"
])

# --- CONTEÚDO DE ALTA DENSIDADE ---
# Links de vídeo direto (Direct MP4) para garantir funcionamento
v1 = "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-circuit-board-1644-large.mp4"
v2 = "https://assets.mixkit.co/videos/preview/mixkit-data-processing-in-a-server-room-41031-large.mp4"

if modulo == "01. Welcome: A Nova Era":
    render_aula(v1, "🛡️ BEM-VINDA AO COMANDO V8", "O mundo das advogadas mudou. Aqui, você deixa de ser executora e passa a ser a arquiteta de sistemas inteligentes.")

elif modulo == "02. Engenharia V8 God Mode":
    render_aula(v2, "🧠 O PROTOCOLO DE COMANDO", "Domine a arte de dar ordens às máquinas. Não peça, comande com precisão cirúrgica.")
    with st.expander("🛠️ WORKSHOP DE PROMPT"):
        st.text_area("Digite seu comando God Mode:")
        st.button("EXECUTAR COMANDO NO SISTEMA")

elif modulo == "03. IA Business Architecture":
    render_aula(v1, "💼 NEGÓCIOS DE ALTA PERFORMANCE", "Implementando IA na estrutura jurídica para análise de contratos e redução de custos operacionais.")

elif modulo == "04. Conteúdo Escalar 10X":
    render_aula(v2, "🎬 FÁBRICA DE AUTORIDADE", "Como criar um ecossistema de conteúdo que vende sua imagem 24 horas por dia.")

elif modulo == "05. Autoridade Visual IA":
    render_aula(v1, "🎨 VISUAL POWER BRANDING", "Crie uma identidade visual que exala poder e tecnologia, superando qualquer estúdio tradicional.")

elif modulo == "06. Deepfake & Avatares":
    render_aula(v2, "🎥 CLONAGEM E ESCALA", "Sua presença digital em qualquer lugar do mundo, sem a necessidade da sua presença física.")

elif modulo == "07. Automação de Processos":
    render_aula(v1, "⚙️ ECOSSISTEMA AUTÔNOMO", "Onde as IAs conversam entre si e resolvem o seu backoffice sozinhas.")

elif modulo == "08. Monetização & Scale":
    render_aula(v2, "💰 MONETIZAÇÃO GOD MODE", "O plano de ação para faturar alto implementando essas tecnologias para outros profissionais.")

elif modulo == "🎓 Certificação":
    st.balloons()
    st.markdown("<h1>🎓 GRADUAÇÃO V8 MASTER</h1>", unsafe_allow_html=True)
    nome = st.text_input("NOME PARA O REGISTRO OFICIAL:")
    if st.button("EMITIR CERTIFICADO"):
        st.success(f"DIPLOMA REGISTRADO: {nome.upper()} AGORA É UMA ESPECIALISTA V8.")
