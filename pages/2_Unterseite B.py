# === Login manager ===
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

st.title("Hämatokritwert berechnen")

st.write("Hier kannst du einen Hämatokritwert berechnen.")

def calculate_hematocrit(rbc, mcv):
    return (rbc * mcv) / 10

st.write("Bitte gib die folgenden Werte ein:")

rbc = st.number_input("Anzahl der roten Blutkörperchen (in 10^12/Liter):", min_value=0.0, step=0.1)
mcv = st.number_input("Mittleres korpuskuläres Volumen (MCV in Femtoliter):", min_value=0.0, step=0.1)
gender = st.selectbox("Geschlecht:", ["Männlich", "Weiblich"])

if st.button("Berechnen"):
    if mcv > 0:
        hematocrit = calculate_hematocrit(rbc, mcv)
        st.write(f"Der Hämatokritwert beträgt: {hematocrit:.2f}%")

        if gender == "Männlich":
            reference_min, reference_max = 43, 49
        else:
            reference_min, reference_max = 37, 45

        data = {
            'Parameter': ['Dein Wert', 'Referenzbereich Min', 'Referenzbereich Max'],
            'Hämatokritwert (%)': [hematocrit, reference_min, reference_max]
        }

        df = pd.DataFrame(data)
        st.write(df)

        # Plotting the data
        fig, ax = plt.subplots()
        ax.barh(['Referenzbereich Min', 'Dein Wert', 'Referenzbereich Max'], [reference_min, hematocrit, reference_max], color=['blue', 'green', 'blue'])
        ax.set_xlim(0, max(reference_max, hematocrit) + 10)
        ax.set_xlabel('Hämatokritwert (%)')
        ax.set_title('Hämatokritwert im Vergleich zum Referenzbereich')

        st.pyplot(fig)
    else:
        st.write("Das MCV muss größer als 0 sein.")