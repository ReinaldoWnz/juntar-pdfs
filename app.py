import streamlit as st
from PyPDF2 import PdfMerger
import io

st.set_page_config(page_title="Juntar PDFs", layout="centered")

st.title("📑 Juntar PDFs em um só arquivo")

# Upload de múltiplos arquivos PDF
uploaded_files = st.file_uploader(
    "Selecione seus arquivos PDF (pode escolher vários)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"Você selecionou **{len(uploaded_files)} PDFs**.")

    if st.button("🔗 Juntar PDFs"):
        merger = PdfMerger()

        for pdf in uploaded_files:
            merger.append(pdf)

        # Salvar em memória
        output = io.BytesIO()
        merger.write(output)
        merger.close()
        output.seek(0)

        st.success("✅ PDFs juntados com sucesso!")
        st.download_button(
            label="📥 Baixar PDF final",
            data=output,
            file_name="pdf_unificado.pdf",
            mime="application/pdf"
        )
