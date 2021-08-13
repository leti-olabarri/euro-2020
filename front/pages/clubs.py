import streamlit as st
from api import get_all_clubs, find_club_players

def clubs():

    options = get_all_clubs()

    st.title("Clubs")
    st.markdown("How many players had each club in the UEFA Euro 2020? Select a club and find!")
    club = st.selectbox("Club", options)
    table = find_club_players(club)
    st.write(table)