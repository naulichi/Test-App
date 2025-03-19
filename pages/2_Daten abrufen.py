# === Login manager ===
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  

import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
import matplotlib.pyplot as plt

st.title("Historie deiner Hämatokritwerte")

st.write("Hier kannst du dir deine bisherigen Hämatokritwerte in einer Übersicht ansehen."
"Der Hämatokritwert gibt den Anteil der festen Bestandteile des Blutes an. "
"Er wird in Prozent angegeben und gibt an, wie viel Prozent des Blutvolumens aus den Erythrozyten besteht.")    

# Load the historical data
data = DataManager.load_records()

# Display the historical data in a table
st.write("Historische Daten:")
df = pd.DataFrame(data)
st.dataframe(df)

reference_min, reference_max = 43, 49
reference_min, reference_max = 37, 45

# Plot the historical data
fig, ax = plt.subplots()
ax.plot(df['hematocrit'], label='Hämatokritwert', marker='o')
ax.axhline(y=reference_min, color='r', linestyle='--', label='Referenzbereich Min')
ax.axhline(y=reference_max, color='r', linestyle='--', label='Referenzbereich Max')
ax.set_ylabel('Hämatokrit (%)')
ax.legend()
st.pyplot(fig)
