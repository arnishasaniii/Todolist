import streamlit as st
import pandas as pd

st.title("Analizimi i Qarkullimit të Mallrave")


skedari = st.file_uploader("Ngarko skedarin qarkullimi.csv", type="csv")

if skedari:
    df = pd.read_csv(skedari, encoding="latin1")

    
    total = df["Qarkullimi (EUR)"].sum()
    st.subheader(f"Qarkullimi Total: {total:.2f} €")

    st.subheader("Qarkullimi sipas Kategorive")
    kategoria = df.groupby("Kategoria")["Qarkullimi (EUR)"].sum()
    st.bar_chart(kategoria)


    st.subheader("Qarkullimi sipas Ditëve")
    ditet = df.groupby("Data")["Qarkullimi (EUR)"].sum()
    st.line_chart(ditet)

    
    st.subheader("Detajet")
    for data, vlera in ditet.items():
        st.write(f"{data}: {vlera:.2f} €")
else:
    st.info("Ju lutem ngarkoni skedarin qarkullimi.csv")