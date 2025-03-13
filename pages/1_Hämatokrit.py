# === Login manager ===
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

import streamlit as st
import pandas as pd

st.title("Hämatokritwert berechnen")

st.write("Hier kannst du einen Hämatokritwert berechnen.")

def calculate_hematocrit(rbc, mcv):
    return (rbc * mcv) / 10

st.write("Bitte gib die folgenden Werte ein:")

rbc = st.number_input("Anzahl der Erythrozyten (in 10^12/Liter):", min_value=0.0, step=0.1)
mcv = st.number_input("Mittleres korpuskuläres Volumen (in Femtoliter):", min_value=0.0, step=0.1)
gender = st.selectbox("Geschlecht:", ["Männlich", "Weiblich"])

if st.button("Berechnen"):
    if mcv > 0:
        hematocrit = calculate_hematocrit(rbc, mcv)
        
        if gender == "Männlich":
            reference_min, reference_max = 43, 49
        else:
            reference_min, reference_max = 37, 45

        # Adding statements based on the result
        if hematocrit < reference_min:
            st.markdown(f"<span style='color:red'>Der Hämatokritwert beträgt: {hematocrit:.2f}%</span>", unsafe_allow_html=True)
            st.write("Ihr Hämatokritwert liegt unterhalb des Referenzbereiches.")
        elif hematocrit > reference_max:
            st.markdown(f"<span style='color:red'>Der Hämatokritwert beträgt: {hematocrit:.2f}%</span>", unsafe_allow_html=True)
            st.write("Ihr Hämatokritwert liegt oberhalb des Referenzbereiches.")
        else:
            st.markdown(f"<span style='color:green'>Der Hämatokritwert beträgt: {hematocrit:.2f}%</span>", unsafe_allow_html=True)
            st.write("Ihr Hämatokritwert liegt im Referenzbereich.")
    else:
        st.write("Das MCV muss größer als 0 sein.")
