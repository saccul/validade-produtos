import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Validade de Produtos", layout="centered")

st.title("📦 Verificador de Validade de Produtos")

data_fabricacao_str = st.text_input("Data de fabricação (dd/mm/aaaa):")
validade_dias = st.number_input("Validade (em dias):", min_value=1, step=1)

if st.button("Calcular validade"):
    try:
        data_fab = datetime.strptime(data_fabricacao_str, "%d/%m/%Y")
        data_venc = data_fab + timedelta(days=validade_dias)
        hoje = datetime.today()
        
        st.write(f"🗓️ Data de vencimento: **{data_venc.strftime('%d/%m/%Y')}**")

        dias_restantes = (data_venc - hoje).days
        if hoje > data_venc:
            st.error("⚠️ Produto VENCIDO")
        elif dias_restantes <= 7:
            st.warning(f"⚠️ Produto PRÓXIMO DO VENCIMENTO ({dias_restantes} dias restantes)")
        else:
            st.success(f"✅ Produto dentro do prazo ({dias_restantes} dias restantes)")

    except:
        st.error("⚠️ Erro: Verifique se a data está no formato correto (dd/mm/aaaa)")
