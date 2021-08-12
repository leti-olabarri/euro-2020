import streamlit as st
from pages.matches import matches
from pages.players import players


st.header("UEFA Euro 2020")

st.sidebar.title("Navigation")
pages = st.sidebar.radio("Pages", ["Home", "Matches", "Players"])

if pages == "Home":
    pass

if pages == "Matches":
    matches()

if pages == "Players":
    players()