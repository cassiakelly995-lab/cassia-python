import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DE ELITE V8 ---
st.set_page_config(page_title="V8 NEXUS | COMMAND CENTER", page_icon="🔱", layout="wide")

# --- CSS AVANÇADO (MERCADO DE LUXO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Syncopate:wght@700&family=Inter:wght@300;600&display=swap');
    
    .stApp { background: #000; color: #fff; font-family: 'Inter', sans-serif; }
    
    /* Cartão Nexus com efeito Glow */
    .nexus-card {
        background: rgba(15, 15, 15, 0.9);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.1);
        transition: 0.5s;
    }
    .nexus-card:hover { border-color: #d4af37; box-shadow: 0 0 60px rgba(212, 175, 55, 0.2); }

    h1 { font-family: 'Orbitron', sans-serif; font-weight: 900; letter-spacing: 15px; background: linear-gradient(90deg, #d4af37, #fff, #d4af37); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; }
    
    .stButton>button {
        width: 100%;
        background: transparent;
        color: #d4af37;
        border: 2px solid #d4af37;
        font-family: 'Syncopate';
        font-weight: 700;
        border-radius: 10px;
        height: 60px;
        transition: 0.4s;
    }
    .stButton>button:hover { background: #d4af37; color: #000; box-shadow: 0 0 30px #d4af37; }
    
    .status-box { padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; font-family: 'Orbitron'; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE DE CONTEÚDO ---
def get_copy(estilo, nicho):
    if estilo == "AGRESSIVO":
        return f"O mercado de {nicho} está cheio de amadores. Se você não é a autoridade, você é a presa. O Protocolo V8 não é para quem quer tentar, é para quem quer dominar."
    elif estilo == "TÉCNICO":
        return f"A análise estrutural de {nicho} revela uma falha na conversão de leads de alto ticket. A solução reside na implementação de processos V8 de autoridade validada."
    return f"Imagine ter a clareza total de como se posicionar em {nicho}. Onde cada post atrai o cliente certo e repele o curioso. Isso é V8."

# --- INTERFACE PRINCIPAL ---
st.markdown("<h1>V8 NEXUS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; letter-spacing:3px;'>ELITE COMMAND & CONTENT ENGINE</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='nexus-card'>", unsafe_allow_html=True)
    
    # INPUTS INTERATIVOS
    c1, c2, c3 = st.columns(3)
    with c1: 
        nome = st.text_input("💎 NOME DO PROJETO", "Cássia V8")
    with c2: 
        nicho = st.text_input("🎯 NICHO", "Direito de Elite")
    with c3: 
        estilo_copy = st.selectbox("🎭 TOM DA VOZ", ["AGRESSIVO", "TÉCNICO", "MAGNÉTICO"])

    st.markdown("---")
    
    # SLIDERS COM GRÁFICO EM TEMPO REAL
    col_sliders, col_grafico = st.columns([1, 1])
    
    with col_sliders:
        st.markdown("### 📊 PARAMETRIZAÇÃO")
        s1 = st.slider("COMUNICAÇÃO", 0, 10, 7)
        s2 = st.slider("AUTORIDADE", 0, 10, 4)
        s3 = st.slider("ESTRATÉGIA", 0, 10, 6)
        s4 = st.slider("VISUAL", 0, 10, 5)
        s5 = st.slider("CONVERSÃO", 0, 10, 3)

    with col_grafico:
        # Gráfico Radar Interativo
        df_radar = pd.DataFrame(dict(
            r=[s1, s2, s3, s4, s5],
            theta=['Comunicação', 'Autoridade', 'Estratégia', 'Visual', 'Conversão']))
        fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True, range_r=[0,10])
        fig.update_traces(fill='toself', line_color='#d4af37')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#fff")
        st.plotly_chart(fig, use_container_width=True)

    if st.button("🚀 GERAR ECOSSISTEMA V8"):
        st.markdown("---")
        
        # ÁREA DE RESULTADOS INTERATIVOS
        res1, res2 = st.columns(2)
        
        with res1:
            st.markdown("### ✍️ SCRIPT DE POSTAGEM")
            copy_gerada = get_copy(estilo_copy, nicho)
            st.info(copy_gerada)
            st.caption("📍 Postar no: FEED (Imagem com olhar de poder)")
            
        with res2:
            st.markdown("### 📱 SEQUÊNCIA DE STORIES (HOJE)")
            st.write("1. **Story 1:** Foto do café/mesa de trabalho: 'O jogo mudou'.")
            st.write("2. **Story 2:** Enquete: 'Você prefere autoridade ou lucro?'.")
            st.write("3. **Story 3:** Vídeo curto explicando a lacuna de " + nicho + ".")
            st.write("4. **Story 4:** CTA: 'Mande V8 no direct'.")

        st.markdown("### 💡 VEREDITO DO SISTEMA")
        if (s1+s2+s3+s4+s5)/5 < 6:
            st.markdown("<div class='status-box' style='background:#ff4b4b; color:white;'>STATUS: ALERTA DE OBSOLESCÊNCIA</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='status-box' style='background:#d4af37; color:black;'>STATUS: DOMÍNIO DE MERCADO</div>", unsafe_allow_html=True)
            
    st.markdown("</div>", unsafe_allow_html=True)
