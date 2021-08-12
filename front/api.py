import requests
import pandas as pd
import streamlit as st
from config import API_URI
from IPython.core.display import HTML


def all_matches():
    res = requests.get(f"{API_URI}/matches").json()
    res = res["matches"]
    df = pd.DataFrame(res)
    return df


def path_to_image_html(path):
    return '<img src="' + path + '" width="80" >'


def find_players(parameters):
    conditions = ""
    for key, value in parameters.items():
        value = str(value)
        if value != "None":
            conditions += f"{key}={value}&"

    size = len(conditions)
    conditions = conditions[:size - 1]

    url = f"{API_URI}/player/stats?" + conditions
    res = requests.get(url).json()
    res = res["players"]
    
    if len(res) == 0:
        sorry = "There are no players which such stats"
        return sorry
    else:
        df = pd.DataFrame(res)
        df = df.dropna(axis="columns")
        df = df.drop("player_id", axis="columns")
        col_dict = {'country_id': 'country', 'squad_number': 'dorsal',
                    "minutes": "mins", "passing_acc_perc": "passing_acc_(%)"}
        df.columns = [col_dict.get(x, x) for x in df.columns]
        df.to_html(escape=False, formatters=dict(picture=path_to_image_html))
        table = HTML(df.to_html(
            escape=False, formatters=dict(picture=path_to_image_html)))
        return table


def get_all_clubs():
    res = requests.get(f"{API_URI}/clubs").json()
    res = res["clubs"]
    clubs = []
    for i in res:
        for key, value in i.items():
            clubs.append(value)

    return clubs


def find_club_players(club):
    res = requests.get(f"{API_URI}/clubs/{club}").json()
    res = res["players"]
    df = pd.DataFrame(res)
    col_dict = {'country_id': 'country'}
    df.columns = [col_dict.get(x, x) for x in df.columns]
    df.to_html(escape=False, formatters=dict(picture=path_to_image_html))
    table = HTML(df.to_html(
        escape=False, formatters=dict(picture=path_to_image_html)))
    return table

def find_all_venues():
    res = requests.get(f"{API_URI}/venues").json()
    res = res["venues"]
    return res