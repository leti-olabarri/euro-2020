import streamlit as st
from pages.matches import matches
from pages.players import players
from pages.venues import venues
from pages.clubs import clubs



st.header("UEFA Euro 2020")

st.sidebar.title("Navigation")
pages = st.sidebar.radio("Pages", ["Venues", "Clubs", "Guardiola", "Ancelotti"])

if pages == "Venues":
    venues()

if pages == "Clubs":
    clubs()

if pages == "Guardiola":
    matches()

if pages == "Ancelotti":
    players()