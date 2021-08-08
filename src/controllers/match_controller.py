from app import app
from utils.json_response import json_response
from utils.handle_error import handle_error
from database import db
from flask import request
import re

@app.route("/matches")
@handle_error
def search_matches_for_stage():
    query = f"""
        SELECT row_to_json(matches)
        FROM (
            SELECT stage, team_name_home, team_home_score, team_name_away, team_away_score
            FROM "match"
        ) matches
    """
    result = list(db.execute(query))

    matches = []

    for i in result:
        single_match = i[0]
        matches.append(single_match)

    data = {
        "status": "OK",
        "matches": matches
    }
    
    return json_response(data)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
