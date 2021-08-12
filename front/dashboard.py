import streamlit as st
from pages.matches import matches
from pages.players import players
from api import get_all_clubs, find_club_players


st.header("UEFA Euro 2020")

options = get_all_clubs()

st.sidebar.title("Navigation")
pages = st.sidebar.radio("Pages", ["Clubs", "Guardiola", "Ancelotti"])

if pages == "Clubs":
    club = st.selectbox("Club", options)
    table = find_club_players(club)
    st.write(table)

if pages == "Guardiola":
    matches()

if pages == "Ancelotti":
    players()