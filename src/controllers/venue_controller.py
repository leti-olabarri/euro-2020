from app import app
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.jsonfy import jsonfy
from database import db

@app.route("/venues")
@handle_error
def search_all_venues():
    query = f"""
        SELECT row_to_json(venues)
        FROM (
            SELECT venue.name, capacity, ST_AsText(geom), ST_AsEwkt(geom), ST_X(geom), ST_Y(geom), city, country, picture
            FROM venue
        ) venues
    """
    result = list(db.execute(query))

    venues = jsonfy(result)

    data = {
        "status": "OK",
        "venues": venues
    }
    
    return json_response(data)