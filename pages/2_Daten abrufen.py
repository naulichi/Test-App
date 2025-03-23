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
data_df = st.session_state['data_df']
if data_df.empty:
    st.write("Du hast noch keine Daten gespeichert.")
    st.stop()

# sort the data by timestamp
data_df = data_df.sort_values(by='timestamp', ascending=False)

# Display the data
st.dataframe(data_df)
