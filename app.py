import streamlit as st
from fpdf import FPDF
import datetime

# Configurações de Elite V8 - Cássia Prompt
st.set_page_config(page_title="Cássia Prompt V8 - IA para Todos", page_icon="🚀", layout="wide")

# Estética Premium (Preto e Dourado)
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stSelectbox label, .stHeader, h1, h2, h3 { color: #d4af37 !important; }
    div.stButton > button:first-child { background-color: #d4af37; color: black; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("💎 Cássia Prompt V8")
st.sidebar.subheader("IA para Todos")
st.sidebar.write("Mentora: **Cássia Kelly**")
st.sidebar.markdown("---")

modulo = st.sidebar.radio("Navegação:", [
    "01. Domine a Máquina",
    "02. Produtividade Extrema",
    "03. Criação de Conteúdo",
    "🎓 Gerar Meu Certificado"
])

if modulo == "01. Domine a Máquina":
    st.title("🧠 Módulo 1: A Arte de Comandar a IA")
    st.markdown("""
    ### O Segredo do Comando (Prompt)
    Para que a IA trabalhe para você, use sempre a estrutura:
    * **Quem ela é:** "Aja como um especialista em..."
    * **O que ela deve fazer:** "Crie um roteiro para..."
    * **Para quem:** "O público são pessoas que..."
    """)

elif modulo == "🎓 Gerar Meu Certificado":
    st.title("🎓 Conclusão de Curso")
    st.subheader("Parabéns pela sua conquista!")
    
    nome_aluno = st.text_input("Digite seu nome completo para o certificado:")
    
    if st.button("Gerar Certificado em PDF"):
        if nome_aluno:
            pdf = FPDF(orientation='L', unit='mm', format='A4')
            pdf.add_page()
            # Borda Dourada
            pdf.set_draw_color(212, 175, 55)
            pdf.set_line_width(5)
            pdf.rect(10, 10, 277, 190)
            
            pdf.set_font('Arial', 'B', 40)
            pdf.cell(0, 50, 'CERTIFICADO DE CONCLUSAO', ln=True, align='C')
            
            pdf.set_font('Arial', '', 20)
            pdf.cell(0, 20, 'Certificamos que', ln=True, align='C')
            
            pdf.set_font('Arial', 'B', 30)
            pdf.cell(0, 30, nome_aluno.upper(), ln=True, align='C')
            
            pdf.set_font('Arial', '', 20)
            pdf.multi_cell(0, 15, f'concluiu o treinamento Cassia Prompt V8\\nsob a mentoria de Cassia Kelly.', align='C')
            
            data_hoje = datetime.date.today().strftime("%d/%m/%Y")
            pdf.cell(0, 30, f'Emitido em: {data_hoje}', ln=True, align='C')
            
            pdf_output = pdf.output(dest='S').encode('latin-1')
            st.download_button(label="📥 Baixar Certificado", data=pdf_output, file_name=f"Certificado_{nome_aluno}.pdf", mime="application/pdf")
        else:
            st.error("Por favor, digite seu nome.")
