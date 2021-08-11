import streamlit as st
from api import all_matches

def matches():
    st.title("Matches")
    table = all_matches()
    st.dataframe(table)