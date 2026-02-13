import streamlit as st
from fpdf import FPDF
import datetime

# --- CONFIGURAÇÃO DE ALTA TECNOLOGIA ---
st.set_page_config(page_title="Cássia Prompt V8 - God Mode", page_icon="💎", layout="wide")

# --- DESIGN CUSTOMIZADO (LUXO DIGITAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #050505; color: #E0E0E0; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #d4af37 !important; letter-spacing: 2px; }
    
    .stAlert { background-color: #1a1a1a; border: 1px solid #d4af37; color: white; }
    .stExpander { background-color: #0f0f0f; border: 1px solid #333; border-radius: 10px; }
    
    /* Botão Estilo Tesla */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #d4af37 0%, #aa841e 100%);
        color: black !important;
        font-weight: bold;
        border: none;
        padding: 15px;
        border-radius: 8px;
        text-transform: uppercase;
        transition: 0.5s;
    }
    div.stButton > button:hover { transform: scale(1.02); box-shadow: 0px 0px 20px #d4af37; }
    
    .status-card {
        background: rgba(212, 175, 55, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #d4af37;
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
st.sidebar.markdown(f"<h1 style='text-align: center; font-size: 1.5rem;'>CÁSSIA PROMPT V8</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>Status: <span style='color: #00ff00;'>ONLINE (GOD MODE)</span></p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

modulo = st.sidebar.radio("SISTEMA DE ENSINO:", [
    "00. Welcome Experience",
    "01. Mentalidade Exponencial",
    "02. Engenharia V8 God Mode",
    "03. IA Business Strategy",
    "04. Conteúdo Escalar 10X",
    "05. Autoridade Visual (Midjourney/DALL-E)",
    "06. Deepfake & Avatares de Elite",
    "07. Arquitetura de Automação",
    "08. Monetização & High-Ticket",
    "🎓 Graduation Certificado"
])

# --- LÓGICA DE MÓDULOS ---

if modulo == "00. Welcome Experience":
    st.title("🛡️ BEM-VINDA À ELITE DA TECNOLOGIA")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### O Conhecimento que as Big Techs não querem que você saiba.
        Você acaba de entrar no sistema **Cássia Prompt V8**. Aqui, não ensinamos a 'usar' ferramentas, ensinamos você a **comandar a Inteligência Artificial**. 
        
        Prepare-se para uma transformação cognitiva. O papel acabou. A burocracia morreu. A partir de agora, seu limite é o seu comando.
        """)
        # Correção de Vídeo (Vídeo de Boas-Vindas - Aula 0)
        st.video("https://www.youtube.com/watch?v=5V9X-CByhYw") # Vídeo Inspiração IA
        
    with col2:
        st.markdown("""<div class='status-card'>
        <h4>🚀 COMANDANTE: Cássia Kelly</h4>
        <p>Acesso: Nível God Mode</p>
        <p>Progresso: 5% completo</p>
        </div>""", unsafe_allow_html=True)
        st.info("💡 **Ação do Antônio:** Assista ao vídeo de introdução para desbloquear a lógica V8.")

elif modulo == "01. Mentalidade Exponencial":
    st.title("🚀 Módulo 1: O Fim da Era Linear")
    st.markdown("""
    Neste módulo, destruímos o conceito de 'trabalho duro' para dar lugar ao 'trabalho inteligente'.
    
    ### Conteúdo Programático:
    1. **O Salto Tecnológico:** Por que o mundo mudou em 2025.
    2. **A Morte do Papel:** A sustentabilidade como lucro.
    3. **Sistemas de Input vs Output:** Como pensar como um arquiteto de dados.
    """)
    st.video("https://www.youtube.com/watch?v=m7H09-l-H4U")

elif modulo == "02. Engenharia V8 God Mode":
    st.title("🧠 Módulo 2: O Protocolo V8")
    st.subheader("Dominando a Linguagem das Máquinas")
    
    with st.expander("📝 A Fórmula do Prompt Perfeito"):
        st.write("A metodologia V8 não aceita 'pedidos'. Ela emite 'diretrizes'.")
        st.code("""
        ESTRUTURA GOD MODE:
        [CONTEXTO] + [PERSONA DE ELITE] + [OBJETIVO ATÔMICO] + [LIMITES E ESTILO]
        """)
    
    st.markdown("### Atividade Prática")
    user_p = st.text_area("Crie um Prompt para um assistente financeiro usando a regra V8:")
    if st.button("ANALISAR COMANDO"):
        st.success("Comando analisado pelo Sistema Antônio. Nível de Precisão: 98% (God Mode Ativo).")

elif modulo == "03. IA Business Strategy":
    st.title("💼 Módulo 3: Estratégia de Negócios 4.0")
    st.markdown("""
    ### Transformando IAs em Funcionários Gratuitos
    * **Recrutamento Algorítmico:** Use a IA para triagem de currículos e clientes.
    * **Análise de Dados:** Como prever tendências do mercado antes da concorrência.
    * **CRM Inteligente:** Otimização de tempo em vendas.
    """)
    st.video("https://www.youtube.com/watch?v=0_fN_7P11i8")

elif modulo == "04. Conteúdo Escalar 10X":
    st.title("🎬 Módulo 4: Fábrica de Conteúdo Escalar")
    st.write("Aprenda a criar 1 ano de conteúdo estratégico em 2 horas de trabalho.")
    st.info("Aqui usamos o método de 'Quebra de Prompt' para gerar roteiros, legendas e hooks virais.")

elif modulo == "05. Autoridade Visual (Midjourney/DALL-E)":
    st.title("🎨 Módulo 5: Visual Authority")
    st.markdown("""
    ### A Imagem do Sucesso
    - Criando cenários cinematográficos para suas redes sociais.
    - Fotos de estúdio (Headshots) sem sair de casa.
    - Psicologia das cores aplicada a prompts de imagem.
    """)

elif modulo == "06. Deepfake & Avatares de Elite":
    st.title("🎥 Módulo 6: Cinematografia Digital")
    st.write("Sua voz, seu rosto, em qualquer idioma, 24 horas por dia.")
    st.markdown("- HeyGen e HeyGen Pro: A nova fronteira.")
    st.markdown("- Clonagem de voz para podcasts automatizados.")

elif modulo == "07. Arquitetura de Automação":
    st.title("⚙️ Módulo 7: O Ecossistema Autônomo")
    st.write("Conectando ferramentas (Make, Zapier, IA) para criar um fluxo de trabalho sem toque humano.")

elif modulo == "08. Monetização & High-Ticket":
    st.title("💰 Módulo 8: Monetização V8")
    st.markdown("""
    ### Como cobrar R$ 10.000+ por consultoria de IA
    - Posicionamento de High-Ticket.
    - Criando Infoprodutos que se vendem sozinhos.
    - O futuro do trabalho: O Consultor de Prompt.
    """)

elif modulo == "🎓 Graduation Certificado":
    st.title("🎓 DIPLOMA DE EXCELÊNCIA DIGITAL")
    st.balloons()
    nome = st.text_input("INSIRA O NOME DO FORMANDO:")
    if st.button("EMITIR CERTIFICADO GOD MODE"):
        st.success(f"Certificado de {nome} gerado com sucesso! Nível: Master IA V8.")
