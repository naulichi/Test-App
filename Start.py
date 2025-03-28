import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Test-App")  # switch drive 

# initialize the login manager
from utils.login_manager import LoginManager

login_manager = LoginManager(data_manager) # initialize login manager
login_manager.login_register()  # opens login page

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value=pd.DataFrame(), 
    parse_dates=['timestamp']  # Ensure this line is uncommented
)

st.title("Meine erste Streamlit App")

"""
Diese App wurde von folgender Person entwickelt:
- Chiara Nauli (naulichi@students.zhaw.ch)
"""
