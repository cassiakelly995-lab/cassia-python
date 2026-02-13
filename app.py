import streamlit as st

# Configurações de Elite V8 - Cássia Prompt
st.set_page_config(page_title="Cássia Prompt V8 - Curso de IA", page_icon="🤖", layout="wide")

# Estética Premium (Preto e Dourado para Autoridade)
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stSelectbox label, .stHeader, h1, h2, h3 { color: #d4af37 !important; }
    .stMarkdown { font-size: 1.1rem; }
    div.stButton > button:first-child { background-color: #d4af37; color: black; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.subheader("Curso de IA para Advogadas")
st.sidebar.write("Instrutora: **Cássia Kelly**")
st.sidebar.markdown("---")

# Navegação do Curso de IA
modulo = st.sidebar.radio("Módulos do Curso:", [
    "01. Mentalidade IA (Prompt Engineering)",
    "02. IA no Dia a Dia Jurídico",
    "03. Criação de Imagens e Vídeos com IA",
    "04. Automação de Processos"
])

if modulo == "01. Mentalidade IA (Prompt Engineering)":
    st.title("🧠 Módulo 1: Engenharia de Prompt para Advogadas")
    st.subheader("Como dar ordens que a IA obedece")
    
    st.markdown("""
    ### O que é um Prompt de Elite?
    Não é uma conversa, é um **comando**. Para ter resultados perfeitos (God Mode), seu comando deve ter:
    1. **Contexto:** "Você é um advogado especialista em Direito Civil..."
    2. **Tarefa:** "Analise este contrato e encontre 3 cláusulas de risco..."
    3. **Formato:** "Entregue o resultado em uma tabela com explicações simples."

    ### Exercício Prático
    Tente usar a fórmula: **Persona + Contexto + Tarefa + Restrição.**
    """)
    st.success("✅ Comando do Antônio: A IA é um motor de execução. Se o resultado foi ruim, o comando foi vago.")

elif modulo == "02. IA no Dia a Dia Jurídico":
    st.title("⚖️ Módulo 2: Produtividade Jurídica com IA")
    st.markdown("""
    ### Casos de Uso Reais:
    * **Resumo de Processos:** Como subir um PDF de 200 páginas e extrair os pontos-chave em 10 segundos.
    * **Peticionamento Estratégico:** Usar a IA para encontrar contradições em depoimentos.
    * **Atendimento ao Cliente:** Criar respostas automáticas que não parecem robóticas.
    """)

elif modulo == "03. Criação de Imagens e Vídeos com IA":
    st.title("🎨 Módulo 3: Autoridade Visual com IA")
    st.info("Aqui usamos IA para criar sua identidade visual sem precisar de estúdio.")
    st.markdown("""
    1. **Geradores de Imagem:** Como criar fotos profissionais de estúdio usando apenas texto.
    2. **Deepfake Ético:** Como traduzir seus vídeos para qualquer língua ou corrigir falas com IA.
    3. **Cenários Virtuais:** Criar um escritório de luxo digital para seus vídeos.
    """)

elif modulo == "04. Automação de Processos":
    st.title("🚀 Módulo 4: O Escritório Autônomo")
    st.markdown("""
    ### O Futuro é Agora:
    * Como conectar o WhatsApp da sua advocacia a uma IA que faz a triagem inicial dos clientes.
    * Automação de prazos e notificações inteligentes.
    """)
