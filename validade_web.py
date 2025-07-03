import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Validade de Produtos", layout="centered")
st.title("📦 Verificador de Validade de Produtos")

# Novo campo: mês e ano
st.subheader("📅 Dados da matéria-prima (validade)")
col1, col2 = st.columns(2)
with col1:
    mes = st.selectbox("Mês", list(range(1, 13)), format_func=lambda m: datetime(2000, m, 1).strftime('%B'))
with col2:
    ano = st.number_input("Ano", min_value=2020, max_value=2035, step=1)

# Menu de seleção de validade
opcao = st.selectbox("Escolha a validade do produto:", [
    "2 anos",
    "1 ano e 5 meses",
    "Personalizado"
])

# Define validade com base na opção
if opcao == "2 anos":
    anos, meses, dias = 2, 0, 0
elif opcao == "1 ano e 5 meses":
    anos, meses, dias = 1, 5, 0
else:
    col3, col4, col5 = st.columns(3)
    with col3:
        anos = st.number_input("Anos", min_value=0, step=1)
    with col4:
        meses = st.number_input("Meses", min_value=0, step=1)
    with col5:
        dias = st.number_input("Dias", min_value=0, step=1)

# Botão para calcular
if st.button("Calcular validade"):
    try:
        # Assume o dia 1 do mês escolhido
        data_fab = datetime(ano, mes, 1)
        data_venc = data_fab + relativedelta(years=anos, months=meses, days=dias)
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
        st.error("⚠️ Erro ao processar os dados.")
