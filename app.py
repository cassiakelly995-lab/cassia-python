import streamlit as st

# Configurações de Elite V8
st.set_page_config(page_title="Cássia Prompt V8 - Digital Only", page_icon="⚡", layout="wide")

# Estética Black & Gold (Sem papel, só pixels!)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stHeader, h1, h2, h3 { color: #d4af37 !important; }
    .conteudo-card { 
        background-color: #1a1a1a; 
        padding: 20px; 
        border-left: 5px solid #d4af37; 
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.write("Comandante: **Cássia Kelly**")

modulo = st.sidebar.radio("ESCOLHA SUA AULA:", [
    "🚀 Início Rápido",
    "🧠 Super Prompts (Copie e Cole)",
    "💰 Monetização Digital",
    "🎓 Certificado Digital"
])

if modulo == "🚀 Início Rápido":
    st.title("A Era Digital: Sem Papel, Mais Poder")
    st.markdown("""
    <div class="conteudo-card">
        <h3>Bem-vinda à Revolução!</h3>
        <p>Aqui não imprimimos nada. O conhecimento é direto, digital e ecológico.</p>
        <p><b>Dica da Cássia:</b> Use a função de busca (Ctrl+F) para achar qualquer comando no curso!</p>
    </div>
    """, unsafe_allow_html=True)

elif modulo == "🧠 Super Prompts (Copie e Cole)":
    st.title("🧠 Biblioteca de Comandos de Elite")
    
    with st.expander("👉 COMANDO: Criador de Conteúdo"):
        st.code("Aja como um Social Media Senior. Crie um calendário de 30 dias para... [complete aqui]")
        st.write("Use este comando para nunca mais ficar sem ideias no Instagram.")

    with st.expander("👉 COMANDO: Consultor de Negócios"):
        st.code("Analise o seguinte cenário de negócio e aponte 3 falhas de eficiência... [cole seus dados]")

elif modulo == "💰 Monetização Digital":
    st.title("💰 Como faturar com IA")
    st.write("1. Criação de infoprodutos digitais.")
    st.write("2. Consultoria de implementação de processos com IA.")
    st.write("3. Gestão de redes sociais com escala industrial.")

elif modulo == "🎓 Certificado Digital":
    st.title("🎓 Seu Diploma Ecológico")
    st.write("Gere seu certificado e compartilhe no LinkedIn. 0% papel, 100% autoridade.")
    # (Aqui mantemos o seu código de gerar o certificado que você já tem)
