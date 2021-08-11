from app import app
from utils.json_response import json_response
from utils.handle_error import handle_error
from utils.jsonfy import jsonfy
from database import db

@app.route("/clubs/count-players")
@handle_error
def count_players_by_club():
    query = f"""
        SELECT row_to_json(clubs)
        FROM (
            SELECT club, COUNT(*)
            FROM player
            GROUP BY club
            ORDER BY COUNT DESC
        ) clubs
    """
    result = list(db.execute(query))

    clubs = jsonfy(result)

    data = {
        "status": "OK",
        "clubs": clubs
    }
    
    return json_response(data)

@app.route("/clubs")
@handle_error
def count_clubs():
    query = f"""
        SELECT row_to_json(clubs)
        FROM (
            SELECT distinct club
            FROM player
            ORDER BY club
        ) clubs
    """
    result = list(db.execute(query))

    clubs = jsonfy(result)

    data = {
        "status": "OK",
        "clubs": clubs
    }
    
    return json_response(data)

@app.route("/clubs/<clubParameter>")
@handle_error
def players_by_club_with_goals(clubParameter):
    if not clubParameter:
        return {
            "status": "error",
            "message": "No club, please select one"
        }, 400

    query = f"""
        SELECT row_to_json(clubs)
        FROM (
            SELECT picture, "name", "position", goals, country_id
            FROM player
            WHERE club='{clubParameter}'
            GROUP BY club, "name", "position", goals, picture, country_id
            ORDER BY club ASC
        ) clubs
    """
    result = list(db.execute(query))

    clubs = jsonfy(result)

    data = {
        "status": "OK",
        "players": clubs
    }
    
    return json_response(data)