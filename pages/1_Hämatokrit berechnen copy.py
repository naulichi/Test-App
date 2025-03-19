# === Login manager ===
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
import matplotlib.pyplot as plt

st.title("Hämatokritwert berechnen")

st.write("Hier kannst du einen Hämatokritwert berechnen."
"Der Hämatokritwert gibt den Anteil der festen Bestandteile des Blutes an. "
"Er wird in Prozent angegeben und gibt an, wie viel Prozent des Blutvolumens aus den Erythrozyten besteht.")    

# Input fields for user data
gender = st.selectbox("Geschlecht", ["Mann", "Frau"])
mcv = st.number_input("Mittleres korpuskuläres Volumen (MCV) in Femtoliter", min_value=0.0, step=0.1)
rbc = st.number_input("Anzahl der Erythrozyten (RBC) in 10^12/Liter", min_value=0.0, step=0.1)

if st.button("Berechnen"):
    # Calculate Hämatokrit
    hematocrit = (mcv * rbc) / 10
    st.write(f"Hämatokrit: {hematocrit:.2f}%")

    # Define reference ranges
    if gender == "Mann":
        lower_bound, upper_bound = 43, 49
    else:
        lower_bound, upper_bound = 37, 45

    # Display result with color coding
    if hematocrit < lower_bound:
        st.markdown(f"<span style='color:red'>{hematocrit:.2f}%</span>", unsafe_allow_html=True)
    elif hematocrit > upper_bound:
        st.markdown(f"<span style='color:green'>{hematocrit:.2f}%</span>", unsafe_allow_html=True)
    else:
        st.write(f"{hematocrit:.2f}%")

    # Plot the result
    fig, ax = plt.subplots()
    ax.axhline(lower_bound, color='blue', linestyle='--', label='Unterer Referenzbereich')
    ax.axhline(upper_bound, color='blue', linestyle='--', label='Oberer Referenzbereich')
    ax.bar(["Hämatokrit"], [hematocrit], color='red' if hematocrit < lower_bound else 'green' if hematocrit > upper_bound else 'blue')
    ax.set_ylim(0, 100)
    ax.set_ylabel('Hämatokrit (%)')
    ax.legend()
    st.pyplot(fig)

    # Save the result
    data_manager = DataManager()
    data_manager.save_hematocrit(gender, mcv, rbc, hematocrit)