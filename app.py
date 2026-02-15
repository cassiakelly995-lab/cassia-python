import streamlit as st
import random

# --- CONFIGURAÇÃO V8 SUPREMA ---
st.set_page_config(page_title="V8 CREATOR | CÁSSIA EDITION", page_icon="⚡", layout="wide")

# --- DESIGN HUD BLACK & GOLD ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Syncopate:wght@700&family=Inter:wght@400;700&display=swap');
    .stApp { background: #000; color: #fff; font-family: 'Inter', sans-serif; }
    .v8-card { background: rgba(15, 15, 15, 0.95); border: 1px solid #d4af37; border-radius: 25px; padding: 40px; box-shadow: 0 0 50px rgba(212, 175, 55, 0.2); }
    h1 { font-family: 'Orbitron', sans-serif; color: #d4af37; text-align: center; letter-spacing: 5px; }
    .stButton>button { background: #d4af37; color: black; font-family: 'Syncopate'; font-weight: bold; border-radius: 8px; height: 55px; border: none; transition: 0.3s; }
    .stButton>button:hover { box-shadow: 0 0 30px #d4af37; transform: translateY(-2px); }
    .output-box { background: #111; border-left: 5px solid #d4af37; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE DE INTELIGÊNCIA ---
def gerar_conteudo(nicho, objetivo, tom):
    opcoes_bio = [
        f"💎 {nicho}\n🔥 Especialista em {objetivo}\n🚀 Autoridade V8 Ativada\n👇 Saiba mais:",
        f"⚖️ Elevando o padrão de {nicho}\n🎯 Foco em {objetivo}\n💎 Protocolo V8 de Elite\n👇 Agende seu diagnóstico:",
        f"⚡ {nicho} | Resultados Extraordinários\n🏛️ {objetivo} com Estratégia V8\n🔒 Posicionamento Inabalável\n👇 Clique aqui:"
    ]
    
    post = {
        "gancho": f"Por que 99% das pessoas falham em {nicho}?",
        "corpo": f"A verdade é dura: a maioria foca no operacional e esquece o posicionamento. No Protocolo V8, nós não jogamos o jogo, nós mudamos as regras. Se você quer {objetivo}, precisa de uma estratégia de elite.",
        "cta": "Comenta 'V8' para receber meu guia de posicionamento."
    }
    return opcoes_bio, post

# --- INTERFACE ---
st.markdown("<h1>V8 CREATOR HUB</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-card'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        nicho = st.text_input("🎯 QUAL O SEU NICHO?", "Estrategista Digital")
        objetivo = st.text_input("🚀 QUAL O OBJETIVO DO POST?", "Venda High-Ticket")
    with col2:
        tom = st.selectbox("🎭 TOM DE VOZ", ["Agressivo", "Inspirador", "Técnico", "Magnético"])
        estilo = st.radio("📱 ONDE VAI POSTAR?", ["Instagram", "LinkedIn", "TikTok/Reels"])

    st.markdown("---")

    if st.button("🔥 ATIVAR MÁQUINA DE CONTEÚDO"):
        bios, post = gerar_conteudo(nicho, objetivo, tom)
        
        tab1, tab2 = st.tabs(["📌 BIOS DE ELITE", "📝 LEGENDA PARA POST"])
        
        with tab1:
            st.markdown("### OPÇÕES DE BIOS (COPIE E COLE)")
            for i, bio in enumerate(bios):
                st.markdown(f"**Opção {i+1}:**")
                st.code(bio)
        
        with tab2:
            st.markdown("### POST PRONTO PARA USO")
            st.markdown(f"<div class='output-box'><b>GANCHO:</b> {post['gancho']}<br><br><b>CORPO:</b> {post['corpo']}<br><br><b>CTA:</b> {post['cta']}</div>", unsafe_allow_html=True)
            st.code(f"{post['gancho']}\n\n{post['corpo']}\n\n{post['cta']}")

    st.markdown("</div>", unsafe_allow_html=True)
