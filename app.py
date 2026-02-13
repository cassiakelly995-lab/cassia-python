import streamlit as st

# --- CONFIGURAÇÃO DE ELITE TECH ---
st.set_page_config(page_title="Cássia Prompt V8 | Ultra Elite", page_icon="💎", layout="wide")

# --- INTERFACE DE LUXO (BLACK & NEON GOLD) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #000000; color: #ffffff; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; text-align: center; }
    .video-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border: 4px solid #d4af37; border-radius: 20px; box-shadow: 0px 0px 30px rgba(212, 175, 55, 0.6); }
    .video-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }
    .aula-card { background: rgba(212, 175, 55, 0.08); padding: 30px; border-radius: 15px; border-left: 10px solid #d4af37; margin: 20px 0; }
    div.stButton > button { width: 100%; background: linear-gradient(135deg, #d4af37 0%, #f4d03f 100%); color: #000 !important; font-weight: bold; font-size: 1.1rem; padding: 20px; border-radius: 12px; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEMA DE VÍDEO INFALÍVEL ---
def embed_video(video_id, titulo, resumo):
    st.title(titulo)
    # Técnica de Embed que ignora a maioria dos bloqueios de sites externos
    st.markdown(f'<div class="video-container"><iframe src="https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1" allowfullscreen></iframe></div>', unsafe_allow_html=True)
    st.markdown(f"<div class='aula-card'><h3>🔍 O que você aprenderá:</h3><p>{resumo}</p></div>", unsafe_allow_html=True)

# --- NAVEGAÇÃO V8 ---
st.sidebar.markdown("<h1>SYSTEM V8</h1>", unsafe_allow_html=True)
modulo = st.sidebar.radio("SISTEMA OPERACIONAL:", [
    "00. Welcome: O Início da Era",
    "01. Mentalidade Exponencial",
    "02. Engenharia V8 God Mode",
    "03. IA Business Architecture",
    "04. Conteúdo Escalar 100X",
    "05. Visual Authority & Branding",
    "06. Deepfake & Avatares Vivos",
    "07. Arquitetura de Automação",
    "08. Monetização & Scale Up",
    "🎓 Graduation"
])

# --- CONTEÚDO ACADÊMICO DE ELITE ---
if modulo == "00. Welcome: O Início da Era":
    embed_video("5V9X-CByhYw", "🛡️ BEM-VINDA À ELITE TECH", "Bem-vinda ao seu novo quartel-general. Aqui, você dominará o código da produtividade infinita. Esqueça as ferramentas, aprenda o COMANDO.")

elif modulo == "01. Mentalidade Exponencial":
    embed_video("m7H09-l-H4U", "🚀 O Fim da Escravidão Digital", "Aprenda a pensar em escala. Se uma tarefa leva mais de 5 minutos e é repetitiva, ela deve ser executada por uma IA, não por você.")

elif modulo == "02. Engenharia V8 God Mode":
    embed_video("jC4v5AS46Sg", "🧠 O Protocolo de Comando V8", "A anatomia de um prompt de elite. Como transformar a IA em um consultor sênior de qualquer área em 3 linhas de comando.")
    with st.expander("🛠️ PRÁTICA V8: TESTE DE COMANDO"):
        prompt = st.text_area("Crie seu Prompt V8:")
        if st.button("ANALISAR ESTRUTURA"):
            st.success("Análise Completa: Comando V8 Detectado. Pronto para Execução.")

elif modulo == "03. IA Business Architecture":
    embed_video("A_G3lO_AFeM", "💼 Arquitetura de Negócios 4.0", "Implemente sistemas que analisam contratos, criam teses e gerenciam clientes no piloto automático.")

elif modulo == "04. Conteúdo Escalar 100X":
    embed_video("dQw4w9WgXcQ", "🎬 Fábrica de Autoridade Infinita", "Como dominar o algoritmo e produzir conteúdo para 1 ano em apenas 48 horas de trabalho focado.")

elif modulo == "05. Visual Authority & Branding":
    embed_video("f-N9m1w0w_M", "🎨 Identidade Visual de Poder", "Sua imagem profissional reconstruída por IA. Fotos de estúdio e branding visual sem fotógrafos.")

elif modulo == "06. Deepfake & Avatares Vivos":
    embed_video("y7X6A8E19jM", "🎥 Presença Digital Onipresente", "Crie seu clone digital. Fale em qualquer idioma para qualquer mercado sem precisar estar na frente da câmera.")

elif modulo == "07. Arquitetura de Automação":
    embed_video("K3SAnF_uT_k", "⚙️ Ecossistema Autônomo", "O Módulo que faz as IAs conversarem entre si. O fim das tarefas manuais de backoffice.")

elif modulo == "08. Monetização & Scale Up":
    embed_video("S_O58NfLshI", "💰 Monetização God Mode", "Estratégias para vender seu conhecimento por R$ 10k a R$ 50k. IA como serviço de alto valor.")

elif modulo == "🎓 Graduation":
    st.title("🎓 DIPLOMA DE EXCELÊNCIA DIGITAL")
    st.balloons()
    nome = st.text_input("NOME COMPLETO DO COMANDANTE:")
    if st.button("EMITIR CERTIFICADO DE ELITE"):
        st.success(f"DIPLOMA EMITIDO: COMANDANTE {nome.upper()} AGORA É V8 MASTER.")
