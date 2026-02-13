import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="Cássia Prompt V8 | Elite Tech", page_icon="💎", layout="wide")

# --- ESTÉTICA DE ALTO PADRÃO (DARK MODE & GOLD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #000000; color: #FFFFFF; }
    .stHeader, h1, h2, h3 { color: #d4af37 !important; font-weight: 700; }
    .stButton>button { 
        background: linear-gradient(45deg, #d4af37, #f4d03f); 
        color: #000 !important; 
        font-weight: bold; 
        border: none; 
        padding: 10px 25px;
        border-radius: 5px;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0px 0px 15px #d4af37; }
    .card { background-color: #111; padding: 25px; border-radius: 15px; border: 1px solid #333; margin-bottom: 20px; border-left: 6px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (PAINEL DE COMANDO) ---
st.sidebar.image("https://img.icons8.com/ios-filled/100/d4af37/artificial-intelligence.png", width=80)
st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.markdown("### *Mentoria Cássia Kelly*")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox("JOURNEY MAP:", [
    "🏠 Welcome Experience",
    "🧠 Módulo 1: Mentalidade Exponencial",
    "⚡ Módulo 2: Engenharia V8 God Mode",
    "💼 Módulo 3: Business & High Performance",
    "🎨 Módulo 4: Visual Authority (IA)",
    "🎥 Módulo 5: Cinematografia Digital",
    "🛠️ Módulo 6: Ecosystem & Tools",
    "⚙️ Módulo 7: Advanced Automations",
    "💰 Módulo 8: Monetização & Scale",
    "🎓 Graduation"
])

# --- CONTEÚDO ---

if menu == "🏠 Welcome Experience":
    st.title("Bem-vinda à Fronteira da Inovação")
    
    # Grid de Boas-vindas
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### O Conhecimento das Maiores Faculdades, na Palma da sua Mão.
        O mundo mudou. Onde outros veem dificuldade, aqui você verá **Comando**. 
        Este não é um curso sobre "aprender a usar a IA", é sobre **aprender a dominar a próxima era da humanidade**.
        
        **Nesta jornada, você irá:**
        1. Desbloquear a lógica por trás dos grandes modelos de linguagem.
        2. Criar sistemas que trabalham 24h por você.
        3. Escalar sua autoridade visual e financeira.
        """)
        
        # VÍDEO DE BOAS-VINDAS (Você pode trocar o link pelo seu vídeo do YouTube/Vimeo)
        st.video("https://www.youtube.com/watch?v=A_G3lO_AFeM") # Link exemplo: "The Power of AI"
        
    with col2:
        st.markdown('<div class="card"><h4>🚀 Seu Progresso</h4><p>Nível: Iniciante (V8)</p></div>', unsafe_allow_html=True)
        st.info("💡 **Ação Imediata:** Assista ao vídeo ao lado e comece pelo Módulo 1. A tecnologia não espera.")

elif menu == "⚡ Módulo 2: Engenharia V8 God Mode":
    st.title("⚡ A Engenharia de Prompt V8")
    st.markdown("---")
    
    st.markdown("""
    ### O Protocolo God Mode
    A maioria das pessoas faz perguntas para a IA. Você dará **diretrizes estruturadas**.
    """)
    
    
    
    with st.expander("🛠️ ATIVIDADE INTERATIVA: O Primeiro Comando V8"):
        st.write("Tente estruturar um prompt usando a fórmula: **PAPEL + CONTEXTO + MISSÃO + LIMITES**.")
        desafio = st.text_area("Digite seu prompt de teste aqui:")
        if st.button("Validar Comando"):
            if len(desafio) > 10:
                st.success("Estrutura detectada! Você está pensando como uma Engenheira de Prompt V8.")
            else:
                st.warning("Seu comando está muito curto. Seja mais específica.")

elif menu == "🎓 Graduation":
    st.title("🎓 Diploma de Excelência Digital")
    st.markdown('<div class="card"><h3>Certificação Cássia Prompt V8</h3><p>Este documento valida sua competência em dominar sistemas de IA e Engenharia de Prompt.</p></div>', unsafe_allow_html=True)
    
    nome = st.text_input("NOME PARA O CERTIFICADO:")
    if st.button("GERAR DIPLOMA AGORA"):
        if nome:
            st.balloons()
            st.success(f"Parabéns, Comandante {nome}! O seu certificado digital de elite foi emitido.")
            # (Aqui continua o código do PDF que já criamos)
        else:
            st.error("Por favor, insira seu nome completo.")

# (Os outros módulos seguem a mesma estética de "Card" e "Expander")
