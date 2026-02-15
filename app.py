import streamlit as st
import random

# --- CONFIGURAÇÃO DE ALTA PATENTE ---
st.set_page_config(page_title="V8 GOD MODE | THE ORACLE", page_icon="🔱", layout="wide")

# --- DESIGN CYBER-LUXURY ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Syncopate:wght@400;700&family=Inter:wght@300;400;700&display=swap');
    
    .stApp { background: radial-gradient(circle at top right, #1a1a1a, #000); color: #e0e0e0; font-family: 'Inter', sans-serif; }
    .v8-card { background: rgba(20, 20, 20, 0.85); backdrop-filter: blur(20px); border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 30px; padding: 40px; box-shadow: 0 25px 60px rgba(0,0,0,0.8); margin: 20px 0; }
    h1 { font-family: 'Orbitron', sans-serif; background: linear-gradient(180deg, #d4af37 0%, #8a6d1d 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3.5em !important; text-align: center; letter-spacing: 8px; font-weight: 900; }
    .post-box { background: #111; border-left: 5px solid #d4af37; padding: 25px; border-radius: 10px; margin-top: 20px; font-family: 'Inter', sans-serif; }
    .channel-tag { background: #d4af37; color: black; padding: 3px 12px; border-radius: 5px; font-weight: bold; font-size: 0.8em; text-transform: uppercase; }
    .stButton>button { background: linear-gradient(135deg, #d4af37, #8a6d1d); color: black; font-weight: 900; border: none; border-radius: 12px; height: 50px; transition: 0.3s; font-family: 'Syncopate'; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(212, 175, 55, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- MOTOR DE INTELIGÊNCIA V8 ---
def criar_post_v8(nicho, objetivo, nivel):
    estilos = [
        {
            "canal": "REELS / TIKTOK",
            "gancho": f"O erro que está destruindo sua autoridade em {nicho}.",
            "legenda": f"Você continua agindo como amador e espera resultados de elite? Em {nicho}, quem não domina a estratégia vira estatística. \n\nPara resolver isso: \n1. Pare de focar no óbvio. \n2. Aplique o Protocolo V8. \n\nComenta 'ESCALA' para o próximo nível.",
            "visual": "Vídeo rápido, cortes secos, música de impacto (Phonk ou Cinematic)."
        },
        {
            "canal": "FEED (CARROSSEL)",
            "gancho": f"5 Pilares do {nicho} que os grandes não te contam.",
            "legenda": f"O mercado está saturado de pessoas comuns. Se você quer {objetivo}, precisa de diferenciação técnica. Arraste para o lado e entenda o jogo dos 1%.",
            "visual": "Design Black & Gold, fontes grandes e minimalistas."
        },
        {
            "canal": "LINKEDIN / ARTIGO",
            "gancho": f"A análise técnica sobre o futuro de {nicho}.",
            "legenda": f"Vivemos uma era de transição em {nicho}. A eficiência não é mais um diferencial, é sobrevivência. Como estamos posicionando nossos clientes para {objetivo}...",
            "visual": "Foto profissional em ambiente de negócios (High-end)."
        }
    ]
    return random.choice(estilos)

# --- INTERFACE ---
st.markdown("<h1>V8 GOD MODE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; letter-spacing:5px; color:#888;'>THE WORLD'S MOST ADVANCED AUDIT SYSTEM</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='v8-card'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: nome = st.text_input("IDENTIFICAÇÃO DO ALVO", placeholder="NOME...")
    with c2: nicho = st.text_input("ÁREA TÉCNICA (NICHO)", placeholder="DIREITO, BUSINESS...")
    with c3: obj = st.text_input("OBJETIVO DE ESCALA", placeholder="VENDAS, AUTORIDADE...")
    
    st.markdown("---")
    st.markdown("### ⚡ PARÂMETROS DE COMPETÊNCIA")
    ca, cb = st.columns(2)
    with ca:
        s1 = st.slider("COMUNICAÇÃO", 0, 10, 5)
        s2 = st.slider("AUTORIDADE", 0, 10, 5)
    with cb:
        s3 = st.slider("POSICIONAMENTO", 0, 10, 5)
        s4 = st.slider("ESTÉTICA VISUAL", 0, 10, 5)

    if st.button("🔥 ATIVAR ORÁCULO E GERAR CONTEÚDO DE ELITE"):
        avg = (s1+s2+s3+s4)/4
        post_pronto = criar_post_v8(nicho, obj, avg)
        
        st.markdown("---")
        st.markdown(f"### 🛡️ VEREDITO V8: {'GOD MODE' if avg > 8 else 'NECESSITA AJUSTE CRÍTICO'}")
        
        # BIO E POSICIONAMENTO
        st.markdown("#### 🖋️ BIO MAGNÉTICA ATUALIZADA")
        st.code(f"⚖️ Especialista em {nicho}\n🏛️ {obj} via Protocolo V8\n🔒 Autoridade Validada pelo Mercado\n👇 Conquiste sua posição de elite aqui:")

        # POST COMPLETO
        st.markdown(f"### 🎬 POST DE ELITE GERADO")
        st.markdown(f"<span class='channel-tag'>{post_pronto['canal']}</span>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='post-box'>
            <p><b>GANCHO (Headline):</b> {post_pronto['gancho']}</p>
            <p><b>LEGENDA:</b><br>{post_pronto['legenda']}</p>
            <p><b>DIRETRIZ VISUAL:</b> {post_pronto['visual']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🗺️ ONDE POSTAR E POR QUÊ?")
        if post_pronto['canal'] == "REELS / TIKTOK":
            st.write("📍 **Por que:** Para atrair novos seguidores (Top of Funnel) e quebrar o padrão de postagens estáticas.")
        elif post_pronto['canal'] == "FEED (CARROSSEL)":
            st.write("📍 **Por que:** Para educar seu público e salvar o post, o que aumenta absurdamente seu alcance orgânico.")
        else:
            st.write("📍 **Por que:** Para reforçar sua autoridade intelectual e atrair parceiros de alto ticket.")

    st.markdown("</div>", unsafe_allow_html=True)
