import streamlit as st
from pages.matches import matches
from pages.clubs import clubs
from pages.players import players


st.header("UEFA Euro 2020")

st.sidebar.title("Navigation")
pages = st.sidebar.radio("Pages", ["Home", "Matches", "Clubs", "Players"])

if pages == "Home":
    pass

if pages == "Matches":
    matches()

if pages == "Clubs":
    clubs()

if pages == "Players":
    players()