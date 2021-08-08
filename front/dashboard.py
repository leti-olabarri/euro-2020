import streamlit as st
from api import all_matches

st.title("UEFA Euro 2020")

if st.button('Hit me'):
    table = all_matches()
    st.dataframe(table)