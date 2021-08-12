import streamlit as st
from api import all_matches
import matplotlib.pyplot as plt


def matches():
    st.title("Matches")
    st.markdown("Hey, Guardiola, here you have the correlation table for some stats of the last UEFA Euro 2020. They may be useful to plan new tactics")
    table = all_matches()

    not_columns = ["match_id", "duels_won_home", "duels_won_away", "pens"]
    for i in not_columns:
        table = table.drop(i, axis="columns")

    corr = table.corr()
    
    st.write(corr)

    st.markdown("I know what you are thinking: 'Too many numbers...' Fair enough.")

    st.markdown("Just press the different buttons to learn about the three most interesting correlations we found. They may give you a surprise!")

    if st.button("Possession vs goals"):
        x = table["possession_home"].values.reshape(-1, 1)
        x2 = table["possession_away"].values.reshape(-1, 1)
        y = table["team_home_score"].values.reshape(-1, 1)
        y2 = table["team_away_score"].values.reshape(-1, 1)

        x = [*x, *x2]
        y = [*y, *y2]
        with plt.xkcd():
            fig, ax = plt.subplots()
            ax.scatter(x,y)
            plt.title("Possession vs number of goals in Euro 2020")
            plt.xlabel("Team possession (%)")
            plt.ylabel("Number of goals")

        st.markdown("I am really not sure if there is correlation between possession and number of goals. Sorry, Pep, we know you love possession :smiling_imp: :smiling_imp: :smiling_imp:")
        st.pyplot(fig)

    if st.button("Shots vs goals"):
        x = table["total_shots_home"].values.reshape(-1, 1)
        x2 = table["total_shots_away"].values.reshape(-1, 1)
        y = table["team_home_score"].values.reshape(-1, 1)
        y2 = table["team_away_score"].values.reshape(-1, 1)

        x = [*x, *x2]
        y = [*y, *y2]
        with plt.xkcd():
            fig, ax = plt.subplots()
            ax.scatter(x,y)
            plt.title("Total shots vs number of goals in Euro 2020")
            plt.xlabel("Total shots (in a single match)")
            plt.ylabel("Number of goals")

        st.markdown("Well, yes but no... or maybe :thinking_face:")
        st.pyplot(fig)
    
    if st.button("Shots vs shots on target"):
        x = table["total_shots_home"].values.reshape(-1, 1)
        x2 = table["total_shots_away"].values.reshape(-1, 1)
        y = table["shots_on_target_home"].values.reshape(-1, 1)
        y2 = table["shots_on_target_away"].values.reshape(-1, 1)

        x = [*x, *x2]
        y = [*y, *y2]
        with plt.xkcd():
            fig, ax = plt.subplots()
            ax.scatter(x,y)
            plt.title("Total shots vs shots on target in Euro 2020")
            plt.xlabel("Total shots (in a single match)")
            plt.ylabel("Total shots on target")

        st.markdown("This is better! At least, forward players are very accurate :soccer: :soccer: :soccer:")
        st.pyplot(fig)
