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
    return '<img src="'+ path + '" width="60" >'

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
        return st.text("There are no players which such stats")
    else:
        df = pd.DataFrame(res)
        df = df.dropna(axis="columns")
        df = df.drop("player_id", axis="columns")
        df.to_html(escape=False, formatters=dict(picture=path_to_image_html))
        thing = HTML(df.to_html(escape=False,formatters=dict(picture=path_to_image_html)))
        return thing