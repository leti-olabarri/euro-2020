import streamlit as st
from pages.matches import matches
from pages.players import players
from pages.venues import venues
from api import get_all_clubs, find_club_players


st.header("UEFA Euro 2020")

options = get_all_clubs()

st.sidebar.title("Navigation")
pages = st.sidebar.radio("Pages", ["Clubs", "Venues", "Guardiola", "Ancelotti"])

if pages == "Clubs":
    st.title("Clubs")
    st.markdown("How many players had each club in the UEFA Euro 2020? Select a club and find!")
    club = st.selectbox("Club", options)
    table = find_club_players(club)
    st.write(table)

if pages == "Venues":
    venues()

if pages == "Guardiola":
    matches()

if pages == "Ancelotti":
    players()