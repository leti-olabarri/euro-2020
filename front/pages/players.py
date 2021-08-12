import streamlit as st
from api import find_players


def players():
    st.title("Players")
    st.text("")

    position = st.selectbox('Position*', [
        "Goalkeeper",
        "Defender",
        "Midfielder",
        "Forward"
    ])
    age = st.slider("Select a range of age:",
                    15, 50, (15, 50))
    matches = st.slider("Matches played:",
                        0, 7, (0, 7))
    passing_acc_perc = st.slider("Porcentage of passing accuracy:",
                        0, 100, (0, 100))
    if position != "Goalkeeper":
        goals = st.slider("Goals:",
                        0, 5, (0, 5))
        speed_km_h = st.slider("Speed (km/h):",
                        5, 70, (5, 70))
    if position == "Forward":
        fouls_suff = st.slider("Fouls suffered:",
                        0, 30, (0, 30))
        attempts_on_target = st.slider("Attempts on target:",
                        0, 7, (0, 7))
        balls_recovered = (None, None)
        distance_covered_km = (None, None)
        fouls_comm = (None, None)
    if position == "Forward" or position == "Midfielder":
        attempts = st.slider("Attempts:",
                        0, 50, (0, 50))
        assists = st.slider("Assists:",
                        0, 15, (0, 15))
        clearances = (None, None)
        saves = (None, None)
        goals_conceded = (None, None)
        clean_sheets = (None, None)
    if position == "Defender" or position == "Midfielder":
        balls_recovered = st.slider("Balls recovered:",
                        0, 60, (0, 60))
        distance_covered_km = st.slider("Distance covered (in km):",
                        0, 100, (0, 100))
        fouls_comm = st.slider("Fouls commited:",
                        0, 30, (0, 30))
        fouls_suff = (None, None)
        attempts_on_target = (None, None)
    if position == "Defender":
        clearances = st.slider("Clearances:",
                        0, 40, (0, 40))
        saves = (None, None)
        goals_conceded = (None, None)
        clean_sheets = (None, None)
        fouls_suff = (None, None)
        attempts = (None, None)
        attempts_on_target = (None, None)
        assists = (None, None)
    if position == "Goalkeeper":
        saves = st.slider("Saves:",
                        0, 30, (0, 30))
        goals_conceded = st.slider("Goals conceded:",
                        0, 15, (0, 15))
        clean_sheets = st.slider("Clean sheets:",
                        0, 7, (0, 7))
        goals = (None, None)
        speed_km_h = (None, None)
        fouls_suff = (None, None)
        attempts = (None, None)
        attempts_on_target = (None, None)
        assists = (None, None)
        balls_recovered = (None, None)
        distance_covered_km = (None, None)
        clearances = (None, None)
        fouls_comm = (None, None)


    stats = {
    "age_min": age[0],
    "age_max": age[1],
    "position": position,
    "matches_min": matches[0],
    "matches_max": matches[1],
    "passing_acc_perc_min": passing_acc_perc[0],
    "passing_acc_perc_max": passing_acc_perc[1],
    "goals_min": goals[0],
    "goals_max": goals[1],
    "fouls_comm_min": fouls_comm[0],
    "fouls_comm_max": fouls_comm[1],
    "fouls_suff_min": fouls_suff[0],
    "fouls_suff_max": fouls_suff[1],
    "attempts_min": attempts[0],
    "attempts_max": attempts[1],
    "attempts_on_target_min": attempts_on_target[0],
    "attempts_on_target_max": attempts_on_target[1],
    "assists_min": assists[0],
    "assists_max": assists[1],
    "speed_km_h_min": speed_km_h[0],
    "speed_km_h_max": speed_km_h[1],
    "balls_recovered_min": balls_recovered[0],
    "balls_recovered_max": balls_recovered[1],
    "distance_covered_km_min": distance_covered_km[0],
    "distance_covered_km_max": distance_covered_km[1],
    "clearances_min": clearances[0],
    "clearances_max": clearances[1],
    "saves_min": saves[0],
    "saves_max": saves[1],
    "goals_conceded_min": goals_conceded[0],
    "goals_conceded_max": goals_conceded[1],
    "clean_sheets_min": clean_sheets[0],
    "clean_sheets_max": clean_sheets[1]
    }

    if st.button("Get your players!"):
        table = find_players(stats)
        if type(table) != "<class 'pandas.core.frame.DataFrame'>":
            st.write(table)