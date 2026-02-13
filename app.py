import streamlit as st
import datetime

# --- CONFIGURAÇÃO DE ELITE (V8 GOD MODE) ---
st.set_page_config(page_title="Cássia Prompt V8 | Elite Tech", page_icon="💎", layout="wide")

# --- DESIGN CINEMATOGRÁFICO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #000000; color: #ffffff; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; letter-spacing: 3px; }
    
    /* Moldura de Vídeo Premium */
    .stVideo { border: 4px solid #d4af37; border-radius: 20px; box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.5); }
    
    /* Cards de Conteúdo */
    .aula-card { background: rgba(255, 255, 255, 0.05); padding: 30px; border-radius: 15px; border-left: 10px solid #d4af37; margin: 20px 0; }
    
    /* Botão de Comando */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #d4af37 0%, #f4d03f 100%);
        color: #000 !important;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 20px;
        border-radius: 12px;
        border: none;
        box-shadow: 0px 5px 15px rgba(212, 175, 55, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- PAINEL LATERAL ---
st.sidebar.markdown("<h1 style='font-size: 1.5rem;'>SYSTEM V8</h1>", unsafe_allow_html=True)
st.sidebar.image("https://img.icons8.com/ios-filled/100/d4af37/artificial-intelligence.png", width=100)
st.sidebar.markdown("---")

modulo = st.sidebar.radio("NAVEGAÇÃO ESTRATÉGICA:", [
    "00. Welcome Experience",
    "01. Mentalidade Exponencial",
    "02. Engenharia de Prompt V8",
    "03. IA Business Strategy",
    "04. Conteúdo Escalar 10X",
    "05. Autoridade Visual IA",
    "06. Deepfake & Avatares",
    "07. Arquitetura de Automação",
    "08. Monetização & High-Ticket",
    "🎓 Graduation"
])

# --- CONTEÚDO DE ALTA DENSIDADE ---

if modulo == "00. Welcome Experience":
    st.title("🛡️ BEM-VINDA À ELITE TECH")
    # Vídeo direto de servidor estável
    st.video("https://www.youtube.com/watch?v=5V9X-CByhYw")
    st.markdown("""<div class='aula-card'>
    <h3>A Revolução Começa Agora</h3>
    <p>Esqueça tudo o que você sabe sobre cursos online. O <b>Cássia Prompt V8</b> é um ecossistema de comando. 
    Aqui, você não é aluna, você é a <b>Comandante</b> de uma frota de inteligências artificiais.</p>
    </div>""", unsafe_allow_html=True)

elif modulo == "01. Mentalidade Exponencial":
    st.title("🚀 Módulo 1: O Fim do Trabalho Humano Manual")
    st.video("https://www.youtube.com/watch?v=m7H09-l-H4U")
    st.markdown("""<div class='aula-card'>
    <b>O QUE VOCÊ VAI DOMINAR:</b><br>
    - Como delegar 90% do seu stress para algoritmos.<br>
    - A psicologia da produtividade 10x.<br>
    - Por que economizar papel é o primeiro passo para a fortuna digital.
    </div>""", unsafe_allow_html=True)

elif modulo == "02. Engenharia de Prompt V8":
    st.title("🧠 Módulo 2: Engenharia de Prompt V8")
    st.video("https://www.youtube.com/watch?v=jC4v5AS46Sg")
    st.markdown("""<div class='aula-card'>
    <b>PROTOCOLO GOD MODE:</b><br>
    1. <b>Persona:</b> Você não pergunta, você encarna um especialista.<br>
    2. <b>Variáveis:</b> Defina exatamente o tom, público e restrições.<br>
    3. <b>Iteração:</b> O comando nunca termina no primeiro Enter.
    </div>""", unsafe_allow_html=True)
    st.text_area("DIGITE SEU COMANDO V8 PARA TESTE:")
    st.button("VALIDAR COMANDO NO SISTEMA")

elif modulo == "03. IA Business Strategy":
    st.title("💼 Módulo 3: Business High Performance")
    st.video("https://www.youtube.com/watch?v=A_G3lO_AFeM")
    st.write("Como usar IAs para fazer análise SWOT, pesquisa de mercado e redação de contratos em segundos.")

elif modulo == "04. Conteúdo Escalar 10X":
    st.title("🎬 Módulo 4: Fábrica de Conteúdo Escalar")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.info("Atividade: Gere 30 ideias de posts agora usando o comando ensinado no vídeo.")

elif modulo == "05. Autoridade Visual IA":
    st.title("🎨 Módulo 5: Visual Authority")
    st.video("https://www.youtube.com/watch?v=f-N9m1w0w_M")
    st.write("Domine Midjourney e Leonardo AI para criar uma marca pessoal inesquecível.")

elif modulo == "06. Deepfake & Avatares":
    st.title("🎥 Módulo 6: Cinematografia Digital")
    st.video("https://www.youtube.com/watch?v=y7X6A8E19jM")
    st.write("Sua clonagem digital. Fale em 50 idiomas com seu rosto sem gravar vídeos novos.")

elif modulo == "07. Arquitetura de Automação":
    st.title("⚙️ Módulo 7: Ecossistema Autônomo")
    st.video("https://www.youtube.com/watch?v=K3SAnF_uT_k")
    st.write("Conectando o cérebro da IA às suas ferramentas de trabalho (E-mail, Agenda, WhatsApp).")

elif modulo == "08. Monetização & High-Ticket":
    st.title("💰 Módulo 8: Monetização V8")
    st.video("https://www.youtube.com/watch?v=S_O58NfLshI")
    st.markdown("""<div class='aula-card'>
    <b>O PLANO DE 10K:</b><br>
    - Como vender consultoria de implementação de IA para advogados e empresários.<br>
    - Criando seu primeiro produto digital de tecnologia.
    </div>""", unsafe_allow_html=True)

elif modulo == "🎓 Graduation":
    st.title("🎓 DIPLOMA DE EXCELÊNCIA DIGITAL")
    st.balloons()
    nome_final = st.text_input("NOME COMPLETO PARA O REGISTRO:")
    if st.button("EMITIR MEU CERTIFICADO"):
        st.success(f"PARABÉNS, {nome_final.upper()}! VOCÊ AGORA É UMA ESPECIALISTA V8.")
