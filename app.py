import streamlit as st

# Configurações de Elite V8 - Cássia Prompt
st.set_page_config(page_title="Cássia Prompt V8 - Mobile Pro", page_icon="⚖️", layout="wide")

# Estética Premium (Preto e Dourado)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stSelectbox label, .stHeader, h1, h2, h3 { color: #d4af37 !important; }
    .stMarkdown { font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.write("Bem-vinda, **Cássia Kelly**.")
st.sidebar.markdown("---")

# Navegação do Curso
modulo = st.sidebar.radio("Selecione o Módulo:", [
    "01. O Setup de Autoridade",
    "02. Técnica Cinematográfica",
    "03. Edição Estratégica",
    "04. Monetização Jurídica"
])

if modulo == "01. O Setup de Autoridade":
    st.title("📸 Módulo 1: O Setup de Autoridade")
    st.subheader("Como não parecer amadora em 3 passos")
    
    st.markdown("""
    ### 1. O Ritual da Lente
    * **O Problema:** Vídeos embaçados e com "glare" (luz espalhada).
    * **A Solução:** Doutora, o primeiro passo é usar um lenço de microfibra. A gordura da mão na lente destrói sua autoridade visual. **Limpeza é nitidez.**

    ### 2. Ângulo de Julgamento
    * **Erro Comum:** Gravar de baixo para cima (mostra o teto e o queixo).
    * **A Regra:** O celular deve estar rigorosamente na **altura dos olhos**. Isso gera uma relação de igualdade e confiança com o cliente.

    ### 3. Luz 'Janela de Escritório'
    * **Técnica:** Fique de frente para uma janela (luz natural). 
    * **Dica Master:** A luz deve bater no rosto a 45 graus para criar uma sombra leve no nariz, afinando o rosto e dando profundidade profissional.
    """)
    st.success("✅ Dica de Ouro: Nunca grave com uma lâmpada comum logo acima da cabeça. Isso cria olheiras artificiais.")

elif modulo == "02. Técnica Cinematográfica":
    st.title("🎥 Módulo 2: Técnica Cinematográfica")
    st.markdown("""
    ### O Segredo do Foco e Exposição
    1. Abra a câmera do celular.
    2. Toque no seu rosto na tela e **segure**.
    3. Vai aparecer um cadeado (AE/AF Lock). 
    *Isso impede que o vídeo fique piscando ou mudando de cor enquanto você fala.*

    ### Estabilização de Elite
    * Use os cotovelos colados ao corpo se não tiver tripé. 
    * Transforme seu corpo em um tripé humano para evitar tremores que passam insegurança.
    """)

elif modulo == "03. Edição Estratégica":
    st.title("✂️ Módulo 3: Edição no CapCut")
    st.info("Foco em Retenção e Legendas Dinâmicas")
    st.markdown("""
    1. **Corte os 'Respiros':** Remova silêncios de mais de 0.5 segundos. O vídeo deve ser dinâmico.
    2. **Legendas Automáticas:** Use a função do CapCut, mas mude a fonte para algo clássico (Montserrat ou Playfair).
    3. **Color Grading:** Aumente levemente o 'Contraste' e a 'Nitidez' (Sharpen) para dar aspecto de câmera cara.
    """)

elif modulo == "04. Monetização Jurídica":
    st.title("⚖️ Módulo 4: Vendendo seu Peixe")
    st.markdown("""
    ### Como cobrar pelo seu novo visual?
    * **Visual Law:** Agora você não entrega apenas um vídeo, você entrega uma peça jurídica visual.
    * **Portfólio:** Use seu Instagram como vitrine técnica.
    """)
