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

# Second page for history
if st.sidebar.button("Historie anzeigen"):
    st.sidebar.write("Historie der berechneten Werte")
    history = data_manager.load_history()
    if history:
        df = pd.DataFrame(history, columns=["Geschlecht", "MCV", "RBC", "Hämatokrit"])
        st.write(df)
        st.line_chart(df.set_index("Geschlecht")["Hämatokrit"])
    else:
        st.write("Keine historischen Daten gefunden.")