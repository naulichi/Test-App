import streamlit as st
import pandas as pd

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

        # Displaying the data without plotting
        st.write(f"Referenzbereich Min: {reference_min}%")
        st.write(f"Referenzbereich Max: {reference_max}%")
        st.write(f"Dein Wert: {hematocrit:.2f}%")

        # Adding statements based on the result
        if hematocrit < reference_min:
            st.write("Ihr Hämatokritwert liegt unterhalb des Referenzbereiches.")
        elif hematocrit > reference_max:
            st.write("Ihr Hämatokritwert liegt oberhalb des Referenzbereiches.")
        else:
            st.write("Ihr Hämatokritwert liegt im Referenzbereich.")
    else:
        st.write("Das MCV muss größer als 0 sein.")
