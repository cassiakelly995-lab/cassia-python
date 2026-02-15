import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DE ALTA PATENTE ---
st.set_page_config(page_title="V8 GOD MODE | ELITE", page_icon="🔱", layout="wide")

# --- DESIGN HUD SUPREMO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@300;700&display=swap');
    .stApp { background: radial-gradient(circle, #111 0%, #000 100%); color: #fff; font-family: 'JetBrains Mono', monospace; }
    .v8-card { background: rgba(0, 0, 0, 0.9); border: 2px solid #d4af37; border-radius: 20px; padding: 40px; box-shadow: 0 0 60px rgba(212, 175, 55, 0.15); }
    h1, h2 { font-family: 'Orbitron', sans-serif; color: #d4af37; text-align: center; letter-spacing: 4px; }
    .stButton>button { background: linear-gradient(90deg, #8a6d1d, #d4af37); color: #000; font-family: 'Orbitron'; font-weight: 900; height: 60px; border: none; transition: 0.4s; }
    .stButton>button:hover { box-shadow: 0 0 40px #d4af37; transform: translateY(-3px); }
    .tip-box { background: rgba(212, 175, 55, 0.1); border-left: 5px solid #d4af37; padding: 15px; margin: 10px 0; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>V8 GOD MODE: ELITE EDITION</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-card'>", unsafe_allow_html=True)
    
    # MATRIZ DE ENTRADA (INTELIGÊNCIA DE PERFIL)
    col1, col2, col3 = st.columns(3)
    with col1:
        nome = st.text_input("💎 NOME DO OPERADOR:", "Cássia Kelly")
        nicho = st.text_input("🎯 NICHO/SETOR:", "Estrategista de Elite")
    with col2:
        momento = st.selectbox("🚦 MOMENTO ATUAL:", ["ESTOU COMEÇANDO (DO ZERO)", "JÁ ESTOU NO MERCADO (ESCALA)"])
        poder = st.text_input("🔥 SUA MAIOR HABILIDADE:", "Método V8")
    with col3:
        target = st.text_input("🚀 PÚBLICO ALVO:", "High-Ticket")
        ticket = st.text_input("💰 VALOR MÉDIO SERVIÇO:", "R$ 5.000,00")

    st.markdown("---")

    if st.button("🔥 EXECUTAR PROTOCOLO GENESIS COMPLETASSO"):
        st.markdown("### 📊 ARQUITETURA DE IMPACTO OMNICHANNEL")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📸 INSTAGRAM ELITE", "💼 LINKEDIN MASTER", "📄 CURRICULUM V8 (COMPLETASSO)", "💡 DICAS DE MESTRE"])
        
        # Lógica de Conteúdo Personalizada
        if momento == "ESTOU COMEÇANDO (DO ZERO)":
            foco_insta = f"💎 Especialista em {nicho}\n⚡ Mentorada pelo {poder}\n🎯 Transformando teoria em lucro para {target}\n👇 Entre na lista de espera:"
            foco_cv = f"Profissional focado em {nicho} com alta densidade técnica no {poder}. Especialista em viabilizar resultados para {target} através de processos de elite, priorizando eficiência e posicionamento premium."
            dicas = [
                "**Quebra de Objeção:** Como você é nova, foque em postar 'Bastidores de Estudo'. Mostre que você domina a técnica que os veteranos esqueceram.",
                "**Visual:** Use fotos com roupas de tons neutros (preto, branco, cinza) para transmitir seriedade imediata.",
                "**Networking:** Comente em posts de grandes players com análises técnicas, não apenas elogios."
            ]
        else:
            foco_insta = f"🏛️ Autoridade em {nicho}\n🚀 Criadora do {poder}\n📈 + de [X] resultados gerados para {target}\n👇 Clique para Escalar:"
            foco_cv = f"Líder estratégico em {nicho} com histórico comprovado de escala através do {poder}. Expert em gestão de branding e conversão High-Ticket para {target}, focado em perpetuar lucros e legado."
            dicas = [
                "**Escala:** Pare de falar de 'como fazer' e comece a falar de 'como delegar' ou 'estratégia macro'.",
                "**Exclusividade:** Seu perfil deve parecer um clube fechado. Menos posts, mais profundidade.",
                "**Lifestyle:** Mostre o resultado da sua liberdade para atrair quem deseja o mesmo estilo de vida."
            ]

        with tab1:
            st.markdown("<div class='tip-box'><b>BIO COPIÁVEL:</b></div>", unsafe_allow_html=True)
            st.code(foco_insta)
            st.markdown("**ESTRATÉGIA DE FEED:** Foque em 3 posts fixados: 1. Quem sou eu | 2. Como o {poder} funciona | 3. Prova de autoridade.")

        with tab2:
            st.subheader("Headline & About")
            st.code(f"{nicho} | Especialista em {poder} | Estrategista para {target}")
            st.text_area("SOBRE (EDITÁVEL):", foco_cv, height=150)

        with tab3:
            st.subheader("📄 CURRICULUM VITAE V8 (COMPLETASSO)")
            cv_full = f"""
NOME: {nome.upper()}
OBJETIVO: {nicho} High-Ticket
---------------------------------------------------------
RESUMO EXECUTIVO:
{foco_cv}

DOMÍNIO TÉCNICO:
- Implementação do {poder}
- Análise Preditiva de Mercado
- Gestão de Imagem e Autoridade para {target}

EXPERIÊNCIA E FORMAÇÃO:
- Especialização em Estratégias de Elite V8
- Desenvolvimento de Metodologias Próprias
- Consultoria para Projetos de Alto Valor

CONTATO:
[SEU EMAIL AQUI] | [SEU WHATSAPP AQUI]
---------------------------------------------------------
            """
            st.text_area("COPIE SEU CURRÍCULO AQUI:", cv_full, height=350)
            st.download_button("📥 BAIXAR CURRÍCULO", cv_full, file_name="curriculo_v8_elite.txt")

        with tab4:
            st.subheader("🧠 DICAS DE POSICIONAMENTO PARA ARRASAR")
            for dica in dicas:
                st.markdown(f"<div class='tip-box'>{dica}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
