import streamlit as st

st.title("Hämatokritwert berechnen")

st.write("Hier kannst du einen Hämatokritwert berechnen.")


def calculate_hematocrit(rbc, blood_volume):
    return (rbc / blood_volume) * 100

st.write("Bitte gib die folgenden Werte ein:")

rbc = st.number_input("Anzahl der roten Blutkörperchen (in Millionen pro Mikroliter):", min_value=0.0, step=0.1)
blood_volume = st.number_input("Blutvolumen (in Mikroliter):", min_value=0.0, step=0.1)

if st.button("Berechnen"):
    if blood_volume > 0:
        hematocrit = calculate_hematocrit(rbc, blood_volume)
        st.write(f"Der Hämatokritwert beträgt: {hematocrit:.2f}%")

        fig, ax = plt.subplots()
        ax.barh(['Referenzbereich', 'Dein Wert'], [45, hematocrit], color=['blue', 'red'])
        ax.set_xlim(0, 100)
        ax.set_xlabel('Hämatokritwert (%)')
        st.pyplot(fig)
    else:
        st.write("Das Blutvolumen muss größer als 0 sein.")