import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Calculadora de Cronograma", page_icon="📅")

st.title("📅 Calculadora de Horas e Dias")

# Entradas na barra lateral
st.sidebar.image("logo.png", width=150)
total_servico = st.sidebar.number_input("Valor Total (R$)", min_value=0.0, value=1000.0)
valor_hora = st.sidebar.number_input("Valor/Hora (R$)", min_value=1.0, value=50.0)
horas_por_dia = st.sidebar.slider("Horas por Dia", 1, 12, 4)
data_inicio = st.sidebar.date_input("Data de Início", datetime.now())

# Cálculo
if valor_hora > 0:
    total_horas = total_servico / valor_hora
    total_dias = int(total_horas / horas_por_dia)
    if total_horas % horas_por_dia > 0:
        total_dias += 1

    st.metric("Total de Horas Necessárias", f"{total_horas:.4f} h")
    st.write(f"Previsão de término em **{total_dias} dias úteis** baseados em {total_horas:.4f} horas totais.")

    # Gerar lista de datas
    datas = []
    curr = data_inicio
    count = 0
    while count < total_dias:
        if curr.weekday() < 5: # Segunda a Sexta
            count += 1
            datas.append({"Dia": count, "Data": curr.strftime("%d/%m/%Y")})
        curr += timedelta(days=1)
    
    st.table(pd.DataFrame(datas))