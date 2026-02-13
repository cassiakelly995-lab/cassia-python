import streamlit as st
from fpdf import FPDF
import datetime

# Configurações de Elite V8 - Cássia Prompt
st.set_page_config(page_title="Cássia Prompt V8 - God Mode", page_icon="💎", layout="wide")

# Estética Black & Gold Premium
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stHeader, h1, h2, h3 { color: #d4af37 !important; }
    .stMarkdown { font-size: 1.1rem; }
    div.stButton > button:first-child { background-color: #d4af37; color: black; border-radius: 8px; font-weight: bold; }
    .stExpander { background-color: #1a1a1a; border: 1px solid #d4af37; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.subheader("A Era da Automação")
st.sidebar.write("Mentora: **Cássia Kelly**")

# Navegação dos 8 Módulos
modulo = st.sidebar.selectbox("ESCOLHA O MÓDULO:", [
    "01. Mentalidade Exponencial",
    "02. Engenharia de Prompt V8",
    "03. IA para Negócios e Carreira",
    "04. Produção de Conteúdo Escalar",
    "05. Criação de Imagens de Elite",
    "06. Vídeos e Avatares Digitais",
    "07. Automação de Processos",
    "08. O Futuro e Monetização",
    "🎓 Emitir Meu Certificado"
])

if modulo == "01. Mentalidade Exponencial":
    st.title("🚀 Módulo 1: Mentalidade Exponencial")
    st.markdown("""
    Neste módulo, você entende que a IA não é uma ferramenta de busca, mas um **motor de execução**.
    - Diferença entre busca e comando.
    - Por que 90% das pessoas falham com a IA.
    - O fim do papel e a era da eficiência máxima.
    """)

elif modulo == "02. Engenharia de Prompt V8":
    st.title("🧠 Módulo 2: Engenharia de Prompt V8")
    st.subheader("O Método Secreto de Comando")
    st.markdown("""
    A **Engenharia de Prompt V8** baseia-se em 4 pilares:
    1. **Persona (Quem):** Atribua um cargo de elite à IA.
    2. **Contexto (Onde):** Explique o cenário detalhadamente.
    3. **Objetivo (O que):** Defina a tarefa com verbos de ação.
    4. **Restrição (Como):** Diga o que a IA **não** deve fazer.
    """)
    st.info("Copie este modelo V8 para testar:")
    st.code("Aja como [CARGO]. Estamos no cenário [CONTEXTO]. Sua tarefa é [TAREFA]. Não use [RESTRIÇÃO].")

elif modulo == "03. IA para Negócios e Carreira":
    st.title("💼 Módulo 3: IA nos Negócios")
    with st.expander("Resumo de Contratos e Documentos"):
        st.write("Como usar a IA para ler 100 páginas em 5 segundos.")
    with st.expander("Análise de Concorrência"):
        st.write("Identificando falhas no mercado usando dados.")

elif modulo == "04. Produção de Conteúdo Escalar":
    st.title("🎬 Módulo 4: Conteúdo em Massa")
    st.write("Aprenda a criar 30 dias de postagens em apenas 15 minutos.")
    st.code("Crie uma tabela com 30 ideias de posts, legenda e sugestão de imagem para...")

elif modulo == "05. Criação de Imagens de Elite":
    st.title("🎨 Módulo 5: Imagens de Autoridade")
    st.write("Como gerar fotos profissionais de estúdio sem precisar de câmera.")

elif modulo == "06. Vídeos e Avatares Digitais":
    st.title("🎥 Módulo 6: Vídeos com IA")
    st.write("Criação de vídeos onde a IA fala por você em qualquer idioma.")

elif modulo == "07. Automação de Processos":
    st.title("⚙️ Módulo 7: O Robô Trabalha, Você Comanda")
    st.write("Conectando ferramentas para que o trabalho aconteça enquanto você dorme.")

elif modulo == "08. O Futuro e Monetização":
    st.title("💰 Módulo 8: Como Ganhar Dinheiro com IA")
    st.write("Estratégias para vender consultoria, infoprodutos e serviços de automação.")

elif modulo == "🎓 Emitir Meu Certificado":
    st.title("🎓 Certificado de Conclusão")
    nome = st.text_input("Nome Completo:")
    if st.button("Gerar Certificado"):
        # Aqui entra aquele seu código de PDF que já funciona
        st.success(f"Parabéns, {nome}! Seu certificado digital foi gerado com sucesso.")
