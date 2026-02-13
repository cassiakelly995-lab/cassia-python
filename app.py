import streamlit as st

# Configurações de Elite V8 - Cássia Prompt
st.set_page_config(page_title="Cássia Prompt V8 - IA para Todos", page_icon="🚀", layout="wide")

# Estética Premium (Preto e Dourado - Poder e Autoridade)
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stSelectbox label, .stHeader, h1, h2, h3 { color: #d4af37 !important; }
    .stMarkdown { font-size: 1.1rem; }
    div.stButton > button:first-child { background-color: #d4af37; color: black; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.subheader("Inteligência Artificial para Todos")
st.sidebar.write("Instrutora: **Cássia Kelly**")
st.sidebar.markdown("---")

# Navegação do Curso Universal
modulo = st.sidebar.radio("Módulos do Curso:", [
    "01. Domine a Máquina (Prompts)",
    "02. IA e Produtividade Extrema",
    "03. Criação de Conteúdo e Imagem",
    "04. O Futuro do Trabalho com IA"
])

if modulo == "01. Domine a Máquina (Prompts)":
    st.title("🧠 Módulo 1: A Arte de Comandar a IA")
    st.subheader("Como falar para a IA executar o que você pensa")
    
    st.markdown("""
    ### O Segredo do Prompt de Elite
    A IA não é um Google para você pesquisar, é um **motor de comando**. Para qualquer profissão, a regra é:
    1. **Papel:** Dê uma identidade à IA ("Aja como um especialista em...")
    2. **Contexto:** Explique o cenário ("Estou criando um projeto para...")
    3. **Objetivo:** O que você quer exatamente? ("Crie um roteiro de...")
    4. **Formato:** Como quer a resposta? (Tabela, lista, código, e-mail...)

    ### Exercício
    Pare de fazer perguntas curtas. Comece a dar instruções detalhadas.
    """)
    st.success("✅ Nota do Antônio: Quem domina o prompt, domina o tempo.")

elif modulo == "02. IA e Produtividade Extrema":
    st.title("⚡ Módulo 2: Ganhando 10 Horas por Semana")
    st.markdown("""
    ### Ferramentas para qualquer Profissional:
    * **Resumo Inteligente:** Transforme vídeos longos ou PDFs enormes em pontos de ação rápidos.
    * **Gestão de E-mails:** Use a IA para redigir respostas difíceis com o tom perfeito.
    * **Brainstorming:** Nunca mais comece um projeto do zero. Use a IA para gerar as primeiras 10 ideias.
    """)

elif modulo == "03. Criação de Conteúdo e Imagem":
    st.title("🎨 Módulo 3: Autoridade Visual e Criatividade")
    st.info("Criação de impacto sem precisar de ferramentas complexas.")
    st.markdown("""
    1. **Imagens Realistas:** Como criar fotos profissionais para redes sociais usando apenas texto.
    2. **Vídeos com IA:** Criação de avatares, narrações e legendas automáticas.
    3. **Design Estratégico:** Como usar a IA para escolher cores e layouts que vendem.
    """)

elif modulo == "04. O Futuro do Trabalho com IA":
    st.title("🚀 Módulo 4: Tornando-se Insubstituível")
    st.markdown("""
    ### A Nova Era:
    * **Automação Pessoal:** Como conectar ferramentas para que trabalhem sozinhas.
    * **Análise de Dados:** Tome decisões baseadas em dados, mesmo sem entender de matemática.
    * **Adaptação Rápida:** Como aprender qualquer coisa 10x mais rápido com auxílio da IA.
    """)
