from api import find_all_venues
import streamlit as st
from streamlit_folium import folium_static
import folium


def venues():

    m = folium.Map(location=[48.224082825962476,
                   46.90666960745771], zoom_start=3)

    response = find_all_venues()
    for i in response:
        longitude = i["st_x"]
        latitude = i["st_y"]
        name = i["name"]
        capacity = i["capacity"]
        popup = f"<b>{name}</b><br/><p>Capacity: {capacity} spectators</p><img src='https://static2-sevilla.abc.es/media/deportes/2021/04/19/s/estadio-cartuja-sevilla-U86314661137dLF-620x349@abc.jpg' width=200/>"
        folium.Marker(
            [latitude, longitude],icon=folium.Icon(color='blue', icon='fa-futbol-o', prefix='fa'), popup=f"{popup}", tooltip=name
        ).add_to(m)

    folium_static(m)
