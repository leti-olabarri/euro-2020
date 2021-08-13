from api import find_all_venues
import streamlit as st
from streamlit_folium import folium_static
import folium


def venues():

    st.title("Venues")

    st.markdown("For pandemic times, social distance has become very important. UEFA people were very farsighted when they decided to host this last Euro 2020 in twelve different stadiums. Click on every one to have more information")

    m = folium.Map(location=[51.49223882457262,
                   31.218865188806557], zoom_start=3)

    response = find_all_venues()
    for i in response:
        longitude = i["st_x"]
        latitude = i["st_y"]
        name = i["name"]
        capacity = i["capacity"]
        picture = i["picture"]
        popup = f"<b>{name}</b><br/><p>Capacity: {capacity} spectators</p><img src={picture} width=200/>"
        folium.Marker(
            [latitude, longitude], icon=folium.Icon(color='blue', icon='fa-futbol-o', prefix='fa'), popup=f"{popup}", tooltip=name
        ).add_to(m)

    folium_static(m)
